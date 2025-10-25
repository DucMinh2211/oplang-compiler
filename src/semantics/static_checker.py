"""
Static Semantic Checker for OPLang Programming Language

This module implements a comprehensive static semantic checker using visitor pattern
for the OPLang object-oriented programming language. It performs type checking,
scope management, inheritance validation, and detects all semantic errors as 
specified in the OPLang language specification.
"""

from functools import reduce
from typing import Dict, List, Set, Optional, Any, Tuple, Union, NamedTuple, overload
from typing_extensions import override
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
    def __init__(self, is_final: bool, var_type: Any, var: Variable) -> None:
        self.is_final: bool = is_final
        self.var_type: Any = var_type
        self.var: Variable = var


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


    def redeclared_check(self, o: list[dict], name: str, kind: str):
        for scope in o:
            if name in scope.keys():
                raise Redeclared(kind, name)

    def visit_program(self, node: "Program", o: Any = None):
        reduce(lambda class_names, class_decl: self.visit(class_decl, class_names), node.class_decls, [{}])

    def visit_class_decl(self, node: "ClassDecl", o: list[dict] = [{}]) -> list[dict] | None: # type: ignore[reportIncompatibleMethodOverride]
        # Redeclared Check
        for scope in o:
            if node.name in scope.keys():
                raise Redeclared(self.CLASS_TXT, node.name)

        # visit children
        o[0][node.name] = None
        reduce(lambda names, member: self.visit(member, names), node.members, o)
        o[0][node.name] = node
        return o

    def visit_attribute_decl(self, node: "AttributeDecl", o: list[dict] = [{}]) -> list[dict] | None: # type: ignore[reportIncompatibleMethodOverride]
        reduce(lambda names, att: self.visit(att, names), node.attributes, o)

    def visit_attribute(self, node: "Attribute", o: list[dict] = [{}]) -> list[dict] | None: # type: ignore[reportIncompatibleMethodOverride]
        # Redeclared Check
        for scope in o:
            if node.name in scope.keys():
                raise Redeclared(self.ATT_TXT, node.name)

        o[1][node.name] = node
        return o

    def visit_method_decl(self, node: "MethodDecl", o: Any = None):
        # Redeclared Check
        self.redeclared_check(o, node.name, self.METHOD_TXT)

        # visit children
        o_params = reduce(lambda params, param: self.visit(param, params), node.params, o)
        o_vars_params = reduce(lambda var_decls, var_decl: self.visit(var_decl, var_decls), node.body.var_decls, o_params)
        # TODO: finish

    def visit_parameter(self, node: "Parameter", o: Any = None):
        self.redeclared_check(o, node.name, self.PARAM_TXT)

        o[2][node.name] = node
        return o

    def visit_variable_decl(self, node: "VariableDecl", o: Any = None):
        return reduce(lambda vars, var: self.visit(var, (vars, node)), node.variables, o)

    def visit_variable(self, node: "Variable", o: Any = None):
        obj = o[0]
        var_decl: VariableDecl = o[1]
        self.redeclared_check(obj, node.name, self.VAR_TXT)

        o[2][node.name] = VariableInfo(var_decl.is_final, var_decl.var_type, node)
        return o
