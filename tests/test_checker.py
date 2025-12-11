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
    static void main() {}
}
"""
    expected = "TypeMismatchInStatement(IfStatement(if Identifier(x) then BlockStatement(stmts=[AssignmentStatement(IdLHS(x) := IntLiteral(1))])))"
    assert Checker(source).check_from_source() == expected

def test_014():
    """Test TypeMismatchInStatement for with bool"""
    source = """
        class ForCheck {
            void check() {
                boolean x;
                for x := 5 to 10 do {}
            }
            static void main() {}
        }
    """
    expected = "TypeMismatchInStatement(ForStatement(for x := IntLiteral(5) to IntLiteral(10) do BlockStatement(stmts=[])))"
    assert Checker(source).check_from_source() == expected

def test_015():
    """Test TypeMismatchInStatement assign int to float (passed)"""
    source = """
    class ValidCoercion {
        void test() {
            float x;
            x := 5;
        }
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_016():
    """Test TypeMismatchInStatement assign int to float (passed)"""
    source = """
    class ValidCoercion {
        void coerce() {
            int x := 10;
            float y := x;  # Valid: int to float coercion
        }
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_017():
   """Test TypeMismatchInStatement with array (wrong arr size)"""
   source = """
   class Test {
        void test() {
            int[5] arr := {1,2,3,4};
        }
        static void main() {}
   }
   """
   expected = "TypeMismatchInStatement(VariableDecl(ArrayType(PrimitiveType(int)[5]), [Variable(arr = ArrayLiteral({IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)}))]))"
   assert Checker(source).check_from_source() == expected

def test_018():
    """Test valid ClassType"""
    source = """
        class Math {}
        class Test {
            void test() {
                Math math := new Math();
            }
            static void main() {}
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_019():
    """Test valid SuperClass"""
    source = """
        class Super {}
        class Child extends Super {}
        class Test {
            void test() {
                Super super := new Child();
            }
            static void main() {}
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_020():
    """Test valid return"""
    source = """
        class Test {
            int test() {
                return 5;
            }
            static void main() {}
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_021():
    """Test TypeMismatchInStatement return"""
    source = """
        class Test {
            int test() {
                return true;
            }
            static void main() {}
        }
    """
    expected = "TypeMismatchInStatement(ReturnStatement(return BoolLiteral(True)))"
    assert Checker(source).check_from_source() == expected

def test_022():
    """Test TypeMismatchInStatement with void lhs"""
    source = """
        class Test {
            void test() {
                void a := 5;
            }
            static void main() {}
        }
    """
    expected = "TypeMismatchInStatement(VariableDecl(PrimitiveType(void), [Variable(a = IntLiteral(5))]))"
    assert Checker(source).check_from_source() == expected

def test_023():
    """Test TypeMismatchInStatement in CallStmt"""
    source = """
        class Test {
            void aaa(int a, b) {}
            void test() {
                this.aaa();
            }
            static void main() {}
        }
    """
    expected = "TypeMismatchInExpression(PostfixExpression(ThisExpression(this).aaa()))"
    # assert ASTGenerator(source).generate().__str__() == expected
    assert Checker(source).check_from_source() == expected

def test_024():
    """Test TypeMismatchInStatement in MethodCall"""
    source = """
        class Math {}
        class Test {
            int add(int a, b) { return a + b; }
            void test() {
                Math math := 5;
            }
            static void main() {}
        }
    """
    expected = "TypeMismatchInStatement(VariableDecl(ClassType(Math), [Variable(math = IntLiteral(5))]))"
    assert Checker(source).check_from_source() == expected

def test_025():
    """Test io"""
    source = """
        class Math {
            static void main() {
                # int a := io.readInt();
                io.writeInt(5);
                io.writeIntLn(10);
            }
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_026():
    """Test TypeMismatchInExpression with array decl"""
    source = """
        class Test {
            static void main() {
                int[1] arr := {1.0};
            }
        }
    """
    expected = "TypeMismatchInStatement(VariableDecl(ArrayType(PrimitiveType(int)[1]), [Variable(arr = ArrayLiteral({FloatLiteral(1.0)}))]))"
    assert Checker(source).check_from_source() == expected

def test_027():
    """Test TypeMismatchInExpression with array access"""
    source = """
        class Test {
            static void main() {
                int[1] arr := {1};
                int a := arr[true];
            }
        }
    """
    expected = "TypeMismatchInExpression(PostfixExpression(Identifier(arr)[BoolLiteral(True)]))"
    assert Checker(source).check_from_source() == expected

def test_028():
    """Test TypeMismatchInExpression with array access"""
    source = """
        class Test {
            static void main() {
                int arr := 5;
                int a := arr[1];
            }
        }
    """
    expected = "TypeMismatchInExpression(PostfixExpression(Identifier(arr)[IntLiteral(1)]))"
    assert Checker(source).check_from_source() == expected

def test_029():
    """Test valid array access"""
    source = """
        class Test {
            static void main() {
                int[1] arr := {5};
                int a := arr[1];
            }
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_030():
    """Test valid binary_op"""
    source = """
        class Test {
            static void main() {
                float a := 3 + 4.0;
            }
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_031():
    """Test valid boolean binary_op"""
    source = """
        class Test {
            static void main() {
                boolean a := (3>2.0) || true;
            }
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_032():
    """Test TypeMismatchInExpression with boolean binary_op"""
    source = """
        class Test {
            static void main() {
                boolean a := (3>2) || true;
            }
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_033():
    """Test TypeMismatchInExpression with comparison binary_op"""
    source = """
        class Test {
            static void main() {
                boolean a := (3>true) || true;
            }
        }
    """
    expected = "TypeMismatchInExpression(BinaryOp(IntLiteral(3), >, BoolLiteral(True)))"
    assert Checker(source).check_from_source() == expected

def test_034():
    """Test TypeMismatchInExpression with not ClassType MethodCall"""
    source = """
        class Test {
            static void main() {
                int a;
                int b := a.get();
            }
        }
    """
    expected = "TypeMismatchInExpression(PostfixExpression(Identifier(a).get()))"
    assert Checker(source).check_from_source() == expected

def test_035():
    """Test TypeMismatchInExpression with void MethodCall"""
    source = """
        class Test {
            void get() {}
            static void main() {
                int b := this.get();
            }
        }
    """
    expected = "TypeMismatchInExpression(PostfixExpression(ThisExpression(this).get()))"
    assert Checker(source).check_from_source() == expected

def test_036():
    """Test valid chain MethodCall and MemberAccess"""
    source = """
        class Math {
            int a_math := 5;
            int get_int() { return 5; }
        }
        class Test {
            Math get_math() { return new Math(); }
            static void main() {
                Math a_math := new Math();
                int a := this.get_math().get_int();
                int b := this.get_math().a_math;
                int c := a_math.a_math;
            }
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_037():
    """Test valid chain MethodCall and MemberAccess (Shape -> Circle) with OOP"""
    source = """
        class Shape {
            float get_area() {}
        }
        class Circle extends Shape {
            float radius;
            final float PI;
            Circle(float radius) {
                this.PI := 3.14;
                this.radius := radius;
            }
            float get_area() {
                return this.PI * this.radius;
            }
        }
        class Test {
            static void main() {
                Shape circle := new Circle(3.0);
                io.writeFloat(circle.get_area());
            }
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_038():
    """Test extremely valid constant decl (passed)"""
    source = """
        class Shape {
            float get_area() {}
        }
        class Circle extends Shape {
            float radius;
            final float PI := 3;
            Circle(int radius) {
                this.radius := radius;
            }
            float get_area() {
                return this.PI * this.radius;
            }
        }
        class Test {
            final int[4] PRIMES := {2, 3, 5, 7};   # Valid
            final int MAX_SIZE := 1000;           # Valid
            final float PI := 3.14159;            # Valid
            final string APP_NAME := "MyApp";     # Valid
            Shape CIRCLE := Circle(3);
            static void main() {
                io.writeFloat(CIRCLE.get_area());
            }
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_039():
    """ Test break/continue outside loop"""
    source = """
        class Test {
            void conditionalError() {
                if true then {
                    break;     # MustInLoop(break)
                    continue;  # MustInLoop(continue)
                }
            }
            static void main() {}
        }
    """
    expected = "MustInLoop(BreakStatement())"
    assert Checker(source).check_from_source() == expected

def test_040():
    """ Test break/continue outside loop"""
    source = """
        class Test {
            void conditionalError() {
                if true then {
                    continue;  # MustInLoop(continue)
                }
            }
            static void main() {}
        }
    """
    expected = "MustInLoop(ContinueStatement())"
    assert Checker(source).check_from_source() == expected

def test_041():
    """ Test valid break/continue in nested loop """
    source = """
    class Test {
        void nestedLoops() {
            int i, j;
            for i := 0 to 5 do {
                for j := 0 to 5 do {
                    if i == j then {
                        continue;  # Valid - affects inner loop
                    }
                    if j > 3 then {
                        break;     # Valid - breaks inner loop
                    }
                }
                break;
            }
        }
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_042():
    """ Test IllegalConstantExpression """
    source = """
    class Test {
        final int a := 3;
        final int b := a;
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_043():
    """Test extreme valid ConstantExpression"""
    source = """
# Valid: Proper constant expressions
class ValidConstantExpressions {
    final int MAX_SIZE := 100;
    final int DOUBLE_SIZE := MAX_SIZE * 2;     # Valid: uses immutable attribute
    final string MESSAGE := "Hello" ^ "World"; # Valid: literal concatenation
    final boolean FLAG := true && false;       # Valid: boolean literals with operators
    final float PI := 3.14159;
    final float CIRCLE_AREA := PI * 10 * 10;   # Valid: uses final attribute
    
    final int SUM := 10 + 20 + 30;         # Valid: literal arithmetic
    static void main() {}
}
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_044():
    """Test IllegalConstantExpression"""
    source = """
# Error: Complex expressions with variables
class ComplexIllegalExpression {
    int a := 10;
    
    final int result := (a * 2) + 5;  # Error: IllegalConstantExpression at constant declaration
    final boolean flag := isValid();   # Error: IllegalConstantExpression at constant declaration
    
    boolean isValid() {
        return true;
    }
}
    """
    expected = "IllegalConstantExpression(AttributeDecl(final PrimitiveType(int), [Attribute(result = BinaryOp(ParenthesizedExpression((BinaryOp(Identifier(a), *, IntLiteral(2)))), +, IntLiteral(5)))]))"
    assert Checker(source).check_from_source() == expected

def test_045():
    """Test IllegalConstantExpression"""
    source = """
# Error: Method calls in constant expression
class MethodCallInConstant {
    final int value := getValue();  # Error: IllegalConstantExpression at constant declaration
    
    int getValue() {
        return 42;
    }
}
    """
    expected = "IllegalConstantExpression(AttributeDecl(final PrimitiveType(int), [Attribute(value = .getValue())]))"
    assert Checker(source).check_from_source() == expected

def test_046():
    """Test IllegalConstantExpression"""
    source = """
# Error: Array element access in constant
class ArrayAccessInConstant {
    final int[5] NUMBERS := {1, 2, 3, 4, 5};
    final int FIRST := NUMBERS[0];  # Error: IllegalConstantExpression at constant declaration
}
    """
    expected = "IllegalConstantExpression(AttributeDecl(final PrimitiveType(int), [Attribute(FIRST = PostfixExpression(Identifier(NUMBERS)[IntLiteral(0)]))]))"
    assert Checker(source).check_from_source() == expected

def test_047():
    """Test valid MemberAccess"""
    source = """
# Setup classes for examples
class Student {
    string name;
    int age;
    static int totalStudents := 0;
    string school := "Default School";
    
    static void resetCount() {
        totalStudents := 0;
    }
    
    void setName(string n) {
        name := n;
    }
    
    void secretMethod() {
        io.writeStrLn("Secret");
    }
}
# Valid: Proper member access
class ValidAccess {
    void test() {
        # Correct static access
        int count := Student.totalStudents;  # Valid
        Student s := new Student();
        s.school := "New School";            # Valid - instance member

        Student.resetCount();               # Valid
        
        # Correct instance access
        s.setName("Alice");                 # Valid - instance method
    }
}

# Valid: Access from within inheritance hierarchy
class GraduateStudent extends Student {
    void accessProtected() {
        age := 25;                          # Valid - inherited member
        this.setName("Graduate");               # Valid - inherited method
    }
    static void main() {}
}
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_048():
    """Test illegalMemberAccess"""
    source = """
# Setup classes for examples
class Student {
    string name;
    int age;
    static int totalStudents := 0;
    string school := "Default School";
    
    static void resetCount() {
        totalStudents := 0;
    }
    
    void setName(string n) {
        name := n;
    }
    
    void secretMethod() {
        io.writeStrLn("Secret");
    }
}

# Error: Accessing instance member via class
class StaticAccessError {
    void test() {
        string school := Student.school;     # Error: IllegalMemberAccess at member access
        Student.setName("John");            # Error: IllegalMemberAccess at method call
    }
    static void main() {}
}
    """
    expected = "IllegalMemberAccess(PostfixExpression(Identifier(Student).school))"
    assert Checker(source).check_from_source() == expected

def test_049():
    """Test illegalMemberAccess"""
    source = """
# Setup classes for examples
class Student {
    string name;
    int age;
    static int totalStudents := 0;
    string school := "Default School";
    
    static void resetCount() {
        totalStudents := 0;
    }
    
    void setName(string n) {
        name := n;
    }
    
    void secretMethod() {
        io.writeStrLn("Secret");
    }
}

# Error: Accessing instance member via class
class StaticAccessError {
    void test() {
        Student.setName("John");            # Error: IllegalMemberAccess at method call
    }
    static void main() {}
}
    """
    expected = "IllegalMemberAccess(PostfixExpression(Identifier(Student).setName(StringLiteral('John'))))"
    assert Checker(source).check_from_source() == expected

def test_050():
    """Test illegalMemberAccess"""
    source = """
# Setup classes for examples
class Student {
    string name;
    int age;
    static int totalStudents := 0;
    string school := "Default School";
    
    static void resetCount() {
        totalStudents := 0;
    }
    
    void setName(string n) {
        name := n;
    }
    
    void secretMethod() {
        io.writeStrLn("Secret");
    }
}

# Error: Accessing static member via instance
class InstanceAccessError {
    void test() {
        Student s := new Student();
        int count := s.totalStudents;        # Error: IllegalMemberAccess at member access
        s.resetCount();                     # Error: IllegalMemberAccess at method call
    }
    static void main() {}
}
    """
    expected = "IllegalMemberAccess(PostfixExpression(Identifier(s).totalStudents))"
    assert Checker(source).check_from_source() == expected

def test_051():
    """Test illegalMemberAccess"""
    source = """
# Setup classes for examples
class Student {
    string name;
    int age;
    static int totalStudents := 0;
    string school := "Default School";
    
    static void resetCount() {
        totalStudents := 0;
    }
    
    void setName(string n) {
        name := n;
    }
    
    void secretMethod() {
        io.writeStrLn("Secret");
    }
}

# Error: Accessing static member via instance
class InstanceAccessError {
    void test() {
        Student s := new Student();
        s.resetCount();                     # Error: IllegalMemberAccess at method call
    }
    static void main() {}
}
    """
    expected = "IllegalMemberAccess(PostfixExpression(Identifier(s).resetCount()))"
    assert Checker(source).check_from_source() == expected

def test_052():
    """Variable in block scope has same name with each other"""
    source = """
    class Test {
        static void main() {
            {
                int y := 5;
                int y := 10;
            }
        }
    }
    """  
    expected = "Redeclared(Variable, y)"
    assert Checker(source).check_from_source() == expected

def test_053():
    """Parameter has same name as variable"""
    source = """
    class Test {
        static void main(int re_var) {
            int re_var;
        }
    }
    """  
    expected = "Redeclared(Variable, re_var)"
    assert Checker(source).check_from_source() == expected

def test_054():
    """Test valid array assignment"""
    source = """
    class Test {
        static void main() {
            int[5] arr1 := {1, 2, 3, 4, 5};
            int[5] arr2 := arr1;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_055():
    """Test array size mismatch"""
    source = """
    class Test {
        static void main() {
            int[5] arr1;
            int[3] arr2 := {1, 2, 3};
            arr1 := arr2;
        }
    }
    """
    expected = "TypeMismatchInStatement(AssignmentStatement(IdLHS(arr1) := Identifier(arr2)))"
    assert Checker(source).check_from_source() == expected

def test_056():
    """Test valid nested class access"""
    source = """
    class Parent {
        int value := 10;
    }
    class Test {
        static void main() {
            Parent p := new Parent();
            int x := p.value;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_057():
    """Test method return type match"""
    source = """
    class Test {
        int getValue() {
            return 42;
        }
        static void main() {
            Test t := new Test();
            int x := t.getValue();
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_058():
    """Test method return type mismatch"""
    source = """
    class Test {
        int getValue() {
            return "hello";
        }
        static void main() {}
    }
    """
    expected = "TypeMismatchInStatement(ReturnStatement(return StringLiteral('hello')))"
    assert Checker(source).check_from_source() == expected

def test_059():
    """Test valid boolean operations"""
    source = """
    class Test {
        static void main() {
            boolean a := true && false;
            boolean b := !a || true;
            boolean c := (5 > 3) && (10 <= 20);
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_060():
    """Test invalid boolean operation with non-boolean"""
    source = """
    class Test {
        static void main() {
            boolean a := 5 && true;
        }
    }
    """
    expected = "TypeMismatchInExpression(BinaryOp(IntLiteral(5), &&, BoolLiteral(True)))"
    assert Checker(source).check_from_source() == expected

def test_061():
    """Test valid arithmetic operations"""
    source = """
    class Test {
        static void main() {
            int a := 10 + 20;
            int b := a - 5;
            int c := b * 2;
            float d := 10 / 3;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_062():
    """Test string concatenation"""
    source = """
    class Test {
        static void main() {
            string s1 := "Hello";
            string s2 := "World";
            string s3 := s1 ^ s2;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_063():
    """Test invalid string operation"""
    source = """
    class Test {
        static void main() {
            string s := "Hello" + 5;
        }
    }
    """
    expected = "TypeMismatchInExpression(BinaryOp(StringLiteral('Hello'), +, IntLiteral(5)))"
    assert Checker(source).check_from_source() == expected

def test_064():
    """Test valid for loop"""
    source = """
    class Test {
        static void main() {
            int i;
            for i := 1 to 10 do {
                int x := i;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_065():
    """Test valid break in loop"""
    source = """
    class Test {
        static void main() {
            int i;
            for i := 1 to 10 do {
                if (i == 5) then {
                    break;
                }
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_066():
    """Test valid continue in loop"""
    source = """
    class Test {
        static void main() {
            int i;
            for i := 1 to 10 do {
                if (i == 5) then {
                    continue;
                }
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_067():
    """Test invalid break outside loop"""
    source = """
    class Test {
        void doSomething() {
            break;
        }
        static void main() {}
    }
    """
    expected = "MustInLoop(BreakStatement())"
    assert Checker(source).check_from_source() == expected

def test_068():
    """Test valid constructor"""
    source = """
    class Person {
        string name;
        int age;
        Person(string n; int a) {
            name := n;
            age := a;
        }
    }
    class Test {
        static void main() {
            Person p := new Person("John", 30);
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_069():
    """Test destructor"""
    source = """
    class Resource {
        ~Resource() {
            io.writeStrLn("Cleaning up");
        }
    }
    class Test {
        static void main() {
            Resource r := new Resource();
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_070():
    """Test inheritance with method override"""
    source = """
    class Animal {
        void makeSound() {
            io.writeStrLn("Some sound");
        }
    }
    class Dog extends Animal {
        void makeSound() {
            io.writeStrLn("Woof");
        }
    }
    class Test {
        static void main() {
            Dog d := new Dog();
            d.makeSound();
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_071():
    """Test valid polymorphism - child to parent"""
    source = """
    class Animal {}
    class Dog extends Animal {}
    class Test {
        static void main() {
            Animal a := new Dog();
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_072():
    """Test invalid polymorphism - parent to child"""
    source = """
    class Animal {}
    class Dog extends Animal {}
    class Test {
        static void main() {
            Dog d := new Animal();
        }
    }
    """
    expected = "TypeMismatchInStatement(VariableDecl(ClassType(Dog), [Variable(d = ObjectCreation(new Animal()))]))"
    assert Checker(source).check_from_source() == expected

def test_073():
    """Test array access with valid index"""
    source = """
    class Test {
        static void main() {
            int[10] arr;
            int x := arr[5];
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_074():
    """Test array access with invalid index type"""
    source = """
    class Test {
        static void main() {
            int[10] arr;
            int x := arr[true];
        }
    }
    """
    expected = "TypeMismatchInExpression(PostfixExpression(Identifier(arr)[BoolLiteral(True)]))"
    assert Checker(source).check_from_source() == expected

def test_075():
    """Test comparison operators"""
    source = """
    class Test {
        static void main() {
            boolean b1 := 5 > 3;
            boolean b2 := 10 <= 20;
            boolean b3 := 5 == 5;
            boolean b4 := 3 != 4;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_076():
    """Test unary minus"""
    source = """
    class Test {
        static void main() {
            int x := -5;
            float y := -3.14;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_077():
    """Test unary not"""
    source = """
    class Test {
        static void main() {
            boolean a := !true;
            boolean b := !false;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_078():
    """Test division returns float"""
    source = """
    class Test {
        static void main() {
            float x := 10 / 3;
            float y := 10 % 3;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_079():
    """Test invalid division assignment to int"""
    source = """
    class Test {
        static void main() {
            int x := 10 / 3;
        }
    }
    """
    expected = "TypeMismatchInStatement(VariableDecl(PrimitiveType(int), [Variable(x = BinaryOp(IntLiteral(10), /, IntLiteral(3)))]))"
    assert Checker(source).check_from_source() == expected

def test_080():
    """Test valid final constant with literal"""
    source = """
    class Test {
        static void main() {
            final int MAX := 100;
            final boolean FLAG := true;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_081():
    """Test invalid final constant with variable"""
    source = """
    class Test {
        static void main() {
            int x := 5;
            final int Y := x;
        }
    }
    """
    expected = "IllegalConstantExpression(Identifier(x))"
    assert Checker(source).check_from_source() == expected

def test_082():
    """Test valid final constant with expression"""
    source = """
    class Test {
        static void main() {
            final int MAX := 50 + 50;
            final boolean FLAG := true && false;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_083():
    """Test method parameter type check"""
    source = """
    class Test {
        void process(int x; string s) {
            int y := x + 10;
        }
        static void main() {
            Test t := new Test();
            t.process(5, "hello");
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_084():
    """Test method parameter count mismatch would be caught"""
    source = """
    class Test {
        void process(int x) {
            int y := x;
        }
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_085():
    """Test this expression"""
    source = """
    class Test {
        int value;
        void setValue(int v) {
            this.value := v;
        }
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_086():
    """Test undeclared class"""
    source = """
    class Test {
        static void main() {
            UnknownClass obj := new UnknownClass();
        }
    }
    """
    expected = "UndeclaredClass(UnknownClass)"
    assert Checker(source).check_from_source() == expected

def test_087():
    """Test undeclared attribute"""
    source = """
    class Test {
        int x;
        static void main() {
            Test t := new Test();
            int y := t.unknownAttr;
        }
    }
    """
    expected = "UndeclaredAttribute(unknownAttr)"
    assert Checker(source).check_from_source() == expected

def test_088():
    """Test undeclared method"""
    source = """
    class Test {
        static void main() {
            Test t := new Test();
            t.unknownMethod();
        }
    }
    """
    expected = "UndeclaredMethod(unknownMethod)"
    assert Checker(source).check_from_source() == expected

def test_089():
    """Test valid static method call"""
    source = """
    class Math {
        static int add(int a; int b) {
            return a + b;
        }
    }
    class Test {
        static void main() {
            int sum := Math.add(5, 10);
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_090():
    """Test valid static attribute access"""
    source = """
    class Counter {
        static int count := 0;
    }
    class Test {
        static void main() {
            int c := Counter.count;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_091():
    """Test illegal access static via instance"""
    source = """
    class Counter {
        static int count := 0;
    }
    class Test {
        static void main() {
            Counter c := new Counter();
            int x := c.count;
        }
    }
    """
    expected = "IllegalMemberAccess(PostfixExpression(Identifier(c).count))"
    assert Checker(source).check_from_source() == expected

def test_092():
    """Test illegal access instance via class"""
    source = """
    class Counter {
        int value := 0;
    }
    class Test {
        static void main() {
            int x := Counter.value;
        }
    }
    """
    expected = "IllegalMemberAccess(PostfixExpression(Identifier(Counter).value))"
    assert Checker(source).check_from_source() == expected

def test_093():
    """Test valid io operations"""
    source = """
    class Test {
        static void main() {
            int x := io.readInt();
            io.writeInt(x);
            io.writeIntLn(42);
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_094():
    """Test multiple inheritance levels"""
    source = """
    class GrandParent {
        int value := 1;
    }
    class Parent extends GrandParent {
        int data := 2;
    }
    class Child extends Parent {
        void test() {
            int x := this.value;
            int y := this.data;
        }
    }
    class Test {
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_095():
    """Test cannot assign to final attribute inherited"""
    source = """
    class Parent {
        final int value := 10;
    }
    class Child extends Parent {
        void modify() {
            this.value := 20;
        }
    }
    class Test {
        static void main() {}
    }
    """
    expected = "CannotAssignToConstant(AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(this).value)) := IntLiteral(20)))"
    assert Checker(source).check_from_source() == expected

def test_096():
    """Test valid nested for loops"""
    source = """
    class Test {
        static void main() {
            int i, j;
            for i := 1 to 10 do {
                for j := 1 to 5 do {
                    int x := i + j;
                }
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_097():
    """Test valid nested if statements"""
    source = """
    class Test {
        static void main() {
            if (5 > 3) then {
                if (true) then {
                    int x := 10;
                }
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_098():
    """Test valid else clause"""
    source = """
    class Test {
        static void main() {
            int x;
            if (5 > 3) then {
                x := 10;
            } else {
                x := 20;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_099():
    """Test complex expression evaluation"""
    source = """
    class Test {
        static void main() {
            int result := (5 + 10) * 2 - (3 * 4);
            boolean flag := (10 > 5) && (3 < 7) || false;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_100():
    """Test comprehensive valid program"""
    source = """
    class Calculator {
        int value;
        Calculator(int initial) {
            value := initial;
        }
        int add(int x) {
            value := value + x;
            return value;
        }
        int getValue() {
            return value;
        }
    }
    class Test {
        static void main() {
            Calculator calc := new Calculator(10);
            int result := calc.add(5);
            io.writeInt(calc.getValue());
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_101():
    """Test NoEntryPoint - no main method"""
    source = """
    class Test {
        void test() {
            int x := 5;
        }
    }
    """
    expected = "No Entry Point"
    assert Checker(source).check_from_source() == expected

def test_102():
    """Test NoEntryPoint - non-static main"""
    source = """
    class Test {
        void main() {
            int x := 5;
        }
    }
    """
    expected = "No Entry Point"
    assert Checker(source).check_from_source() == expected

def test_103():
    """Test NoEntryPoint - main with parameters"""
    source = """
    class Test {
        static void main(int x) {
            int y := 5;
        }
    }
    """
    expected = "No Entry Point"
    assert Checker(source).check_from_source() == expected

def test_104():
    """Test NoEntryPoint - main with non-void return"""
    source = """
    class Test {
        static int main() {
            return 5;
        }
    }
    """
    expected = "No Entry Point"
    assert Checker(source).check_from_source() == expected

def test_105():
    """Test NoEntryPoint - main with multiple parameters"""
    source = """
    class Test {
        static void main(int x; string s) {
            int y := 5;
        }
    }
    """
    expected = "No Entry Point"
    assert Checker(source).check_from_source() == expected

def test_106():
    """Test NoEntryPoint - main is an attribute not a method"""
    source = """
    class Test {
        static int main := 5;
        void test() {
            int x := main;
        }
    }
    """
    expected = "No Entry Point"
    assert Checker(source).check_from_source() == expected

def test_107():
    """Test valid entry point - static void main()"""
    source = """
    class Test {
        static void main() {
            int x := 5;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_108():
    """Test valid entry point with other methods"""
    source = """
    class Test {
        void helper() {
            int x := 10;
        }
        static void main() {
            int y := 5;
        }
        int calculate(int a; int b) {
            return a + b;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_109():
    """Test valid entry point in different class"""
    source = """
    class Helper {
        void assist() {
            int x := 1;
        }
    }
    class Main {
        static void main() {
            Helper h := new Helper();
            h.assist();
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_110():
    """Test NoEntryPoint - main returns string"""
    source = """
    class Test {
        static string main() {
            return "hello";
        }
    }
    """
    expected = "No Entry Point"
    assert Checker(source).check_from_source() == expected

def test_111():
    """Test error priority: Undeclared (P1) over TypeMismatch (P2)"""
    source = """
    class Test {
        static void main() {
            int x := unknownVar;
            int y := "string";
        }
    }
    """
    expected = "UndeclaredIdentifier(unknownVar)"
    assert Checker(source).check_from_source() == expected

def test_112():
    """Test error priority: Redeclared (P1) over TypeMismatch (P2)"""
    source = """
    class Test {
        static void main() {
            int x := 5;
            int x := 10;
            int y := "hello";
        }
    }
    """
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_113():
    """Test error priority: UndeclaredClass (P1) over TypeMismatch (P2)"""
    source = """
    class Test {
        static void main() {
            UnknownClass obj := new UnknownClass();
            int x := "not an int";
        }
    }
    """
    expected = "UndeclaredClass(UnknownClass)"
    assert Checker(source).check_from_source() == expected

def test_114():
    """Test error priority: UndeclaredAttribute (P1) over IllegalMemberAccess (P3)"""
    source = """
    class Counter {
        static int count := 0;
    }
    class Test {
        static void main() {
            Counter c := new Counter();
            int x := c.unknown;
            int y := c.count;
        }
    }
    """
    expected = "UndeclaredAttribute(unknown)"
    assert Checker(source).check_from_source() == expected

def test_115():
    """Test error priority: TypeMismatch (P2) over IllegalMemberAccess (P3)"""
    source = """
    class Counter {
        static int count := 0;
    }
    class Test {
        static void main() {
            int x := "string not int";
            Counter c := new Counter();
            int y := c.count;
        }
    }
    """
    expected = "TypeMismatchInStatement(VariableDecl(PrimitiveType(int), [Variable(x = StringLiteral('string not int'))]))"
    assert Checker(source).check_from_source() == expected

def test_116():
    """Test error priority: TypeMismatch (P2) over MustInLoop (P4)"""
    source = """
    class Test {
        static void main() {
            int x := true;
            break;
        }
    }
    """
    expected = "TypeMismatchInStatement(VariableDecl(PrimitiveType(int), [Variable(x = BoolLiteral(True))]))"
    assert Checker(source).check_from_source() == expected

def test_117():
    """Test error priority: TypeMismatch (P2) over CannotAssignToConstant (P5)"""
    source = """
    class Test {
        static void main() {
            int x := "not int";
            final int y := 5;
            y := 10;
        }
    }
    """
    expected = "TypeMismatchInStatement(VariableDecl(PrimitiveType(int), [Variable(x = StringLiteral('not int'))]))"
    assert Checker(source).check_from_source() == expected

def test_118():
    """Test error priority: IllegalMemberAccess (P3) over MustInLoop (P4)"""
    source = """
    class Counter {
        static int count := 0;
    }
    class Test {
        static void main() {
            Counter c := new Counter();
            int x := c.count;
            break;
        }
    }
    """
    expected = "IllegalMemberAccess(PostfixExpression(Identifier(c).count))"
    assert Checker(source).check_from_source() == expected

def test_119():
    """Test error priority: IllegalMemberAccess (P3) over CannotAssignToConstant (P5)"""
    source = """
    class Counter {
        static int count := 0;
    }
    class Test {
        static void main() {
            Counter c := new Counter();
            int x := c.count;
            final int y := 5;
            y := 10;
        }
    }
    """
    expected = "IllegalMemberAccess(PostfixExpression(Identifier(c).count))"
    assert Checker(source).check_from_source() == expected

def test_120():
    """Test error priority: MustInLoop (P4) over CannotAssignToConstant (P5)"""
    source = """
    class Test {
        static void main() {
            final int x := 5;
            x := 10;
            break;
        }
    }
    """
    expected = "MustInLoop(BreakStatement())"
    assert Checker(source).check_from_source() == expected

def test_121():
    """Test error priority: MustInLoop (P4) over IllegalArrayLiteral (P6)"""
    source = """
    class Test {
        static void main() {
            int[2] arr := {1, "string"};
            continue;
        }
    }
    """
    expected = "MustInLoop(ContinueStatement())"
    assert Checker(source).check_from_source() == expected

def test_122():
    """Test error priority: CannotAssignToConstant (P5) over IllegalArrayLiteral (P6)"""
    source = """
    class Test {
        static void main() {
            final int x := 5;
            int[2] arr := {1, "mixed"};
            x := 10;
        }
    }
    """
    expected = "CannotAssignToConstant(AssignmentStatement(IdLHS(x) := IntLiteral(10)))"
    assert Checker(source).check_from_source() == expected

def test_123():
    """Test error priority: CannotAssignToConstant (P5) over NoEntryPoint (P7)"""
    source = """
    class Test {
        void notMain() {
            final int x := 5;
            x := 10;
        }
    }
    """
    expected = "CannotAssignToConstant(AssignmentStatement(IdLHS(x) := IntLiteral(10)))"
    assert Checker(source).check_from_source() == expected

def test_124():
    """Test error priority: IllegalArrayLiteral (P6) over NoEntryPoint (P7)"""
    source = """
    class Test {
        void notMain() {
            int[3] arr := {1, 2.5, 3};
        }
    }
    """
    expected = "IllegalArrayLiteral(ArrayLiteral({IntLiteral(1), FloatLiteral(2.5), IntLiteral(3)}))"
    assert Checker(source).check_from_source() == expected

def test_125():
    """Test error priority: Multiple declaration errors - first one reported"""
    source = """
    class Test {
        static void main() {
            int x := unknown1;
            int y := unknown2;
        }
    }
    """
    expected = "UndeclaredIdentifier(unknown1)"
    assert Checker(source).check_from_source() == expected

def test_126():
    """Test error priority: UndeclaredMethod (P1) over TypeMismatch (P2)"""
    source = """
    class Test {
        static void main() {
            Test t := new Test();
            int x := "not int";
            t.unknownMethod();
        }
    }
    """
    expected = "UndeclaredMethod(unknownMethod)"
    assert Checker(source).check_from_source() == expected

def test_127():
    """Test error priority: Redeclared class (P1) over all others"""
    source = """
    class Test {
        static void main() {}
    }
    class Test {
        void other() {}
    }
    """
    expected = "Redeclared(Class, Test)"
    assert Checker(source).check_from_source() == expected

def test_128():
    """Test error priority: TypeMismatchInConstant (P2) over CannotAssignToConstant (P5)"""
    source = """
    class Test {
        final int x := "not int";
        static void main() {
            final int y := 5;
            y := 10;
        }
    }
    """
    expected = "TypeMismatchInConstant(AttributeDecl(final PrimitiveType(int), [Attribute(x = StringLiteral('not int'))]))"
    assert Checker(source).check_from_source() == expected

def test_129():
    """Test error priority: IllegalConstantExpression (P5) over NoEntryPoint (P7)"""
    source = """
    class Test {
        void notMain() {
            int x := 5;
            final int y := x;
        }
    }
    """
    expected = "IllegalConstantExpression(Identifier(x))"
    assert Checker(source).check_from_source() == expected

def test_131():
    """Test ReferenceType with void - expect TypeMismatchInExpression"""
    source = """
    class Test {
        void &referenceToVoid;
        static void main() { }
    }
    """
    expected = "TypeMismatchInExpression(ReferenceType(PrimitiveType(void) &))"
    assert Checker(source).check_from_source() == expected


