from utils import Tokenizer


def test_001():
    """Test basic identifier tokenization"""
    source = "abc"
    expected = "abc,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_002():
    """Test keywords recognition"""
    source = "class extends static final if else for do then to downto new this void boolean int float string true false nil break continue return"
    expected = "class,extends,static,final,if,else,for,do,then,to,downto,new,this,void,boolean,int,float,string,true,false,nil,break,continue,return,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_003():
    """Test integer literals"""
    source = "42 0 255 2500"
    expected = "42,0,255,2500,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_004():
    """Test float literals"""
    source = "9.0 12e8 1. 0.33E-3 128e+42"
    expected = "9.0,12e8,1.,0.33E-3,128e+42,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_005():
    """Test boolean literals"""
    source = "true false"
    expected = "true,false,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_006():
    """Test unclosed string literal error"""
    source = '"Hello World'
    expected = "Unclosed String: Hello World"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_007():
    """Test illegal escape sequence error"""
    source = '"Hello \\x World"'
    expected = "Illegal Escape In String: Hello \\x"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_008():
    """Test error character (non-ASCII or invalid character)"""
    source = "int x := 5; @ invalid"
    expected = "int,x,:=,5,;,Error Token @"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_009():
    """Test valid string literals with escape sequences"""
    source = '"This is a string containing tab \\t" "He asked me: \\"Where is John?\\""'
    expected = "This is a string containing tab \\t,He asked me: \\\"Where is John?\\\",EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_009a():
    """Test string literals return content without quotes"""
    source = '"Hello World"'
    expected = "Hello World,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_009b():
    """Test empty string literal"""
    source = '""'
    expected = ",EOF"  # Empty string content
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_010():
    """Test operators and separators"""
    source = "+ - * / \\ % == != < <= > >= && || ! := ^ new . ( ) [ ] { } , ; :"
    expected = "+,-,*,/,\\,%,==,!=,<,<=,>,>=,&&,||,!,:=,^,new,.,(,),[,],{,},,,;,:,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_011():
    source = """
        Class A
        """
    expected = "Class,A,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_012():
    source = "int b, c, d"
    expected = "int,b,,,c,,,d,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_013():
    """Test line comment"""
    source = "# this is a line comment"
    expected = "EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_014():
    """Test block comment"""
    source = "/* this is a block comment */"
    expected = "EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_015():
    """Test unterminated block comment"""
    source = "/* */"
    expected = "EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_016():
    """Test string with all valid escapes"""
    source = '"\\b\\f\\r\\n\\t\\"\\\\"'
    expected = "\\b\\f\\r\\n\\t\\\"\\\\,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_017():
    """Test special characters ~ and &"""
    source = "~ &"
    expected = "~,&,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_018():
    """Test invalid float starting with ."""
    source = ".123"
    expected = ".,123,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_019():
    """Test invalid float ending with e"""
    source = "123e"
    expected = "123,e,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_020():
    """Test another invalid character"""
    source = "?"
    expected = "Error Token ?"
    assert Tokenizer(source).get_tokens_as_string() == expected

# Auto-generated tests from 21 to 100

# Identifiers
def test_021():
    source = "_test"
    expected = "_test,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_022():
    source = "test_case"
    expected = "test_case,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_023():
    source = "Test1"
    expected = "Test1,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_024():
    source = "_1"
    expected = "_1,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_025():
    source = "t1_"
    expected = "t1_,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

# Integers
def test_026():
    source = "1234567890"
    expected = "1234567890,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_027():
    source = "007"
    expected = "007,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

# Floats
def test_028():
    source = "1.23"
    expected = "1.23,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_029():
    source = "1.e3"
    expected = "1.e3,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_030():
    source = "1.2E-3"
    expected = "1.2E-3,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

# Strings
def test_031():
    source = '"a string"'
    expected = "a string,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_032():
    source = '"str with space"'
    expected = "str with space,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_033():
    source = '"\\n"'
    expected = "\\n,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_034():
    source = '"\\t"'
    expected = "\\t,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_035():
    source = '"\\""'
    expected = '\\",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

