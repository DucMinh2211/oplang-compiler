from utils import Checker


def test_001():
    """Test a valid program that should pass all checks"""
    source = """
class Test {
    static void main() {
        int x := 5;
        int y := x + 1;
    }
}
"""
    expected = "Static checking passed"
    # Just check that it doesn't return an error
    assert Checker(source).check_from_source() == expected

def test_002():
    """Test redeclared variable error"""
    source = """
class Test {
    static void main() {
        int x := 5;
        int x := 10;
    }
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_003():
    """Test undeclared identifier error"""
    source = """
class Test {
    static void main() {
        int x := y + 1;
    }
}
"""
    expected = "UndeclaredIdentifier(y)"
    assert Checker(source).check_from_source() == expected

def test_004():
    """Test type mismatch error"""
    source = """
class Test {
    static void main() {
        int x := "hello";
    }
}
"""
    expected = "TypeMismatchInStatement(VariableDecl(PrimitiveType(int), [Variable(x = StringLiteral('hello'))]))"
    assert Checker(source).check_from_source() == expected

def test_005():
    """Test break not in loop error"""
    source = """
class Test {
    static void main() {
        break;
    }
}
"""
    expected = "MustInLoop(BreakStatement())"
    assert Checker(source).check_from_source() == expected

def test_006():
    """Test cannot assign to constant error"""
    source = """
class Test {
    static void main() {
        final int x := 5;
        x := 10;
    }
}
"""
    expected = "CannotAssignToConstant(AssignmentStatement(IdLHS(x) := IntLiteral(10)))"
    assert Checker(source).check_from_source() == expected

def test_007():
    """Test illegal array literal error - alternative case"""
    source = """
class Test {
    static void main() {
        boolean[2] flags := {true, 42};
    }
}
"""
    expected = "IllegalArrayLiteral(ArrayLiteral({BoolLiteral(True), IntLiteral(42)}))"
    assert Checker(source).check_from_source() == expected

def test_010():
    """Test TypeMismatchInConstant"""
    source = """
class Test {
    final int a := "hi";
    static void main() {
    }
}
"""
    expected = "TypeMismatchInConstant(AttributeDecl(final PrimitiveType(int), [Attribute(a = StringLiteral('hi'))]))"
    assert Checker(source).check_from_source() == expected

def test_011():
    """Test assign to final in constructor"""
    source = """
class Test {
    final int a := 1;
    Test() {
        a := 2;
    }
    static void main() {
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_012():
    """Test assign to final in constructor and method"""
    source = """
class Test {
    final int a := 1;
    Test() {
        a := 2;
    }
    static void main() {
        a := 3;
    }
}
"""
    expected = "CannotAssignToConstant(AssignmentStatement(IdLHS(a) := IntLiteral(3)))"
    assert Checker(source).check_from_source() == expected

def test_013():
    """Test TypeMismatchInStatement if with int"""
    source = """
class ConditionalError {
    void check() {
        int x := 5;
        if x then {
            x := 1;
        }
    }
}
"""
    expected = "TypeMismatchInStatement(IfStatement(if Identifier(x) then BlockStatement(stmts=[AssignmentStatement(IdLHS(x) := IntLiteral(1))])))"
    assert Checker(source).check_from_source() == expected

def test_14():
    """Test TypeMismatchInStatement for with bool"""
    source = """
        class ForCheck {
            void check() {
                boolean x;
                for x := 5 to 10 do {}
            }
        }
    """
    expected = "TypeMismatchInStatement(ForStatement(for x := IntLiteral(5) to IntLiteral(10) do BlockStatement(stmts=[])))"
    assert Checker(source).check_from_source() == expected

def test_15():
    """Test TypeMismatchInStatement assign int to float (passed)"""
    source = """
    class ValidCoercion {
        void test() {
            float x;
            x := 5;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_16():
    """Test TypeMismatchInStatement assign int to float (passed)"""
    source = """
    class ValidCoercion {
        void coerce() {
            int x := 10;
            float y := x;  # Valid: int to float coercion
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_17():
   """Test TypeMismatchInStatement with array (wrong arr size)"""
   source = """
   class Test {
        void test() {
            int[5] arr := {1,2,3,4};
        }
   }
   """
   expected = "TypeMismatchInStatement(VariableDecl(ArrayType(PrimitiveType(int)[5]), [Variable(arr = ArrayLiteral({IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)}))]))"
   assert Checker(source).check_from_source() == expected

def test_18():
    """Test valid ClassType"""
    source = """
        class Math {}
        class Test {
            void test() {
                Math math := new Math();
            }
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected
