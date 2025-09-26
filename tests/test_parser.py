from utils import Parser


def test_001():
    """Test basic class with main method"""
    source = """class Program { static void main() {} }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_002():
    """Test method with parameters"""
    source = """class Math { int add(int a; int b) { return a + b; } }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_003():
    """Test class with attribute declaration"""
    source = """class Test { int x; static void main() { x := 42; } }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_004():
    """Test class with string attribute"""
    source = """class Test { string name; static void main() { name := "Alice"; } }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_005():
    """Test final attribute declaration"""
    source = """class Constants { final float PI := 3.14159; static void main() {} }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_006():
    """Test if-else statement"""
    source = """class Test { 
        static void main() { 
            if (x > 0) then { 
                io.writeStrLn("positive"); 
            } else { 
                io.writeStrLn("negative"); 
            }
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_007():
    """Test for loop with to keyword"""
    source = """class Test { 
        static void main() { 
            int i;
            for i := 1 to 10 do { 
                i := i + 1; 
            }
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_008():
    """Test for loop with downto keyword"""
    source = """class Test { 
        static void main() { 
            int i;
            for i := 10 downto 1 do { 
                io.writeInt(i); 
            }
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_009():
    """Test array declaration and access"""
    source = """class Test { 
        static void main() { 
            int[3] arr := {1, 2, 3};
            int first;
            first := arr[0];
            arr[1] := 42;
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_010():
    """Test string concatenation and object creation"""
    source = """class Test { 
        static void main() { 
            string result;
            Test obj;
            result := "Hello" ^ " " ^ "World";
            obj := new Test();
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_011():
    """Test parser error: missing closing brace in class declaration"""
    source = """class Test { int x := 1; """  # Thiếu dấu }
    expected = "Error on line 1 col 25: <EOF>"
    assert Parser(source).parse() == expected

def test_012():
    """Test class inheritance"""
    source = """class A {} class B extends A {} """
    expected = "success"
    assert Parser(source).parse() == expected

def test_013():
    """Test multiple attribute declarations"""
    source = """class Test { int a, b; float c; }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_014():
    """Test constructor declaration"""
    source = """class Test { Test() {} }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_015():
    """Test destructor declaration"""
    source = """class Test { ~Test() {} }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_016():
    """Test copy constructor"""
    source = """class Test { Test(Test other) {} }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_017():
    """Test reference parameter"""
    source = """class Test { void foo(int & a) {} }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_018():
    """Test reference return type"""
    source = """class Test { int & foo() { return x; } }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_019():
    """Test break and continue statements"""
    source = """class Test { static void main() { for i := 1 to 10 do { break; continue; } } }"""
    expected = "success"
    assert Parser(source).parse() == expected

def test_020():
    """Test member access and method invocation"""
    source = """class Test { int x; void foo() { this.x := self.foo(); } }"""
    expected = "success"
    assert Parser(source).parse() == expected

# More parser tests from 21 to 100

def test_021():
    """Test empty class"""
    source = "class Empty {}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_022():
    """Test multiple classes"""
    source = "class A {} class B {}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_023():
    """Test static attribute"""
    source = "class Test { static int x; }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_024():
    """Test static final attribute"""
    source = "class Test { static final int x := 1; }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_025():
    """Test method returning an array"""
    source = "class Test { int[5] foo() {} }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_026():
    """Test method with array parameter"""
    source = "class Test { void foo(int[5] arr) {} }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_027():
    """Test block statement with variable declarations"""
    source = "class Test { void main() { int x; float y; } }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_028():
    """Test nested block statements"""
    source = "class Test { void main() { { int x; } } }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_029():
    """Test arithmetic expressions with precedence"""
    source = "class Test { void main() { x := 1 + 2 * 3; } }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_030():
    """Test boolean expressions"""
    source = "class Test { void main() { flag := a && b || !c; } }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_031():
    """Test relational expressions"""
    source = "class Test { void main() { flag := (a > b) || (c < d); } }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_032():
    """Test object creation with parameters"""
    source = "class Test { void main() { obj := new Test(1, 2); } }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_033():
    """Test static method call"""
    source = "class Test { void main() { Math.abs(-1); } }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_034():
    """Test if without else"""
    source = "class Test { void main() { if true then {} } }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_035():
    """Test empty for loop"""
    source = "class Test { void main() { for i := 1 to 1 do {} } }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_036():
    """Test return statement with expression"""
    source = "class Test { int main() { return 0; } }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_037():
    """Test empty return statement"""
    source = "class Test { void main() { return; } }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_038():
    """Test unary minus"""
    source = "class Test { void main() { x := -y; } }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_039():
    """Test array literal"""
    source = "class Test { void main() { arr := {1,2,3}; } }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_040():
    """Test this keyword"""
    source = "class Test { int x; void foo() { this.x := 1; } }"
    expected = "success"
    assert Parser(source).parse() == expected

# Error tests
def test_041():
    """Error: missing semicolon after attribute"""
    source = "class Test { int x }"
    expected = "Error on line 1 col 19: }"
    assert Parser(source).parse() == expected

def test_042():
    """Error: missing class name"""
    source = "class {} "
    expected = "Error on line 1 col 6: {"
    assert Parser(source).parse() == expected

def test_043():
    """Error: invalid inheritance"""
    source = "class A extends {} "
    expected = "Error on line 1 col 16: {"
    assert Parser(source).parse() == expected

def test_044():
    """Error: missing parameter type"""
    source = "class Test { void foo(a) {} }"
    expected = "Error on line 1 col 23: )"
    assert Parser(source).parse() == expected

def test_045():
    """Error: missing `then` in if statement"""
    source = "class Test { void main() { if true {} } }"
    expected = "Error on line 1 col 35: {"
    assert Parser(source).parse() == expected

def test_046():
    """Error: missing `do` in for statement"""
    source = "class Test { void main() { for i := 1 to 10 {} } }"
    expected = "Error on line 1 col 44: {"
    assert Parser(source).parse() == expected

def test_047():
    """Error: invalid assignment operator"""
    source = "class Test { void main() { x = 1; } }"
    expected = "Error Token ="
    assert Parser(source).parse() == expected

def test_048():
    """Error: return in constructor"""
    source = "class Test { Test() { return; } }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_049():
    """Error: return in destructor"""
    source = "class Test { ~Test() { return; } }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_050():
    """Error: break outside loop"""
    source = "class Test { void main() { break; } }"
    expected = "success" # Semantic check, not parser
    assert Parser(source).parse() == expected

# Auto-generated simple tests 51-100

def test_051():
    source = "class T {int x;}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_052():
    source = "class T {float x;}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_053():
    source = "class T {boolean x;}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_054():
    source = "class T {string x;}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_055():
    source = "class T {int[1] x;}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_056():
    source = "class T {void f(){}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_057():
    source = "class T {int f(){}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_058():
    source = "class T {float f(){}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_059():
    source = "class T {boolean f(){}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_060():
    source = "class T {string f(){}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_061():
    source = "class T {int[1] f(){}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_062():
    source = "class T {void f(int a){}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_063():
    source = "class T {void f(int a; float b){}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_064():
    source = "class T {void f(int & a){}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_065():
    source = "class T {int & f(){}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_066():
    source = "class T {static int x;}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_067():
    source = "class T {final int x := 1;}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_068():
    source = "class T {static final int x := 1;}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_069():
    source = "class T {static void f(){}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_070():
    source = "class T {T(){}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_071():
    source = "class T {~T(){}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_072():
    source = "class T {T(T t){}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_073():
    source = "class T {void f(){a:=1;}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_074():
    source = "class T {void f(){if true then {}}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_075():
    source = "class T {void f(){if true then {} else {}}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_076():
    source = "class T {void f(){for i:=1 to 2 do {}}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_077():
    source = "class T {void f(){for i:=2 downto 1 do {}}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_078():
    source = "class T {void f(){break;}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_079():
    source = "class T {void f(){continue;}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_080():
    source = "class T {void f(){return;}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_081():
    source = "class T {int f(){return 1;}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_082():
    source = "class T {void f(){T.f();}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_083():
    source = "class T {void f(){this.f();}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_084():
    source = "class T {void f(){a.b[1] := 1;}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_085():
    source = "class T {void f(){a := new T();}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_086():
    source = "class T {void f(){a := -b;}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_087():
    source = "class T {void f(){a := !b;}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_088():
    source = "class T {void f(){a := b+c*d;}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_089():
    source = "class T {void f(){a := b&&c||d;}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_090():
    source = "class T {void f(){a := b==c;}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_091():
    source = "class T {void f(){a := b^c;}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_092():
    source = "class T {void f(){a := {1,2};}}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_093():
    source = "class T{int x:=1;}"
    expected = "success"
    assert Parser(source).parse() == expected

def test_094():
    source = "class T{int f(a){}}"
    expected = "Error on line 1 col 15: )"
    assert Parser(source).parse() == expected

def test_095():
    source = "class T{void f(){a=1;}}"
    expected = "Error Token ="
    assert Parser(source).parse() == expected

def test_096():
    source = "class T{void f(){if(a>b){}}}"
    expected = "Error on line 1 col 24: {"
    assert Parser(source).parse() == expected

def test_097():
    source = "class T{void f(){for i:=1 to 10 {}}}"
    expected = "Error on line 1 col 32: {"
    assert Parser(source).parse() == expected

def test_098():
    source = "class T{void f(){return 1}}"
    expected = "Error on line 1 col 25: }"
    assert Parser(source).parse() == expected

def test_099():
    source = "class T extends A, B{}"
    expected = "Error on line 1 col 17: ,"
    assert Parser(source).parse() == expected

def test_100():
    """ function or constructor? Test constructor """
    source = "class T{ f() { int & a := 1;} }"
    expected = "success"
    assert Parser(source).parse() == expected

def test_101():
    source = "class T {void f() { a[3+x.foo(2)] := a[b[2]] + 3; } } "
    expected = "success"
    assert Parser(source).parse() == expected

def test_102():
    source = "class T {void f() { a := (new C()).get(); } } "
    expected = "success"
    assert Parser(source).parse() == expected

def test_103():
    source = "class T {void f() { T a := (new C()).get(); } } "
    expected = "success"
    assert Parser(source).parse() == expected

def test_104():
    source = "class T {void f() { T a := (c > d) || (d > b); } } "
    expected = "success"
    assert Parser(source).parse() == expected
