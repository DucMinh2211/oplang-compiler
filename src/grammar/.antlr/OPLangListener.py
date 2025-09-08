# Generated from /Users/nongthithuykieu/projects/oplang-compiler/src/grammar/OPLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .OPLangParser import OPLangParser
else:
    from OPLangParser import OPLangParser

# This class defines a complete listener for a parse tree produced by OPLangParser.
class OPLangListener(ParseTreeListener):

    # Enter a parse tree produced by OPLangParser#program.
    def enterProgram(self, ctx:OPLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by OPLangParser#program.
    def exitProgram(self, ctx:OPLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by OPLangParser#list_class_declaration.
    def enterList_class_declaration(self, ctx:OPLangParser.List_class_declarationContext):
        pass

    # Exit a parse tree produced by OPLangParser#list_class_declaration.
    def exitList_class_declaration(self, ctx:OPLangParser.List_class_declarationContext):
        pass


    # Enter a parse tree produced by OPLangParser#class_declaration.
    def enterClass_declaration(self, ctx:OPLangParser.Class_declarationContext):
        pass

    # Exit a parse tree produced by OPLangParser#class_declaration.
    def exitClass_declaration(self, ctx:OPLangParser.Class_declarationContext):
        pass


    # Enter a parse tree produced by OPLangParser#array_literal.
    def enterArray_literal(self, ctx:OPLangParser.Array_literalContext):
        pass

    # Exit a parse tree produced by OPLangParser#array_literal.
    def exitArray_literal(self, ctx:OPLangParser.Array_literalContext):
        pass


    # Enter a parse tree produced by OPLangParser#value.
    def enterValue(self, ctx:OPLangParser.ValueContext):
        pass

    # Exit a parse tree produced by OPLangParser#value.
    def exitValue(self, ctx:OPLangParser.ValueContext):
        pass



del OPLangParser