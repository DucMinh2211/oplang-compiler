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

    def visit_program(self, node: "Program", o: Any = None):
        reduce(lambda class_names, class_decl: self.visit(class_decl, class_names), node.class_decls, [{}])

    def visit_class_decl(self, node: "ClassDecl", o: list[dict] = [{}]) -> list[dict] | None:
        for scope in o:
            if node.name in scope.keys():
                raise Redeclared(self.CLASS_TXT, node.name)
        o[0].update({ node.name : self.CLASS_TXT })
        return reduce(lambda names, member: self.visit(member, names), node.members, o)

    def visit_attribute_decl(self, node: "AttributeDecl", o: list[dict] = [{}]) -> list[dict] | None:
        return reduce(lambda names, att: self.visit(att, names), node.attributes, o)

    def visit_attribute(self, node: "Attribute", o: list[dict] = [{}]) -> list[dict] | None:
        for scope in o:
            if node.name in scope.keys():
                raise Redeclared("", node.name)

