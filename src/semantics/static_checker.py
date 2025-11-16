"""
Static Semantic Checker for OPLang Programming Language

This module implements a comprehensive static semantic checker using visitor pattern
for the OPLang object-oriented programming language. It performs type checking,
scope management, inheritance validation, and detects all semantic errors as 
specified in the OPLang language specification.
"""

from functools import reduce
from typing import Dict, List, Set, Optional, Any, Tuple, Union, NamedTuple
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    ASTNode, Program, ClassDecl, AttributeDecl, Attribute, MethodDecl,
    ConstructorDecl, DestructorDecl, Parameter, VariableDecl, Variable,
    AssignmentStatement, IfStatement, ForStatement, BreakStatement,
    ContinueStatement, ReturnStatement, MethodInvocationStatement,
    BlockStatement, PrimitiveType, ArrayType, ClassType, ReferenceType,
    IdLHS, PostfixLHS, BinaryOp, UnaryOp, PostfixExpression, PostfixOp,
    MethodCall, MemberAccess, ArrayAccess, ObjectCreation, Identifier,
    ThisExpression, ParenthesizedExpression, IntLiteral, FloatLiteral,
    BoolLiteral, StringLiteral, ArrayLiteral, NilLiteral
)
from .static_error import (
    StaticError, Redeclared, UndeclaredIdentifier, UndeclaredClass,
    UndeclaredAttribute, UndeclaredMethod, CannotAssignToConstant,
    TypeMismatchInStatement, TypeMismatchInExpression, TypeMismatchInConstant,
    MustInLoop, IllegalConstantExpression, IllegalArrayLiteral,
    IllegalMemberAccess, NoEntryPoint
)


class Scope:
    GLOBAL = 0
    CLASS = 1
    METHOD = 2
    BLOCK = 3

class VarAttInfo:
    def __init__(
        self,
        is_final: bool,
        _type: Any,
        info: Variable|Attribute,
        is_static: bool = False,
        owned_cls: str = ""
    ) -> None:
        self.is_final: bool = is_final
        self.is_static: bool = is_static
        self._type: Any = _type
        self.info: Variable|Attribute = info
        self.owned_cls: str = owned_cls

    def __str__(self) -> str:
        return f"""
            is_final = {self.is_final}
            is_static = {self.is_static}
            type = {self._type}
            info = {self.info.__str__()}
            owned_cls = {self.owned_cls}
        """

class MethodInfo:
    def __init__(self, owned_cls: str, info: MethodDecl):
        assert isinstance(info.return_type, (PrimitiveType, ArrayType, ClassType)), f"info.return_type should not be {type(info.return_type)} in MethodInfo()"
        self.return_type: Union[PrimitiveType, ArrayType, ClassType] = info.return_type

        self.name = info.name
        self.owned_cls = owned_cls
        self.is_static: bool = info.is_static
        self.params: list[Parameter] = info.params
        self.bodies: dict[str, BlockStatement] = {owned_cls: info.body}

    def __str__(self) -> str:
        return f"""
            return_type = {self.return_type},
            owned_cls = {self.owned_cls},
            is_static = {self.is_static},
            params = {self.params},
            bodies = {self.bodies}
        """

