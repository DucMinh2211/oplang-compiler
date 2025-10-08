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
