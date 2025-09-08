# Generated from /Users/nongthithuykieu/projects/oplang-compiler/src/grammar/OPLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,65,45,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,1,1,1,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,
        3,2,28,8,2,1,3,1,3,1,3,1,3,5,3,34,8,3,10,3,12,3,37,9,3,3,3,39,8,
        3,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,1,1,0,59,62,44,0,11,1,0,
        0,0,2,21,1,0,0,0,4,23,1,0,0,0,6,29,1,0,0,0,8,42,1,0,0,0,10,12,3,
        4,2,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,
        15,1,0,0,0,15,16,5,0,0,1,16,1,1,0,0,0,17,18,3,4,2,0,18,19,3,2,1,
        0,19,22,1,0,0,0,20,22,3,4,2,0,21,17,1,0,0,0,21,20,1,0,0,0,22,3,1,
        0,0,0,23,24,5,7,0,0,24,27,5,4,0,0,25,26,5,11,0,0,26,28,5,4,0,0,27,
        25,1,0,0,0,27,28,1,0,0,0,28,5,1,0,0,0,29,38,5,51,0,0,30,35,3,8,4,
        0,31,32,5,56,0,0,32,34,3,8,4,0,33,31,1,0,0,0,34,37,1,0,0,0,35,33,
        1,0,0,0,35,36,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,38,30,1,0,0,0,
        38,39,1,0,0,0,39,40,1,0,0,0,40,41,5,52,0,0,41,7,1,0,0,0,42,43,7,
        0,0,0,43,9,1,0,0,0,5,13,21,27,35,38
    ]

class OPLangParser ( Parser ):

    grammarFileName = "OPLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'boolean'", "'break'", "'class'", "'continue'", 
                     "'do'", "'else'", "'extends'", "'float'", "'if'", "'int'", 
                     "'new'", "'string'", "'then'", "'for'", "'return'", 
                     "'true'", "'false'", "'void'", "'nil'", "'this'", "'final'", 
                     "'static'", "'to'", "'downto'", "'+'", "'-'", "'*'", 
                     "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", "'>'", 
                     "'<='", "'>='", "':='", "'||'", "'&&'", "'!'", "'^'", 
                     "'|'", "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", 
                     "':'", "'.'", "','", "'~'", "'&'" ]

    symbolicNames = [ "<INVALID>", "WS", "COMMENT_LINE", "COMMENT_BLOCK", 
                      "ID", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", 
                      "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", 
                      "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", 
                      "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                      "PLUS", "MINUS", "MULTIPLY", "FLOAT_DIVISION", "INTEGER_DIVISION", 
                      "MODULO", "NOT_EQUAL", "EQUAL", "LESS_THAN", "GREATER_THAN", 
                      "LESS_THAN_OR_EQUAL", "GREATER_THAN_OR_EQUAL", "ASSIGN", 
                      "LOGICAL_OR", "LOGICAL_AND", "NOT", "POWER", "BITWISE_OR", 
                      "LBRACKET", "RBRACKET", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "SEMICOLON", "COLON", "DOT", "COMMA", "TILDE", 
                      "AMPERSAND", "INTEGER_LITERAL", "FLOAT_LITERAL", "BOOLEAN_LITERAL", 
                      "STRING_LITERAL", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_list_class_declaration = 1
    RULE_class_declaration = 2
    RULE_array_literal = 3
    RULE_value = 4

    ruleNames =  [ "program", "list_class_declaration", "class_declaration", 
                   "array_literal", "value" ]

    EOF = Token.EOF
    WS=1
    COMMENT_LINE=2
    COMMENT_BLOCK=3
    ID=4
    BOOLEAN=5
    BREAK=6
    CLASS=7
    CONTINUE=8
    DO=9
    ELSE=10
    EXTENDS=11
    FLOAT=12
    IF=13
    INT=14
    NEW=15
    STRING=16
    THEN=17
    FOR=18
    RETURN=19
    TRUE=20
    FALSE=21
    VOID=22
    NIL=23
    THIS=24
    FINAL=25
    STATIC=26
    TO=27
    DOWNTO=28
    PLUS=29
    MINUS=30
    MULTIPLY=31
    FLOAT_DIVISION=32
    INTEGER_DIVISION=33
    MODULO=34
    NOT_EQUAL=35
    EQUAL=36
    LESS_THAN=37
    GREATER_THAN=38
    LESS_THAN_OR_EQUAL=39
    GREATER_THAN_OR_EQUAL=40
    ASSIGN=41
    LOGICAL_OR=42
    LOGICAL_AND=43
    NOT=44
    POWER=45
    BITWISE_OR=46
    LBRACKET=47
    RBRACKET=48
    LPAREN=49
    RPAREN=50
    LBRACE=51
    RBRACE=52
    SEMICOLON=53
    COLON=54
    DOT=55
    COMMA=56
    TILDE=57
    AMPERSAND=58
    INTEGER_LITERAL=59
    FLOAT_LITERAL=60
    BOOLEAN_LITERAL=61
    STRING_LITERAL=62
    ILLEGAL_ESCAPE=63
    UNCLOSE_STRING=64
    ERROR_CHAR=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(OPLangParser.EOF, 0)

        def class_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.Class_declarationContext)
            else:
                return self.getTypedRuleContext(OPLangParser.Class_declarationContext,i)


        def getRuleIndex(self):
            return OPLangParser.RULE_program




    def program(self):

        localctx = OPLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.class_declaration()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

            self.state = 15
            self.match(OPLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_class_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_declaration(self):
            return self.getTypedRuleContext(OPLangParser.Class_declarationContext,0)


        def list_class_declaration(self):
            return self.getTypedRuleContext(OPLangParser.List_class_declarationContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_list_class_declaration




    def list_class_declaration(self):

        localctx = OPLangParser.List_class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_class_declaration)
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.class_declaration()
                self.state = 18
                self.list_class_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.class_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(OPLangParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(OPLangParser.ID)
            else:
                return self.getToken(OPLangParser.ID, i)

        def EXTENDS(self):
            return self.getToken(OPLangParser.EXTENDS, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_class_declaration




    def class_declaration(self):

        localctx = OPLangParser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(OPLangParser.CLASS)
            self.state = 24
            self.match(OPLangParser.ID)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 25
                self.match(OPLangParser.EXTENDS)
                self.state = 26
                self.match(OPLangParser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(OPLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(OPLangParser.RBRACE, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.ValueContext)
            else:
                return self.getTypedRuleContext(OPLangParser.ValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(OPLangParser.COMMA)
            else:
                return self.getToken(OPLangParser.COMMA, i)

        def getRuleIndex(self):
            return OPLangParser.RULE_array_literal




    def array_literal(self):

        localctx = OPLangParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(OPLangParser.LBRACE)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8646911284551352320) != 0):
                self.state = 30
                self.value()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==56:
                    self.state = 31
                    self.match(OPLangParser.COMMA)
                    self.state = 32
                    self.value()
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 40
            self.match(OPLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(OPLangParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(OPLangParser.FLOAT_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OPLangParser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(OPLangParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_value




    def value(self):

        localctx = OPLangParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8646911284551352320) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





