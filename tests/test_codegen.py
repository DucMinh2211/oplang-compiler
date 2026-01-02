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

""" --- TEST INHERITANCE --- """

def test_025():
    """Test basic inheritance: access parent attribute and method"""
    ast = Program([
        ClassDecl("Parent", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("x", IntLiteral(10))]),
            MethodDecl(False, PrimitiveType("void"), "sayHello", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Hello from Parent")])]))
            ]))
        ]),
        ClassDecl("Child", "Parent", []),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("Child"), [Variable("c", ObjectCreation("Child", []))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("c"), [MemberAccess("x")])])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("c"), [MethodCall("sayHello", [])]))
                ]
            ))
        ])
    ])
    expected = "10\nHello from Parent"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_026():
    """Test method overriding and dynamic dispatch"""
    ast = Program([
        ClassDecl("Shape", None, [
            MethodDecl(False, PrimitiveType("void"), "draw", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Drawing Shape")])]))
            ]))
        ]),
        ClassDecl("Circle", "Shape", [
            MethodDecl(False, PrimitiveType("void"), "draw", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Drawing Circle")])]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, ClassType("Shape"), [Variable("s1", ObjectCreation("Shape", []))]),
                    VariableDecl(False, ClassType("Shape"), [Variable("s2", ObjectCreation("Circle", []))])
                ],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("s1"), [MethodCall("draw", [])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("s2"), [MethodCall("draw", [])]))
                ]
            ))
        ])
    ])
    expected = "Drawing Shape\nDrawing Circle"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_027():
    """Test multi-level inheritance A -> B -> C"""
    ast = Program([
        ClassDecl("A", None, [
            MethodDecl(False, PrimitiveType("void"), "m1", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("A.m1")])]))
            ]))
        ]),
        ClassDecl("B", "A", [
            MethodDecl(False, PrimitiveType("void"), "m2", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("B.m2")])]))
            ]))
        ]),
        ClassDecl("C", "B", [
            MethodDecl(False, PrimitiveType("void"), "m1", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("C.m1")])]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("C"), [Variable("obj", ObjectCreation("C", []))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("obj"), [MethodCall("m1", [])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("obj"), [MethodCall("m2", [])]))
                ]
            ))
        ])
    ])
    expected = "C.m1\nB.m2"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_028():
    """Test inheritance with constructors and super() call chain"""
    ast = Program([
        ClassDecl("Base", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("val")]),
            ConstructorDecl("Base", [Parameter(PrimitiveType("int"), "v")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("val")])), Identifier("v")),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Base constructor")])]))
            ]))
        ]),
        ClassDecl("Derived", "Base", [
            ConstructorDecl("Derived", [Parameter(PrimitiveType("int"), "v")], BlockStatement([], [
                # Implicit super(v) is not supported by our simple codegen, 
                # but our current codegen automatically calls super() without args.
                # Since Base constructor takes an arg, we would need explicit super call support.
                # Let's test with default constructors first to see if chain works.
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Derived constructor")])]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("Derived"), [Variable("d", ObjectCreation("Derived", [IntLiteral(100)]))])],
                []
            ))
        ])
    ])
    # Note: Our current codegen for visit_constructor_decl ALWAYS calls super() without args.
    # If Base constructor has args, this test might fail bytecode verification if not handled.
    # Let's adjust Base to have a no-arg constructor for this test.
    ast.class_decls[0].members[1] = ConstructorDecl("Base", [], BlockStatement([], [
        MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Base constructor")])]))
    ]))
    ast.class_decls[1].members[0] = ConstructorDecl("Derived", [], BlockStatement([], [
        MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Derived constructor")])]))
    ]))
    ast.class_decls[2].members[0].body.var_decls[0].variables[0].init_value = ObjectCreation("Derived", [])
    
    expected = "Base constructor\nDerived constructor"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST RECURSION --- """
def test_029():
    """Test recursion with factorial"""
    ast = Program([
        ClassDecl("MyMath", None, [
            MethodDecl(True, PrimitiveType("int"), "fact", [Parameter(PrimitiveType("int"), "n")], BlockStatement([], [
                IfStatement(
                    BinaryOp(Identifier("n"), "<=", IntLiteral(1)),
                    ReturnStatement(IntLiteral(1)),
                    ReturnStatement(BinaryOp(Identifier("n"), "*", PostfixExpression(Identifier("MyMath"), [MethodCall("fact", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])])))
                ),
                ReturnStatement(IntLiteral(0))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("MyMath"), [MethodCall("fact", [IntLiteral(5)])])])]))
            ]))
        ])
    ])
    expected = "120"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST STATIC MEMBERS --- """
def test_030():
    """Test static field and method access"""
    ast = Program([
        ClassDecl("Config", None, [
            AttributeDecl(True, False, PrimitiveType("int"), [Attribute("VAL")]),
            MethodDecl(True, PrimitiveType("int"), "getVal", [], BlockStatement([], [
                ReturnStatement(PostfixExpression(Identifier("Config"), [MemberAccess("VAL")]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                # Config.VAL = 100
                AssignmentStatement(PostfixLHS(PostfixExpression(Identifier("Config"), [MemberAccess("VAL")])), IntLiteral(100)),
                # print(Config.getVal())
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("Config"), [MethodCall("getVal", [])])])]))
            ]))
        ])
    ])
    expected = "100"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST COMPLEX EXPRESSIONS --- """
def test_031():
    """Test complex arithmetic expression precedence"""
    # (10 + 5) * 2 - 4 \\ 2 = 15 * 2 - 2 = 30 - 2 = 28
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                    MethodCall("writeIntLn", [
                        BinaryOp(
                            BinaryOp(
                                ParenthesizedExpression(BinaryOp(IntLiteral(10), "+", IntLiteral(5))),
                                "*",
                                IntLiteral(2)
                            ),
                            "-",
                            BinaryOp(IntLiteral(4), "\\", IntLiteral(2))
                        )
                    ])
                ]))
            ]))
        ])
    ])
    expected = "28"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST PARAMETER PASSING --- """
def test_032():
    """Test passing object by reference"""
    ast = Program([
        ClassDecl("Box", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("val")])
        ]),
        ClassDecl("Modifier", None, [
            MethodDecl(True, PrimitiveType("void"), "modify", [Parameter(ClassType("Box"), "b")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(Identifier("b"), [MemberAccess("val")])), IntLiteral(99))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("Box"), [Variable("box", ObjectCreation("Box", []))])],
                [
                    AssignmentStatement(PostfixLHS(PostfixExpression(Identifier("box"), [MemberAccess("val")])), IntLiteral(1)),
                    MethodInvocationStatement(PostfixExpression(Identifier("Modifier"), [MethodCall("modify", [Identifier("box")])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("box"), [MemberAccess("val")])])]))
                ]
            ))
        ])
    ])
    expected = "99"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST NESTED LOOPS --- """
def test_033():
    """Test nested for loops"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("i")]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("j")])
                ],
                [
                    ForStatement(
                        "i", IntLiteral(1), "to", IntLiteral(2),
                        ForStatement(
                            "j", IntLiteral(1), "to", IntLiteral(2),
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [
                                MethodCall("writeIntLn", [
                                    BinaryOp(
                                        BinaryOp(Identifier("i"), "*", IntLiteral(10)),
                                        "+",
                                        Identifier("j")
                                    )
                                ])
                            ]))
                        )
                    )
                ]
            ))
        ])
    ])
    expected = "11\n12\n21\n22"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST STRING CONCATENATION --- """
def test_034():
    """Test string concatenation with ^ operator"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [BinaryOp(StringLiteral("Hello "), "^", StringLiteral("World"))])]))
            ]))
        ])
    ])
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST UNARY PLUS --- """
def test_035():
    """Test unary plus operator"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [UnaryOp("+", IntLiteral(10))])])),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [UnaryOp("+", FloatLiteral(3.14))])]))
            ]))
        ])
    ])
    expected = "10\n3.14"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST VARIABLE SHADOWING --- """
def test_036():
    """Test variable shadowing in block"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("x", IntLiteral(10))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("x")])])),
                    BlockStatement(
                        [VariableDecl(False, PrimitiveType("int"), [Variable("x", IntLiteral(20))])],
                        [
                            MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("x")])]))
                        ]
                    ),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("x")])]))
                ]
            ))
        ])
    ])
    expected = "10\n20\n10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST SHORT-CIRCUIT AND --- """
def test_037():
    """Test short-circuit AND (&&)"""
    ast = Program([
        ClassDecl("Main", None, [
            AttributeDecl(True, False, PrimitiveType("boolean"), [Attribute("flag", BoolLiteral(False))]),
            MethodDecl(True, PrimitiveType("boolean"), "sideEffect", [], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(Identifier("Main"), [MemberAccess("flag")])), BoolLiteral(True)),
                ReturnStatement(BoolLiteral(True))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                IfStatement(
                    BinaryOp(BoolLiteral(False), "&&", PostfixExpression(Identifier("Main"), [MethodCall("sideEffect", [])])),
                    BlockStatement([], []),
                    None
                ),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [PostfixExpression(Identifier("Main"), [MemberAccess("flag")])])]))
            ]))
        ])
    ])
    # flag should remain False because False && ... short-circuits
    expected = "false"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST SHORT-CIRCUIT OR --- """
def test_038():
    """Test short-circuit OR (||)"""
    ast = Program([
        ClassDecl("Main", None, [
            AttributeDecl(True, False, PrimitiveType("boolean"), [Attribute("flag", BoolLiteral(False))]),
            MethodDecl(True, PrimitiveType("boolean"), "sideEffect", [], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(Identifier("Main"), [MemberAccess("flag")])), BoolLiteral(True)),
                ReturnStatement(BoolLiteral(True))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                IfStatement(
                    BinaryOp(BoolLiteral(True), "||", PostfixExpression(Identifier("Main"), [MethodCall("sideEffect", [])])),
                    BlockStatement([], []),
                    None
                ),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [PostfixExpression(Identifier("Main"), [MemberAccess("flag")])])]))
            ]))
        ])
    ])
    # flag should remain False because True || ... short-circuits
    expected = "false"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST ARRAY ASSIGNMENT --- """
