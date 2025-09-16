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

/*
####################
### PARSER RULES ###
####################
 */

program: classDeclList EOF; // write for program rule here using vardecl and funcdecl

/* === CLASS DECLARATION === */
classDeclList: classDecl classDeclList | classDecl;
classDecl: CLASS ID classExtends LBRACE memberNulist RBRACE;

classExtends: EXTENDS ID | ;
memberNulist: member memberNulist | ;
member: (isStatic (attributeDecl | methodDecl)) | constructors;
isStatic: STATIC | ;
/* === === === */

/* === ATTRIBUTE DECLARATION === */
attributeDecl: isFinal type attributeNameList SEMI;
attributeNameList: attributeName COMMA attributeNameList | attributeName;

isFinal: FINAL | ;
attributeName: ID MEMBER_ASSIGN literals | ID;
/* === === === */

/* === METHOD DECLARATION === */
methodDecl: type isRef ID LPAREN paramNulist RPAREN blockStatement;

paramNulist: paramPrime | ;
paramPrime: param SEMI paramPrime | param;
param: type isRef idList;
idList: ID COMMA idList | ID;

isRef: AMPERSAND | ;
/* === === === */

/* === CONSTRUCTOR DECLARATION === */
constructors: defConstructor
            | copyConstructor
            | customConstructor
            | destructor
            ;

defConstructor: ID LPAREN RPAREN blockStatement;
copyConstructor: ID LPAREN ID 'other' RPAREN blockStatement;
customConstructor: ID LPAREN paramNulist RPAREN blockStatement;

destructor: TILDE ID LPAREN RPAREN blockStatement;
/* === === === */

/* === EXPRESSION === */
expr0: expr1 CMP_WITH_OP expr1 | expr1;
CMP_WITH_OP:  LESS_THAN | GREATER_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL;

expr1: expr2 CMP_OP expr2 | expr2;
CMP_OP: EQUAL | NOT_EQUAL;

expr2: expr2 AND_OR_OP expr3 | expr3;
AND_OR_OP: LOGICAL_AND | LOGICAL_OR;

expr3: expr3 ADD_SUB_OP expr4 | expr4;
ADD_SUB_OP: PLUS | MINUS;

expr4: expr4 MUL_DIV_MOD_OP expr5 | expr5;
MUL_DIV_MOD_OP: MULTIPLY | FLOAT_DIVISION | INTEGER_DIVISION | MODULO;

expr5: expr5 STR_CONCAT_OP expr6 | expr6;
STR_CONCAT_OP: STR_CONCAT;

expr6: NOT expr6 | expr7;

expr7: ADD_SUB_OP expr7 | expr8;

expr8: expr8 arrayAccess | expr9;
arrayAccess: LBRACKET expr0 RBRACKET;

expr9: expr9 DOT (methodInvocation | ID) | fact;

fact: literals
    | ID
    | NIL
    | methodInvocation
    | objCreation
    | THIS
    | LPAREN expr0 RPAREN
    ;

objCreation: NEW ID LPAREN exprNulist RPAREN;
exprNulist: exprPrime | ;
exprPrime: expr0 COMMA exprPrime | expr0;

methodInvocation: ID LPAREN exprNulist RPAREN;
/* === === === */

/* === BLOCK STATEMENT === */
blockStatement: LBRACE stmtNulist RBRACE;

stmtNulist: stmt stmtNulist | ;

stmt: varDecl
    | assignStmt
    | ifStmt
    | forStmt
    | breakStmt
    | continueStmt
    | returnStmt
    | methodInvoStmt
    | blockStatement
    ;

varDecl: isFinal type attributeNameList SEMI;

assignStmt: lhs ASSIGN expr0 SEMI;
lhs: idOrRef arrayAccess | idOrRef;
idOrRef: ID | THIS DOT ID | ID DOT ID;

ifStmt: IF expr0 THEN stmt (ELSE stmt | );
forStmt: FOR ID /*(scalar var)*/ ASSIGN expr0 (TO | DOWNTO) expr0 DO stmt;
breakStmt: BREAK SEMI;
continueStmt: CONTINUE SEMI;
returnStmt: RETURN expr0 SEMI | RETURN SEMI;
methodInvoStmt: ((ID | THIS) DOT | ) methodInvocation SEMI;
/* === === === */

type: (INT | FLOAT | BOOLEAN | STRING | ID) arrayDecl | VOID;
arrayDecl: LBRACKET INTEGER_LITERAL RBRACKET | ;

literals: INTEGER_LITERAL | FLOAT_LITERAL | BOOLEAN_LITERAL | STRING_LITERAL | arrayLiteral;

arrayLiteral: floatArray | intArray | boolArray idArray | strArray;
floatArray: LBRACE floatNulist RBRACE;
intArray: LBRACE intNulist RBRACE;
boolArray: LBRACE boolNulist RBRACE;
strArray: LBRACE strNulist RBRACE;
idArray: LBRACE idNulist RBRACE;

floatNulist: floatPrime | ;
intNulist: intPrime | ;
boolNulist: boolPrime | ;
strNulist: strPrime | ;
idNulist: idPrime | ;

floatPrime: FLOAT_LITERAL COMMA floatPrime | FLOAT_LITERAL;
intPrime: INTEGER_LITERAL COMMA intPrime | INTEGER_LITERAL;
boolPrime: BOOLEAN_LITERAL COMMA boolPrime | BOOLEAN_LITERAL;
strPrime: STRING_LITERAL COMMA strPrime | STRING_LITERAL;
idPrime: ID COMMA idPrime | ID;


/*
###################
### LEXER RULES ###
###################
 */

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs 
COMMENT_LINE: '#' ~[\r\n]* -> skip; // skip comment line (skip anything till end of line or end of file)
COMMENT_BLOCK: '/*' .*? '*/' -> skip; // skip comment block (a comment block must be closed)

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
fragment TRUE: 'true';
fragment FALSE: 'false';
VOID: 'void';
NIL: 'nil';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';
TO: 'to';
DOWNTO: 'downto';

// IDENTIFIER
/* rule which can be read as KEYWORDS must be at below KEYWORDS */
ID: [a-zA-Z_][a-zA-Z0-9_]*;

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
MEMBER_ASSIGN: '=';

// Logical Operators
LOGICAL_OR: '||';
LOGICAL_AND: '&&';
NOT: '!';

// String Operators
STR_CONCAT: '^'; // String concatenation

// SEPARATORS
LBRACKET: '[';
RBRACKET: ']';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
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

// ERRORS
ILLEGAL_ESCAPE: '"' ~[\n\r"]*? ('\\' ~[btnfr"'\\]) { self.text = self.text[1:] };
UNCLOSE_STRING: '"' ~[\n\r"]*? (EOF | '\n' | '\r') { self.text = self.text[1:] };
ERROR_CHAR: .;
