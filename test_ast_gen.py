from tests.utils import ASTGenerator

def test_001():
    """Test basic class declaration AST generation"""
    source = """class TestClass {
        int x;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(int), [Attribute(x)])])])"
    # Just check that it doesn't return an error
    assert str(ASTGenerator(source).generate()) == expected


def test_002():
    """Test class with method declaration AST generation"""
    source = """class TestClass {
        void main() {
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) main([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_003():
    """Test class with constructor AST generation"""
    source = """class TestClass {
        int x;
        TestClass(int x) {
            this.x := x;
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(int), [Attribute(x)]), ConstructorDecl(TestClass([Parameter(PrimitiveType(int) x)]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(this).x)) := Identifier(x))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_004():
    """Test class with inheritance AST generation"""
    source = """class Child extends Parent {
        int y;
    }"""
    expected = "Program([ClassDecl(Child, extends Parent, [AttributeDecl(PrimitiveType(int), [Attribute(y)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_005():
    """Test static and final attributes AST generation"""
    source = """class TestClass {
        static final int MAX_SIZE := 100;
        final float PI := 3.14;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(static final PrimitiveType(int), [Attribute(MAX_SIZE = IntLiteral(100))]), AttributeDecl(final PrimitiveType(float), [Attribute(PI = FloatLiteral(3.14))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_006():
    """Test if-else statement AST generation"""
    source = """class TestClass {
        void main() {
            if x > 0 then {
                return x;
            } else {
                return 0;
            }
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) main([]), BlockStatement(stmts=[IfStatement(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStatement(stmts=[ReturnStatement(return Identifier(x))]), else BlockStatement(stmts=[ReturnStatement(return IntLiteral(0))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_007():
    """Test for loop AST generation"""
    source = """class TestClass {
        void main() {
            int sum := 0;
            for i := 1 to 10 do {
                sum := sum + i;
            }
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) main([]), BlockStatement(vars=[VariableDecl(PrimitiveType(int), [Variable(sum = IntLiteral(0))])], stmts=[ForStatement(for i := IntLiteral(1) to IntLiteral(10) do BlockStatement(stmts=[AssignmentStatement(IdLHS(sum) := BinaryOp(Identifier(sum), +, Identifier(i)))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_008():
    """Test array operations AST generation"""
    source = """class TestClass {
        void main() {
            int[5] arr;
            arr[0] := 42;
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) main([]), BlockStatement(vars=[VariableDecl(ArrayType(PrimitiveType(int)[5]), [Variable(arr)])], stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(Identifier(arr)[IntLiteral(0)])) := IntLiteral(42))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_009():
    """Test object creation and method call AST generation"""
    source = """class TestClass {
        void main() {
            Rectangle r := new Rectangle(5.0, 3.0);
            float area := r.getArea();
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) main([]), BlockStatement(vars=[VariableDecl(ClassType(Rectangle), [Variable(r = ObjectCreation(new Rectangle(FloatLiteral(5.0), FloatLiteral(3.0))))]), VariableDecl(PrimitiveType(float), [Variable(area = PostfixExpression(Identifier(r).getArea()))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_010():
    """Test reference type AST generation"""
    source = """class TestClass {
        void swap(int & a; int & b) {
            int temp := a;
            a := b;
            b := temp;
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) swap([Parameter(ReferenceType(PrimitiveType(int) &) a), Parameter(ReferenceType(PrimitiveType(int) &) b)]), BlockStatement(vars=[VariableDecl(PrimitiveType(int), [Variable(temp = Identifier(a))])], stmts=[AssignmentStatement(IdLHS(a) := Identifier(b)), AssignmentStatement(IdLHS(b) := Identifier(temp))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_011():
    """Test destructor AST generation"""
    source = """class TestClass {
        ~TestClass() {
            int x := 0;
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [DestructorDecl(~TestClass(), BlockStatement(vars=[VariableDecl(PrimitiveType(int), [Variable(x = IntLiteral(0))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_012():
    """Test final att"""
    source = """
        class T {
            final int a;
            float b, c;
        }
    """
    expected = "Program([ClassDecl(T, [AttributeDecl(final PrimitiveType(int), [Attribute(a)]), AttributeDecl(PrimitiveType(float), [Attribute(b), Attribute(c)])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_013():
    """Test array att"""
    source = """
        class T {
            final int[3] a;
        }
        class C {}
    """
    expected = "Program([ClassDecl(T, [AttributeDecl(final ArrayType(PrimitiveType(int)[3]), [Attribute(a)])]), ClassDecl(C, [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_014():
    """Test constructor"""
    source = """
        class T {
            T(){}
        }
        class C {}
    """
    expected = "Program([ClassDecl(T, [ConstructorDecl(T([]), BlockStatement(stmts=[]))]), ClassDecl(C, [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_015():
    """Test methodDecl"""
    source = """
        class T {
            void do_this() {}
        }
        class C {}
    """
    expected = "Program([ClassDecl(T, [MethodDecl(PrimitiveType(void) do_this([]), BlockStatement(stmts=[]))]), ClassDecl(C, [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_016():
    """Test methodDecl with params"""
    source = """
        class T {
            void do_this(int a, b) {}
        }
        class C {}
    """
    expected = "Program([ClassDecl(T, [MethodDecl(PrimitiveType(void) do_this([Parameter(PrimitiveType(int) a), Parameter(PrimitiveType(int) b)]), BlockStatement(stmts=[]))]), ClassDecl(C, [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_017():
    """Test break, continue stmt"""
    source = """
        class T {
            void do_this() {
                break;
                continue;
            }
        }
        class C {}
    """
    expected = "Program([ClassDecl(T, [MethodDecl(PrimitiveType(void) do_this([]), BlockStatement(stmts=[BreakStatement(), ContinueStatement()]))]), ClassDecl(C, [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_018():
    """Test VarDecl"""
    source = """
        class T {
            void do_this() {
                a := b;
            }
        }
    """
    expected = "Program([ClassDecl(T, [MethodDecl(PrimitiveType(void) do_this([]), BlockStatement(stmts=[AssignmentStatement(IdLHS(a) := Identifier(b))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_019():
    """Test simple expr"""
    source = """
        class T {
            int c := a + b;
        }
    """
    expected = "Program([ClassDecl(T, [AttributeDecl(PrimitiveType(int), [Attribute(c = BinaryOp(Identifier(a), +, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_020():
    """Test simple recursive this expr"""
    source = """
        class T {
            void do_this() {
                this.a.b := this.a;
            }
        }
    """
    expected = "Program([ClassDecl(T, [MethodDecl(PrimitiveType(void) do_this([]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(this).a.b)) := PostfixExpression(ThisExpression(this).a))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_021():
    """Test class with multiple attributes of same type"""
    source = """class TestClass {
        int a, b, c;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(int), [Attribute(a), Attribute(b), Attribute(c)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_022():
    """Test class with mixed attributes"""
    source = """class TestClass {
        int x := 10;
        float y;
        boolean z := true;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(int), [Attribute(x = IntLiteral(10))]), AttributeDecl(PrimitiveType(float), [Attribute(y)]), AttributeDecl(PrimitiveType(boolean), [Attribute(z = BoolLiteral(True))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_023():
    """Test class with string attribute"""
    source = """class TestClass {
        string name := "Hello";
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(string), [Attribute(name = StringLiteral('Hello'))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_024():
    """Test empty class"""
    source = """class Empty {}"""
    expected = "Program([ClassDecl(Empty, [])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_025():
    """Test static attribute"""
    source = """class TestClass {
        static int count;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(static PrimitiveType(int), [Attribute(count)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_026():
    """Test static method"""
    source = """class TestClass {
        static void helper() {}
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(static PrimitiveType(void) helper([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_027():
    """Test method with return type reference"""
    source = """class TestClass {
        int & getRef() {}
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(ReferenceType(PrimitiveType(int) &) getRef([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_028():
    """Test method with single parameter"""
    source = """class TestClass {
        void process(int value) {}
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) process([Parameter(PrimitiveType(int) value)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_029():
    """Test method with multiple parameters of different types"""
    source = """class TestClass {
        void process(int x; float y; boolean flag) {}
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) process([Parameter(PrimitiveType(int) x), Parameter(PrimitiveType(float) y), Parameter(PrimitiveType(boolean) flag)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_030():
    """Test method with reference parameters"""
    source = """class TestClass {
        void modify(int & x; float & y) {}
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) modify([Parameter(ReferenceType(PrimitiveType(int) &) x), Parameter(ReferenceType(PrimitiveType(float) &) y)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_031():
    """Test copy constructor"""
    source = """class TestClass {
        TestClass(TestClass other) {}
    }"""
    expected = "Program([ClassDecl(TestClass, [ConstructorDecl(TestClass([Parameter(ClassType(TestClass) other)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_032():
    """Test user-defined constructor with multiple parameters"""
    source = """class TestClass {
        TestClass(int x; float y; string name) {}
    }"""
    expected = "Program([ClassDecl(TestClass, [ConstructorDecl(TestClass([Parameter(PrimitiveType(int) x), Parameter(PrimitiveType(float) y), Parameter(PrimitiveType(string) name)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_033():
    """Test array type attribute"""
    source = """class TestClass {
        int[10] numbers;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(ArrayType(PrimitiveType(int)[10]), [Attribute(numbers)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_034():
    """Test array type with reference"""
    source = """class TestClass {
        int[5] & getArray() {}
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(ReferenceType(ArrayType(PrimitiveType(int)[5]) &) getArray([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_035():
    """Test class type attribute"""
    source = """class TestClass {
        Rectangle rect;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(ClassType(Rectangle), [Attribute(rect)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_036():
    """Test return statement without expression"""
    source = """class TestClass {
        void method() {
            return nil;
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[ReturnStatement(return NilLiteral(nil))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_037():
    """Test return statement with expression"""
    source = """class TestClass {
        int getValue() {
            return 42;
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(int) getValue([]), BlockStatement(stmts=[ReturnStatement(return IntLiteral(42))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_038():
    """Test if statement without else"""
    source = """class TestClass {
        void method() {
            if x > 0 then {
                x := x + 1;
            }
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[IfStatement(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStatement(stmts=[AssignmentStatement(IdLHS(x) := BinaryOp(Identifier(x), +, IntLiteral(1)))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_039():
    """Test for loop with downto"""
    source = """class TestClass {
        void method() {
            for i := 10 downto 1 do {
                x := x - 1;
            }
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[ForStatement(for i := IntLiteral(10) downto IntLiteral(1) do BlockStatement(stmts=[AssignmentStatement(IdLHS(x) := BinaryOp(Identifier(x), -, IntLiteral(1)))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_040():
    """Test array literal"""
    source = """class TestClass {
        int[3] arr := {1, 2, 3};
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(ArrayType(PrimitiveType(int)[3]), [Attribute(arr = ArrayLiteral({IntLiteral(1), IntLiteral(2), IntLiteral(3)}))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_041():
    """Test array access expression"""
    source = """class TestClass {
        void method() {
            int x := arr[5];
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(PrimitiveType(int), [Variable(x = PostfixExpression(Identifier(arr)[IntLiteral(5)]))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_042():
    """Test method invocation with no arguments"""
    source = """class TestClass {
        void method() {
            obj.getValue();
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[MethodInvocationStatement(PostfixExpression(Identifier(obj).getValue()))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_043():
    """Test method invocation with arguments"""
    source = """class TestClass {
        void method() {
            obj.setValue(10, "test");
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[MethodInvocationStatement(PostfixExpression(Identifier(obj).setValue(IntLiteral(10), StringLiteral('test'))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_044():
    """Test static method invocation"""
    source = """
    class Math {}
    class TestClass {
        void method() {
            Math.abs(-5);
        }
    }"""
    expected = "Program([ClassDecl(Math, []), ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[MethodInvocationStatement(PostfixExpression(Identifier(Math).abs(UnaryOp(-, IntLiteral(5)))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_045():
    """Test object creation with no arguments"""
    source = """class TestClass {
        void method() {
            Rectangle r := new Rectangle();
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(ClassType(Rectangle), [Variable(r = ObjectCreation(new Rectangle()))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_046():
    """Test binary operation with addition"""
    source = """class TestClass {
        int result := a + b;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(int), [Attribute(result = BinaryOp(Identifier(a), +, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_047():
    """Test binary operation with multiplication"""
    source = """class TestClass {
        int result := a * b;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(int), [Attribute(result = BinaryOp(Identifier(a), *, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_048():
    """Test binary operation with division"""
    source = """class TestClass {
        float result := a / b;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(float), [Attribute(result = BinaryOp(Identifier(a), /, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_049():
    """Test binary operation with modulo"""
    source = """class TestClass {
        int result := a % b;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(int), [Attribute(result = BinaryOp(Identifier(a), %, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_050():
    """Test binary operation with subtraction"""
    source = """class TestClass {
        int result := a - b;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(int), [Attribute(result = BinaryOp(Identifier(a), -, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_051():
    """Test logical AND operation"""
    source = """class TestClass {
        boolean result := a && b;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(boolean), [Attribute(result = BinaryOp(Identifier(a), &&, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_052():
    """Test logical OR operation"""
    source = """class TestClass {
        boolean result := a || b;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(boolean), [Attribute(result = BinaryOp(Identifier(a), ||, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_053():
    """Test equality comparison"""
    source = """class TestClass {
        boolean result := a == b;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(boolean), [Attribute(result = BinaryOp(Identifier(a), ==, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_054():
    """Test inequality comparison"""
    source = """class TestClass {
        boolean result := a != b;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(boolean), [Attribute(result = BinaryOp(Identifier(a), !=, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_055():
    """Test less than comparison"""
    source = """class TestClass {
        boolean result := a < b;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(boolean), [Attribute(result = BinaryOp(Identifier(a), <, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_056():
    """Test less than or equal comparison"""
    source = """class TestClass {
        boolean result := a <= b;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(boolean), [Attribute(result = BinaryOp(Identifier(a), <=, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_057():
    """Test greater than comparison"""
    source = """class TestClass {
        boolean result := a > b;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(boolean), [Attribute(result = BinaryOp(Identifier(a), >, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_058():
    """Test greater than or equal comparison"""
    source = """class TestClass {
        boolean result := a >= b;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(boolean), [Attribute(result = BinaryOp(Identifier(a), >=, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_059():
    """Test string concatenation"""
    source = """class TestClass {
        string result := a ^ b;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(string), [Attribute(result = BinaryOp(Identifier(a), ^, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_060():
    """Test unary minus operation"""
    source = """class TestClass {
        int result := -x;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(int), [Attribute(result = UnaryOp(-, Identifier(x)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_061():
    """Test unary plus operation"""
    source = """class TestClass {
        int result := +x;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(int), [Attribute(result = UnaryOp(+, Identifier(x)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_062():
    """Test logical NOT operation"""
    source = """class TestClass {
        boolean result := !flag;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(boolean), [Attribute(result = UnaryOp(!, Identifier(flag)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_063():
    """Test parenthesized expression"""
    source = """class TestClass {
        int result := (a + b) * c;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(int), [Attribute(result = BinaryOp(ParenthesizedExpression((BinaryOp(Identifier(a), +, Identifier(b)))), *, Identifier(c)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_064():
    """Test complex nested expression"""
    source = """class TestClass {
        boolean result := (a > 0) && (b < 10) || (c == 5);
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(boolean), [Attribute(result = BinaryOp(BinaryOp(ParenthesizedExpression((BinaryOp(Identifier(a), >, IntLiteral(0)))), &&, ParenthesizedExpression((BinaryOp(Identifier(b), <, IntLiteral(10))))), ||, ParenthesizedExpression((BinaryOp(Identifier(c), ==, IntLiteral(5))))))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_065():
    """Test nil literal"""
    source = """class TestClass {
        Rectangle obj := nil;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(ClassType(Rectangle), [Attribute(obj = NilLiteral(nil))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_066():
    """Test this expression in assignment"""
    source = """class TestClass {
        void method() {
            this.x := 10;
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(this).x)) := IntLiteral(10))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_067():
    """Test member access chain"""
    source = """class TestClass {
        void method() {
            obj.member.field := value;
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(Identifier(obj).member.field)) := Identifier(value))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_068():
    """Test multiple classes"""
    source = """class ClassA {
        int x;
    }
    class ClassB extends ClassA {
        float y;
    }"""
    expected = "Program([ClassDecl(ClassA, [AttributeDecl(PrimitiveType(int), [Attribute(x)])]), ClassDecl(ClassB, extends ClassA, [AttributeDecl(PrimitiveType(float), [Attribute(y)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_069():
    """Test method with class type parameter"""
    source = """class TestClass {
        void process(Rectangle rect) {}
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) process([Parameter(ClassType(Rectangle) rect)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_070():
    """Test method with array parameter"""
    source = """class TestClass {
        void process(int[10] arr) {}
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) process([Parameter(ArrayType(PrimitiveType(int)[10]) arr)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_071():
    """Test variable declaration in block"""
    source = """class TestClass {
        void method() {
            int x;
            float y := 3.14;
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(PrimitiveType(int), [Variable(x)]), VariableDecl(PrimitiveType(float), [Variable(y = FloatLiteral(3.14))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_072():
    """Test variable declaration with multiple variables"""
    source = """class TestClass {
        void method() {
            int a, b := 5, c;
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(PrimitiveType(int), [Variable(a), Variable(b = IntLiteral(5)), Variable(c)])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_073():
    """Test array assignment with array literal"""
    source = """class TestClass {
        void method() {
            int[3] arr := {10, 20, 30};
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(ArrayType(PrimitiveType(int)[3]), [Variable(arr = ArrayLiteral({IntLiteral(10), IntLiteral(20), IntLiteral(30)}))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_074():
    """Test boolean literals true/false"""
    source = """class TestClass {
        boolean flag1 := true;
        boolean flag2 := false;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(boolean), [Attribute(flag1 = BoolLiteral(True))]), AttributeDecl(PrimitiveType(boolean), [Attribute(flag2 = BoolLiteral(False))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_075():
    """Test float literal with decimal"""
    source = """class TestClass {
        float pi := 3.14159;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(float), [Attribute(pi = FloatLiteral(3.14159))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_076():
    """Test nested method calls"""
    source = """class TestClass {
        void method() {
            obj.getChild().getValue();
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[MethodInvocationStatement(PostfixExpression(Identifier(obj).getChild().getValue()))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_077():
    """Test array access with expression index"""
    source = """class TestClass {
        void method() {
            int x := arr[i + 1];
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(PrimitiveType(int), [Variable(x = PostfixExpression(Identifier(arr)[BinaryOp(Identifier(i), +, IntLiteral(1))]))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_078():
    """Test nested array access"""
    source = """class TestClass {
        void method() {
            int x := matrix[i][j];
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(PrimitiveType(int), [Variable(x = PostfixExpression(Identifier(matrix)[Identifier(i)][Identifier(j)]))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_079():
    """Test for loop with expression bounds"""
    source = """class TestClass {
        void method() {
            for i := 0 to n - 1 do {
                arr[i] := i;
            }
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[ForStatement(for i := IntLiteral(0) to BinaryOp(Identifier(n), -, IntLiteral(1)) do BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(Identifier(arr)[Identifier(i)])) := Identifier(i))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_080():
    """Test final static attribute order"""
    source = """class TestClass {
        final static int CONSTANT := 100;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(static final PrimitiveType(int), [Attribute(CONSTANT = IntLiteral(100))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_081():
    """Test reference type attribute"""
    source = """class TestClass {
        int & ref;
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(ReferenceType(PrimitiveType(int) &), [Attribute(ref)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_082():
    """Test reference assignment"""
    source = """class TestClass {
        void method() {
            int & ref := variable;
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(ReferenceType(PrimitiveType(int) &), [Variable(ref = Identifier(variable))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_083():
    """Test class with all member types"""
    source = """class TestClass {
        int attr;
        TestClass() {}
        ~TestClass() {}
        void method() {}
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(int), [Attribute(attr)]), ConstructorDecl(TestClass([]), BlockStatement(stmts=[])), DestructorDecl(~TestClass(), BlockStatement(stmts=[])), MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_084():
    """Test method returning class type"""
    source = """class TestClass {
        Rectangle createRect() {}
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(ClassType(Rectangle) createRect([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_085():
    """Test method returning array type"""
    source = """class TestClass {
        int[5] getNumbers() {}
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(ArrayType(PrimitiveType(int)[5]) getNumbers([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_086():
    """Test complex assignment with member access"""
    source = """class TestClass {
        void method() {
            this.obj.field := another.getValue();
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(this).obj.field)) := PostfixExpression(Identifier(another).getValue()))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_087():
    """Test assignment to array element"""
    source = """class TestClass {
        void method() {
            arr[index] := value + 1;
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(Identifier(arr)[Identifier(index)])) := BinaryOp(Identifier(value), +, IntLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_088():
    """Test string literal with escape characters"""
    source = """class TestClass {
        string msg := "Hello\\nWorld";
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(string), [Attribute(msg = StringLiteral('Hello\\\\nWorld'))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_089():
    """Test empty array literal"""
    source = """class TestClass {
        int[0] empty := {};
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(ArrayType(PrimitiveType(int)[0]), [Attribute(empty = ArrayLiteral({}))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_090():
    """Test method with class type return and reference"""
    source = """class TestClass {
        Rectangle & getRect() {}
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(ReferenceType(ClassType(Rectangle) &) getRect([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_091():
    """Test nested if statement with complex condition"""
    source = """class TestClass {
        void method() {
            if (i < n) && (arr[i] != 0) then {
                i := i + 1;
            }
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[IfStatement(if BinaryOp(ParenthesizedExpression((BinaryOp(Identifier(i), <, Identifier(n)))), &&, ParenthesizedExpression((BinaryOp(PostfixExpression(Identifier(arr)[Identifier(i)]), !=, IntLiteral(0))))) then BlockStatement(stmts=[AssignmentStatement(IdLHS(i) := BinaryOp(Identifier(i), +, IntLiteral(1)))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_092():
    """Test if-else with complex conditions"""
    source = """class TestClass {
        void method() {
            if (x > 0) && (y > 0) then {
                result := x + y;
            } else {
                result := 0;
            }
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[IfStatement(if BinaryOp(ParenthesizedExpression((BinaryOp(Identifier(x), >, IntLiteral(0)))), &&, ParenthesizedExpression((BinaryOp(Identifier(y), >, IntLiteral(0))))) then BlockStatement(stmts=[AssignmentStatement(IdLHS(result) := BinaryOp(Identifier(x), +, Identifier(y)))]), else BlockStatement(stmts=[AssignmentStatement(IdLHS(result) := IntLiteral(0))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_093():
    """Test nested parentheses"""
    source = """class TestClass {
        int result := ((a + b) * (c - d));
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(int), [Attribute(result = ParenthesizedExpression((BinaryOp(ParenthesizedExpression((BinaryOp(Identifier(a), +, Identifier(b)))), *, ParenthesizedExpression((BinaryOp(Identifier(c), -, Identifier(d))))))))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_094():
    """Test constructor with reference parameters"""
    source = """class TestClass {
        TestClass(int & x; float & y) {}
    }"""
    expected = "Program([ClassDecl(TestClass, [ConstructorDecl(TestClass([Parameter(ReferenceType(PrimitiveType(int) &) x), Parameter(ReferenceType(PrimitiveType(float) &) y)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_095():
    """Test method with mixed parameter types"""
    source = """class TestClass {
        void process(int value; int & ref; int[5] arr; Rectangle obj) {}
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) process([Parameter(PrimitiveType(int) value), Parameter(ReferenceType(PrimitiveType(int) &) ref), Parameter(ArrayType(PrimitiveType(int)[5]) arr), Parameter(ClassType(Rectangle) obj)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_096():
    """Test object creation with complex arguments"""
    source = """class TestClass {
        void method() {
            Point p := new Point(x + 1, y * 2);
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(ClassType(Point), [Variable(p = ObjectCreation(new Point(BinaryOp(Identifier(x), +, IntLiteral(1)), BinaryOp(Identifier(y), *, IntLiteral(2)))))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_097():
    """Test chained method calls with arguments"""
    source = """class TestClass {
        void method() {
            builder.append("Hello").append(" ").append("World");
        }
    }"""
    expected = "Program([ClassDecl(TestClass, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[MethodInvocationStatement(PostfixExpression(Identifier(builder).append(StringLiteral('Hello')).append(StringLiteral(' ')).append(StringLiteral('World'))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_098():
    """Test multiple inheritance levels"""
    source = """class A {}
    class B extends A {}
    class C extends B {}"""
    expected = "Program([ClassDecl(A, []), ClassDecl(B, extends A, []), ClassDecl(C, extends B, [])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_099():
    """Test complex expression with all operators"""
    source = """class TestClass {
        boolean result := !((a + b) > (c * d)) && ((x <= y) || (z >= w));
    }"""
    expected = "Program([ClassDecl(TestClass, [AttributeDecl(PrimitiveType(boolean), [Attribute(result = BinaryOp(UnaryOp(!, ParenthesizedExpression((BinaryOp(ParenthesizedExpression((BinaryOp(Identifier(a), +, Identifier(b)))), >, ParenthesizedExpression((BinaryOp(Identifier(c), *, Identifier(d)))))))), &&, ParenthesizedExpression((BinaryOp(ParenthesizedExpression((BinaryOp(Identifier(x), <=, Identifier(y)))), ||, ParenthesizedExpression((BinaryOp(Identifier(z), >=, Identifier(w)))))))))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_100():
    """Test comprehensive class with all features"""
    source = """class CompleteClass extends BaseClass {
        static final int CONSTANT := 100;
        final string name;
        int value;
        int[10] array;
        
        CompleteClass() {}
        CompleteClass(string name) {}
        CompleteClass(CompleteClass other) {}
        ~CompleteClass() {}
        
        static int getConstant() {
            return CONSTANT;
        }
        
        void setValue(int v) {
            this.value := v;
        }
        
        int & getValueRef() {
            return this.value;
        }
    }"""
    expected = "Program([ClassDecl(CompleteClass, extends BaseClass, [AttributeDecl(static final PrimitiveType(int), [Attribute(CONSTANT = IntLiteral(100))]), AttributeDecl(final PrimitiveType(string), [Attribute(name)]), AttributeDecl(PrimitiveType(int), [Attribute(value)]), AttributeDecl(ArrayType(PrimitiveType(int)[10]), [Attribute(array)]), ConstructorDecl(CompleteClass([]), BlockStatement(stmts=[])), ConstructorDecl(CompleteClass([Parameter(PrimitiveType(string) name)]), BlockStatement(stmts=[])), ConstructorDecl(CompleteClass([Parameter(ClassType(CompleteClass) other)]), BlockStatement(stmts=[])), DestructorDecl(~CompleteClass(), BlockStatement(stmts=[])), MethodDecl(static PrimitiveType(int) getConstant([]), BlockStatement(stmts=[ReturnStatement(return Identifier(CONSTANT))])), MethodDecl(PrimitiveType(void) setValue([Parameter(PrimitiveType(int) v)]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(this).value)) := Identifier(v))])), MethodDecl(ReferenceType(PrimitiveType(int) &) getValueRef([]), BlockStatement(stmts=[ReturnStatement(return PostfixExpression(ThisExpression(this).value))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_101():
    """Test empty class"""
    source = """class Empty {}"""
    expected = "Program([ClassDecl(Empty, [])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_102():
    """Test multiple empty classes"""
    source = """class A {}
    class B {}
    class C {}"""
    expected = "Program([ClassDecl(A, []), ClassDecl(B, []), ClassDecl(C, [])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_103():
    """Test single level inheritance"""
    source = """class Parent {}
    class Child extends Parent {}"""
    expected = "Program([ClassDecl(Parent, []), ClassDecl(Child, extends Parent, [])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_104():
    """Test multiple level inheritance"""
    source = """class A {}
    class B extends A {}
    class C extends B {}"""
    expected = "Program([ClassDecl(A, []), ClassDecl(B, extends A, []), ClassDecl(C, extends B, [])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_105():
    """Test class with single attribute"""
    source = """class Test {
        int x;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(PrimitiveType(int), [Attribute(x)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_106():
    """Test class with multiple attributes"""
    source = """class Test {
        int x;
        float y;
        string name;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(PrimitiveType(int), [Attribute(x)]), AttributeDecl(PrimitiveType(float), [Attribute(y)]), AttributeDecl(PrimitiveType(string), [Attribute(name)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_107():
    """Test class member ordering: attributes then constructor"""
    source = """class Test {
        int x;
        Test() {}
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(PrimitiveType(int), [Attribute(x)]), ConstructorDecl(Test([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_108():
    """Test class member ordering: attributes, constructor, destructor, method"""
    source = """class Test {
        int x;
        Test() {}
        ~Test() {}
        void method() {}
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(PrimitiveType(int), [Attribute(x)]), ConstructorDecl(Test([]), BlockStatement(stmts=[])), DestructorDecl(~Test(), BlockStatement(stmts=[])), MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_109():
    """Test class with only constructor"""
    source = """class Test {
        Test() {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_110():
    """Test class with only destructor"""
    source = """class Test {
        ~Test() {}
    }"""
    expected = "Program([ClassDecl(Test, [DestructorDecl(~Test(), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_111():
    """Test class with only method"""
    source = """class Test {
        void run() {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) run([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_112():
    """Test class with multiple constructors"""
    source = """class Test {
        Test() {}
        Test(int x) {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([]), BlockStatement(stmts=[])), ConstructorDecl(Test([Parameter(PrimitiveType(int) x)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_113():
    """Test class with multiple methods"""
    source = """class Test {
        void run() {}
        int getValue() {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) run([]), BlockStatement(stmts=[])), MethodDecl(PrimitiveType(int) getValue([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# ATTRIBUTE TESTS (test_114 - test_140)
# ============================================================================

def test_114():
    """Test static attribute"""
    source = """class Test {
        static int count;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(static PrimitiveType(int), [Attribute(count)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_115():
    """Test final attribute"""
    source = """class Test {
        final int MAX;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(final PrimitiveType(int), [Attribute(MAX)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_116():
    """Test static final attribute"""
    source = """class Test {
        static final int CONSTANT := 100;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(static final PrimitiveType(int), [Attribute(CONSTANT = IntLiteral(100))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_117():
    """Test final static attribute (reversed order)"""
    source = """class Test {
        final static int CONSTANT := 100;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(static final PrimitiveType(int), [Attribute(CONSTANT = IntLiteral(100))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_118():
    """Test primitive type attributes"""
    source = """class Test {
        int a;
        float b;
        boolean c;
        string d;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(PrimitiveType(int), [Attribute(a)]), AttributeDecl(PrimitiveType(float), [Attribute(b)]), AttributeDecl(PrimitiveType(boolean), [Attribute(c)]), AttributeDecl(PrimitiveType(string), [Attribute(d)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_119():
    """Test class type attribute"""
    source = """class Test {
        Rectangle rect;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(ClassType(Rectangle), [Attribute(rect)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_120():
    """Test array type attribute"""
    source = """class Test {
        int[10] arr;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(ArrayType(PrimitiveType(int)[10]), [Attribute(arr)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_121():
    """Test reference type attribute"""
    source = """class Test {
        int & ref;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(ReferenceType(PrimitiveType(int) &), [Attribute(ref)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_122():
    """Test multiple declarators in one attribute"""
    source = """class Test {
        int a, b, c;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(PrimitiveType(int), [Attribute(a), Attribute(b), Attribute(c)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_123():
    """Test mixed initialized and uninitialized attributes"""
    source = """class Test {
        int a := 1, b, c := 3;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(PrimitiveType(int), [Attribute(a = IntLiteral(1)), Attribute(b), Attribute(c = IntLiteral(3))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_124():
    """Test attribute with integer literal initialization"""
    source = """class Test {
        int value := 42;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(PrimitiveType(int), [Attribute(value = IntLiteral(42))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_125():
    """Test attribute with float literal initialization"""
    source = """class Test {
        float pi := 3.14;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(PrimitiveType(float), [Attribute(pi = FloatLiteral(3.14))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_126():
    """Test attribute with boolean literal initialization"""
    source = """class Test {
        boolean flag := true;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(PrimitiveType(boolean), [Attribute(flag = BoolLiteral(True))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_127():
    """Test attribute with string literal initialization"""
    source = """class Test {
        string msg := "Hello";
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(PrimitiveType(string), [Attribute(msg = StringLiteral('Hello'))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_128():
    """Test attribute with expression initialization"""
    source = """class Test {
        int sum := a + b;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(PrimitiveType(int), [Attribute(sum = BinaryOp(Identifier(a), +, Identifier(b)))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_129():
    """Test array attribute with size"""
    source = """class Test {
        int[5] numbers;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(ArrayType(PrimitiveType(int)[5]), [Attribute(numbers)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_130():
    """Test array attribute with initializer"""
    source = """class Test {
        int[3] values := {1, 2, 3};
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(ArrayType(PrimitiveType(int)[3]), [Attribute(values = ArrayLiteral({IntLiteral(1), IntLiteral(2), IntLiteral(3)}))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_131():
    """Test array attribute with empty initializer"""
    source = """class Test {
        int[0] empty := {};
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(ArrayType(PrimitiveType(int)[0]), [Attribute(empty = ArrayLiteral({}))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_132():
    """Test float array attribute"""
    source = """class Test {
        float[3] coords;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(ArrayType(PrimitiveType(float)[3]), [Attribute(coords)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_133():
    """Test string array attribute"""
    source = """class Test {
        string[5] names;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(ArrayType(PrimitiveType(string)[5]), [Attribute(names)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_134():
    """Test boolean array attribute"""
    source = """class Test {
        boolean[10] flags;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(ArrayType(PrimitiveType(boolean)[10]), [Attribute(flags)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_135():
    """Test class type array attribute"""
    source = """class Test {
        Rectangle[5] shapes;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(ArrayType(ClassType(Rectangle)[5]), [Attribute(shapes)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_136():
    """Test reference to class type"""
    source = """class Test {
        Rectangle & ref;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(ReferenceType(ClassType(Rectangle) &), [Attribute(ref)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_137():
    """Test reference to array type"""
    source = """class Test {
        int[5] & arrRef;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(ReferenceType(ArrayType(PrimitiveType(int)[5]) &), [Attribute(arrRef)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_138():
    """Test static array attribute"""
    source = """class Test {
        static int[100] cache;
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(static ArrayType(PrimitiveType(int)[100]), [Attribute(cache)])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_139():
    """Test final array attribute with initializer"""
    source = """class Test {
        final int[2] pair := {10, 20};
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(final ArrayType(PrimitiveType(int)[2]), [Attribute(pair = ArrayLiteral({IntLiteral(10), IntLiteral(20)}))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_140():
    """Test array attribute size 1"""
    source = """class Test {
        int[1] single := {42};
    }"""
    expected = "Program([ClassDecl(Test, [AttributeDecl(ArrayType(PrimitiveType(int)[1]), [Attribute(single = ArrayLiteral({IntLiteral(42)}))])])])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# CONSTRUCTOR AND DESTRUCTOR TESTS (test_141 - test_160)
# ============================================================================

def test_141():
    """Test default constructor"""
    source = """class Test {
        Test() {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_142():
    """Test copy constructor"""
    source = """class Test {
        Test(Test other) {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([Parameter(ClassType(Test) other)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_143():
    """Test user-defined constructor with single parameter"""
    source = """class Test {
        Test(int x) {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([Parameter(PrimitiveType(int) x)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_144():
    """Test user-defined constructor with multiple parameters"""
    source = """class Test {
        Test(int x; float y; string name) {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([Parameter(PrimitiveType(int) x), Parameter(PrimitiveType(float) y), Parameter(PrimitiveType(string) name)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_145():
    """Test constructor with comma-separated parameters of same type"""
    source = """class Test {
        Test(int x, y, z) {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([Parameter(PrimitiveType(int) x), Parameter(PrimitiveType(int) y), Parameter(PrimitiveType(int) z)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_146():
    """Test constructor with reference parameter"""
    source = """class Test {
        Test(int & ref) {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([Parameter(ReferenceType(PrimitiveType(int) &) ref)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_147():
    """Test constructor with array parameter"""
    source = """class Test {
        Test(int[5] arr) {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([Parameter(ArrayType(PrimitiveType(int)[5]) arr)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_148():
    """Test constructor with class type parameter"""
    source = """class Test {
        Test(Rectangle rect) {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([Parameter(ClassType(Rectangle) rect)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_149():
    """Test constructor with body containing variable declaration"""
    source = """class Test {
        Test() {
            int x := 10;
        }
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([]), BlockStatement(vars=[VariableDecl(PrimitiveType(int), [Variable(x = IntLiteral(10))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_150():
    """Test constructor with body containing assignment"""
    source = """class Test {
        Test(int x) {
            this.x := x;
        }
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([Parameter(PrimitiveType(int) x)]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(this).x)) := Identifier(x))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_151():
    """Test destructor"""
    source = """class Test {
        ~Test() {}
    }"""
    expected = "Program([ClassDecl(Test, [DestructorDecl(~Test(), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_152():
    """Test destructor with body"""
    source = """class Test {
        ~Test() {
            int cleanup := 1;
        }
    }"""
    expected = "Program([ClassDecl(Test, [DestructorDecl(~Test(), BlockStatement(vars=[VariableDecl(PrimitiveType(int), [Variable(cleanup = IntLiteral(1))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_153():
    """Test constructor with semicolon-separated parameter groups"""
    source = """class Test {
        Test(int a; float b) {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([Parameter(PrimitiveType(int) a), Parameter(PrimitiveType(float) b)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_154():
    """Test constructor with mixed parameter styles"""
    source = """class Test {
        Test(int a, b; float c) {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([Parameter(PrimitiveType(int) a), Parameter(PrimitiveType(int) b), Parameter(PrimitiveType(float) c)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_155():
    """Test constructor with reference parameters"""
    source = """class Test {
        Test(int & x; float & y) {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([Parameter(ReferenceType(PrimitiveType(int) &) x), Parameter(ReferenceType(PrimitiveType(float) &) y)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_156():
    """Test constructor and destructor together"""
    source = """class Test {
        Test() {}
        ~Test() {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([]), BlockStatement(stmts=[])), DestructorDecl(~Test(), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_157():
    """Test multiple constructors with destructor"""
    source = """class Test {
        Test() {}
        Test(int x) {}
        ~Test() {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([]), BlockStatement(stmts=[])), ConstructorDecl(Test([Parameter(PrimitiveType(int) x)]), BlockStatement(stmts=[])), DestructorDecl(~Test(), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_158():
    """Test constructor with complex body"""
    source = """class Test {
        Test(int x) {
            int temp := x;
            this.value := temp;
        }
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([Parameter(PrimitiveType(int) x)]), BlockStatement(vars=[VariableDecl(PrimitiveType(int), [Variable(temp = Identifier(x))])], stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(this).value)) := Identifier(temp))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_159():
    """Test destructor with method call"""
    source = """class Test {
        ~Test() {
            this.cleanup();
        }
    }"""
    expected = "Program([ClassDecl(Test, [DestructorDecl(~Test(), BlockStatement(stmts=[MethodInvocationStatement(PostfixExpression(ThisExpression(this).cleanup()))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_160():
    """Test constructor with array reference parameter"""
    source = """class Test {
        Test(int[10] & arr) {}
    }"""
    expected = "Program([ClassDecl(Test, [ConstructorDecl(Test([Parameter(ReferenceType(ArrayType(PrimitiveType(int)[10]) &) arr)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# METHOD TESTS (test_161 - test_180)
# ============================================================================

def test_161():
    """Test instance method with void return"""
    source = """class Test {
        void run() {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) run([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_162():
    """Test static method"""
    source = """class Test {
        static void helper() {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(static PrimitiveType(void) helper([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_163():
    """Test method with int return type"""
    source = """class Test {
        int getValue() {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(int) getValue([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_164():
    """Test method with float return type"""
    source = """class Test {
        float calculate() {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(float) calculate([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_165():
    """Test method with boolean return type"""
    source = """class Test {
        boolean check() {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(boolean) check([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_166():
    """Test method with string return type"""
    source = """class Test {
        string getText() {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(string) getText([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_167():
    """Test method with class return type"""
    source = """class Test {
        Rectangle createRect() {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(ClassType(Rectangle) createRect([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_168():
    """Test method with array return type"""
    source = """class Test {
        int[5] getArray() {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(ArrayType(PrimitiveType(int)[5]) getArray([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_169():
    """Test method with reference return type"""
    source = """class Test {
        int & getRef() {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(ReferenceType(PrimitiveType(int) &) getRef([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_170():
    """Test method with class reference return type"""
    source = """class Test {
        Rectangle & getRect() {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(ReferenceType(ClassType(Rectangle) &) getRect([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_171():
    """Test method with array reference return type"""
    source = """class Test {
        int[10] & getArrayRef() {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(ReferenceType(ArrayType(PrimitiveType(int)[10]) &) getArrayRef([]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_172():
    """Test method with single parameter"""
    source = """class Test {
        void process(int value) {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) process([Parameter(PrimitiveType(int) value)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_173():
    """Test method with multiple parameters same type"""
    source = """class Test {
        void process(int a, b, c) {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) process([Parameter(PrimitiveType(int) a), Parameter(PrimitiveType(int) b), Parameter(PrimitiveType(int) c)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_174():
    """Test method with semicolon-separated parameters"""
    source = """class Test {
        void process(int x; float y; string z) {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) process([Parameter(PrimitiveType(int) x), Parameter(PrimitiveType(float) y), Parameter(PrimitiveType(string) z)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_175():
    """Test method with reference parameter"""
    source = """class Test {
        void modify(int & ref) {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) modify([Parameter(ReferenceType(PrimitiveType(int) &) ref)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_176():
    """Test method with array parameter"""
    source = """class Test {
        void process(int[10] arr) {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) process([Parameter(ArrayType(PrimitiveType(int)[10]) arr)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_177():
    """Test method with class type parameter"""
    source = """class Test {
        void draw(Rectangle rect) {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) draw([Parameter(ClassType(Rectangle) rect)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_178():
    """Test method with mixed parameter types"""
    source = """class Test {
        void process(int value; int & ref; int[5] arr; Rectangle obj) {}
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) process([Parameter(PrimitiveType(int) value), Parameter(ReferenceType(PrimitiveType(int) &) ref), Parameter(ArrayType(PrimitiveType(int)[5]) arr), Parameter(ClassType(Rectangle) obj)]), BlockStatement(stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_179():
    """Test static method with return statement"""
    source = """class Test {
        static int getCount() {
            return 5;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(static PrimitiveType(int) getCount([]), BlockStatement(stmts=[ReturnStatement(return IntLiteral(5))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_180():
    """Test method with non-empty body"""
    source = """class Test {
        void setValue(int v) {
            this.value := v;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) setValue([Parameter(PrimitiveType(int) v)]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(this).value)) := Identifier(v))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# STATEMENT TESTS (test_181 - test_220)
# ============================================================================

def test_181():
    """Test block statement with variables only"""
    source = """class Test {
        void method() {
            int x;
            float y;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(PrimitiveType(int), [Variable(x)]), VariableDecl(PrimitiveType(float), [Variable(y)])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_182():
    """Test block statement with statements only"""
    source = """class Test {
        void method() {
            x := 5;
            y := 10;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[AssignmentStatement(IdLHS(x) := IntLiteral(5)), AssignmentStatement(IdLHS(y) := IntLiteral(10))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_183():
    """Test assignment to identifier"""
    source = """class Test {
        void method() {
            x := 10;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[AssignmentStatement(IdLHS(x) := IntLiteral(10))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_184():
    """Test assignment to member access"""
    source = """class Test {
        void method() {
            this.x := 10;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(this).x)) := IntLiteral(10))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_185():
    """Test assignment to array element"""
    source = """class Test {
        void method() {
            arr[0] := 42;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(Identifier(arr)[IntLiteral(0)])) := IntLiteral(42))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_186():
    """Test assignment to chained member access"""
    source = """class Test {
        void method() {
            obj.a.b := 5;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(Identifier(obj).a.b)) := IntLiteral(5))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_187():
    """Test assignment to array element with expression index"""
    source = """class Test {
        void method() {
            arr[i + 1] := value;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(Identifier(arr)[BinaryOp(Identifier(i), +, IntLiteral(1))])) := Identifier(value))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_188():
    """Test if statement without else"""
    source = """class Test {
        void method() {
            if x > 0 then {
                y := 1;
            }
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[IfStatement(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStatement(stmts=[AssignmentStatement(IdLHS(y) := IntLiteral(1))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_189():
    """Test if statement with else"""
    source = """class Test {
        void method() {
            if x > 0 then {
                y := 1;
            } else {
                y := 0;
            }
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[IfStatement(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStatement(stmts=[AssignmentStatement(IdLHS(y) := IntLiteral(1))]), else BlockStatement(stmts=[AssignmentStatement(IdLHS(y) := IntLiteral(0))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_190():
    """Test nested if statements"""
    source = """class Test {
        void method() {
            if x > 0 then {
                if y > 0 then {
                    z := 1;
                }
            }
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[IfStatement(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStatement(stmts=[IfStatement(if BinaryOp(Identifier(y), >, IntLiteral(0)) then BlockStatement(stmts=[AssignmentStatement(IdLHS(z) := IntLiteral(1))]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_191():
    """Test if with complex boolean condition"""
    source = """class Test {
        void method() {
            if (x > 0) && (y < 10) then {
                z := 1;
            }
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[IfStatement(if BinaryOp(ParenthesizedExpression((BinaryOp(Identifier(x), >, IntLiteral(0)))), &&, ParenthesizedExpression((BinaryOp(Identifier(y), <, IntLiteral(10))))) then BlockStatement(stmts=[AssignmentStatement(IdLHS(z) := IntLiteral(1))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_192():
    """Test for loop with to"""
    source = """class Test {
        void method() {
            for i := 1 to 10 do {
                sum := sum + i;
            }
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[ForStatement(for i := IntLiteral(1) to IntLiteral(10) do BlockStatement(stmts=[AssignmentStatement(IdLHS(sum) := BinaryOp(Identifier(sum), +, Identifier(i)))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_193():
    """Test for loop with downto"""
    source = """class Test {
        void method() {
            for i := 10 downto 1 do {
                x := x - 1;
            }
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[ForStatement(for i := IntLiteral(10) downto IntLiteral(1) do BlockStatement(stmts=[AssignmentStatement(IdLHS(x) := BinaryOp(Identifier(x), -, IntLiteral(1)))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_194():
    """Test for loop with expression bounds"""
    source = """class Test {
        void method() {
            for i := 0 to n - 1 do {
                arr[i] := i;
            }
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[ForStatement(for i := IntLiteral(0) to BinaryOp(Identifier(n), -, IntLiteral(1)) do BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(Identifier(arr)[Identifier(i)])) := Identifier(i))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_195():
    """Test break statement"""
    source = """class Test {
        void method() {
            break;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[BreakStatement()]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_196():
    """Test continue statement"""
    source = """class Test {
        void method() {
            continue;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[ContinueStatement()]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_197():
    """Test break and continue in for loop"""
    source = """class Test {
        void method() {
            for i := 1 to 10 do {
                if i == 5 then break;
                continue;
            }
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[ForStatement(for i := IntLiteral(1) to IntLiteral(10) do BlockStatement(stmts=[IfStatement(if BinaryOp(Identifier(i), ==, IntLiteral(5)) then BreakStatement()), ContinueStatement()]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_198():
    """Test return statement with expression"""
    source = """class Test {
        int getValue() {
            return 42;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(int) getValue([]), BlockStatement(stmts=[ReturnStatement(return IntLiteral(42))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_199():
    """Test return statement with nil"""
    source = """class Test {
        void method() {
            return nil;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[ReturnStatement(return NilLiteral(nil))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_200():
    """Test return statement with complex expression"""
    source = """class Test {
        int calculate() {
            return a + b * c;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(int) calculate([]), BlockStatement(stmts=[ReturnStatement(return BinaryOp(Identifier(a), +, BinaryOp(Identifier(b), *, Identifier(c))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_201():
    """Test method invocation statement instance method"""
    source = """class Test {
        void method() {
            obj.doSomething();
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[MethodInvocationStatement(PostfixExpression(Identifier(obj).doSomething()))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_202():
    """Test method invocation with arguments"""
    source = """class Test {
        void method() {
            obj.process(1, 2, 3);
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[MethodInvocationStatement(PostfixExpression(Identifier(obj).process(IntLiteral(1), IntLiteral(2), IntLiteral(3))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_203():
    """Test static method invocation"""
    source = """class Math {}
    class Test {
        void method() {
            Math.abs(5);
        }
    }"""
    expected = "Program([ClassDecl(Math, []), ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[MethodInvocationStatement(PostfixExpression(Identifier(Math).abs(IntLiteral(5))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_204():
    """Test nested block statements"""
    source = """class Test {
        void method() {
            {
                int x := 1;
            }
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[BlockStatement(vars=[VariableDecl(PrimitiveType(int), [Variable(x = IntLiteral(1))])], stmts=[])]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_205():
    """Test variable declaration with final"""
    source = """class Test {
        void method() {
            final int MAX := 100;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(final PrimitiveType(int), [Variable(MAX = IntLiteral(100))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_206():
    """Test variable declaration with reference"""
    source = """class Test {
        void method() {
            int & ref := x;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(ReferenceType(PrimitiveType(int) &), [Variable(ref = Identifier(x))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_207():
    """Test variable declaration multiple variables"""
    source = """class Test {
        void method() {
            int a, b := 5, c;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(PrimitiveType(int), [Variable(a), Variable(b = IntLiteral(5)), Variable(c)])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_208():
    """Test array variable declaration"""
    source = """class Test {
        void method() {
            int[5] arr;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(ArrayType(PrimitiveType(int)[5]), [Variable(arr)])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_209():
    """Test array variable declaration with initializer"""
    source = """class Test {
        void method() {
            int[3] arr := {1, 2, 3};
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(ArrayType(PrimitiveType(int)[3]), [Variable(arr = ArrayLiteral({IntLiteral(1), IntLiteral(2), IntLiteral(3)}))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_210():
    """Test final array declaration"""
    source = """class Test {
        void method() {
            final int[2] pair := {10, 20};
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(vars=[VariableDecl(final ArrayType(PrimitiveType(int)[2]), [Variable(pair = ArrayLiteral({IntLiteral(10), IntLiteral(20)}))])], stmts=[]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_211():
    """Test assignment with complex member access"""
    source = """class Test {
        void method() {
            this.obj.field := value;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(this).obj.field)) := Identifier(value))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_212():
    """Test assignment to multi-dimensional array"""
    source = """class Test {
        void method() {
            matrix[i][j] := value;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(Identifier(matrix)[Identifier(i)][Identifier(j)])) := Identifier(value))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_213():
    """Test assignment to array of object member"""
    source = """class Test {
        void method() {
            obj.arr[0] := 5;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(Identifier(obj).arr[IntLiteral(0)])) := IntLiteral(5))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_214():
    """Test chained method calls in statement"""
    source = """class Test {
        void method() {
            obj.a().b();
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[MethodInvocationStatement(PostfixExpression(Identifier(obj).a().b()))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_215():
    """Test if with assignment in then block"""
    source = """class Test {
        void method() {
            if flag then x := 1;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[IfStatement(if Identifier(flag) then AssignmentStatement(IdLHS(x) := IntLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_216():
    """Test for loop with method call in body"""
    source = """class Test {
        void method() {
            for i := 1 to 10 do obj.process(i);
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[ForStatement(for i := IntLiteral(1) to IntLiteral(10) do MethodInvocationStatement(PostfixExpression(Identifier(obj).process(Identifier(i)))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_217():
    """Test complex nested statements"""
    source = """class Test {
        void method() {
            for i := 1 to 10 do {
                if i % 2 == 0 then {
                    arr[i] := i * 2;
                }
            }
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(void) method([]), BlockStatement(stmts=[ForStatement(for i := IntLiteral(1) to IntLiteral(10) do BlockStatement(stmts=[IfStatement(if BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)) then BlockStatement(stmts=[AssignmentStatement(PostfixLHS(PostfixExpression(Identifier(arr)[Identifier(i)])) := BinaryOp(Identifier(i), *, IntLiteral(2)))]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_218():
    """Test return with member access"""
    source = """class Test {
        int method() {
            return this.value;
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(int) method([]), BlockStatement(stmts=[ReturnStatement(return PostfixExpression(ThisExpression(this).value))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_219():
    """Test return with method call"""
    source = """class Test {
        int method() {
            return obj.getValue();
        }
    }"""
    expected = "Program([ClassDecl(Test, [MethodDecl(PrimitiveType(int) method([]), BlockStatement(stmts=[ReturnStatement(return PostfixExpression(Identifier(obj).getValue()))]))])])"
    assert str(ASTGenerator(source).generate()) == expected