def test_039():
    """Test array assignment"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ArrayType(PrimitiveType("int"), 3), [Variable("arr", ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))])],
                [
                    AssignmentStatement(PostfixLHS(PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(1))])), IntLiteral(99)),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(1))])])]))
                ]
            ))
        ])
    ])
    expected = "99"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST METHOD CHAINING --- """
def test_040():
    """Test method chaining"""
    ast = Program([
        ClassDecl("Chainer", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("val", IntLiteral(0))]),
            MethodDecl(False, ClassType("Chainer"), "inc", [], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("val")])), 
                                    BinaryOp(PostfixExpression(ThisExpression(), [MemberAccess("val")]), "+", IntLiteral(1))),
                ReturnStatement(ThisExpression())
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("Chainer"), [Variable("c", ObjectCreation("Chainer", []))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("c"), [MethodCall("inc", []), MethodCall("inc", []), MethodCall("inc", [])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("c"), [MemberAccess("val")])])]))
                ]
            ))
        ])
    ])
    expected = "3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST MULTIPLE VARIABLE DECLARATION --- """
def test_041():
    """Test multiple variable declaration in one line"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("a", IntLiteral(1)), Variable("b", IntLiteral(2))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("a")])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("b")])]))
                ]
            ))
        ])
    ])
    expected = "1\n2"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST COPY CONSTRUCTOR --- """
def test_042():
    """Test copy constructor logic (manual simulation)"""
    ast = Program([
        ClassDecl("Point", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("x"), Attribute("y")]),
            ConstructorDecl("Point", [Parameter(PrimitiveType("int"), "a"), Parameter(PrimitiveType("int"), "b")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("x")])), Identifier("a")),
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("y")])), Identifier("b"))
            ])),
            ConstructorDecl("Point", [Parameter(ClassType("Point"), "other")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("x")])), PostfixExpression(Identifier("other"), [MemberAccess("x")])),
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("y")])), PostfixExpression(Identifier("other"), [MemberAccess("y")]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, ClassType("Point"), [Variable("p1", ObjectCreation("Point", [IntLiteral(10), IntLiteral(20)]))]),
                    VariableDecl(False, ClassType("Point"), [Variable("p2", ObjectCreation("Point", [Identifier("p1")]))])
                ],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("p2"), [MemberAccess("x")])])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("p2"), [MemberAccess("y")])])]))
                ]
            ))
        ])
    ])
    expected = "10\n20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST ARRAY ACCESS IN EXPRESSION --- """
def test_043():
    """Test array access within arithmetic expression"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ArrayType(PrimitiveType("int"), 3), [Variable("arr", ArrayLiteral([IntLiteral(10), IntLiteral(20), IntLiteral(30)]))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [
                        BinaryOp(PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(0))]), "+", PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(2))]))
                    ])]))
                ]
            ))
        ])
    ])
    expected = "40"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST CLASS WITH NO MEMBERS --- """
def test_044():
    """Test class with no members"""
    ast = Program([
        ClassDecl("Empty", None, []),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("Empty"), [Variable("e", ObjectCreation("Empty", []))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Created empty object")])]))
                ]
            ))
        ])
    ])
    expected = "Created empty object"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST CONTINUE IN NESTED LOOP --- """
def test_045():
    """Test continue in nested loop"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("i")]), VariableDecl(False, PrimitiveType("int"), [Variable("j")])],
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(2),
                        ForStatement("j", IntLiteral(1), "to", IntLiteral(2),
                            BlockStatement([], [
                                IfStatement(BinaryOp(Identifier("j"), "==", IntLiteral(1)), ContinueStatement(), None),
                                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [BinaryOp(Identifier("i"), "*", IntLiteral(10))])]))
                            ])
                        )
                    )
                ]
            ))
        ])
    ])
    expected = "10\n20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST STATIC FROM INSTANCE --- """
def test_046():
    """Test accessing static field from instance method using ClassName"""
    ast = Program([
        ClassDecl("A", None, [
            AttributeDecl(True, False, PrimitiveType("int"), [Attribute("val", IntLiteral(5))]),
            MethodDecl(False, PrimitiveType("void"), "printVal", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("A"), [MemberAccess("val")])])]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("A"), [Variable("a", ObjectCreation("A", []))])],
                [
                    AssignmentStatement(PostfixLHS(PostfixExpression(Identifier("A"), [MemberAccess("val")])), IntLiteral(5)),
                    MethodInvocationStatement(PostfixExpression(Identifier("a"), [MethodCall("printVal", [])]))
                ]
            ))
        ])
    ])
    expected = "5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST EXPLICIT THIS --- """
def test_047():
    """Test accessing instance field with explicit 'this'"""
    ast = Program([
        ClassDecl("A", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("x", IntLiteral(10))]),
            MethodDecl(False, PrimitiveType("void"), "printX", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(ThisExpression(), [MemberAccess("x")])])]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("A"), [Variable("a", ObjectCreation("A", []))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("a"), [MethodCall("printX", [])]))
                ]
            ))
        ])
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST LARGE INT --- """
def test_048():
    """Test large integer literal"""
    val = 2147483647
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [IntLiteral(val)])]))
            ]))
        ])
    ])
    expected = str(val)
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST COMPLEX BOOLEAN --- """
def test_049():
    """Test boolean logic with mixed operators"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [
                    BinaryOp(
                        BinaryOp(
                            BinaryOp(IntLiteral(5), ">", IntLiteral(3)),
                            "&&",
                            UnaryOp("!", BinaryOp(IntLiteral(2), "==", IntLiteral(2)))
                        ),
                        "||",
                        BinaryOp(IntLiteral(1), "<", IntLiteral(2))
                    )
                ])]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST EMPTY BLOCK --- """
def test_050():
    """Test empty block statement"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                BlockStatement([], []), 
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Done")])]))
            ]))
        ])
    ])
    expected = "Done"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST ARRAY TYPES --- """
def test_051():
    """Test array of strings"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ArrayType(PrimitiveType("string"), 2), [Variable("arr", ArrayLiteral([StringLiteral("A"), StringLiteral("B")]))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(0))])])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(1))])])]))
                ]
            ))
        ])
    ])
    expected = "A\nB"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_052():
    """Test array of floats"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ArrayType(PrimitiveType("float"), 2), [Variable("arr", ArrayLiteral([FloatLiteral(1.5), FloatLiteral(2.5)]))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(0))])])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(1))])])]))
                ]
            ))
        ])
    ])
    expected = "1.5\n2.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_053():
    """Test array of booleans"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ArrayType(PrimitiveType("boolean"), 2), [Variable("arr", ArrayLiteral([BoolLiteral(True), BoolLiteral(False)]))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(0))])])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(1))])])]))
                ]
            ))
        ])
    ])
    expected = "true\nfalse"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST ARRAY PASSING/RETURN --- """
def test_054():
    """Test passing array to method"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "printFirst", [Parameter(ArrayType(PrimitiveType("int"), 0), "arr")], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(0))])])]))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ArrayType(PrimitiveType("int"), 1), [Variable("a", ArrayLiteral([IntLiteral(100)]))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("Main"), [MethodCall("printFirst", [Identifier("a")])]))
                ]
            ))
        ])
    ])
    expected = "100"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_055():
    """Test returning array from method"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, ArrayType(PrimitiveType("int"), 2), "createArray", [], BlockStatement([], [
                ReturnStatement(ArrayLiteral([IntLiteral(10), IntLiteral(20)]))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ArrayType(PrimitiveType("int"), 2), [Variable("a", PostfixExpression(Identifier("Main"), [MethodCall("createArray", [])]))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("a"), [ArrayAccess(IntLiteral(1))])])]))
                ]
            ))
        ])
    ])
    expected = "20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_056():
    """Test using array element as method argument"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ArrayType(PrimitiveType("int"), 2), [Variable("a", ArrayLiteral([IntLiteral(5), IntLiteral(10)]))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("a"), [ArrayAccess(IntLiteral(1))])])]))
                ]
            ))
        ])
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_057():
    """Test assigning to array element from return value"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("int"), "getVal", [], BlockStatement([], [ReturnStatement(IntLiteral(7))])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ArrayType(PrimitiveType("int"), 1), [Variable("a")])],
                [
                    AssignmentStatement(PostfixLHS(PostfixExpression(Identifier("a"), [ArrayAccess(IntLiteral(0))])), PostfixExpression(Identifier("Main"), [MethodCall("getVal", [])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("a"), [ArrayAccess(IntLiteral(0))])])]))
                ]
            ))
        ])
    ])
    expected = "7"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST STRING CONCAT CHAIN --- """
def test_058():
    """Test chained string concatenation"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [
                    BinaryOp(BinaryOp(StringLiteral("A"), "^", StringLiteral("B")), "^", StringLiteral("C"))
                ])]))
            ]))
        ])
    ])
    expected = "ABC"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST BOOLEAN NOT --- """
def test_059():
    """Test double negation"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [
                    UnaryOp("!", UnaryOp("!", BoolLiteral(True)))
                ])]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_060():
    """Test complex if condition"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                IfStatement(
                    BinaryOp(
                        BinaryOp(IntLiteral(1), "<", IntLiteral(2)), 
                        "&&", 
                        BinaryOp(IntLiteral(3), ">", IntLiteral(2))
                    ),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Yes")])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("No")])]))
                )
            ]))
        ])
    ])
    expected = "Yes"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST CONTROL FLOW 2 --- """
def test_061():
    """Test for loop with variables as bounds"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, PrimitiveType("int"), [Variable("start", IntLiteral(1)), Variable("end", IntLiteral(3)), Variable("i")])
                ],
                [
                    ForStatement("i", Identifier("start"), "to", Identifier("end"), 
                        MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("i")])]))
                    )
                ]
            ))
        ])
    ])
    expected = "1\n2\n3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_062():
    """Test break in nested loop (inner)"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("i")]), VariableDecl(False, PrimitiveType("int"), [Variable("j")])],
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(2),
                        ForStatement("j", IntLiteral(1), "to", IntLiteral(3),
                            BlockStatement([], [
                                IfStatement(BinaryOp(Identifier("j"), "==", IntLiteral(2)), BreakStatement(), None),
                                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("j")])]))
                            ])
                        )
                    )
                ]
            ))
        ])
    ])
    # i=1: j=1 print 1, j=2 break.
    # i=2: j=1 print 1, j=2 break.
    expected = "1\n1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_063():
    """Test continue in nested loop (inner)"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("i")]), VariableDecl(False, PrimitiveType("int"), [Variable("j")])],
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(1),
                        ForStatement("j", IntLiteral(1), "to", IntLiteral(3),
                            BlockStatement([], [
                                IfStatement(BinaryOp(Identifier("j"), "==", IntLiteral(2)), ContinueStatement(), None),
                                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("j")])]))
                            ])
                        )
                    )
                ]
            ))
        ])
    ])
    # j=1 print 1, j=2 cont, j=3 print 3
    expected = "1\n3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST RECURSION 2 --- """
def test_064():
    """Test mutual recursion (even/odd)"""
    ast = Program([
        ClassDecl("Util", None, [
            MethodDecl(True, PrimitiveType("boolean"), "isEven", [Parameter(PrimitiveType("int"), "n")], BlockStatement([], [
                IfStatement(BinaryOp(Identifier("n"), "==", IntLiteral(0)), ReturnStatement(BoolLiteral(True)), None),
                ReturnStatement(PostfixExpression(Identifier("Util"), [MethodCall("isOdd", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])]))
            ])),
            MethodDecl(True, PrimitiveType("boolean"), "isOdd", [Parameter(PrimitiveType("int"), "n")], BlockStatement([], [
                IfStatement(BinaryOp(Identifier("n"), "==", IntLiteral(0)), ReturnStatement(BoolLiteral(False)), None),
                ReturnStatement(PostfixExpression(Identifier("Util"), [MethodCall("isEven", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [PostfixExpression(Identifier("Util"), [MethodCall("isEven", [IntLiteral(4)])])])])),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [PostfixExpression(Identifier("Util"), [MethodCall("isOdd", [IntLiteral(4)])])])]))
            ]))
        ])
    ])
    expected = "true\nfalse"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST OBJECT REFERENCES --- """
def test_065():
    """Test linked list node (recursive class structure)"""
    ast = Program([
        ClassDecl("Node", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("val")]),
            AttributeDecl(False, False, ClassType("Node"), [Attribute("next")]),
            ConstructorDecl("Node", [Parameter(PrimitiveType("int"), "v")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("val")])), Identifier("v"))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, ClassType("Node"), [Variable("n1", ObjectCreation("Node", [IntLiteral(1)]))]),
                    VariableDecl(False, ClassType("Node"), [Variable("n2", ObjectCreation("Node", [IntLiteral(2)]))])
                ],
                [
                    AssignmentStatement(PostfixLHS(PostfixExpression(Identifier("n1"), [MemberAccess("next")])), Identifier("n2")),
                    # print n1.next.val
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [
                        PostfixExpression(PostfixExpression(Identifier("n1"), [MemberAccess("next")]), [MemberAccess("val")])
                    ])]))
                ]
            ))
        ])
    ])
    expected = "2"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_066():
    """Test method returning object"""
    ast = Program([
        ClassDecl("Box", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("val")]),
            ConstructorDecl("Box", [Parameter(PrimitiveType("int"), "v")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("val")])), Identifier("v"))
            ]))
        ]),
        ClassDecl("Factory", None, [
            MethodDecl(True, ClassType("Box"), "create", [Parameter(PrimitiveType("int"), "v")], BlockStatement([], [
                ReturnStatement(ObjectCreation("Box", [Identifier("v")]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("Box"), [Variable("b", PostfixExpression(Identifier("Factory"), [MethodCall("create", [IntLiteral(55)])]))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("b"), [MemberAccess("val")])])]))
                ]
            ))
        ])
    ])
    expected = "55"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_067():
    """Test modifying object passed to method"""
    ast = Program([
        ClassDecl("Data", None, [AttributeDecl(False, False, PrimitiveType("int"), [Attribute("x", IntLiteral(0))])]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "update", [Parameter(ClassType("Data"), "d")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(Identifier("d"), [MemberAccess("x")])), IntLiteral(100))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("Data"), [Variable("d", ObjectCreation("Data", []))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("Main"), [MethodCall("update", [Identifier("d")])])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("d"), [MemberAccess("x")])])]))
                ]
            ))
        ])
    ])
    expected = "100"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST INHERITANCE 2 --- """
