"""
Test cases for OPLang code generation.
This file contains test cases for the code generator.
Students should add more test cases here.
"""

from src.utils.nodes import *
from utils import CodeGenerator


def test_001():
    """Test basic class with main method and print statement"""
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,  # is_static
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeStrLn", [StringLiteral("Hello World")])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_002():
    """Test integer literal"""
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeIntLn", [IntLiteral(42)])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


""" --- TEST IO --- """
def test_003():
    """Test printing a string literal using io.writeStrLn"""
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,  # is_static
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeStrLn", [StringLiteral("Hello World")])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_004():
    """Test printing an integer literal using io.writeIntLn"""
    ast = Program([
        ClassDecl(
            "Main",
            None,
            [
                MethodDecl(
                    True,
                    PrimitiveType("void"),
                    "main",
                    [],
                    BlockStatement([], [
                        MethodInvocationStatement(
                            PostfixExpression(
                                Identifier("io"),
                                [MethodCall("writeIntLn", [IntLiteral(42)])]
                            )
                        )
                    ])
                )
            ]
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_005():
    """Test object creation and constructor with parameters"""
    ast = Program([
        ClassDecl("Point", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("x"), Attribute("y")]),
            ConstructorDecl("Point", [Parameter(PrimitiveType("int"), "a"), Parameter(PrimitiveType("int"), "b")], 
                BlockStatement([], [
                    AssignmentStatement(
                        PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("x")])),
                        Identifier("a")
                    ),
                    AssignmentStatement(
                        PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("y")])),
                        Identifier("b")
                    )
                ])
            )
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("Point"), [Variable("p", ObjectCreation("Point", [IntLiteral(10), IntLiteral(20)]))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("p"), [MemberAccess("x")])])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("p"), [MemberAccess("y")])])]))
                ]
            ))
        ])
    ])
    expected = "10\n20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_006():
    """Test destructor with explicit finalize call"""
    ast = Program([
        ClassDecl("Resource", None, [
            DestructorDecl("Resource", BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Destructor called")])]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("Resource"), [Variable("r", ObjectCreation("Resource", []))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("r"), [MethodCall("finalize", [])]))
                ]
            ))
        ])
    ])
    expected = "Destructor called"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_007():
    """Test postfix expressions: array access and method chaining"""
    ast = Program([
        ClassDecl("Helper", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("val")]),
            MethodDecl(False, ClassType("Helper"), "set", [Parameter(PrimitiveType("int"), "v")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("val")])), Identifier("v")),
                ReturnStatement(ThisExpression())
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, ArrayType(PrimitiveType("int"), 2), [Variable("a")]),
                    VariableDecl(False, ClassType("Helper"), [Variable("h", ObjectCreation("Helper", []))])
                ],
                [
                    # a[0] := 10
                    AssignmentStatement(PostfixLHS(PostfixExpression(Identifier("a"), [ArrayAccess(IntLiteral(0))])), IntLiteral(10)),
                    # h.set(a[0])
                    MethodInvocationStatement(PostfixExpression(Identifier("h"), [MethodCall("set", [PostfixExpression(Identifier("a"), [ArrayAccess(IntLiteral(0))])])])),
                    # io.writeIntLn(h.val)
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("h"), [MemberAccess("val")])])]))
                ]
            ))
        ])
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


# TODO: Add more test cases here
# Students should implement at least 100 test cases covering:
# - All literal types (int, float, boolean, string, array, nil)
# - Variable declarations and assignments
# - Binary operations (+, -, *, /, %, ==, !=, <, >, <=, >=, &&, ||)
# - Unary operations (-, +, !)
# - Control flow (if, for, break, continue)
# - Return statements
# - Method calls (static and instance)
# - Member access
# - Array access
# - Object creation
# - This expression
# - Constructors and destructors
# - Inheritance and polymorphism

