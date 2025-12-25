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

""" --- TEST CONTROL FLOW (IF/ELSE) --- """
def test_008():
    """Test simple if statement (true condition)"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                IfStatement(
                    BoolLiteral(True),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("True branch")])])),
                    None
                )
            ]))
        ])
    ])
    expected = "True branch"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_009():
    """Test simple if statement (false condition) - should print nothing"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                IfStatement(
                    BoolLiteral(False),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Should not print")])])),
                    None
                ),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Done")])]))
            ]))
        ])
    ])
    expected = "Done"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_010():
    """Test if-else statement (true condition)"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                IfStatement(
                    BinaryOp(IntLiteral(10), ">", IntLiteral(5)),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Greater")])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Smaller")])]))
                )
            ]))
        ])
    ])
    expected = "Greater"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_011():
    """Test if-else statement (false condition)"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                IfStatement(
                    BinaryOp(IntLiteral(2), ">", IntLiteral(5)),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Greater")])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Smaller")])]))
                )
            ]))
        ])
    ])
    expected = "Smaller"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_012():
    """Test nested if statements"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("x", IntLiteral(10))])],
                [
                    IfStatement(
                        BinaryOp(Identifier("x"), ">", IntLiteral(0)),
                        BlockStatement([], [
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Positive")])])),
                            IfStatement(
                                BinaryOp(Identifier("x"), "%", IntLiteral(2)), # 10 % 2 != 0 is False (0)
                                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Odd")])])),
                                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Even")])]))
                            )
                        ]),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Non-Positive")])]))
                    )
                ]
            ))
        ])
    ])
    expected = "Positive\nEven"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


""" --- TEST CONTROL FLOW (FOR LOOP) --- """

def test_013():
    """Test for loop (to direction)"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("i")])],
                [
                    ForStatement(
                        "i", IntLiteral(1), "to", IntLiteral(3),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("i")])]))
                    )
                ]
            ))
        ])
    ])
    expected = "1\n2\n3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_014():
    """Test for loop (downto direction)"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("i")])],
                [
                    ForStatement(
                        "i", IntLiteral(3), "downto", IntLiteral(1),
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("i")])]))
                    )
                ]
            ))
        ])
    ])
    expected = "3\n2\n1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_015():
    """Test break statement in loop"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("i")])],
                [
                    ForStatement(
                        "i", IntLiteral(1), "to", IntLiteral(5),
                        BlockStatement([], [
                            IfStatement(
                                BinaryOp(Identifier("i"), "==", IntLiteral(3)),
                                BreakStatement(),
                                None
                            ),
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("i")])]))
                        ])
                    )
                ]
            ))
        ])
    ])
    expected = "1\n2"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_016():
    """Test continue statement in loop"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("i")])],
                [
                    ForStatement(
                        "i", IntLiteral(1), "to", IntLiteral(5),
                        BlockStatement([], [
                            IfStatement(
                                BinaryOp(Identifier("i"), "%", IntLiteral(2)), # Skip odd numbers (if 1 then continue)
                                ContinueStatement(),
                                None
                            ),
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("i")])]))
                        ])
                    )
                ]
            ))
        ])
    ])
    # 1%2=1(True)->Cont, 2%2=0(False)->Print, 3%2=1->Cont, 4%2=0->Print, 5%2=1->Cont
    expected = "2\n4"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


""" --- TEST BINARY OPERATORS --- """

def test_017():
    """Test basic arithmetic operators (+, -, *, /, %)"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [BinaryOp(IntLiteral(10), "+", IntLiteral(5))])])), # 15
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [BinaryOp(IntLiteral(10), "-", IntLiteral(5))])])), # 5
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [BinaryOp(IntLiteral(10), "*", IntLiteral(5))])])), # 50
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [BinaryOp(IntLiteral(10), "\\", IntLiteral(2))])])), # 5
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [BinaryOp(IntLiteral(10), "/", IntLiteral(2))])])), # 5.0
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [BinaryOp(IntLiteral(10), "%", IntLiteral(3))])]))  # 1
            ]))
        ])
    ])
    expected = "15\n5\n50\n5\n5.0\n1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_018():
    """Test comparison operators (>, <, >=, <=, ==, !=)"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [BinaryOp(IntLiteral(10), ">", IntLiteral(5))])])),  # true
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [BinaryOp(IntLiteral(10), "<", IntLiteral(5))])])),  # false
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [BinaryOp(IntLiteral(10), ">=", IntLiteral(10))])])), # true
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [BinaryOp(IntLiteral(10), "<=", IntLiteral(9))])])),  # false
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [BinaryOp(IntLiteral(10), "==", IntLiteral(10))])])), # true
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [BinaryOp(IntLiteral(10), "!=", IntLiteral(10))])]))  # false
            ]))
        ])
    ])
    expected = "true\nfalse\ntrue\nfalse\ntrue\nfalse"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_019():
    """Test logical operators (&&, ||)"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [BinaryOp(BoolLiteral(True), "&&", BoolLiteral(False))])])), # false
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [BinaryOp(BoolLiteral(True), "||", BoolLiteral(False))])])), # true
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [BinaryOp(BoolLiteral(True), "&&", BoolLiteral(True))])])),   # true
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [BinaryOp(BoolLiteral(False), "||", BoolLiteral(False))])]))  # false
            ]))
        ])
    ])
    expected = "false\ntrue\ntrue\nfalse"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_020():
    """Test float arithmetic and comparison"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [BinaryOp(FloatLiteral(2.5), "+", FloatLiteral(1.5))])])), # 4.0
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [BinaryOp(FloatLiteral(2.5), ">", FloatLiteral(1.5))])]))   # true
            ]))
        ])
    ])
    expected = "4.0\ntrue"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST UNARY OPERATORS --- """

def test_021():
    """Test unary operators (-, !)"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [UnaryOp("-", IntLiteral(10))])])),       # -10
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [UnaryOp("-", FloatLiteral(5.5))])])),   # -5.5
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [UnaryOp("!", BoolLiteral(True))])])),     # false
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [UnaryOp("!", BoolLiteral(False))])]))    # true
            ]))
        ])
    ])
    expected = "-10\n-5.5\nfalse\ntrue"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST IMPLICIT COERCION --- """

def test_022():
    """Test implicit coercion in binary operations (int + float)"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [BinaryOp(IntLiteral(10), "+", FloatLiteral(5.5))])])), # 15.5
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [BinaryOp(FloatLiteral(10.5), "-", IntLiteral(5))])])), # 5.5
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [BinaryOp(IntLiteral(10), ">", FloatLiteral(5.5))])])),   # true
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [BinaryOp(IntLiteral(1), "/", IntLiteral(2))])]))      # 0.5
            ]))
        ])
    ])
    expected = "15.5\n5.5\ntrue\n0.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_023():
    """Test implicit coercion in assignment and initialization"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("float"), [Variable("f1", IntLiteral(10))]), # Init coercion
                    VariableDecl(False, PrimitiveType("float"), [Variable("f2")])
                ],
                [
                    AssignmentStatement(IdLHS("f2"), IntLiteral(20)), # Assignment coercion
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [Identifier("f1")])])), # 10.0
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [Identifier("f2")])]))  # 20.0
                ]
            ))
        ])
    ])
    expected = "10.0\n20.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_024():
    """Test implicit coercion in return statements"""
    ast = Program([
        ClassDecl("Helper", None, [
            MethodDecl(True, PrimitiveType("float"), "getIntAsFloat", [], BlockStatement([], [
                ReturnStatement(IntLiteral(42))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [PostfixExpression(Identifier("Helper"), [MethodCall("getIntAsFloat", [])])])]))
            ]))
        ])
    ])
    expected = "42.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


