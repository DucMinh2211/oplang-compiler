import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "build"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from antlr4 import *
from build.OPLangLexer import OPLangLexer
from build.OPLangParser import OPLangParser
from src.astgen.ast_generation import ASTGeneration
from src.semantics.static_checker import StaticChecker

source = """
    class Test {
        void add(int a, b) { return a + b; }
        void test() {
            this.add(5, 3);
        }
    }
"""

# Generate AST
input_stream = InputStream(source)
lexer = OPLangLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = OPLangParser(token_stream)
ast_generator = ASTGeneration()

parse_tree = parser.program()
ast = ast_generator.visit(parse_tree)

# Print the AST
print("AST:")
print(ast)
print()

# Check the method's parameters
test_class = ast.class_decls[0]
print(f"Class: {test_class.name}")
for member in test_class.members:
    print(f"  Member: {member}")
    if hasattr(member, 'params'):
        print(f"    Params: {member.params}")
        for param in member.params:
            print(f"      Param: {param.name}, Type: {param.param_type}")