class StaticChecker(ASTVisitor):
    """
    Stateless static semantic checker for OPLang using visitor pattern.
    
    Checks for all 10 error types specified in OPLang semantic constraints:
    1. Redeclared - Variables, constants, attributes, classes, methods, parameters
    2. Undeclared - Identifiers, classes, attributes, methods  
    3. CannotAssignToConstant - Assignment to final variables/attributes
    4. TypeMismatchInStatement - Type incompatibilities in statements
    5. TypeMismatchInExpression - Type incompatibilities in expressions
    6. TypeMismatchInConstant - Type incompatibilities in constant declarations
    7. MustInLoop - Break/continue outside loop contexts
    8. IllegalConstantExpression - Invalid expressions in constant initialization
    9. IllegalArrayLiteral - Inconsistent types in array literals
    10. IllegalMemberAccess - Improper access to static/instance members

    Also checks for valid entry point: static void main() with no parameters.
    """
    first_time = True # for filling symbol_dict without actually checking for symbol

    CLASS_TXT = "Class"
    ATT_TXT = "Attribute"
    METHOD_TXT = "Method"
    PARAM_TXT = "Parameter"
    CONST_TXT = "Constant"
    VAR_TXT = "Variable"
    ID_TXT = "Identifier"
    CONSTRUC_TXT = "Constructor"

    MATH_BIN_OP = ["+", "-", "*", "/"]
    INT_MATH_BIN_OP = ["%"]
    INT_COMPARION_BIN_OP = ["==", "!="]
    COMPARISON_BIN_OP = [">", ">=", "<", "<="]
    LOGICAL_BIN_OP = ["&&", "||"]


    def get_io_class(self) -> ClassDecl:
        readInt = MethodDecl(
            is_static=True,
            return_type=PrimitiveType("int"),
            name="readInt",
            params=[],
            body=BlockStatement(
                var_decls=[],
                statements=[]
            ),
        )

        writeInt = MethodDecl(
            is_static=True,
            return_type=PrimitiveType("void"),
            name="writeInt",
            params=[Parameter(
                PrimitiveType("int"),
                name="anArg",
            )],
            body=BlockStatement(
                var_decls=[],
                statements=[]
            ),
        )

        writeIntLn = MethodDecl(
            is_static=True,
            return_type=PrimitiveType("void"),
            name="writeIntLn",
            params=[Parameter(
                PrimitiveType("int"),
                name="anArg",
            )],
            body=BlockStatement(
                var_decls=[],
                statements=[]
            ),
        )

        readFloat = MethodDecl(
            is_static=True,
            return_type=PrimitiveType("float"),
            name="readFloat",
            params=[],
            body=BlockStatement(
                var_decls=[],
                statements=[]
            ),
        )

        writeFloat = MethodDecl(
            is_static=True,
            return_type=PrimitiveType("void"),
            name="writeFloat",
            params=[Parameter(
                PrimitiveType("float"),
                name="anArg",
            )],
            body=BlockStatement(
                var_decls=[],
                statements=[]
            ),
        )

        writeFloatLn = MethodDecl(
            is_static=True,
            return_type=PrimitiveType("void"),
            name="writeFloatLn",
            params=[Parameter(
                PrimitiveType("float"),
                name="anArg",
            )],
            body=BlockStatement(
                var_decls=[],
                statements=[]
            ),
        )

        readBool = MethodDecl(
            is_static=True,
            return_type=PrimitiveType("boolean"),
            name="readBool",
            params=[],
            body=BlockStatement(
                var_decls=[],
                statements=[]
            ),
        )

        writeBool = MethodDecl(
            is_static=True,
            return_type=PrimitiveType("void"),
            name="writeBool",
            params=[Parameter(
                PrimitiveType("boolean"),
                name="anArg",
            )],
            body=BlockStatement(
                var_decls=[],
                statements=[]
            ),
        )

        writeBoolLn = MethodDecl(
            is_static=True,
            return_type=PrimitiveType("void"),
            name="writeBoolLn",
            params=[Parameter(
                PrimitiveType("boolean"),
                name="anArg",
            )],
            body=BlockStatement(
                var_decls=[],
                statements=[]
            ),
        )

        readStr = MethodDecl(
            is_static=True,
            return_type=PrimitiveType("string"),
            name="readStr",
            params=[],
            body=BlockStatement(
                var_decls=[],
                statements=[]
            ),
        )

        writeStr = MethodDecl(
            is_static=True,
            return_type=PrimitiveType("void"),
            name="writeStr",
            params=[Parameter(
                PrimitiveType("string"),
                name="anArg",
            )],
            body=BlockStatement(
                var_decls=[],
                statements=[]
            ),
        )

        writeStrLn = MethodDecl(
            is_static=True,
            return_type=PrimitiveType("void"),
            name="writeStrLn",
            params=[Parameter(
                PrimitiveType("string"),
                name="anArg",
            )],
            body=BlockStatement(
                var_decls=[],
                statements=[]
            ),
        )

        return ClassDecl(
            name="io",
            superclass=None,
            members=[
                readInt, writeInt, writeIntLn,
                readFloat, writeFloat, writeFloatLn,
                readBool, writeBool, writeBoolLn,
                readStr, writeStr, writeStrLn,
            ]
        )

    def IllegalConstantExpression_check(
            self,
            decl: Union[VariableDecl, AttributeDecl],
            init_val: Optional[Any],
            o: list[dict],
    ):
        if not decl.is_final: return
        if not init_val: raise IllegalConstantExpression(decl)
        decl_type = None
        init_type = self.visit(init_val, o)
        assert isinstance(init_type, (str, ArrayLiteral, ObjectCreation))
        if isinstance(init_type,(ObjectCreation)): raise IllegalConstantExpression(decl)
        init_type = self.get_type_name(init_type)

        if isinstance(decl, VariableDecl): decl_type = decl.var_type
        elif isinstance(decl, AttributeDecl): decl_type = decl.attr_type
        assert decl_type, f"decl_type None in IllegalConstantExpression_check"
        if self.compare_type(init_type, "void", o):
            raise IllegalConstantExpression(decl)

    def _check_undecl_class(self, class_type: Any, o: list[dict]):
        if not isinstance(class_type, ClassType):
            return
        if not o[0].get(class_type.class_name, None):
            raise UndeclaredClass(class_type.class_name)

    def is_constant_expression(self, expr: Any, o: list[dict]) -> bool:
        """
        Check if an expression is a valid constant expression.
        Constant expressions can only contain:
        - Literals (int, float, bool, string, array literals with constant elements)
        - References to other final attributes
        - Operators (no method calls, no array access, no mutable variable access)
        """
        # Literal types are always constant
        if isinstance(expr, (IntLiteral, FloatLiteral, BoolLiteral, StringLiteral)):
            return True
        
        # Nil is not allowed in constant expressions
        if isinstance(expr, NilLiteral) or not expr:
            return False
        
        # Array literals must have all constant elements
        if isinstance(expr, ArrayLiteral):
            for element in expr.value:
                if not self.is_constant_expression(element, o):
                    return False
            return True
        
        # Binary operations are allowed if both operands are constant
        if isinstance(expr, BinaryOp):
            return (self.is_constant_expression(expr.left, o) and 
                   self.is_constant_expression(expr.right, o))
        
        # Unary operations are allowed if operand is constant
        if isinstance(expr, UnaryOp):
            return self.is_constant_expression(expr.operand, o)
        
        # Parenthesized expressions - check inner expression
        if isinstance(expr, ParenthesizedExpression):
            return self.is_constant_expression(expr.expr, o)
        
        # Identifier - must be a final attribute, not a mutable variable
        if isinstance(expr, Identifier):
            # Look up the identifier in scopes
            for scope in reversed(o):
                if expr.name in scope:
                    var_info = scope[expr.name]
                    if isinstance(var_info, VarAttInfo):
                        # Must be final to be used in constant expression
                        return var_info.is_final
                    break
            return False
        
        # Method calls, object creation, array access, this, member access not allowed
        if isinstance(expr, (MethodCall, ObjectCreation, ArrayAccess, ThisExpression, 
                           PostfixExpression, MemberAccess)):
            return False
        
        # Default: not a constant expression
        return False

    def must_in_loop_check(self, o: list[dict], node: Union[BreakStatement, ContinueStatement]):
        for scope in o:
            if "for stmt" in scope:
                return
        raise MustInLoop(node)

    def undeclared_check(self, o: list[dict], name: str, kind: str):
        for scope in o:
            if name in scope.keys():
                return
        match kind:
            case self.CLASS_TXT:
                raise UndeclaredClass(name)
            case self.ATT_TXT:
                raise UndeclaredAttribute(name)
            case self.METHOD_TXT:
                raise UndeclaredMethod(name)
            case self.ID_TXT:
                raise UndeclaredIdentifier(name)

    def redeclared_check(self, o: list[dict], name: str, kind: str, exception: list[str] = []):
        for scope in o:
            if name in scope.keys():
                raise Redeclared(kind, name)

    def get_type_name(self, typ: Union[PrimitiveType, ArrayType, ClassType, ObjectCreation, str]) -> str:
        if isinstance(typ, PrimitiveType): return typ.type_name
        elif isinstance(typ, ArrayType): 
            if isinstance(typ.element_type, (PrimitiveType, ArrayType, ClassType)):
                return self.get_type_name(typ.element_type)
        elif isinstance(typ, ClassType): return typ.class_name
        elif isinstance(typ, ObjectCreation): return typ.class_name
        assert type(typ) is str, f"typ should not be {type(typ)} in get_type_name"
        return typ

    def compare_type(
        self,
        lhs: Union[PrimitiveType, ArrayType, ClassType, str],
        rhs: Union[str, ArrayLiteral, ObjectCreation, PrimitiveType, ArrayType, ClassType],
        o: list[dict],
        coercible: bool = True,
    ) -> bool:
        lhs_type = None
        rhs_type = None

        # Handle ArrayType vs ArrayType comparison
        if type(lhs) is ArrayType and type(rhs) is ArrayType:
            # Check if sizes match
            if lhs.size != rhs.size:
                return False
            # Recursively check element types
            return self.compare_type(lhs.element_type, rhs.element_type, o, coercible)

        if type(lhs) is ArrayType and type(rhs) is ArrayLiteral:
            lhs_type = lhs.element_type

            if lhs.size != len(rhs.value): return False

            if type(rhs.value) != list or len(rhs.value) <= 0:
                return False
            rhs_type = self.visit(rhs.value[0])
            assert isinstance(rhs_type, (str, ArrayLiteral, ObjectCreation)), f"Unknown rhs_type in comp_type"
            assert isinstance(lhs_type, (PrimitiveType, ArrayType, ClassType, str)), f"Unknown rhs_type in comp_type"
            return self.compare_type(lhs_type, rhs_type, o, False)

        if type(lhs) is PrimitiveType:
            lhs_type = lhs.type_name
        elif type(lhs) is str:
            lhs_type = lhs
        
        if type(rhs) is PrimitiveType:
            rhs_type = rhs.type_name
        elif type(rhs) is str:
            rhs_type = rhs

        # check void lhs
        if lhs_type == "void":
            return False

        if type(lhs) is ClassType:
            if not isinstance(rhs, (ObjectCreation, str, ClassType)): return False
            if isinstance(rhs, ObjectCreation): 
                rhs_type = rhs.class_name
            elif isinstance(rhs, ClassType): 
                rhs_type = rhs.class_name
            else:  # rhs is str
                rhs_type = rhs
                # If rhs is a primitive type name, not compatible with ClassType
                if rhs_type in ["int", "float", "boolean", "string", "void"]:
                    return False
            
            lhs_class: Optional[ClassDecl] = o[0].get(lhs.class_name, None)
            rhs_class: Optional[ClassDecl] = o[0].get(rhs_type, None)
            assert lhs_class, "lhs_class is None in comp_type"
            if not rhs_class:
                # rhs_type is not a valid class
                return False
            
            # Exact match
            if lhs_class.name == rhs_type:
                return True
            
            # Coercion: can assign child to parent (RHS is child of LHS)
            # Check if RHS's superclass chain contains LHS
            if coercible:
                current = rhs_class
                while current.superclass:
                    if current.superclass == lhs_class.name:
                        return True
                    current = o[0].get(current.superclass, None)
                    if not current:
                        break
            
            return False

        assert lhs_type, "lhs_type is None in comp_type"
        assert rhs_type, "rhs_type is None in comp_type"
        if coercible and lhs_type == "float" and rhs_type == "int":
            return True
        return lhs_type == rhs_type

    def check_program(self, node):
        self.visit(node)

    def visit_program(self, node: "Program", o: Any = None):
        o_with_io = self.visit(self.get_io_class(), [{}])
        assert type(o_with_io) is list, f"o_with_io is {type(o_with_io)} not list[dict] in visit_program"

        # filling symbol_dict
        self.first_time = True
        o_filled = reduce(lambda class_names, class_decl: self.visit(class_decl, class_names), node.class_decls, o_with_io)

        # checking with filled symbol_dict (useful for OOP)
        self.first_time = False
        reduce(lambda class_names, class_decl: self.visit(class_decl, class_names), node.class_decls, o_filled)

    def visit_class_decl(self, node: "ClassDecl", o: list[dict] = [{}]) -> list[dict] | None: # type: ignore[reportIncompatibleMethodOverride]
        if self.first_time:
            # Redeclared Check
            if node.name in o[0].keys():
                raise Redeclared(self.CLASS_TXT, node.name)

            # visit children - add class scope
            o[0][node.name] = node

        # Check UndeclaredClass superclass
        if node.superclass:
            super_class = o[0].get(node.superclass, None)
            if not super_class:
                raise UndeclaredClass(node.superclass)

        # NOTE: symbol_dict special key no.4: "current class"
        o[0]["current class"] = node.name
        o[0]["current superclass"] = node.superclass

        o_with_class = o + [{}] if self.first_time else o  # Add CLASS scope
        o_with_class = reduce(lambda names, member: self.visit(member, names), node.members, o_with_class)
        return o_with_class

    def visit_attribute_decl(self, node: "AttributeDecl", o: list[dict] = [{}]) -> list[dict] | None: # type: ignore[reportIncompatibleMethodOverride]
        self._check_undecl_class(node.attr_type, o)
        obj = reduce(lambda acc, att: self.visit(att, (acc, node)), node.attributes, o)
        return obj

    def visit_attribute(self, node: "Attribute", o: Tuple[list[dict], AttributeDecl] = [{}]) -> list[dict] | None: # type: ignore[reportIncompatibleMethodOverride]
        obj = o[0]
        att_decl: AttributeDecl = o[1]

        # Redeclared Check
        if self.first_time:
            for scope in obj:
                same_att = scope.get(node.name, None)
                if same_att:
                    if not isinstance(same_att, VarAttInfo):
                        raise Redeclared(self.ATT_TXT, node.name)
                    if not isinstance(same_att.info, Attribute) or same_att.owned_cls == obj[0]["current class"]:
                        raise Redeclared(self.ATT_TXT, node.name)

        if node.init_value:
            # Check if constant expression is valid for final attributes
            if att_decl.is_final:
                if not self.is_constant_expression(node.init_value, obj):
                    raise IllegalConstantExpression(att_decl)
            
            if att_decl.is_final: obj[0]["assigning constant"] = True
            init_val = self.visit(node.init_value, obj)

            if isinstance(att_decl.attr_type, (PrimitiveType, ArrayType, ClassType)) and isinstance(init_val, (str, ArrayLiteral, ObjectCreation)):
                if not self.compare_type(att_decl.attr_type, init_val, obj):
                    if att_decl.is_final: raise TypeMismatchInConstant(att_decl)
                    else: raise TypeMismatchInStatement(att_decl)
        elif att_decl.is_final and att_decl.is_static:
            # Static final attributes must be initialized at declaration
            # Instance final attributes can be initialized in constructors
            raise IllegalConstantExpression(att_decl)

        obj[1][node.name] = VarAttInfo(is_final=att_decl.is_final, _type=att_decl.attr_type, info=node, is_static=att_decl.is_static, owned_cls=obj[0]["current class"])
        return obj

    def visit_method_decl(self, node: "MethodDecl", o: Any = None):
        # Redeclared Check
        if self.first_time:
            # Check if method is redeclared in the CURRENT class only (not parent classes)
            # MethodInfo has owned_cls, so check if there's already a method with same name and same class
            current_class_name = o[0]["current class"]
            if node.name in o[1].keys():
                existing = o[1][node.name]
                if isinstance(existing, MethodInfo) and (existing.owned_cls == current_class_name):
                    raise Redeclared(self.METHOD_TXT, node.name)
                # Method cannot have the same name as an attribute in the same class
                if isinstance(existing, VarAttInfo) and existing.owned_cls == current_class_name:
                    raise Redeclared(self.METHOD_TXT, node.name)
            
            o[1][node.name] = MethodInfo(o[0]["current class"], node)
            return o

        # visit children - add method and block scopes
        o_method = o[:2] + [{}]  # Create METHOD scope - use only GLOBAL and CLASS scopes, discard any METHOD scope from previous method
        # Store the current method info (MethodInfo from first pass) so we can access it from return statements
        # NOTE: symbol_dict special key no.3: "current method"
        method_info = o[1].get(node.name)  # Get the MethodInfo stored in first pass
        o_method[2]['current method'] = method_info  # Store in METHOD scope (o_method[2])
        o_params: list = reduce(lambda acc, param: self.visit(param, acc), node.params, o_method)
        o_block = o_params + [{}]  # Add BLOCK scope for variables
        o_vars_params = reduce(lambda acc, var_decl: self.visit(var_decl, acc), node.body.var_decls, o_block)
        reduce(lambda acc, stmt: self.visit(stmt, acc), node.body.statements, o_vars_params)
        return o[:2]  # Return only GLOBAL and CLASS scopes, discard METHOD scope

    def visit_parameter(self, node: "Parameter", o: Any = None):
        self.redeclared_check(o[2:], node.name, self.PARAM_TXT)

        o[2][node.name] = VarAttInfo(False, node.param_type, Variable(node.name, None), False)  # Add to METHOD scope (o[2])
        return o

    def visit_variable_decl(self, node: "VariableDecl", o: Any = None):
        self._check_undecl_class(node.var_type, o)
        return reduce(lambda vars, var: self.visit(var, (vars, node)), node.variables, o)

    def visit_variable(self, node: "Variable", o: Any = None):
        obj = o[0]
        var_decl: VariableDecl = o[1]

        err_txt = self.CONST_TXT if var_decl.is_final else self.VAR_TXT

        # Assign to Nil
        if var_decl.is_final:
            if not node.init_value or node.init_value is NilLiteral:
                raise IllegalConstantExpression(node.init_value)

        # Check current scope (BLOCK) for redeclaration of variables
        current_scope = obj[-1]
        if node.name in current_scope:
            same_att = current_scope[node.name]
            if not isinstance(same_att, VarAttInfo):
                raise Redeclared(err_txt, node.name)
            # Variables/constants cannot be redeclared in the same scope
            if isinstance(same_att.info, Variable):
                raise Redeclared(err_txt, node.name)

        # Check METHOD scope (always at index 2) for parameters
        # obj structure: [GLOBAL, CLASS, METHOD, BLOCK, ...nested blocks...]
        # METHOD scope is always at index 2, regardless of nested blocks
        if len(obj) >= 4:
            method_scope = obj[2]  # METHOD scope is always at index 2
            if node.name in method_scope:
                # Cannot redeclare a parameter as a variable
                raise Redeclared(err_txt, node.name)

        # Check all scopes for methods (can't have variable with same name as method)
        for scope in obj:
            same_att = scope.get(node.name, None)
            if same_att:
                if not isinstance(same_att, VarAttInfo):
                    raise Redeclared(err_txt, node.name)

        if node.init_value:
            # Check if constant expression is valid for final variables
            if var_decl.is_final:
                if not self.is_constant_expression(node.init_value, obj):
                    raise IllegalConstantExpression(node.init_value)
            
            init_val = self.visit(node.init_value, (obj, var_decl.var_type))
            if isinstance(var_decl.var_type, (PrimitiveType, ArrayType, ClassType)) and isinstance(init_val, (str, ArrayLiteral, ObjectCreation, PrimitiveType, ArrayType, ClassType)):
                if not self.compare_type(var_decl.var_type, init_val, obj):
                    if var_decl.is_final: raise TypeMismatchInConstant(var_decl)
                    else: raise TypeMismatchInStatement(var_decl)

        obj[-1][node.name] = VarAttInfo(var_decl.is_final, var_decl.var_type, node)
        return obj

    def visit_assignment_statement(self, node: "AssignmentStatement", o: list[dict] = [{}]): # type: ignore[reportIncompatibleMethodOverride]
        lhs = self.visit(node.lhs, o)
        rhs = self.visit(node.rhs, o)

        can_init_final = False

        if isinstance(lhs, VarAttInfo):
            for scope in o:
                if scope.get("can init final", None):
                    can_init_final = True
            if lhs.is_final and not can_init_final: raise CannotAssignToConstant(node)

        # Extract type from VarAttInfo if needed
        rhs_type = rhs
        if isinstance(rhs, VarAttInfo):
            rhs_type = rhs._type

        if isinstance(lhs, VarAttInfo) and isinstance(rhs_type, (str, PrimitiveType, ArrayType, ClassType, ObjectCreation, ArrayLiteral)):
            if not self.compare_type(lhs._type, rhs_type, o):
                raise TypeMismatchInStatement(node)

        return o

    def visit_id_lhs(self, node: "IdLHS", o: Any = None):
        self.undeclared_check(o=o, name=node.name, kind=self.ID_TXT)
        result = next(filter(lambda value: value is not None, (scope.get(node.name, None) for scope in reversed(o))))
        return result

    def visit_postfix_lhs(self, node: "PostfixLHS", o: Any = None):
        # For LHS, we need to preserve VarAttInfo to check if it's final
        obj = o if type(o) is list else o[0]
        primary = self.visit(node.postfix_expr.primary, obj)
        op = reduce(lambda acc, op: self.visit(op, (obj, acc)), node.postfix_expr.postfix_ops, primary)
        
        # Return the VarAttInfo directly for LHS (don't extract type)
        # This allows visit_assignment_statement to check if it's final
        if isinstance(op, VarAttInfo):
            return op
        
        # For non-VarAttInfo, check if it's a valid type
        if isinstance(op, IllegalMemberAccess): raise IllegalMemberAccess(node.postfix_expr)
        if not isinstance(op, (PrimitiveType, ArrayType, ClassType)): raise TypeMismatchInExpression(node.postfix_expr)
        return op

    def visit_postfix_expression(self, node: "PostfixExpression", o: Any = None): # type: ignore[reportIncompatibleMethodOverride]
        obj = o if type(o) is list else o[0]
        parent = None if type(o) is list else o[1]
        primary = self.visit(node.primary, obj)
        op = reduce(lambda acc, op: self.visit(op, (obj, acc)), node.postfix_ops, primary)
        
        # If op is VarAttInfo, extract the type
        if isinstance(op, VarAttInfo):
            op = op._type
        
        if isinstance(op, IllegalMemberAccess): raise IllegalMemberAccess(node)
        if not isinstance(op, (PrimitiveType, ArrayType, ClassType)): raise TypeMismatchInExpression(node)
        if self.get_type_name(op) == "void" and not isinstance(parent, MethodInvocationStatement): raise TypeMismatchInExpression(node)
        return op

    def _find_attribute_in_class(self, class_decl: ClassDecl, attr_name: str) -> Optional[tuple[AttributeDecl, Attribute]]:
        """Find an attribute in a class by searching through members"""
        # Get all AttributeDecl members
        attr_decls = list(filter(lambda m: isinstance(m, AttributeDecl), class_decl.members))
        
        # For each AttributeDecl, find the matching Attribute
        for attr_decl in attr_decls:
            attr = next(filter(lambda a: a.name == attr_name, attr_decl.attributes), None)
            if attr:
                return (attr_decl, attr)
        
        return None
    
    def _find_attribute_in_hierarchy(self, obj: list, class_decl: ClassDecl, attr_name: str) -> Optional[tuple[AttributeDecl, Attribute, str]]:
        """Find an attribute in a class or its inheritance hierarchy, returns (attr_decl, attr, owner_class_name)"""
        # Check in the current class
        result = self._find_attribute_in_class(class_decl, attr_name)
        if result:
            return (result[0], result[1], class_decl.name)
        
        # Check in the superclass recursively
        if class_decl.superclass:
            superclass = obj[0].get(class_decl.superclass, None)
            if superclass and isinstance(superclass, ClassDecl):
                return self._find_attribute_in_hierarchy(obj, superclass, attr_name)
        
        return None

    def visit_member_access(self, node: "MemberAccess", o: Union[tuple[list, Any],list] = [{}]): # type: ignore[reportIncompatibleMethodOverride]
        obj: list = o if type(o) is list else o[0]
        var = None if type(o) is list else o[1]
        
        # If var is a type (from a previous method call/expression), look up the member in that class
        if isinstance(var, ClassType):
            # Look up the class by name in the global scope
            class_name = var.class_name
            class_decl = obj[0].get(class_name, None)
            if class_decl is None:
                return UndeclaredClass(class_name)
            if not isinstance(class_decl, ClassDecl):
                return TypeMismatchInExpression(node)
            
            # Find the attribute in the class hierarchy
            result = self._find_attribute_in_hierarchy(obj, class_decl, node.member_name)
            if result:
                attr_decl, attr, owner_class = result
                return VarAttInfo(attr_decl.is_final, attr_decl.attr_type, attr, attr_decl.is_static, owner_class)
            
            # Attribute not found in the class hierarchy
            return UndeclaredAttribute(node.member_name)
        
        # Static member access via class name (e.g., Student.totalStudents)
        if isinstance(var, ClassDecl):
            # Find the attribute in the class
            result = self._find_attribute_in_class(var, node.member_name)
            if result:
                attr_decl, attr = result
                # Check if accessing correctly (static via class name)
                if not attr_decl.is_static:
                    return IllegalMemberAccess(node)
                return VarAttInfo(attr_decl.is_final, attr_decl.attr_type, attr, attr_decl.is_static, var.name)
            
            # Attribute not found
            return TypeMismatchInExpression(node)
        
        # Instance member access via variable (e.g., student.name)
        if isinstance(var, VarAttInfo) and isinstance(var._type, ClassType):
            # Look up the class
            class_name = var._type.class_name
            class_decl = obj[0].get(class_name, None)
            if class_decl is None or not isinstance(class_decl, ClassDecl):
                return TypeMismatchInExpression(node)
            
            # Find the attribute in the class hierarchy
            result = self._find_attribute_in_hierarchy(obj, class_decl, node.member_name)
            if result:
                attr_decl, attr, owner_class = result
                # Check if accessing correctly (instance via variable)
                if attr_decl.is_static:
                    return IllegalMemberAccess(node)
                return VarAttInfo(attr_decl.is_final, attr_decl.attr_type, attr, attr_decl.is_static, owner_class)
            
            # Attribute not found
            raise UndeclaredAttribute(node.member_name)
        
        # Original behavior for normal member access
        self.undeclared_check(o=obj, name=node.member_name, kind=self.ID_TXT)
        member = next(filter(lambda value: value is not None, (scope.get(node.member_name, None) for scope in reversed(obj))))
        return member

    def visit_array_access(self, node: "ArrayAccess", o: Any = None): # type: ignore[reportIncompatibleMethodOverride]
        obj = o if type(o) is list else o[0]
        assert type(obj) is list, f"obj is {type(obj)} not list in visit_array_access"

        idx = self.visit(node.index, o)
        var = None if type(o) is list else o[1]

        assert isinstance(idx, (str, PrimitiveType, ClassType, ArrayType)), f"idx should not be {type(idx)} in visit_array_access"
        if isinstance(var, VarAttInfo):
            if not isinstance(var._type, ArrayType):
                return TypeMismatchInExpression(node)
            if not self.compare_type(idx, "int", obj):
                return TypeMismatchInExpression(node)
            # Return the element type, not the array type
            return var._type.element_type

    def _find_method_in_hierarchy(self, class_decl: ClassDecl, method_name: str, o: list[dict]) -> Optional[MethodDecl]:
        """Recursively search for a method in the class hierarchy"""
        # Search in current class
        method = next(filter(lambda m: isinstance(m, MethodDecl) and m.name == method_name, class_decl.members), None)
        
        if method:
            assert isinstance(method, MethodDecl), f"method should not be {type(method)} in _find_method_in_hierarchy"
            return method
        
        # If not found and has superclass, search in parent
        if class_decl.superclass:
            parent_class = o[0].get(class_decl.superclass, None)
            if parent_class and isinstance(parent_class, ClassDecl):
                return self._find_method_in_hierarchy(parent_class, method_name, o)
        
        return None

    def visit_method_call(self, node: "MethodCall", o: Union[tuple,list] = [{}]): # type: ignore[reportIncompatibleMethodOverride]
        obj:list[dict] = o if type(o) is list else o[0]

        var = None if type(o) is list else o[1]
        
        # Determine if this is an instance or static call based on var type
        # ClassDecl (from class name like 'io') → static call
        # ClassType (from method return or 'this') → instance call
        # VarAttInfo with ClassType (from variable) → instance call
        is_static = isinstance(var, ClassDecl)
        
        if isinstance(var, VarAttInfo) and isinstance(var._type, ClassType):
            var = var._type
            is_static = False  # Instance call through variable
        
        # If var is a type (from a previous method call), look up the class declaration
        class_decl = None
        if isinstance(var, ClassType):
            # Look up the class by name in the global scope
            class_name = var.class_name
            class_decl = obj[0].get(class_name, None)
            if class_decl is None or not isinstance(class_decl, ClassDecl):
                raise TypeMismatchInExpression(node)
        elif isinstance(var, ClassDecl):
            class_decl = var
        else:
            return TypeMismatchInExpression(node)

        # Find the method in the class hierarchy
        method = self._find_method_in_hierarchy(class_decl, node.method_name, obj)
        
        if method is None:
            raise UndeclaredMethod(node.method_name)

        assert isinstance(method, (MethodDecl))
        
        if method.is_static != is_static:
            return IllegalMemberAccess(node)

        if len(method.params) != len(node.args):
            return TypeMismatchInStatement(node)

        # Check all arguments match parameters using all()
        args_valid = all(
            self.compare_type(param.param_type, 
                             self.get_type_name(arg_result._type if isinstance(arg_result, VarAttInfo) else arg_result), 
                             obj)
            for idx, param in enumerate(method.params)
            if (arg_result := self.visit(node.args[idx], obj))
        )
        
        if not args_valid:
            return node

        if isinstance(method.return_type, (ArrayType, PrimitiveType, ClassType, str)) and self.get_type_name(method.return_type) != "void": 
            return method.return_type

        return PrimitiveType("void")

    def visit_binary_op(self, node: "BinaryOp", o: list[dict] = [{}]): # type: ignore[reportIncompatibleMethodOverride]
        o_left = self.visit(node.left, o)
        o_right = self.visit(node.right, o)
        if type(o_left) == VarAttInfo:
            o_left = self.visit(o_left._type, o)
        if type(o_right) == VarAttInfo:
            o_right = self.visit(o_right._type, o)

        assert isinstance(o_left, (str, PrimitiveType, ClassType, ArrayType)), f"o_left should not be {type(o_left)} in visit_binary_op"
        assert isinstance(o_right, (str, PrimitiveType, ClassType, ArrayType)), f"o_right should not be {type(o_right)} in visit_binary_op"

        # Division operators (/, \, %) always return float regardless of operand types
        if node.operator in ["/", "\\", "%"]:
            left_is_numeric = self.compare_type(o_left, "int", o) or self.compare_type(o_left, "float", o)
            right_is_numeric = self.compare_type(o_right, "int", o) or self.compare_type(o_right, "float", o)
            if left_is_numeric and right_is_numeric:
                return PrimitiveType("float")
            raise TypeMismatchInExpression(node)

        if node.operator == "^":
            if self.compare_type(o_left, "string", o) and self.compare_type(o_right, "string", o):
                return PrimitiveType("string")


        elif node.operator in self.INT_COMPARION_BIN_OP:
            if self.compare_type(o_left, "int", o) and self.compare_type(o_right, "int", o):
                return PrimitiveType("boolean")

        elif node.operator in self.MATH_BIN_OP + self.COMPARISON_BIN_OP:
            if self.compare_type(self.get_type_name(o_left), self.get_type_name(o_right), o):
                return PrimitiveType("boolean") if node.operator in self.COMPARISON_BIN_OP else o_left
            elif self.compare_type(o_left, "float", o) and self.compare_type(o_right, "int", o):
                return PrimitiveType("boolean") if node.operator in self.COMPARISON_BIN_OP else o_left
            elif self.compare_type(o_left, "int", o) and self.compare_type(o_right, "float", o):
                return PrimitiveType("boolean") if node.operator in self.COMPARISON_BIN_OP else o_right
        elif node.operator in self.LOGICAL_BIN_OP:
            if self.compare_type(o_left, "boolean", o) and self.compare_type(o_right, "boolean", o):
                return PrimitiveType("boolean")

        raise TypeMismatchInExpression(node)

    def visit_unary_op(self, node: "UnaryOp", o: Any = None):
        operand = self.visit(node.operand, o)
        
        # Extract type from VarAttInfo if needed
        if isinstance(operand, VarAttInfo):
            operand = operand._type
        
        # Handle negation (!)
        if node.operator == "!":
            if self.compare_type(operand, "boolean", o):
                return PrimitiveType("boolean")
        # Handle unary minus (-)
        elif node.operator == "-":
            if self.compare_type(operand, "int", o):
                return PrimitiveType("int")
            elif self.compare_type(operand, "float", o):
                return PrimitiveType("float")
        
        raise TypeMismatchInExpression(node)

    def visit_object_creation(self, node: "ObjectCreation", o: Union[tuple[list, Any], list] = ()): # type: ignore[reportIncompatibleMethodOverride]
        obj: list = o if type(o) is list else o[0]
        self.undeclared_check(obj, node.class_name, self.CLASS_TXT)
        list(map(lambda arg: self.visit(arg, o), node.args))
        return node

    def visit_identifier(self, node: "Identifier", o: Any = None):
        obj = o[0] if type(o) is tuple else o
        self.undeclared_check(obj, node.name, self.ID_TXT)
        result = next(filter(lambda value: value is not None, (scope.get(node.name, None) for scope in reversed(obj))))
        return result

    def visit_this_expression(self, node: "ThisExpression", o: Any = None): # type: ignore[reportIncompatibleMethodOverride]
        obj = o if type(o) is list else o[0]
        return ClassType(obj[0]["current class"])

    def visit_parenthesized_expression(self, node: "ParenthesizedExpression", o: Any = None):
        return self.visit(node.expr, o)

    def visit_int_literal(self, node: "IntLiteral", o: Any = None):
        return self.visit(PrimitiveType("int"), o)

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        return self.visit(PrimitiveType("float"))

    def visit_bool_literal(self, node: "BoolLiteral", o: Any = None):
        return self.visit(PrimitiveType("boolean"))

    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        return self.visit(PrimitiveType("string"))

    def visit_array_literal(self, node: "ArrayLiteral", o: Any = None): # type: ignore[reportIncompatibleMethodOverride]
        obj = o[0]
        typ: ArrayType = o[1]
        elems: list = list(map(lambda elem: self.visit(elem, o), node.value))
        
        # Check for IllegalArrayLiteral - all elements must have the same type
        if elems:
            first_elem_type = elems[0]
            for ele_type in elems[1:]:
                if ele_type != first_elem_type:
                    raise IllegalArrayLiteral(node)

        return node

    def visit_nil_literal(self, node: "NilLiteral", o: Any = None):
        return self.visit(PrimitiveType("void"))

    def visit_constructor_decl(self, node: "ConstructorDecl", o: list[dict] = [{}]): # type: ignore[reportIncompatibleMethodOverride]
        if self.first_time:
            self.redeclared_check(o[1:], node.name, self.METHOD_TXT)
            return o

        # Don't store current method for constructors - they can't have return statements
        o_method = o + [{}]  # Add METHOD scope for parameters
        o_params = reduce(lambda acc, param: self.visit(param, acc), node.params, o_method)
        assert type(o_params) is list, f"ConstructorDecl o_params is {type(o_params)} not list"
        # NOTE: symbol_dict's special key no.1 = "can init final"
        o_block = o_params + [{"can init final": True}]  # Add BLOCK scope for variables
        o_vars_params = reduce(lambda acc, var_decl: self.visit(var_decl, acc), node.body.var_decls, o_block)
        list(map(lambda stmt: self.visit(stmt, o_vars_params), node.body.statements))

        o[1][node.name] = MethodInfo(o[0]["current class"], MethodDecl(
            is_static=True,
            params=node.params,
            name=node.name,
            body=node.body,
            return_type=ClassType(o[0]["current class"])
        ))
        return o[:2]

    def visit_destructor_decl(self, node: "DestructorDecl", o: Any = None):
        if self.first_time:
            self.redeclared_check(o[2:], node.name, self.METHOD_TXT)
            return o

        o_block = o + [{}]  # Add BLOCK scope for variables
        o_vars = reduce(lambda acc, var_decl: self.visit(var_decl, acc), node.body.var_decls, o_block)
        list(map(lambda stmt: self.visit(stmt, o_vars), node.body.statements))

        o[1][node.name] = node
        return o[:2]

    def visit_if_statement(self, node: "IfStatement", o: list[dict] = [{}]): # type: ignore[reportIncompatibleMethodOverride]
        cond = self.visit(node.condition, o)
        if isinstance(cond, VarAttInfo):
            if isinstance(cond._type, PrimitiveType) and cond._type.type_name != "boolean":
                raise TypeMismatchInStatement(node)
        elif type(cond) is str and cond != "boolean":
            raise TypeMismatchInStatement(node)
        self.visit(node.then_stmt, o)
        if node.else_stmt:
            self.visit(node.else_stmt, o)

        return o

    def visit_for_statement(self, node: "ForStatement", o: Any = None):
        start_expr = self.visit(node.start_expr, o)
        end_expr = self.visit(node.end_expr, o)
        var: Optional[VarAttInfo] = next(filter(lambda value: value is not None, (scope.get(node.variable, None) for scope in reversed(o))), None)

        if not var:
            raise UndeclaredIdentifier(node.variable)

        if var.is_final:
            raise CannotAssignToConstant(node)
        if type(var._type) is PrimitiveType and var._type.type_name != "int":
            raise TypeMismatchInStatement(node)
        if start_expr != "int":
            raise TypeMismatchInStatement(node)
        if end_expr != "int":
            raise TypeMismatchInStatement(node)

        # Create a new scope for the for loop body and mark it
        # NOTE: symbol_dict's special key no.2 = "for stmt"
        o_for = o + [{"for stmt": node}]
        self.visit(node.body, o_for)
        # Return original scope without the for marker
        return o

    def visit_break_statement(self, node: "BreakStatement", o: Any = None):
        self.must_in_loop_check(o, node)
        return o

    def visit_continue_statement(self, node: "ContinueStatement", o: Any = None):
        self.must_in_loop_check(o, node)
        return o

    def visit_return_statement(self, node: "ReturnStatement", o: list[dict] = [{}]): # type: ignore[reportIncompatibleMethodOverride]
        val = self.visit(node.value, o)
        # Get the current method from the method scope (o[2])
        method: Optional[MethodInfo] = o[2].get('current method')
        assert isinstance(method, MethodInfo), f"method should be MethodInfo in visit_return_statement, got {type(method)}"
        assert isinstance(method.return_type, (PrimitiveType, ArrayType, ClassType, str)) and val
        
        # Extract type from VarAttInfo if needed
        val_type = val._type if isinstance(val, VarAttInfo) else val
        
        if not self.compare_type(method.return_type, self.get_type_name(val_type), o):
            raise TypeMismatchInStatement(node)
        return o

    def visit_method_invocation_statement(self, node: "MethodInvocationStatement", o: Any = None):
        method_call = self.visit(node.method_call, (o, node))
        if isinstance(method_call, (ArrayType, PrimitiveType, ClassType, str)) and self.get_type_name(method_call) != "void": raise TypeMismatchInStatement(node)
        return o

    def visit_block_statement(self, node: "BlockStatement", o: Any = None):
        o_block = o + [{}]  # Add new BLOCK scope
        o_vars = reduce(lambda acc, var_decl: self.visit(var_decl, acc), node.var_decls, o_block)
        list(map(lambda stmt: self.visit(stmt, o_vars), node.statements))
        return o

    def visit_primitive_type(self, node: "PrimitiveType", o: Any = None): # type: ignore[reportIncompatibleMethodOverride]
        return node.type_name

    def visit_array_type(self, node: "ArrayType", o: Any = None): # type: ignore[reportIncompatibleMethodOverride]
        return node.element_type

    def visit_class_type(self, node: "ClassType", o: Any = None): # type: ignore[reportIncompatibleMethodOverride]
        self.undeclared_check(o, node.class_name, self.CLASS_TXT)
        return node

    def visit_reference_type(self, node: "ReferenceType", o: Any = None):
        self.visit(node.referenced_type, o)

    def visit_static_method_invocation(self, node: "MethodCall", o: Any = None):
        list(map(lambda arg: self.visit(arg, o), node.args))

    def visit_static_member_access(self, node: "StaticMemberAccess", o: Any = None):
        pass

    def visit_method_invocation(self, node: "MethodInvocation", o: Any = None):
        pass