def test_068():
    """Test accessing inherited field in subclass method"""
    ast = Program([
        ClassDecl("Parent", None, [AttributeDecl(False, False, PrimitiveType("int"), [Attribute("pVal", IntLiteral(10))])]),
        ClassDecl("Child", "Parent", [
            MethodDecl(False, PrimitiveType("void"), "printP", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(ThisExpression(), [MemberAccess("pVal")])])]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("Child"), [Variable("c", ObjectCreation("Child", []))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("c"), [MethodCall("printP", [])]))
                ]
            ))
        ])
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_069():
    """Test overriding method calling another method"""
    ast = Program([
        ClassDecl("Parent", None, [
            MethodDecl(False, PrimitiveType("void"), "greet", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Parent")])]))
            ])),
            MethodDecl(False, PrimitiveType("void"), "act", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(ThisExpression(), [MethodCall("greet", [])]))
            ]))
        ]),
        ClassDecl("Child", "Parent", [
            MethodDecl(False, PrimitiveType("void"), "greet", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Child")])]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("Parent"), [Variable("p", ObjectCreation("Child", []))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("p"), [MethodCall("act", [])]))
                ]
            ))
        ])
    ])
    expected = "Child"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_070():
    """Test polymorphism with array of base class"""
    ast = Program([
        ClassDecl("Shape", None, [
            MethodDecl(False, PrimitiveType("void"), "draw", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Shape")])]))
            ]))
        ]),
        ClassDecl("Circle", "Shape", [
            MethodDecl(False, PrimitiveType("void"), "draw", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Circle")])]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ArrayType(ClassType("Shape"), 2), [Variable("arr")])],
                [
                    AssignmentStatement(PostfixLHS(PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(0))])), ObjectCreation("Shape", [])),
                    AssignmentStatement(PostfixLHS(PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(1))])), ObjectCreation("Circle", [])),
                    MethodInvocationStatement(PostfixExpression(PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(0))]), [MethodCall("draw", [])])),
                    MethodInvocationStatement(PostfixExpression(PostfixExpression(Identifier("arr"), [ArrayAccess(IntLiteral(1))]), [MethodCall("draw", [])]))
                ]
            ))
        ])
    ])
    expected = "Shape\nCircle"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

""" --- TEST FLOAT OPS 2 --- """
def test_071():
    """Test float less than"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [BinaryOp(FloatLiteral(1.0), "<", FloatLiteral(2.0))])]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_072():
    """Test float greater equals"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [BinaryOp(FloatLiteral(2.0), ">=", FloatLiteral(2.0))])]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_073():
    """Test float equality"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeBoolLn", [BinaryOp(FloatLiteral(1.5), "==", FloatLiteral(1.5))])]))
            ]))
        ])
    ])
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_074():
    """Test integer division (backslash)"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [BinaryOp(IntLiteral(7), "\\", IntLiteral(2))])]))
            ]))
        ])
    ])
    expected = "3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_075():
    """Test float division with integers"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [BinaryOp(IntLiteral(7), "/", IntLiteral(2))])]))
            ]))
        ])
    ])
    expected = "3.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_076():
    """Test modulo with negative numbers"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [BinaryOp(IntLiteral(-10), "%", IntLiteral(3))])])), # -1
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [BinaryOp(IntLiteral(10), "%", IntLiteral(-3))])]))  # 1
            ]))
        ])
    ])
    expected = "-1\n1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_077():
    """Test unary minus on expression"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [UnaryOp("-", BinaryOp(IntLiteral(5), "+", IntLiteral(5)))])]))
            ]))
        ])
    ])
    expected = "-10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_078():
    """Test unary plus on variable"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("x", IntLiteral(-5))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [UnaryOp("+", Identifier("x"))])]))
                ]
            ))
        ])
    ])
    expected = "-5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_079():
    """Test if statement with empty then block"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                IfStatement(BoolLiteral(True), BlockStatement([], []), None),
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Done")])]))
            ]))
        ])
    ])
    expected = "Done"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_080():
    """Test for loop with empty body"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("i")])],
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(100), BlockStatement([], [])),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("i")])]))
                ]
            ))
        ])
    ])
    expected = "101" # Loop increments i to 101 then exits
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_081():
    """Test local variable shadowing class attribute"""
    ast = Program([
        ClassDecl("Main", None, [
            AttributeDecl(True, False, PrimitiveType("int"), [Attribute("x", IntLiteral(10))]),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("x", IntLiteral(20))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("x")])]))
                ]
            ))
        ])
    ])
    expected = "20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_082():
    """Test local variable shadowing parameter"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "foo", [Parameter(PrimitiveType("int"), "x")], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("x", IntLiteral(20))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("x")])]))
                ]
            )),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("Main"), [MethodCall("foo", [IntLiteral(10)])]))
            ]))
        ])
    ])
    expected = "20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_083():
    """Test parameter shadowing class attribute"""
    ast = Program([
        ClassDecl("Main", None, [
            AttributeDecl(True, False, PrimitiveType("int"), [Attribute("x", IntLiteral(10))]),
            MethodDecl(True, PrimitiveType("void"), "foo", [Parameter(PrimitiveType("int"), "x")], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("x")])]))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("Main"), [MethodCall("foo", [IntLiteral(30)])]))
            ]))
        ])
    ])
    expected = "30"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_084():
    """Test initializing local variable with parameter value"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "foo", [Parameter(PrimitiveType("int"), "p")], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("l", Identifier("p"))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [Identifier("l")])]))
                ]
            )),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("Main"), [MethodCall("foo", [IntLiteral(55)])]))
            ]))
        ])
    ])
    expected = "55"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_085():
    """Test initializing attribute with static method call"""
    ast = Program([
        ClassDecl("Util", None, [
            MethodDecl(True, PrimitiveType("int"), "getVal", [], BlockStatement([], [ReturnStatement(IntLiteral(99))]))
        ]),
        ClassDecl("Main", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("val", PostfixExpression(Identifier("Util"), [MethodCall("getVal", [])]))]),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("Main"), [Variable("m", ObjectCreation("Main", []))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("m"), [MemberAccess("val")])])]))
                ]
            ))
        ])
    ])
    expected = "99"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_086():
    """Test passing 'this' as argument"""
    ast = Program([
        ClassDecl("Handler", None, [
            MethodDecl(True, PrimitiveType("void"), "handle", [Parameter(ClassType("Container"), "c")], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Handled")])]))
            ]))
        ]),
        ClassDecl("Container", None, [
            MethodDecl(False, PrimitiveType("void"), "process", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("Handler"), [MethodCall("handle", [ThisExpression()])]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("Container"), [Variable("c", ObjectCreation("Container", []))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("c"), [MethodCall("process", [])]))
                ]
            ))
        ])
    ])
    expected = "Handled"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_087():
    """Test method call directly on object creation"""
    ast = Program([
        ClassDecl("Worker", None, [
            MethodDecl(False, PrimitiveType("void"), "work", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Working")])]))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(ObjectCreation("Worker", []), [MethodCall("work", [])]))
            ]))
        ])
    ])
    expected = "Working"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_088():
    """Test field access directly on object creation"""
    ast = Program([
        ClassDecl("Data", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("val", IntLiteral(123))])
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(ObjectCreation("Data", []), [MemberAccess("val")])])]))
            ]))
        ])
    ])
    expected = "123"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_089():
    """Test array access on returned array"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, ArrayType(PrimitiveType("int"), 2), "getArr", [], BlockStatement([], [
                ReturnStatement(ArrayLiteral([IntLiteral(1), IntLiteral(2)]))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [
                    PostfixExpression(PostfixExpression(Identifier("Main"), [MethodCall("getArr", [])]), [ArrayAccess(IntLiteral(1))])
                ])]))
            ]))
        ])
    ])
    expected = "2"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_090():
    """Test passing nil to object parameter"""
    ast = Program([
        ClassDecl("Box", None, []),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "check", [Parameter(ClassType("Box"), "b")], BlockStatement([], [
                # Just checking if passing nil crashes
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("OK")])]))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("Main"), [MethodCall("check", [NilLiteral()])]))
            ]))
        ])
    ])
    expected = "OK"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_091():
    """Test assigning nil to variable"""
    ast = Program([
        ClassDecl("Box", None, []),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("Box"), [Variable("b", ObjectCreation("Box", []))])],
                [
                    AssignmentStatement(IdLHS("b"), NilLiteral()),
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Assigned")])]))
                ]
            ))
        ])
    ])
    expected = "Assigned"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_092():
    """Test returning nil"""
    ast = Program([
        ClassDecl("Box", None, []),
        ClassDecl("Main", None, [
            MethodDecl(True, ClassType("Box"), "getNull", [], BlockStatement([], [
                ReturnStatement(NilLiteral())
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("Main"), [MethodCall("getNull", [])])), # Pop result
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("Returned")])]))
            ]))
        ])
    ])
    expected = "Returned"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_093():
    """Test float division by zero (Infinity)"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [BinaryOp(FloatLiteral(1.0), "/", FloatLiteral(0.0))])]))
            ]))
        ])
    ])
    expected = "Infinity"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_094():
    """Test small float"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [FloatLiteral(0.0001)])]))
            ]))
        ])
    ])
    # 0.0001 formatted as 0.0001 in emitter.
    expected = "1.0E-4"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"
def test_095():
    """Test calling method with multiple args"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("int"), "add3", [Parameter(PrimitiveType("int"), "a"), Parameter(PrimitiveType("int"), "b"), Parameter(PrimitiveType("int"), "c")], BlockStatement([], [
                ReturnStatement(BinaryOp(BinaryOp(Identifier("a"), "+", Identifier("b")), "+", Identifier("c")))
            ])),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("Main"), [MethodCall("add3", [IntLiteral(1), IntLiteral(2), IntLiteral(3)])])])]))
            ]))
        ])
    ])
    expected = "6"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_096():
    """Test complex calc"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                # (2+3)*4 - 10/2 + 5%2 = 5*4 - 5.0 + 1 = 20 - 5.0 + 1 = 16.0
                # Use float div /
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeFloatLn", [
                    BinaryOp(
                        BinaryOp(
                            BinaryOp(ParenthesizedExpression(BinaryOp(IntLiteral(2), "+", IntLiteral(3))), "*", IntLiteral(4)),
                            "-",
                            BinaryOp(IntLiteral(10), "/", IntLiteral(2))
                        ),
                        "+",
                        BinaryOp(IntLiteral(5), "%", IntLiteral(2))
                    )
                ])]))
            ]))
        ])
    ])
    expected = "16.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_097():
    """Test return from loop"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("int"), "find", [], BlockStatement(
                [VariableDecl(False, PrimitiveType("int"), [Variable("i")])],
                [
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(10), BlockStatement([], [
                        IfStatement(BinaryOp(Identifier("i"), "==", IntLiteral(5)), ReturnStatement(Identifier("i")), None)
                    ])),
                    ReturnStatement(IntLiteral(-1))
                ]
            )),
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("Main"), [MethodCall("find", [])])])]))
            ]))
        ])
    ])
    expected = "5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_098():
    """Test string with escape characters"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement([], [
                MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeStrLn", [StringLiteral("A\\tB")])]))
            ]))
        ])
    ])
    expected = "A\tB" 
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_099():
    """Test object creation with expression argument"""
    ast = Program([
        ClassDecl("Box", None, [
            AttributeDecl(False, False, PrimitiveType("int"), [Attribute("val")]),
            ConstructorDecl("Box", [Parameter(PrimitiveType("int"), "v")], BlockStatement([], [
                AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(), [MemberAccess("val")])), Identifier("v"))
            ]))
        ]),
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [VariableDecl(False, ClassType("Box"), [Variable("b", ObjectCreation("Box", [BinaryOp(IntLiteral(1), "+", IntLiteral(2))]))])],
                [
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("b"), [MemberAccess("val")])])]))
                ]
            ))
        ])
    ])
    expected = "3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_100():
    """Integration: Factorial into Array"""
    ast = Program([
        ClassDecl("Main", None, [
            MethodDecl(True, PrimitiveType("void"), "main", [], BlockStatement(
                [
                    VariableDecl(False, ArrayType(PrimitiveType("int"), 5), [Variable("fact")]),
                    VariableDecl(False, PrimitiveType("int"), [Variable("i")])
                ],
                [
                    # Init fact[0] = 1
                    AssignmentStatement(PostfixLHS(PostfixExpression(Identifier("fact"), [ArrayAccess(IntLiteral(0))])), IntLiteral(1)),
                    # Loop 1 to 4
                    ForStatement("i", IntLiteral(1), "to", IntLiteral(4), BlockStatement([], [
                        AssignmentStatement(
                            PostfixLHS(PostfixExpression(Identifier("fact"), [ArrayAccess(Identifier("i"))])),
                            BinaryOp(
                                PostfixExpression(Identifier("fact"), [ArrayAccess(BinaryOp(Identifier("i"), "-", IntLiteral(1)))]),
                                "*",
                                BinaryOp(Identifier("i"), "+", IntLiteral(1))
                            )
                        )
                    ])),
                    # Print fact[4] = 1*2*3*4*5 = 120
                    MethodInvocationStatement(PostfixExpression(Identifier("io"), [MethodCall("writeIntLn", [PostfixExpression(Identifier("fact"), [ArrayAccess(IntLiteral(4))])])]))
                ]
            ))
        ])
    ])
    # 0:1
    # 1: 1*(1+1) = 2
    # 2: 2*(2+1) = 6
    # 3: 6*(3+1) = 24
    # 4: 24*(4+1) = 120
    expected = "120"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


