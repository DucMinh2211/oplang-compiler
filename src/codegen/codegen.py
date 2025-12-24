"""
Code Generator for OPLang programming language.
This module implements a code generator that traverses AST nodes and generates
Java bytecode using the Emitter and Frame classes.
"""

from typing import Any, List, Optional
from ..utils.visitor import ASTVisitor
from ..utils.nodes import *
from .emitter import Emitter, is_void_type, is_int_type, is_string_type, is_bool_type, is_float_type
from .frame import Frame
from .error import IllegalOperandException, IllegalRuntimeException
from .io import IO_SYMBOL_LIST
from .utils import *
from functools import *

class PostfixAccess:
    """A helper class to pass state during postfix expression traversal."""
    def __init__(self, frame, sym, code, current_type, is_static_context, is_left=False, is_first=False, is_last=False):
        self.frame = frame
        self.sym = sym
        self.code = code
        self.current_type = current_type
        self.is_static_context = is_static_context
        self.is_left = is_left
        self.is_first = is_first
        self.is_last = is_last


class CodeGenerator(ASTVisitor):
    """
    Code generator for OPLang.
    Traverses AST and generates JVM bytecode.
    """
    
    def __init__(self):
        self.current_class = None
        self.emit = None  # Will be initialized per class
        self.classes_members = {}

    def get_members(self, class_type):
        if hasattr(class_type, 'members'):
            return class_type.members
        return self.classes_members.get(class_type.class_name, [])

    # ============================================================================
    # Program and Class Declarations
    # ============================================================================

    def visit_program(self, node: "Program", o: Any = None):
        """
        Visit program node - generate code for all classes.
        """
        # Process all class declarations
        for class_decl in node.class_decls:
            self.visit(class_decl, o)

    def visit_class_decl(self, node: "ClassDecl", o: Any = None):
        """
        Visit class declaration - generate class structure.
        """
        self.current_class = node.name
        
        # Populate classes_members
        class_members_syms = []
        for member in node.members:
            if isinstance(member, MethodDecl):
                param_types = [p.param_type for p in member.params]
                func_type = FunctionType(param_types, member.return_type)
                class_members_syms.append(Symbol(member.name, func_type, CName(node.name)))
            elif isinstance(member, DestructorDecl):
                 func_type = FunctionType([], PrimitiveType("void"))
                 class_members_syms.append(Symbol("finalize", func_type, CName(node.name)))
            elif isinstance(member, AttributeDecl):
                for attr in member.attributes:
                    class_members_syms.append(Symbol(attr.name, member.attr_type, CName(node.name)))
        
        self.classes_members[node.name] = class_members_syms

        class_file = node.name + ".j"
        self.emit = Emitter(class_file)
        
        # Determine superclass
        superclass = node.superclass if node.superclass else "java/lang/Object"
        
        # Emit class prolog
        self.emit.print_out(self.emit.emit_prolog(node.name, superclass))
        
        # Process class members (attributes, methods, constructors, destructors)
        has_constructor = False
        for member in node.members:
            if isinstance(member, ConstructorDecl):
                has_constructor = True
            self.visit(member, o)
        
        if not has_constructor:
             # Default constructor
             func_type = FunctionType([], PrimitiveType("void"))
             self.emit.print_out(self.emit.emit_method("<init>", func_type, False))
             
             frame = Frame("<init>", PrimitiveType("void"))
             frame.enter_scope(True)
             from_label = frame.get_start_label()
             to_label = frame.get_end_label()
             
             this_idx = frame.get_new_index()
             self.emit.print_out(self.emit.emit_var(this_idx, "this", ClassType(node.name), from_label, to_label))
             
             self.emit.print_out(self.emit.emit_label(from_label, frame))
             
             self.emit.print_out(self.emit.jvm.emitALOAD(this_idx))
             frame.push()
             self.emit.print_out(self.emit.emit_invoke_special(frame, "java/lang/Object/<init>", FunctionType([], PrimitiveType("void"))))
             
             self.emit.print_out(self.emit.emit_return(PrimitiveType("void"), frame))
             self.emit.print_out(self.emit.emit_label(to_label, frame))
             self.emit.print_out(self.emit.emit_end_method(frame))
             frame.exit_scope()
        
        # Emit class epilog
        self.emit.emit_epilog()

    # ============================================================================
    # Attribute Declarations
    # ============================================================================

    def visit_attribute_decl(self, node: "AttributeDecl", o: Any = None):
        """
        Visit attribute declaration - generate field directives.
        """
        for attr in node.attributes:
            self.visit(attr, node)

    def visit_attribute(self, node: "Attribute", o: Any = None):
        """
        Visit individual attribute - generate field directive.
        """
        attr_decl = o  # AttributeDecl node
        class_name = self.current_class
        field_name = node.name
        
        # Emit field directive
        if attr_decl.is_static:
            self.emit.print_out(
                self.emit.emit_attribute(
                    field_name,
                    attr_decl.attr_type,
                    attr_decl.is_final
                )
            )
        else:
            # Instance field
            self.emit.print_out(
                self.emit.jvm.emitINSTANCEFIELD(
                    field_name,
                    self.emit.get_jvm_type(attr_decl.attr_type)
                )
            )
        
        # TODO: Handle initialization if node.init_value is not None
        if node.init_value:
            pass

    # ============================================================================
    # Method Declarations
    # ============================================================================

    def visit_method_decl(self, node: "MethodDecl", o: Any = None):
        """
        Visit method declaration - generate method code.
        """
        frame = Frame(node.name, node.return_type)
        self.generate_method(node, frame, node.is_static)

    def visit_constructor_decl(self, node: "ConstructorDecl", o: Any = None):
        """
        Visit constructor declaration - generate constructor code.
        """
        frame = Frame("<init>", PrimitiveType("void"))
        param_types = [p.param_type for p in node.params]
        func_type = FunctionType(param_types, PrimitiveType("void"))
        
        self.emit.print_out(self.emit.emit_method("<init>", func_type, False))
        
        frame.enter_scope(True)
        from_label = frame.get_start_label()
        to_label = frame.get_end_label()
        
        # this
        this_idx = frame.get_new_index()
        self.emit.print_out(self.emit.emit_var(this_idx, "this", ClassType(self.current_class), from_label, to_label))
        sym_list = [Symbol("this", ClassType(self.current_class), Index(this_idx))]
        
        # params
        for param in node.params:
            idx = frame.get_new_index()
            self.emit.print_out(self.emit.emit_var(idx, param.name, param.param_type, from_label, to_label))
            sym_list.append(Symbol(param.name, param.param_type, Index(idx)))
            
        sym_list = IO_SYMBOL_LIST + sym_list
        
        self.emit.print_out(self.emit.emit_label(from_label, frame))
        
        # super()
        self.emit.print_out(self.emit.jvm.emitALOAD(this_idx))
        frame.push()
        self.emit.print_out(self.emit.emit_invoke_special(frame, "java/lang/Object/<init>", FunctionType([], PrimitiveType("void"))))
        
        o = SubBody(frame, sym_list)
        self.visit(node.body, o)
        
        self.emit.print_out(self.emit.emit_return(PrimitiveType("void"), frame))
        self.emit.print_out(self.emit.emit_label(to_label, frame))
        self.emit.print_out(self.emit.emit_end_method(frame))
        frame.exit_scope()

    def visit_destructor_decl(self, node: "DestructorDecl", o: Any = None):
        """
        Visit destructor declaration - generate destructor code.
        """
        frame = Frame("finalize", PrimitiveType("void"))
        func_type = FunctionType([], PrimitiveType("void"))
        
        self.emit.print_out(self.emit.emit_method("finalize", func_type, False))
        
        frame.enter_scope(True)
        from_label = frame.get_start_label()
        to_label = frame.get_end_label()
        
        this_idx = frame.get_new_index()
        self.emit.print_out(self.emit.emit_var(this_idx, "this", ClassType(self.current_class), from_label, to_label))
        sym_list = [Symbol("this", ClassType(self.current_class), Index(this_idx))] + IO_SYMBOL_LIST
        
        self.emit.print_out(self.emit.emit_label(from_label, frame))
        
        o = SubBody(frame, sym_list)
        self.visit(node.body, o)
        
        # super.finalize()
        self.emit.print_out(self.emit.jvm.emitALOAD(this_idx))
        frame.push()
        self.emit.print_out(self.emit.emit_invoke_special(frame, "java/lang/Object/finalize", FunctionType([], PrimitiveType("void"))))
        
        self.emit.print_out(self.emit.emit_return(PrimitiveType("void"), frame))
        self.emit.print_out(self.emit.emit_label(to_label, frame))
        self.emit.print_out(self.emit.emit_end_method(frame))
        frame.exit_scope()

    def visit_parameter(self, node: "Parameter", o: Any = None):
        """
        Visit parameter - register parameter in frame.
        """
        # This is handled in generate_method
        pass

    def generate_method(self, node: "MethodDecl", frame: Frame, is_static: bool):
        """
        Generate code for a method.
        
        Args:
            node: Method declaration node
            frame: Frame for this method
            is_static: Whether method is static
        """
        class_name = self.current_class
        method_name = node.name
        is_main = is_static and method_name == "main" and len(node.params) == 0

        # Build method signature
        if is_main:
            param_types = [ArrayType(PrimitiveType("string"), 0)]
            return_type = PrimitiveType("void")
        else:
            param_types = [p.param_type for p in node.params]
            return_type = node.return_type
        
        # Create function type for method signature
        func_type = FunctionType(param_types, return_type)
        
        # Emit method directive
        self.emit.print_out(
            self.emit.emit_method(
                method_name,
                func_type,
                is_static
            )
        )
        
        frame.enter_scope(True)
        from_label = frame.get_start_label()
        to_label = frame.get_end_label()
        
        sym_list = []
        
        # Handle 'this' parameter for instance methods
        if not is_static:
            this_idx = frame.get_new_index()
            self.emit.print_out(
                self.emit.emit_var(
                    this_idx,
                    "this",
                    ClassType(class_name),
                    from_label,
                    to_label
                )
            )
            sym_list.append(Symbol("this", ClassType(class_name), Index(this_idx)))
        
        if is_main:
            # Add `String[] args` to the main method
            args_idx = frame.get_new_index()
            self.emit.print_out(
                self.emit.emit_var(
                    args_idx,
                    "args",
                    ArrayType(PrimitiveType("string"), 0),
                    from_label,
                    to_label
                )
            )
            sym_list.append(Symbol("args", ArrayType(PrimitiveType("string"), 0), Index(args_idx)))
        else:
            # Generate code for parameters
            for i, param in enumerate(node.params):
                idx = frame.get_new_index()
                self.emit.print_out(
                    self.emit.emit_var(
                        idx,
                        param.name,
                        param.param_type,
                        from_label,
                        to_label
                    )
                )
                sym_list.append(Symbol(param.name, param.param_type, Index(idx)))

        sym_list = IO_SYMBOL_LIST + sym_list
        
        self.emit.print_out(self.emit.emit_label(from_label, frame))
        
        # Generate code for method body
        o = SubBody(frame, sym_list)
        self.visit(node.body, o)
        
        # Emit return if void
        if is_void_type(return_type):
            self.emit.print_out(self.emit.emit_return(return_type, frame))
        
        self.emit.print_out(self.emit.emit_label(to_label, frame))
        self.emit.print_out(self.emit.emit_end_method(frame))
        
        frame.exit_scope()

    # ============================================================================
    # Type System
    # ============================================================================

    def visit_primitive_type(self, node: "PrimitiveType", o: Any = None):
        pass

    def visit_array_type(self, node: "ArrayType", o: Any = None):
        pass

    def visit_class_type(self, node: "ClassType", o: Any = None):
        pass

    def visit_reference_type(self, node: "ReferenceType", o: Any = None):
        pass

    # ============================================================================
    # Statements
    # ============================================================================

    def visit_block_statement(self, node: "BlockStatement", o: SubBody = None):
        """
        Visit block statement - process variable declarations and statements.
        """
        if o is None:
            return
        
        # Process variable declarations
        for var_decl in node.var_decls:
            o = self.visit(var_decl, o)
        
        # Process statements
        for stmt in node.statements:
            self.visit(stmt, o)

    def visit_variable_decl(self, node: "VariableDecl", o: SubBody = None):
        """
        Visit variable declaration - register local variables.
        """
        if o is None:
            return o
        
        frame = o.frame
        from_label = frame.get_start_label()
        to_label = frame.get_end_label()
        
        new_sym = []
        for var in node.variables:
            idx = frame.get_new_index()
            self.emit.print_out(
                self.emit.emit_var(
                    idx,
                    var.name,
                    node.var_type,
                    from_label,
                    to_label
                )
            )
            
            # Add to symbol list
            new_sym.append(Symbol(var.name, node.var_type, Index(idx)))
            
            # Handle initialization if present
            if var.init_value is not None:
                # Generate code for initialization
                code, typ = self.visit(var.init_value, Access(frame, o.sym))
                self.emit.print_out(code)
                self.emit.print_out(
                    self.emit.emit_write_var(var.name, node.var_type, idx, frame)
                )
            elif isinstance(node.var_type, ArrayType) and node.var_type.size > 0:
                 # Auto-initialize array
                 self.emit.print_out(self.emit.emit_push_iconst(node.var_type.size, frame))
                 typ_str = self.emit.get_full_type(node.var_type.element_type)
                 self.emit.print_out(self.emit.emit_new_array(typ_str))
                 # newarray pops size (1) and pushes ref (1), so net stack change is 0. 
                 # But emit_new_array doesn't touch frame, emit_push_iconst pushed 1.
                 # So frame thinks +1. Correct.
                 self.emit.print_out(self.emit.emit_write_var(var.name, node.var_type, idx, frame))
        
        return SubBody(frame, new_sym + o.sym)

    def visit_variable(self, node: "Variable", o: Any = None):
        pass

    def visit_assignment_statement(self, node: "AssignmentStatement", o: SubBody = None):
        """
        Visit assignment statement - generate assignment code.
        """
        if o is None:
            return

        if isinstance(node.lhs, PostfixLHS):
            # LHS is a postfix expression (e.g. a[i] or a.x)
            # Standard order: Evaluate container, Evaluate index (if any), Evaluate RHS, Store.
            
            # Decompose PostfixLHS
            postfix_expr = node.lhs.postfix_expr
            primary = postfix_expr.primary
            ops = postfix_expr.postfix_ops
            
            if not ops:
                # Assigning to primary directly (only valid if primary is ID?)
                if isinstance(primary, Identifier):
                     # RHS first
                     code, typ = self.visit(node.rhs, Access(o.frame, o.sym))
                     self.emit.print_out(code)
                     
                     # Write var
                     sym = next(filter(lambda x: x.name == primary.name, o.sym), None)
                     if sym and type(sym.value) is Index:
                         self.emit.print_out(self.emit.emit_write_var(sym.name, sym.type, sym.value.value, o.frame))
                return

            # Complex Postfix: container + ops
            # Last op determines the store target.
            prefix_ops = ops[:-1]
            last_op = ops[-1]
            
            # 1. Evaluate Prefix (Container)
            # We construct a temp PostfixExpression for the prefix
            prefix_expr = PostfixExpression(primary, prefix_ops)
            # Visit it to load the container reference on stack
            ref_code, ref_type = self.visit(prefix_expr, Access(o.frame, o.sym))
            self.emit.print_out(ref_code)
            
            is_static_access = isinstance(ref_type, ClassType) and not ref_code
            
            # 2. Handle Last Op
            if isinstance(last_op, ArrayAccess):
                # arr[idx] = val
                # Stack has: arr_ref
                
                # Evaluate Index
                idx_code, idx_type = self.visit(last_op.index, Access(o.frame, o.sym))
                self.emit.print_out(idx_code)
                
                # Stack has: arr_ref, index
                
                # Evaluate RHS
                rhs_code, rhs_type = self.visit(node.rhs, Access(o.frame, o.sym))
                self.emit.print_out(rhs_code)
                
                # Stack has: arr_ref, index, value
                
                # Emit Store
                if isinstance(ref_type, ArrayType):
                    self.emit.print_out(self.emit.emit_astore(ref_type.element_type, o.frame))

            elif isinstance(last_op, MemberAccess):
                # obj.field = val
                # Stack has: obj_ref (or nothing if static)
                
                # Evaluate RHS
                rhs_code, rhs_type = self.visit(node.rhs, Access(o.frame, o.sym))
                self.emit.print_out(rhs_code)
                
                # Stack has: obj_ref, value
                
                # Emit Store
                field_name = last_op.member_name
                if isinstance(ref_type, ClassType):
                    class_name = ref_type.class_name
                    # Find field type
                    members = self.get_members(ref_type)
                    member_sym = next((m for m in members if m.name == field_name), None)
                    if member_sym:
                        if is_static_access:
                             self.emit.print_out(self.emit.emit_put_static(f"{class_name}/{field_name}", member_sym.type, o.frame))
                        else:
                             self.emit.print_out(self.emit.emit_put_field(f"{class_name}/{field_name}", member_sym.type, o.frame))
        
        else:
            # Generate code for RHS
            code, typ = self.visit(node.rhs, Access(o.frame, o.sym))
            self.emit.print_out(code)
            
            # Generate code for LHS
            lhs_code, lhs_type = self.visit(node.lhs, Access(o.frame, o.sym, is_left=True))
            self.emit.print_out(lhs_code)

    def visit_if_statement(self, node: "IfStatement", o: Any = None):
        """
        Visit if statement.
        TODO: Implement if statement code generation
        """
        pass

    def visit_for_statement(self, node: "ForStatement", o: Any = None):
        """
        Visit for statement.
        TODO: Implement for statement code generation
        """
        pass

    def visit_break_statement(self, node: "BreakStatement", o: Any = None):
        """
        Visit break statement.
        TODO: Implement break statement code generation
        """
        pass

    def visit_continue_statement(self, node: "ContinueStatement", o: Any = None):
        """
        Visit continue statement.
        TODO: Implement continue statement code generation
        """
        pass

    def visit_return_statement(self, node: "ReturnStatement", o: SubBody = None):
        """
        Visit return statement - generate return code.
        """
        if o is None:
            return
        
        # Generate code for return value
        code, typ = self.visit(node.value, Access(o.frame, o.sym))
        self.emit.print_out(code)
        
        # Emit return instruction
        self.emit.print_out(self.emit.emit_return(typ, o.frame))

    def visit_method_invocation_statement(
        self, node: "MethodInvocationStatement", o: Any = None
    ):
        """
        Visit method invocation statement.
        """
        if o is None:
            return
        
        code, typ = self.visit(node.method_call, Access(o.frame, o.sym))
        self.emit.print_out(code)

        if not is_void_type(typ):
            self.emit.print_out(self.emit.emit_pop(o.frame))


    # ============================================================================
    # Left-hand Side (LHS)
    # ============================================================================

    def visit_id_lhs(self, node: "IdLHS", o: Access = None):
        """
        Visit identifier LHS - generate code to write to variable.
        """
        if o is None:
            return "", None
        
        # Find symbol
        sym = next(filter(lambda x: x.name == node.name, o.sym), None)
        if sym is None:
            raise IllegalOperandException(f"Undeclared variable: {node.name}")
        
        if type(sym.value) is Index:
            code = self.emit.emit_write_var(
                sym.name, sym.type, sym.value.value, o.frame
            )
            return code, sym.type
        else:
            raise IllegalOperandException(f"Cannot assign to: {node.name}")

    def visit_postfix_lhs(self, node: "PostfixLHS", o: Any = None):
        """
        Visit postfix LHS (for member access, array access).
        TODO: Implement postfix LHS code generation
        """
        pass

    # ============================================================================
    # Expressions
    # ============================================================================

    def visit_binary_op(self, node: "BinaryOp", o: Access = None):
        """
        Visit binary operation.
        TODO: Implement binary operation code generation
        """
        pass

    def visit_unary_op(self, node: "UnaryOp", o: Access = None):
        """
        Visit unary operation.
        TODO: Implement unary operation code generation
        """
        pass

    def visit_postfix_expression(self, node: "PostfixExpression", o: Access = None):
        """
        Visit postfix expression by visiting the primary expression and then chaining
        the postfix operations.
        """
        if o is None:
            return "", None

        code, current_type = self.visit(node.primary, o)
        is_static_context = isinstance(current_type, ClassType) and not code

        # Create a context object to pass state through the postfix operation chain
        postfix_o = PostfixAccess(o.frame, o.sym, code, current_type, is_static_context)

        for op in node.postfix_ops:
            postfix_o = self.visit(op, postfix_o)

        return postfix_o.code, postfix_o.current_type

    def visit_method_call(self, node: "MethodCall", o: PostfixAccess = None):
        """
        Visit method call as part of a postfix expression.
        """
        if o is None:
            return None
        
        if not isinstance(o.current_type, ClassType):
            raise IllegalOperandException(f"Method call on non-class type: {o.current_type}")

        class_name = o.current_type.class_name
        method_name = node.method_name

        members = self.get_members(o.current_type)

        method_sym = next((m for m in members if m.name == method_name and isinstance(m.type, FunctionType)), None)
        if not method_sym:
            raise IllegalOperandException(f"Method '{method_name}' not found in class '{class_name}'")

        arg_codes = []
        for i, arg in enumerate(node.args):
            arg_code, arg_type = self.visit(arg, Access(o.frame, o.sym))
            expected_type = method_sym.type.param_types[i]
            if is_float_type(expected_type) and is_int_type(arg_type):
                arg_code += self.emit.emit_i2f(o.frame)
            arg_codes.append(arg_code)
        
        o.code += "".join(arg_codes)
        
        if o.is_static_context:
            o.code += self.emit.emit_invoke_static(f"{class_name}/{method_name}", method_sym.type, o.frame)
        else:
            o.code += self.emit.emit_invoke_virtual(f"{class_name}/{method_name}", method_sym.type, o.frame)
        
        o.current_type = method_sym.type.return_type
        o.is_static_context = False
        return o

    def visit_member_access(self, node: "MemberAccess", o: PostfixAccess = None):
        """
        Visit member access as part of a postfix expression.
        """
        if o is None:
            return None

        if not isinstance(o.current_type, ClassType):
            raise IllegalOperandException(f"Member access on non-class type: {o.current_type}")

        class_name = o.current_type.class_name
        member_name = node.member_name

        members = self.get_members(o.current_type)
        
        member_sym = next((m for m in members if m.name == member_name), None)
        if not member_sym:
            raise IllegalOperandException(f"Member '{member_name}' not found in class '{class_name}'")

        if o.is_static_context:
            o.code += self.emit.emit_get_static(f"{class_name}/{member_name}", member_sym.type, o.frame)
        else:
            o.code += self.emit.emit_get_field(f"{class_name}/{member_name}", member_sym.type, o.frame)
        
        o.current_type = member_sym.type
        o.is_static_context = False
        return o

    def visit_array_access(self, node: "ArrayAccess", o: PostfixAccess = None):
        """
        Visit array access as part of a postfix expression.
        """
        if o is None:
            return None

        if not isinstance(o.current_type, ArrayType):
            raise IllegalOperandException(f"Array access on non-array type: {o.current_type}")

        index_code, index_type = self.visit(node.index, Access(o.frame, o.sym))
        if not is_int_type(index_type):
            raise IllegalOperandException("Array index must be an integer")
        
        o.code += index_code
        o.code += self.emit.emit_aload(o.current_type.element_type, o.frame)
        
        o.current_type = o.current_type.element_type
        o.is_static_context = False
        return o

    def visit_object_creation(self, node: "ObjectCreation", o: Access = None):
        """
        Visit object creation.
        """
        if o is None:
            return "", None
        
        class_name = node.class_name
        code = self.emit.jvm.emitNEW(class_name)
        o.frame.push()
        code += self.emit.emit_dup(o.frame)
        
        arg_codes = ""
        arg_types = []
        for arg in node.args:
            arg_code, arg_type = self.visit(arg, o)
            arg_codes += arg_code
            arg_types.append(arg_type)
            
        code += arg_codes
        
        # Constructor signature
        constructor_type = FunctionType(arg_types, PrimitiveType("void"))
        code += self.emit.emit_invoke_special(o.frame, f"{class_name}/<init>", constructor_type)
        
        return code, ClassType(class_name)

    def visit_identifier(self, node: "Identifier", o: Access = None):
        """
        Visit identifier - generate code to read variable.
        """
        if o is None:
            return "", None
        
        # Find symbol
        sym = next(filter(lambda x: x.name == node.name, o.sym), None)
        if sym is None:
            # It might be a class name for a static access
            class_type = ClassType(node.name)
            if node.name == "io":
                # Special handling for the built-in 'io' class
                # Decorate the ClassType with its known members from IO_SYMBOL_LIST
                class_type.members = IO_SYMBOL_LIST
            return "", class_type
        
        if type(sym.value) is Index:
            code = self.emit.emit_read_var(
                sym.name, sym.type, sym.value.value, o.frame
            )
            return code, sym.type
        elif type(sym.value) is CName: # Static field or ClassName
            class_type = ClassType(sym.value.value)
            if sym.value.value == "io":
                class_type.members = IO_SYMBOL_LIST
            return "", class_type
        else:
            raise IllegalOperandException(f"Cannot read: {node.name}")

    def visit_this_expression(self, node: "ThisExpression", o: Access = None):
        """
        Visit this expression - load 'this' reference.
        """
        if o is None:
            return "", None
        
        # Find 'this' in symbol table (should be at index 0 for instance methods)
        this_sym = next(filter(lambda x: x.name == "this", o.sym), None)
        if this_sym is None:
            raise IllegalOperandException("'this' not available in static context")
        
        if type(this_sym.value) is Index:
            code = self.emit.emit_read_var(
                "this", this_sym.type, this_sym.value.value, o.frame
            )
            return code, this_sym.type
        else:
            raise IllegalOperandException("Invalid 'this' reference")

    def visit_parenthesized_expression(
        self, node: "ParenthesizedExpression", o: Access = None
    ):
        """
        Visit parenthesized expression - just visit inner expression.
        """
        return self.visit(node.expr, o)

    # ============================================================================
    # Literals
    # ============================================================================

    def visit_int_literal(self, node: "IntLiteral", o: Access = None):
        """
        Visit integer literal - push integer constant.
        """
        if o is None:
            return "", None
        code = self.emit.emit_push_iconst(node.value, o.frame)
        return code, PrimitiveType("int")

    def visit_float_literal(self, node: "FloatLiteral", o: Access = None):
        """
        Visit float literal - push float constant.
        """
        if o is None:
            return "", None
        code = self.emit.emit_push_fconst(str(node.value), o.frame)
        return code, PrimitiveType("float")

    def visit_bool_literal(self, node: "BoolLiteral", o: Access = None):
        """
        Visit boolean literal - push boolean constant.
        """
        if o is None:
            return "", None
        value_str = "1" if node.value else "0"
        code = self.emit.emit_push_iconst(value_str, o.frame)
        return code, PrimitiveType("boolean")

    def visit_string_literal(self, node: "StringLiteral", o: Access = None):
        """
        Visit string literal - push string constant.
        """
        if o is None:
            return "", None
        code = self.emit.emit_push_const('"' + node.value + '"', PrimitiveType("string"), o.frame)
        return code, PrimitiveType("string")

    def visit_array_literal(self, node: "ArrayLiteral", o: Access = None):
        """
        Visit array literal.
        TODO: Implement array literal code generation
        """
        pass

    def visit_nil_literal(self, node: "NilLiteral", o: Access = None):
        """
        Visit nil literal - push null reference.
        """
        if o is None:
            return "", None
        o.frame.push()
        code = self.emit.jvm.emitPUSHNULL()
        return code, None  # Type will be determined by context

    def visit_method_invocation(self, node, o = None):
        pass

    def visit_static_member_access(self, node, o = None):
        pass

    def visit_static_method_invocation(self, node, o = None):
        pass
