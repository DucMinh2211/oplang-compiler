grammar OPLang;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program: EOF; // write for program rule here using vardecl and funcdecl

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs 
COMMENT_LINE: '#' ~[\r\n]* -> skip; // skip comment line (skip anything till end of line or end of file)
COMMENT_BLOCK: '\/\*' .*? '\*\/' -> skip; // skip comment block (a comment block must be closed)

ERROR_CHAR: .;
ILLEGAL_ESCAPE:.;
UNCLOSE_STRING:.;

// KEYWORDS
BOOLEAN: 'boolean';
BREAK: 'break';
CLASS: 'class';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
EXTENDS: 'extends';
FLOAT: 'float';
IF: 'if';
INT: 'int';
NEW: 'new';
STRING: 'string';
THEN: 'then';
FOR: 'for';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
VOID: 'void';
NIL: 'nil';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';
TO: 'to';
DOWNTO: 'downto';

// OPERATOR
// Arithmetic Operators
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '%';

// Relational and Equality Operators
NOT_EQUAL: '!=';
EQUAL: '==';
LESS_THAN: '<';
GREATER_THAN: '>';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN_OR_EQUAL: '>=';

// Logical Operators
LOGICAL_OR: '||';
LOGICAL_AND: '&&';
NOT: '!';

// Bitwise or Other Operators (depending on the language)
POWER: '^'; // Could be exponentiation or XOR
BITWISE_OR: '|'; // Could also be used in logical expressions

// Keyword
NEW: 'new';

// A common rule for backslash, often used for escape sequences in strings.
BACKSLASH: '\';

// SEPARATORS
LBRACKET: '[';
RBRACKET: ']';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMICOLON: ';';
COLON: ':';
DOT: '.';
COMMA: ',';

