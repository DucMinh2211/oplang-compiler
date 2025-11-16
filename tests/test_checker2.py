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
    print(Checker(source).check_from_source())
    assert Checker(source).check_from_source() == expected



# REDECLARED TESTCASES

# Normal declaration
def test_008():
    source = """
    class Test {
        static void main() {
            int x := 5;
            {
                int x := 10;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Function has same name as attribute
def test_009():
    source = """
    class Test {
        int x;
        void x() {
            return nil;
        }
        static void main() {
        }
    }
    """  
    expected = "Redeclared(Method, x)"
    assert Checker(source).check_from_source() == expected



# Parameter has same name as variable
def test_011():
    source = """
    class Test {
        static void main(int x) {
            int x;
        }
    }
    """  
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected


# Variable in block scope has same name with each other
def test_012():
    source = """
    class Test {
        static void main() {
            {
                int x := 5;
                int x := 10;
            }
        }
    }
    """  
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected


# Normal inheritance with no redeclaration
def test_013():    
    source = """
    class Parent {
        int x;
        void display() {
        }
    }
    class Child extends Parent {
        int y;
        void display() {
        }
    }
    class Test {
        static void main() {
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Class has same name with other class
def test_014():   
    source = """
    class Parent {
        int x;
        void display() {                                       
        }
    }
    class Parent {
        int y;
        void display() {
        }
    }       
    class Test {
        static void main() {
        }
    }
    """  
    expected = "Redeclared(Class, Parent)"
    assert Checker(source).check_from_source() == expected


# Child class has same name with parent class
def test_015():   
    source = """
    class Parent {
        int x;
        void display() {                                        
        }       
    }
    class Parent extends Parent {
        int y;
        void display() {
        }
    }       
    class Test {
        static void main() {
        }
    }
    """  
    expected = "Redeclared(Class, Parent)"
    assert Checker(source).check_from_source() == expected


# Attritube in child class overrides attribute in parent class normally
def test_016(): 
    source = """
    class Parent {
        int x;
        void display() {
        }
    }
    class Child extends Parent {
        int x;
        void display() {
        }
    }
    class Test {
        static void main() {
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Redeclared attribute in the same class
def test_017(): 
    source = """
    class Test {
        int x;
        int x;
        static void main() {
        }
    }
    """  
    expected = "Redeclared(Attribute, x)"
    assert Checker(source).check_from_source() == expected


# Redeclared method in the same class
def test_018(): 
    source = """
    class Test {
        void display(int a; int b) {
        }
        void display(int x; int y) {
        }
        static void main() {
        }
    }
    """  
    expected = "Redeclared(Method, display)"
    assert Checker(source).check_from_source() == expected


# Redeclared parameter in method
def test_019():
    source = """
    class Test {
        void display(int x; int y; int x) {
        }
        static void main() {
        }
    }
    """
    expected = "Redeclared(Parameter, x)"
    assert Checker(source).check_from_source() == expected


# Redeclared constant
def test_020():
    source = """
    class Test {
        static void main() {
            final int x := 5;
            final int x := 10;
        }
    }
    """  
    expected = "Redeclared(Constant, x)"
    assert Checker(source).check_from_source() == expected


# Redeclared global constant
def test_021():
    source = """
    class Test {
        static void main() {
            final int x := 5;
            final int x := 10;
        }
    }
    """  
    expected = "Redeclared(Constant, x)"
    assert Checker(source).check_from_source() == expected


# Overloading global variable in function
def test_022():
    source = """
    int x;

    class Test {
        void func() {
            int x := 10;
        }
        static void main() {
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Overloading global function in method
def test_023():
    source = """
    class Test {
        void func() {
            
        }
        static void main() {
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Undecleared class
def test_024():
    source = """
    class Test {
        static void main() {
            Dog d;
        }
    }
    """  
    expected = "UndeclaredClass(Dog)"
    assert Checker(source).check_from_source() == expected  

# Undeclared class in inheritance
def test_025():
    source = """
    class Test {
        static void main() {
            Cat c;
        }
    }
    """
    expected = "UndeclaredClass(Cat)"
    assert Checker(source).check_from_source() == expected

# Undeclared attribute
def test_026():
    source = """
    class Test {
        static void main() {
            int x := this.y;
        }
    }
    """  
    expected = "UndeclaredAttribute(y)"
    assert Checker(source).check_from_source() == expected



# Valid attribute inheritance
def test_027():
    source = """
    class Parent {
        int x;
    }
    class Child extends Parent {
        int y;
        void display() {
            int z := this.x + this.y;
        }
    }
    class Test {
        static void main() {
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Undeclared method
def test_028():
    source = """
    class Test {
        static void main() {
            this.display();
        }
    }
    """
    expected = "UndeclaredMethod(display)"
    assert Checker(source).check_from_source() == expected


# Valid method inheritance
def test_029():
    source = """
    class Parent {
        void display() {
        }
    }
    class Child extends Parent {
        void show() {
            this.display();
        }
    }
    class Test {
        static void main() {
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected



# Undeclared identifier in method
def test_030():
    source = """
    class Test {
        void display() {
            int z := x + 1;
        }
        static void main() {
        }
    }
    """  
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected



# Undeclared method in normal class
def test_031():
    source = """
    class Test {
        void display() {
            this.show();
        }
        static void main() {
        }
    }
    """  
    expected = "UndeclaredMethod(show)"
    assert Checker(source).check_from_source() == expected


# Undeclared class in inheritance
def test_032():
    source = """
    class Parent extends Animal {
        int x;
    }
    class Test {
        static void main() {
        }
    }
    """  
    expected = "UndeclaredClass(Animal)"
    assert Checker(source).check_from_source() == expected


# Undeclared class in variable assignment
def test_033():
    source = """
    class Test {
        static void main() {
            Dog d := new Dog();
        }
    }
    """ 
    expected = "UndeclaredClass(Dog)"
    assert Checker(source).check_from_source() == expected


# Normal inheritance and attribute/method access
def test_034():
    source = """
    class Animal {
        int age;
        void makeSound() {
        }
    }
    class Dog extends Animal {
        void bark() {
            this.makeSound();
            int a := this.age;
        }
    }
    class Test {
        static void main() {
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Valid parent class declaration
def test_035():
    source = """
    class Animal {
        int age;
    }
    class Dog extends Animal {
        void bark() {
        }
    }
    class Test {
        static void main() {
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Method call in wrong class
def test_036():
    source = """
    class Animal {
        void makeSound() {
        }
    }
    class Dog extends Animal {
        void bark() {
            this.fly();
        }
    }
    class Test {
        static void main() {
        }
    }
    """  
    expected = "UndeclaredMethod(fly)"
    assert Checker(source).check_from_source() == expected


# Method call wrong class with no inheritance
def test_037():
    source = """
    class Animal {
        void makeSound() {
        }
    }
    class Dog {
        void bark() {
            Animal a;
            a.fly();
        }
    }
    class Test {
        static void main() {
        }
    }
    """  
    expected = "UndeclaredMethod(fly)"
    assert Checker(source).check_from_source() == expected


# Out of scope variable access
def test_038():
    source = """
    class Test {
        static void main() {
            {
                int x := 5;
            }
            int y := x + 1;
        }
    }
    """  
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected


# Final variable must be initialized when declared
def test_039():
    source = """
    class Test {
        static void main() {
            final int x;
            x := 10;
        }
    }       
    """
    expected = "IllegalConstantExpression(None)"
    assert Checker(source).check_from_source() == expected


# Final variable assigned more than once
def test_040():
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


# Final variable must be initialized in constructor
def test_041():
    source = """
    class Test {
        final int x;
        Test(int val) {
            this.x := val;
        }
        static void main() {
        }
    }
    """  
    expected = "IllegalConstantExpression(None)"
    assert Checker(source).check_from_source() == expected


# Final attritube cannot be assigned outside constructor
def test_042():
    source = """
    class Test {
        Test(int val) {
            final int x := val;
        }
        void setX(int val) {
            this.x := val;
        }
        static void main() {   
        }
    }
    """
    expected = "IllegalConstantExpression(Identifier(val))"
    assert Checker(source).check_from_source() == expected



# Valid constant declaration and usage
def test_043():
    source = """
    class Test {
        static void main() {
            final int x := 5;
            int y := x + 10;
        }
    }                                       
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

# Invalid constant in loop
def test_044():
    source = """
    class Test {
        static void main() {
            final int limit := 10;
            for i := 1 to 100 do {
                limit := limit + 1;
            }
        }
    }
    """  
    expected = "CannotAssignToConstant(AssignmentStatement(IdLHS(limit) := BinaryOp(Identifier(limit), +, IntLiteral(1))))"
    assert Checker(source).check_from_source() == expected


# Cannot assign to constant error in attribute
def test_045():
    source = """
    class Test {
        final int x := 5;
        void updateX() {
            this.x := 10;
        }
        static void main() {
        }
    }
    """
    expected = "CannotAssignToConstant(AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(this).x)) := IntLiteral(10)))"
    assert Checker(source).check_from_source() == expected



# Assignment to a final attribute in granparent class
def test_046():
    source = """
    class Grandparent {
        final int x := 5;
    }
    class Parent extends Grandparent {
    }
    class Child extends Parent {
        void updateX() {
            this.x := 10;
        }
    }
    class Test {
        static void main() {
        }
    }
    """  
    expected = "CannotAssignToConstant(AssignmentStatement(PostfixLHS(PostfixExpression(ThisExpression(this).x)) := IntLiteral(10)))"
    assert Checker(source).check_from_source() == expected


# TYPE MISMATCH TESTCASES

# Redelared variable in function parameter list
def test_047():
    source = """
    class Test {
        static void main(int x) {
            int x := 5;
            return nil;
        }
    }
    """  
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected



# If statement with non-boolean condition
def test_048():
    source = """
    class Test {
        static void main() {
            if (5) {
                int x := 10;
            }
        }
    }
    """  
    expected = "TypeMismatchInStatement(IfStatement(if ParenthesizedExpression((IntLiteral(5))) then BlockStatement(vars=[VariableDecl(PrimitiveType(int), [Variable(x = IntLiteral(10))])], stmts=[])))"
    assert Checker(source).check_from_source() == expected

# Scalar variable in for statement must be integer
def test_049():
    source = """
    class Test {
        static void main() {
            boolean i;
            for i := true to false do {
                io.writeIntLn(i);
            }   
        }
    }
    """  
    expected = "TypeMismatchInStatement(ForStatement(for i := BoolLiteral(True) to BoolLiteral(False) do BlockStatement(stmts=[MethodInvocationStatement(PostfixExpression(Identifier(io).writeIntLn(Identifier(i))))])))"
    assert Checker(source).check_from_source() == expected


# Exp1 and Exp2 in for statement must be integer type
def test_050():
    source = """
    class Test {
        static void main() {
            int i;
            for i := true to "10" do {
                io.writeIntLn(i);
            }   
        }
    }
    """  
    expected = "TypeMismatchInStatement(ForStatement(for i := BoolLiteral(True) to StringLiteral('10') do BlockStatement(stmts=[MethodInvocationStatement(PostfixExpression(Identifier(io).writeIntLn(Identifier(i))))])))"
    assert Checker(source).check_from_source() == expected


# LHS cannot be void type
def test_051():
    source = """
    class Test {
        static void main() {
            void x;
            x := nil;
        }
    }
    """  
    expected = "TypeMismatchInStatement(AssignmentStatement(IdLHS(x) := NilLiteral(nil)))"
    assert Checker(source).check_from_source() == expected


# RHS must have same type as LHS
def test_052():
    source = """
    class Test {
        static void main() {
            int x;
            x := "hello";
        }
    }
    """  
    expected = "TypeMismatchInStatement(AssignmentStatement(IdLHS(x) := StringLiteral('hello')))"
    assert Checker(source).check_from_source() == expected


# RHS can coerce to LHS type
def test_053():
    source = """
    class Test {
        static void main() {
            float x;
            x := 10;
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected



# LHS is parent of RHS in assignment
def test_054():
    source = """
    class Parent {
    }
    class Child extends Parent {
    }
    class Test {
        static void main() {
            Parent p;
            p := new Child();
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Array assignment with incompatible types
def test_055():
    source = """
    class Test {
        static void main() {
            int[5] arr1;
            float[5] arr2;
            arr1 := arr2;
        }
    }
    """ 
    expected = "TypeMismatchInStatement(AssignmentStatement(IdLHS(arr1) := Identifier(arr2)))"
    assert Checker(source).check_from_source() == expected


# Array assignment with different sizes
def test_056():
    source = """
    class Test {
        static void main() {
            int[5] arr1;
            int[10] arr2;
            arr1 := arr2;
        }
    }
    """  
    expected = "TypeMismatchInStatement(AssignmentStatement(IdLHS(arr1) := Identifier(arr2)))"
    assert Checker(source).check_from_source() == expected


# Array assignment with diffent type size
def test_057():
    source = """
    class Test {
        static void main() {
            int[5] arr1;
            boolean[5] arr2;
            arr1 := arr2;
        }
    }
    """  
    expected = "TypeMismatchInStatement(AssignmentStatement(IdLHS(arr1) := Identifier(arr2)))"
    assert Checker(source).check_from_source() == expected



# Array assigment with differnt size and incompatible types
def test_058():
    source = """
    class Test {
        static void main() {
            int[5] arr1;
            float[10] arr2;
            arr1 := arr2;
        }
    }
    """  
    expected = "TypeMismatchInStatement(AssignmentStatement(IdLHS(arr1) := Identifier(arr2)))"    
    assert Checker(source).check_from_source() == expected


# Valid array assignment
def test_059(): 
    source = """
    class Test {
        static void main() {
            int[5] arr1;
            int[5] arr2;
            arr1 := arr2;
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected



# Method return type mismatch
def test_060():
    source = """
    class Test {
        static int main() {
            return "hello";
        }
    }
    """  
    expected = "TypeMismatchInStatement(ReturnStatement(return StringLiteral('hello')))"
    assert Checker(source).check_from_source() == expected


# Void method returning a value
def test_061():
    source = """
    class Test {
        static void main() {
            return 5;
        }
    }
    """  
    expected = "TypeMismatchInStatement(ReturnStatement(return IntLiteral(5)))"
    assert Checker(source).check_from_source() == expected


# Illegal member access
def test_063():
    source = """
    class Test {
        void display() {
        }
        static void main() {
            Test.display();
        }
    }
    """  
    expected = "IllegalMemberAccess(PostfixExpression(Identifier(Test).display()))"
    assert Checker(source).check_from_source() == expected


# Argument must coerce to parameter type
def test_064():
    source = """
    class Test {
        void display(int x) {
        }
        static void main() {
            Test t;
            t.display("hello");
        }
    }
    """  
    expected = "TypeMismatchInExpression(PostfixExpression(Identifier(t).display(StringLiteral('hello'))))"
    assert Checker(source).check_from_source() == expected


# Valid method call with compatible argument types
def test_065():
    source = """
    class Test {
        void display(float x; float y) {
        }
        static void main() {
            Test t;
            t.display(10, 20.5);
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected



# Invalid assignment superclass to subclass
def test_066():
    source = """
    class Parent {
    }
    class Child extends Parent {
    }
    class Test {
        static void main() {
            Child c;
            c := new Parent();
        }
    }
    """  
    expected = "TypeMismatchInStatement(AssignmentStatement(IdLHS(c) := ObjectCreation(new Parent())))"
    assert Checker(source).check_from_source() == expected


# Invalid array literal with mixed types
def test_067():
    source = """
    class Test {
        static void main() {
            int[3] arr := {1, 2.5, 3};
        }
    }
    """  
    expected = "IllegalArrayLiteral(ArrayLiteral({IntLiteral(1), FloatLiteral(2.5), IntLiteral(3)}))"
    assert Checker(source).check_from_source() == expected


# Invalid array literal with incompatible types
def test_068():
    source = """
    class Test {
        static void main() {
            boolean[2] flags := {true, 42};
        }
    }
    """  
    expected = "IllegalArrayLiteral(ArrayLiteral({BoolLiteral(True), IntLiteral(42)}))"
    assert Checker(source).check_from_source() == expected


# Invalid assignment grandparent class to child class
def test_069():
    source = """
    class Grandparent {
    }
    class Parent extends Grandparent {
    }
    class Child extends Parent {
    }
    class Test {
        static void main() {
            Child c;
            c := new Grandparent();
        }
    }
    """  
    expected = "TypeMismatchInStatement(AssignmentStatement(IdLHS(c) := ObjectCreation(new Grandparent())))"
    assert Checker(source).check_from_source() == expected  


# Valid assignment child class to parent class
def test_070():
    source = """
    class Parent {
    }
    class Child extends Parent {
    }
    class Test {
        static void main() {
            Parent p;
            p := new Child();
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# invalid assignment array with different sizes
def test_071():
    source = """
    class Test {
        static void main() {
            int[5] arr1;
            int[10] arr2;
            arr2 := arr1;
        }
    }
    """  
    expected = "TypeMismatchInStatement(AssignmentStatement(IdLHS(arr2) := Identifier(arr1)))"
    assert Checker(source).check_from_source() == expected



# Valid array Subscripting
def test_072():
    source = """
    class Test {
        static void main() {
            int[5] arr;
            int x := arr[2];
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Invalid array Subscripting with non-integer index
def test_073():
    source = """
    class Test {
        static void main() {
            int[5] arr;
            int x := arr[true];
        }
    }
    """  
    expected = "TypeMismatchInExpression(PostfixExpression(Identifier(arr)[BoolLiteral(True)]))"
    assert Checker(source).check_from_source() == expected


# # the two `\` and `%` operators require all their operands must be in integer type
# def test_075():
#     source = """
#     class Test {
#         static void main() {
#             int x := 10 \ 3;
#             float y := 10.5 % 2.0;
#         }
#     }
#     """  
#     expected = "TypeMismatchInExpression(BinaryOp(FloatLiteral(10.5), %, FloatLiteral(2.0)))"
#     assert Checker(source).check_from_source() == expected


# # Valid \ and % operations
# def test_076():
#     source = """
#     class Test {
#         static void main() {
#             int x := 10 \ 3;
#             int y := 10 % 2;
#         }
#     }
#     """  
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected


# **Boolean expressions** have logical operators, such as `&&` (AND), `||` (OR), `!` (NOT). The operands of these operators must be in boolean type and their result type is also boolean.
def test_077():
    source = """
    class Test {
        static void main() {
            boolean a := true && false;
            boolean b := !a || (5 > 3);
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

# Invalid boolean expression with non-boolean operands
def test_078():
    source = """
    class Test {
        static void main() {
            boolean a := true && 5;
        }
    }
    """  
    expected = "TypeMismatchInExpression(BinaryOp(BoolLiteral(True), &&, IntLiteral(5)))"
    assert Checker(source).check_from_source() == expected


# Invalid boolean expression with non-boolean result
def test_079():
    source = """
    class Test {
        static void main() {
            boolean a := 5 + 3;
        }
    }
    """  
    expected = "TypeMismatchInStatement(VariableDecl(PrimitiveType(boolean), [Variable(a = BinaryOp(IntLiteral(5), +, IntLiteral(3)))]))"
    assert Checker(source).check_from_source() == expected

# Invalid assignment result of a boolean expression to an integer variable
def test_080():
    source = """
    class Test {
        static void main() {
            int x := true || false;
        }
    }
    """  
    expected = "TypeMismatchInStatement(VariableDecl(PrimitiveType(int), [Variable(x = BinaryOp(BoolLiteral(True), ||, BoolLiteral(False)))]))"
    assert Checker(source).check_from_source() == expected


# \ and % must return float no wheterr operands are int or float
def test_081():
    source = """
    class Test {
        static void main() {
            float x := 10 \\ 3;
            float y := 10 % 2;
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Invalid return for \ and %
def test_082():
    source = """
    class Test {
        static void main() {
            int x := 10 / 3;
            int y := 10 % 2;
        }
    }
    """  
    expected = "TypeMismatchInStatement(VariableDecl(PrimitiveType(int), [Variable(x = BinaryOp(IntLiteral(10), /, IntLiteral(3)))]))"
    assert Checker(source).check_from_source() == expected


# MethodInvocationStatement must return void
def test_083():
    source = """
    class Test {
        int display() {
            return 5;
        }
        static void main() {
            Test t;
            t.display();
        }
    }
    """  
    expected = "TypeMismatchInStatement(MethodInvocationStatement(PostfixExpression(Identifier(t).display())))"
    assert Checker(source).check_from_source() == expected


# Valid method invocation statement
def test_084():
    source = """
    class Test {
        void display() {
        }
        static void main() {
            Test t;
            t.display();
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# When you access an attribute, the object must be class type
def test_085():
    source = """
    class Test {
        static void main() {
            int x;
            int y := x.value;
        }
    }
    """  
    expected = "TypeMismatchInExpression(PostfixExpression(Identifier(x).value))"
    assert Checker(source).check_from_source() == expected


# When you access a method, the object must be class type
def test_086():
    source = """
    class Test {
        static void main() {
            float x;
            x.toString();
        }
    }
    """  
    expected = "TypeMismatchInExpression(PostfixExpression(Identifier(x).toString()))"
    assert Checker(source).check_from_source() == expected



# Valid attribute access
def test_087():
    source = """
    class Person {
        int age;
    }
    class Test {
        static void main() {
            Person p;
            int a := p.age;
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Valid method access
def test_088():
    source = """
    class Person {
        void greet() {
        }
    }
    class Test {
        static void main() {
            Person p;
            p.greet();
        }
    }
    """  
    expected = "Static checking passed" 
    assert Checker(source).check_from_source() == expected



# Arugemnt must compatible with parameter type in method invocation expression
def test_089():
    source = """
    class Test {
        int add(int x; int y) {
            return x + y;
        }
        static void main() {
            Test t;
            int result := t.add(5, "10");
        }
    }
    """  
    expected = "TypeMismatchInExpression(PostfixExpression(Identifier(t).add(IntLiteral(5), StringLiteral('10'))))"
    assert Checker(source).check_from_source() == expected



# Class C call attribiute b of class B and b is an object of class A which is not a subclass of B
def test_090():
    source = """
    class A {
        int a;
    }
    class B {
        A b;
    }
    class C {
        static void main() {
            B objB;
            int x := objB.b.a;
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected



# Valid constant declaration
def test_091():
    source = """
    class Test {
        static void main() {
            final int x := 5;
            int y := x + 10;
        }
    }                                       
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Incomtipatible types in constant declaration
def test_092():
    source = """
    class Test {
        static void main() {
            final int x := "hello";
        }
    }                                       
    """  
    expected = "TypeMismatchInConstant(VariableDecl(final PrimitiveType(int), [Variable(x = StringLiteral('hello'))]))"
    assert Checker(source).check_from_source() == expected



# Coercion in constant declaration
def test_093():
    source = """
    class Test {
        static void main() {
            final float x := 10;
            float y := x + 5.5;
        }
    }                                       
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# # Coercion subtype in constant declaration
# def test_094():
#     source = """
# class Parent {
# }
# class Child extends Parent {
# }
# class Test {
#     static void main() {
#         final Parent p := new Child();
#         Parent q := p;
#     }
# }                                       
# """  
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected



# Invalid coercion supertype in constant declaration
# def test_095():
#     source = """
# class Parent {
# }
# class Child extends Parent {
# }
# class Test {    
#     static void main() {
#         final Child c := new Parent();
#         Child d := c;
#     }
# }                                       
# """  
#     expected = "TypeMismatchInStatement(VariableDecl(ClassType(Child), [Variable(c = ObjectCreation(new Parent()))]))"
#     assert Checker(source).check_from_source() == expected


# Invalid float coercion in constant declaration
def test_096():
    """Invalid float coercion in constant declaration native case"""
    source = """
    class Test {
        static void main() {
            final int x := 10.5;
        }
    }                                       
    """  
    expected = "TypeMismatchInConstant(VariableDecl(final PrimitiveType(int), [Variable(x = FloatLiteral(10.5))]))"
    assert Checker(source).check_from_source() == expected


# Valid loop with break
def test_097():
    source = """
    class Test {
        static void main() {
            for i := 1 to 10 do {
                if (i == 5) {
                    break;
                }
            }
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Break statement outside loop
def test_098():
    source = """
    class Test {
        static void main() {
            if (true) {
                break;
            }
        }
    }
    """  
    expected = "MustInLoop(BreakStatement())"
    assert Checker(source).check_from_source() == expected



# Break and continue in nested loops
def test_099():
    source = """
    class Test {
        static void main() {
            for i := 1 to 10 do {
                for j := 1 to 5 do {
                    if (j == 3) {
                        break;
                    }
                }
                if (i == 7) {
                    continue;
                }
            }
        }
    }
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Continue outside loop
def test_100():
    source = """
    class Test {
        static void main() {
            {
                continue;
            }
        }
    }
    """  
    expected = "MustInLoop(ContinueStatement())"    
    assert Checker(source).check_from_source() == expected


# Cannot cross function/method boundary with break
def test_101():
    source = """
    class Test {
        void helper() {
            break;
        }
        static void main() {
            for i := 1 to 10 do {
                this.helper();
            }
        }    
    }
    """  
    expected = "MustInLoop(BreakStatement())"
    assert Checker(source).check_from_source() == expected


# Cannot cross function/method boundary with continue
def test_102():
    source = """
    class Test {
        void helper() {
            continue;
        }
        static void main() {
            for i := 1 to 10 do {
                this.helper();
            }
        }
    }
    """  
    expected = "MustInLoop(ContinueStatement())"
    assert Checker(source).check_from_source() == expected


# Illegal constant expression with non-constant RHS
def test_103():
    source = """
    class Test {
        static void main() {
            int x := 5;
            final int y := x + 10;
        }
    }                                       
    """ 
    expected = "IllegalConstantExpression(BinaryOp(Identifier(x), +, IntLiteral(10)))"
    assert Checker(source).check_from_source() == expected


# Valid constant expression
def test_104():
    source = """
    class Test {
        static void main() {
            final int x := 5 + 10 * 2;
            final boolean flag := true && false;
        }
    }                                       
    """ 
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Constant variable must be initialized
def test_105():
    source = """
    class Test {
        static void main() {
            final int x;
        }
    }                                       
    """ 
    expected = "IllegalConstantExpression(None)"
    assert Checker(source).check_from_source() == expected


# Cannot initialize constant with method invocation
def test_106():
    source = """
    class Test {
        int getValue() {
            return 10;
        }
        static void main() {
            final int x := this.getValue();
        }
    }                                       
    """ 
    expected = "IllegalConstantExpression(PostfixExpression(ThisExpression(this).getValue()))"
    assert Checker(source).check_from_source() == expected


# constant variable can only use operators, no method call
def test_107():
    source = """
    class Test {
        static void main() {
            final int x := io.readInt();
        }
    }                                       
    """ 
    expected = "IllegalConstantExpression(PostfixExpression(Identifier(io).readInt()))"
    assert Checker(source).check_from_source() == expected


# Constant varriable cannot be initialized with nil
def test_108():
    source = """
    class Test {
        static void main() {
            final int x := nil;
        }
    }
    """ 
    expected = "IllegalConstantExpression(NilLiteral(nil))"
    assert Checker(source).check_from_source() == expected

# Coercion subtype in constant declaration
def test_094():
    source = """
class Parent {
}
class Child extends Parent {
}
class Test {
    static void main() {
        final Parent p := new Child();
        Parent q := p;
    }
}                                       
"""  
    expected = "IllegalConstantExpression(ObjectCreation(new Child()))"
    assert Checker(source).check_from_source() == expected



# Invalid coercion supertype in constant declaration
def test_095():
    source = """
class Parent {
}
class Child extends Parent {
}
class Test {    
    static void main() {
        final Child c := new Parent();
        Child d := c;
    }
}                                       
"""  
    expected = "IllegalConstantExpression(ObjectCreation(new Parent()))"
    assert Checker(source).check_from_source() == expected



# Elements of constant array literal must be the same type
def test_109():
    source = """
    class Test {
        static void main() {
            final int[3] arr := {1, 2.5, 3};
        }
    }                                       
    """  
    expected = "IllegalArrayLiteral(ArrayLiteral({IntLiteral(1), FloatLiteral(2.5), IntLiteral(3)}))"
    assert Checker(source).check_from_source() == expected


# No type coercion in constant array literal
def test_110():
    source = """
    class Test {
        static void main() {
            final float[3] arr := {1, 2, 3.5};
        }
    }                                       
    """  
    expected = "IllegalArrayLiteral(ArrayLiteral({IntLiteral(1), IntLiteral(2), FloatLiteral(3.5)}))"
    assert Checker(source).check_from_source() == expected


# Valid array literal with object
def test_111():
    source = """
    class Person {
        int age;
    }
    class Test {
        static void main() {
            Person[2] people := {new Person(), new Person()};
        }
    }                                       
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# # Valid nested array literal
# def test_112():
#     source = """
#     class Test {
#         static void main() {
#             int[2][3] matrix := {
#                 {1, 2, 3},
#                 {4, 5, 6}
#             };
#         }
#     }                                       
#     """  
#     expected = "Static checking passed"
#     assert Checker(source).check_from_source() == expected


# Valid empty array if type can be inferred
def test_113():
    source = """
    class Test {
        static void main() {
            int[0] arr := {};
        }
    }                                       
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Invalid array literal with different object
def test_114():
    source = """
    class Person {
        int age;
    }
    class Animal {
        int legs;
    }
    class Test {
        static void main() {
            Person[2] people := {new Person(), new Animal()};
        }
    }                                       
    """  
    expected = "IllegalArrayLiteral(ArrayLiteral({ObjectCreation(new Person()), ObjectCreation(new Animal())}))"
    assert Checker(source).check_from_source() == expected


# Valid access static member through class name
def test_115():
    source = """
    class Test {
        static int count;
        static void main() {
            Test.count := 10;
            int c := Test.count;
        }
    }                                       
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

# Invalid access non-static member through class name
def test_116():
    source = """
    class Test {
        int value;
        static void main() {
            Test.value := 5;
            int v := Test.value;
        }
    }                                       
    """ 
    expected = "IllegalMemberAccess(PostfixExpression(Identifier(Test).value))"
    assert Checker(source).check_from_source() == expected


# Valid access non-static member through instance
def test_117():
    source = """
    class Test {
        int value;
        static void main() {
            Test t;
            t.value := 5;
            int v := t.value;
        }
    }                                       
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


# Invalid access static member through instance
def test_118():
    source = """
    class Test {
        static int count;
        static void main() {
            Test t;
            t.count := 10;
            int c := t.count;
        }
    }                                       
    """  
    expected = "IllegalMemberAccess(PostfixExpression(Identifier(t).count))"
    assert Checker(source).check_from_source() == expected




# Member access must base on rule of scope
def test_120():
    source = """
    class Test {
        int instanceValue;
        static void main() {
            Test t;
            t.instanceValue := 10;
            int iv := t.instanceValue;
            Test.staticValue := 20;
            int sv := Test.staticValue;
        }
    }   
    """  
    expected = "UndeclaredAttribute(staticValue)"
    assert Checker(source).check_from_source() == expected


# Member access must base on inheritance
def test_121():
    source = """
    class Parent {
        int parentValue;
    }
    class Child extends Parent {
    }
    class Test {
        static void main() {
            Child c;
            c.parentValue := 15;
            int pv := c.parentValue;
        }
    }   
    """  
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_122():
    source = """
    class Test {
        int display() {
            return 5;
        }
        static void main() {
            Test t;
            t.display();
        }
    }
    """  
    expected = "TypeMismatchInStatement(MethodInvocationStatement(PostfixExpression(Identifier(t).display())))"
    assert Checker(source).check_from_source() == expected

def test_151():
        """Chained method calls with void in middle"""
        source = """
        class Helper {
            void process() {}
        }
        class Test {
            Helper getHelper() { return new Helper(); }
            static void main() {
                Test t := new Test();
                t.getHelper().process();
            }
        }
        """
        expected = "Static checking passed"
        assert Checker(source).check_from_source() == expected

def test_174():
    source = """
    class LoopExample {
    final int limit := 10;
    
    void process() {
        for limit := 0 to 20 do {
            io.writeIntLn(limit);
        }
    }
}"""
    expected = "CannotAssignToConstant(ForStatement(limit, 0, 20, BlockStatement([MethodInvocationStatement(PostfixExpression(Identifier(io).writeIntLn(Identifier(limit))))]))))"
    assert Checker(source).check_from_source() == expected
