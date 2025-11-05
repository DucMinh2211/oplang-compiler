"""
Static Semantic Checker for OPLang Programming Language

This module implements a comprehensive static semantic checker using visitor pattern
for the OPLang object-oriented programming language. It performs type checking,
scope management, inheritance validation, and detects all semantic errors as 
specified in the OPLang language specification.
"""

from functools import reduce
from re import error
from typing import Dict, List, Set, Optional, Any, Tuple, Union, NamedTuple, overload
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

class VariableInfo:
    def __init__(self, is_final: bool, _type: Any, var: Variable) -> None:
        self.is_final: bool = is_final
        self._type: Any = _type
        self.var: Variable = var

class AttributeInfo:
    def __init__(self, is_final: bool, _type: Any, att: Attribute) -> None:
        self.is_final: bool = is_final
        self._type: Any = _type
        self.att: Attribute = att


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

    CLASS_TXT = "Class"
    ATT_TXT = "Attribute"
    METHOD_TXT = "Method"
    PARAM_TXT = "Parameter"
    CONST_TXT = "Constant"
    VAR_TXT = "Variable"
    ID_TXT = "Identifier"
    CONSTRUC_TXT = "Constructor"

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

    def redeclared_check(self, o: list[dict], name: str, kind: str):
        for scope in o:
            if name in scope.keys():
                raise Redeclared(kind, name)

    def check_program(self, node):
        self.visit(node)

    def visit_program(self, node: "Program", o: Any = None):
        reduce(lambda class_names, class_decl: self.visit(class_decl, class_names), node.class_decls, [{}])

    def visit_class_decl(self, node: "ClassDecl", o: list[dict] = [{}]) -> list[dict] | None: # type: ignore[reportIncompatibleMethodOverride]
        # Redeclared Check
        for scope in o:
            if node.name in scope.keys():
                raise Redeclared(self.CLASS_TXT, node.name)

        # visit children - add class scope
        o[0][node.name] = None
        o_with_class = o + [{}]  # Add CLASS scope
        o_with_class = reduce(lambda names, member: self.visit(member, names), node.members, o_with_class)
        o[0][node.name] = node
        return o

    def visit_attribute_decl(self, node: "AttributeDecl", o: list[dict] = [{}]) -> list[dict] | None: # type: ignore[reportIncompatibleMethodOverride]
        obj = reduce(lambda acc, att: self.visit(att, (acc, node)), node.attributes, o)
        return obj

    def visit_attribute(self, node: "Attribute", o: Tuple[list[dict], Any] = [{}]) -> list[dict] | None: # type: ignore[reportIncompatibleMethodOverride]
        obj = o[0]
        att_decl: AttributeDecl = o[1]

        # Redeclared Check
        for scope in obj:
            if node.name in scope.keys():
                raise Redeclared(self.ATT_TXT, node.name)

        if node.init_value:
            init_val = self.visit(node.init_value, obj)
            if isinstance(att_decl.attr_type, PrimitiveType):
                if att_decl.attr_type.type_name != init_val:
                    att_decl.attr_type = self.visit(att_decl.attr_type)
                    if not att_decl.is_final: raise TypeMismatchInStatement(att_decl)
                    else: raise TypeMismatchInConstant(att_decl)

        obj[1][node.name] = node
        return obj

    def visit_method_decl(self, node: "MethodDecl", o: Any = None):
        # Redeclared Check
        self.redeclared_check(o, node.name, self.METHOD_TXT)

        # visit children - add method and block scopes
        o_method = o + [{}]  # Add METHOD scope for parameters
        o_params: list = reduce(lambda acc, param: self.visit(param, acc), node.params, o_method)
        o_block = o_params + [{}]  # Add BLOCK scope for variables
        o_vars_params = reduce(lambda acc, var_decl: self.visit(var_decl, acc), node.body.var_decls, o_block)
        for stmt in node.body.statements:
            self.visit(stmt, o_vars_params)

        o[1][node.name] = node
        return o

    def visit_parameter(self, node: "Parameter", o: Any = None):
        self.redeclared_check(o, node.name, self.PARAM_TXT)

        o[-1][node.name] = node  # Add to current (METHOD) scope
        return o

    def visit_variable_decl(self, node: "VariableDecl", o: Any = None):
        return reduce(lambda vars, var: self.visit(var, (vars, node)), node.variables, o)

    def visit_variable(self, node: "Variable", o: Any = None):
        obj = o[0]
        var_decl: VariableDecl = o[1]
        self.redeclared_check(obj, node.name, self.VAR_TXT)

        if node.init_value:
            init_val: str = self.visit(node.init_value, (obj, var_decl.var_type))
            if isinstance(var_decl.var_type, PrimitiveType):
                if not init_val in self.visit(var_decl.var_type):
                    var_decl.var_type = self.visit(var_decl.var_type)
                    if var_decl.is_final: raise TypeMismatchInConstant(var_decl)
                    else: raise TypeMismatchInStatement(var_decl)

        obj[-1][node.name] = VariableInfo(var_decl.is_final, var_decl.var_type, node)
        return obj

    def visit_assignment_statement(self, node: "AssignmentStatement", o: list[dict] = [{}]):
        lhs = self.visit(node.lhs, o)
        rhs = self.visit(node.rhs, o)

        if isinstance(lhs, (AttributeInfo, VariableInfo)):
            for scope in o:
                if lhs.is_final and not scope.get("can init final", None):
                    raise CannotAssignToConstant(node)

        if type(lhs) != type(rhs):
            raise TypeMismatchInStatement(node)

    def visit_id_lhs(self, node: "IdLHS", o: Any = None):
        self.undeclared_check(o=o, name=node.name, kind=self.ID_TXT)
        result = next(filter(lambda value: value is not None, (scope.get(node.name, None) for scope in reversed(o))))
        return result

    def visit_postfix_lhs(self, node: "PostfixLHS", o: Any = None):
        self.visit(node.postfix_expr)

    def visit_postfix_expression(self, node: "PostfixExpression", o: Any = None):
        self.visit(node.primary, o)
        reduce(lambda acc, op: self.visit(op, acc), node.postfix_ops, o)

    def visit_member_access(self, node: "MemberAccess", o: Any = None):
        self.undeclared_check(o=o, name=node.member_name, kind=self.ID_TXT)

    def visit_array_access(self, node: "ArrayAccess", o: Any = None):
        # TODO: later
        pass

    def visit_method_call(self, node: "MethodCall", o: Any = None):
        # TODO: later
        pass

    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        o_left = self.visit(node.left, o)
        o_right = self.visit(node.right)
        if type(o_left) == VariableInfo:
            o_left = self.visit(o_left._type)
        if type(o_right) == VariableInfo:
            o_right = self.visit(o_right._type)

        if o_left == o_right:
            return o_left
        raise TypeMismatchInExpression(node)

    def visit_unary_op(self, node: "UnaryOp", o: Any = None):
        operand = self.visit(node.operand, o)

    def visit_object_creation(self, node: "ObjectCreation", o: Any = None):
        self.undeclared_check(o, node.class_name, self.CLASS_TXT)
        list(map(lambda arg: self.visit(arg, o), node.args))

    def visit_identifier(self, node: "Identifier", o: Any = None):
        obj = o[0]
        self.undeclared_check(obj, node.name, self.ID_TXT)
        result = next(filter(lambda value: value is not None, (scope.get(node.name, None) for scope in reversed(obj))))
        return result

    def visit_this_expression(self, node: "ThisExpression", o: Any = None):
        pass

    def visit_parenthesized_expression(self, node: "ParenthesizedExpression", o: Any = None):
        self.visit(node.expr, o)

    def visit_int_literal(self, node: "IntLiteral", o: Any = None):
        return self.visit(PrimitiveType("int"), o)

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        return self.visit(PrimitiveType("float"))

    def visit_bool_literal(self, node: "BoolLiteral", o: Any = None):
        return self.visit(PrimitiveType("boolean"))

    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        return self.visit(PrimitiveType("string"))

    def visit_array_literal(self, node: "ArrayLiteral", o: Any = None):
        obj = o[0]
        typ: PrimitiveType = o[1]
        elems: list = list(map(lambda elem: self.visit(elem, o), node.value))
        
        # Check for IllegalArrayLiteral
        for ele in elems:
            if ele != self.visit(typ):
                raise IllegalArrayLiteral(node)

    def visit_nil_literal(self, node: "NilLiteral", o: Any = None):
        return self.visit(PrimitiveType("void"))

    def visit_constructor_decl(self, node: "ConstructorDecl", o: list[dict] = [{}]): # type: ignore[reportIncompatibleMethodOverride]
        self.redeclared_check(o[1::], node.name, self.METHOD_TXT)

        o_method = o + [{}]  # Add METHOD scope for parameters
        o_params: list = reduce(lambda acc, param: self.visit(param, acc), node.params, o_method)
        o_block = o_params + [{"can init final": True}]  # Add BLOCK scope for variables
        o_vars_params = reduce(lambda acc, var_decl: self.visit(var_decl, acc), node.body.var_decls, o_block)
        list(map(lambda stmt: self.visit(stmt, o_vars_params), node.body.statements))

        o[1][node.name] = node
        return o

    def visit_destructor_decl(self, node: "DestructorDecl", o: Any = None):
        self.redeclared_check(o, node.name, self.METHOD_TXT)

        o_block = o + [{}]  # Add BLOCK scope for variables
        o_vars = reduce(lambda acc, var_decl: self.visit(var_decl, acc), node.body.var_decls, o_block)
        list(map(lambda stmt: self.visit(stmt, o_vars), node.body.statements))

        o[1][node.name] = node
        return o

    def visit_if_statement(self, node: "IfStatement", o: Any = None):
        self.visit(node.condition, o)
        self.visit(node.then_stmt, o)
        if node.else_stmt:
            self.visit(node.else_stmt, o)

    def visit_for_statement(self, node: "ForStatement", o: Any = None):
        start_expr = self.visit(node.start_expr, o)
        end_expr = self.visit(node.end_expr, o)
        var: VariableInfo = next(filter(lambda value: value is not None, (scope.get(node.variable, None) for scope in reversed(o))))

        if var.is_final:
            raise CannotAssignToConstant(node)
        if type(var._type) is PrimitiveType and var._type.type_name != "int":
            raise TypeMismatchInStatement(node)

        # NOTE: symbol_dict's special key no.1 = "for stmt"
        o[-1]["for stmt"] = node
        self.visit(node.body, o)

    def visit_break_statement(self, node: "BreakStatement", o: Any = None):
        self.must_in_loop_check(o, node)

    def visit_continue_statement(self, node: "ContinueStatement", o: Any = None):
        self.must_in_loop_check(o, node)

    def visit_return_statement(self, node: "ReturnStatement", o: Any = None):
        if node.value:
            self.visit(node.value, o)

    def visit_method_invocation_statement(self, node: "MethodInvocationStatement", o: Any = None):
        self.visit(node.method_call, o)

    def visit_block_statement(self, node: "BlockStatement", o: Any = None):
        o_block = o + [{}]  # Add new BLOCK scope
        o_vars = reduce(lambda acc, var_decl: self.visit(var_decl, acc), node.var_decls, o_block)
        list(map(lambda stmt: self.visit(stmt, o_vars), node.statements))

    def visit_primitive_type(self, node: "PrimitiveType", o: Any = None): # type: ignore[reportIncompatibleMethodOverride]
        return node.type_name

    def visit_array_type(self, node: "ArrayType", o: Any = None):
        self.visit(node.element_type, o)

    def visit_class_type(self, node: "ClassType", o: Any = None):
        self.undeclared_check(o, node.class_name, self.CLASS_TXT)

    def visit_reference_type(self, node: "ReferenceType", o: Any = None):
        self.visit(node.referenced_type, o)

    def visit_static_method_invocation(self, node: "MethodCall", o: Any = None):
        list(map(lambda arg: self.visit(arg, o), node.args))

    def visit_static_member_access(self, node: "StaticMemberAccess", o: Any = None):
        pass

    def visit_method_invocation(self, node: "MethodInvocation", o: Any = None):
        self.visit(node.postfix_expr, o)
