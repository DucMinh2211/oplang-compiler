"""
Test file for attribute access rules in OPLang
Tests that:
1. Instance attributes must be accessed with "this."
2. Static attributes must be accessed with "ClassName."
"""

from utils import Checker


def test_000():
    """Instance attribute cannot be accessed directly by name"""
    source = """
    class Test {
        int x := 5;
        
        void method() {
            int y := x;
        }
        
        static void main() {}
    }
    """
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected


def test_001():
    """Instance attribute can be accessed with this."""
    source = """
    class Test {
        int x := 5;
        
        void method() {
            int y := this.x;
        }
        
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_002():
    """Static attribute cannot be accessed directly by name"""
    source = """
    class Test {
        static int x := 5;
        
        static void main() {
            int y := x;
        }
    }
    """
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected


def test_003():
    """Static attribute can be accessed with ClassName."""
    source = """
    class Test {
        static int x := 5;
        
        static void main() {
            int y := Test.x;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_004():
    """Multiple instance attributes accessed with this."""
    source = """
    class Calculator {
        int value := 0;
        int count := 0;
        
        void add(int n) {
            this.value := this.value + n;
            this.count := this.count + 1;
        }
        
        int getValue() {
            return this.value;
        }
        
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_005():
    """Static attribute accessed with ClassName. in instance method"""
    source = """
    class Counter {
        static int totalCount := 0;
        int myCount := 0;
        
        void increment() {
            this.myCount := this.myCount + 1;
            Counter.totalCount := Counter.totalCount + 1;
        }
        
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_006():
    """Final attribute accessed with this. in constant expression"""
    source = """
    class Circle {
        final float PI := 3.14;
        final float radius := 5.0;
        final float area := this.PI * this.radius * this.radius;
        
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_007():
    """Constructor accessing attributes with this."""
    source = """
    class Person {
        string name;
        int age;
        
        Person(string n; int a) {
            this.name := n;
            this.age := a;
        }
        
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_008():
    """Inherited instance attribute accessed with this."""
    source = """
    class Animal {
        string name;
        
        void setName(string n) {
            this.name := n;
        }
    }
    
    class Dog extends Animal {
        void bark() {
            io.writeStr(this.name);
        }
        
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_009():
    """Mix of instance (this.) and static (ClassName.) access"""
    source = """
    class Student {
        static int totalStudents := 0;
        string name;
        int id;
        
        Student(string n) {
            this.name := n;
            this.id := Student.totalStudents;
            Student.totalStudents := Student.totalStudents + 1;
        }
        
        string getName() {
            return this.name;
        }
        
        static int getTotal() {
            return Student.totalStudents;
        }
        
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_010():
    """Static attribute accessed from another class"""
    source = """
    class Config {
        static int MAX_SIZE := 100;
        static string APP_NAME := "MyApp";
    }
    
    class Test {
        static void main() {
            int size := Config.MAX_SIZE;
            io.writeStr(Config.APP_NAME);
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_011():
    """Instance attribute direct access in constructor fails"""
    source = """
    class Test {
        int x := 5;
        
        Test() {
            int y := x;
        }
        
        static void main() {}
    }
    """
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected


def test_012():
    """Instance attribute with this. in constructor passes"""
    source = """
    class Test {
        int x := 5;
        
        Test() {
            int y := this.x;
        }
        
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_013():
    """Multiple this. accesses in same expression"""
    source = """
    class Point {
        int x := 0;
        int y := 0;
        
        int distance() {
            return this.x * this.x + this.y * this.y;
        }
        
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_014():
    """Static attribute in another class without ClassName. fails"""
    source = """
    class Config {
        static int MAX_SIZE := 100;
    }
    
    class Test {
        static void main() {
            int size := MAX_SIZE;
        }
    }
    """
    expected = "UndeclaredIdentifier(MAX_SIZE)"
    assert Checker(source).check_from_source() == expected


def test_015():
    """Final instance attribute accessed with this. in method"""
    source = """
    class Test {
        final int MAX := 100;
        
        void check() {
            int x := this.MAX;
        }
        
        static void main() {}
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected
