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
COMMENT_BLOCK: '/*' .*? '*/' -> skip; // skip comment block (a comment block must be closed)

// IDENTIFIER
ID: [a-zA-Z_][a-zA-Z0-9_]*;

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
FLOAT_DIVISION: '/';
INTEGER_DIVISION: '\\';
MODULO: '%';

// Relational and Equality Operators
NOT_EQUAL: '!=';
EQUAL: '==';
LESS_THAN: '<';
GREATER_THAN: '>';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN_OR_EQUAL: '>=';

// Assign
ASSIGN: ':=';

// Logical Operators
LOGICAL_OR: '||';
LOGICAL_AND: '&&';
NOT: '!';

// Bitwise or Other Operators (depending on the language)
POWER: '^'; // Could be exponentiation or XOR
BITWISE_OR: '|'; // Could also be used in logical expressions

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

// SPECIAL CHARACTERS
TILDE: '~'; // for class deconstructor
AMPERSAND: '&'; // for variable reference

// LITERALS
INTEGER_LITERAL: [0-9]+;
FLOAT_LITERAL: [0-9]+ ('.' [0-9]*)? (('e'|'E') ('+'|'-')? [0-9]+)?;
BOOLEAN_LITERAL: TRUE | FALSE;
STRING_LITERAL: '"' ( '\\' [btnfr"'\\] | ~[\b\t\f\r\n\\"] )* '"' { self.text = self.text[1:-1] };
array_literal: LBRACE (value (COMMA value)*)? RBRACE;
value: INTEGER_LITERAL | FLOAT_LITERAL | BOOLEAN_LITERAL | STRING_LITERAL;

// ERRORS
ILLEGAL_ESCAPE: '"' ~[\n\r"]*? ('\\' ~[btnfr"'\\]) { self.text = self.text[1:] };
UNCLOSE_STRING: '"' ~[\n\r"]*? (EOF | '\n' | '\r') { self.text = self.text[1:] };
ERROR_CHAR: .;