# Errors
def test_036():
    source = '"unclosed'
    expected = "Unclosed String: unclosed"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_037():
    source = '"illegal \\a"'
    expected = "Illegal Escape In String: illegal \\a"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_038():
    source = "#"
    expected = "EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_039():
    source = "/**/"
    expected = "EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_040():
    source = """
        /* 
        multi line comments
        */
    """
    expected = "EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

# Keywords
def test_041():
    source = "boolean"
    expected = "boolean,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_042():
    source = "break"
    expected = "break,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_043():
    source = "continue"
    expected = "continue,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_044():
    source = "do"
    expected = "do,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_045():
    source = "downto"
    expected = "downto,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_046():
    source = "else"
    expected = "else,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_047():
    source = "extends"
    expected = "extends,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_048():
    source = "false"
    expected = "false,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_049():
    source = "final"
    expected = "final,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_050():
    source = "float"
    expected = "float,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_051():
    source = "for"
    expected = "for,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_052():
    source = "if"
    expected = "if,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_053():
    source = "int"
    expected = "int,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_054():
    source = "new"
    expected = "new,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_055():
    source = "nil"
    expected = "nil,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_056():
    source = "return"
    expected = "return,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_057():
    source = "static"
    expected = "static,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_058():
    source = "string"
    expected = "string,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_059():
    source = "then"
    expected = "then,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_060():
    source = "this"
    expected = "this,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_061():
    source = "to"
    expected = "to,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_062():
    source = "true"
    expected = "true,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_063():
    source = "void"
    expected = "void,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

# Operators
def test_064():
    source = "+"
    expected = "+,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_065():
    source = "-"
    expected = "-,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_066():
    source = "*"
    expected = "*,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_067():
    source = "/"
    expected = "/,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_068():
    source = "\\"
    expected = "\\,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_069():
    source = "%"
    expected = "%,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_070():
    source = "=="
    expected = "==,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_071():
    source = "!="
    expected = "!=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_072():
    source = "<"
    expected = "<,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_073():
    source = ">"
    expected = ">,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_074():
    source = "<="
    expected = "<=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_075():
    source = ">="
    expected = ">=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_076():
    source = "&&"
    expected = "&&,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_077():
    source = "||"
    expected = "||,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_078():
    source = "!"
    expected = "!,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_079():
    source = ":="
    expected = ":=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_080():
    source = "^"
    expected = "^,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

# Separators
def test_081():
    source = "("
    expected = "(,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_082():
    source = ")"
    expected = "),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_083():
    source = "["
    expected = "[,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_084():
    source = "]"
    expected = "],EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_085():
    source = "{"
    expected = "{,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_086():
    source = "}"
    expected = "},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_087():
    source = ";"
    expected = ";,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_088():
    source = ":"
    expected = ":,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_089():
    source = "."
    expected = ".,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_090():
    source = ","
    expected = ",,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

# Combinations
def test_091():
    source = "a := b + c"
    expected = "a,:=,b,+,c,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_092():
    source = "if (a > b) then c := a"
    expected = "if,(,a,>,b,),then,c,:=,a,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_093():
    source = "for i := 1 to 10 do io.writeInt(i)"
    expected = "for,i,:=,1,to,10,do,io,.,writeInt,(,i,),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_094():
    source = "return this.x"
    expected = "return,this,.,x,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_095():
    source = "obj := new MyClass()"
    expected = "obj,:=,new,MyClass,(,),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_096():
    source = "arr[0] := 1"
    expected = "arr,[,0,],:=,1,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_097():
    source = "a.b.c"
    expected = "a,.,b,.,c,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_098():
    source = "a && b || c"
    expected = "a,&&,b,||,c,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_099():
    source = "-a + +b"
    expected = "-,a,+,+,b,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_100():
    source = "a := {1,2,3}"
    expected = "a,:=,{,1,,,2,,,3,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected
