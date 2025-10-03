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
member: attributeDecl | methodDecl | constructor;

/* === ATTRIBUTE DECLARATION === */
attributeDecl: (STATIC (FINAL)? | FINAL (STATIC)?)? typeRef attributeNameList SEMI;
attributeNameList: attributeName COMMA attributeNameList | attributeName;

isFinal: FINAL | ;
attributeName: ID ASSIGN expr0 | ID;
/* === === === */

/* === METHOD DECLARATION === */
methodDecl: (STATIC)? typeRef ID LPAREN paramNulist RPAREN blockStatement;

paramNulist: paramPrime | ;
paramPrime: param SEMI paramPrime | param;
param: typeRef idList;
idList: ID COMMA idList | ID;

typeRef: type AMPERSAND | type;
/* === === === */

/* === CONSTRUCTOR DECLARATION === */
constructor
    : defConstructor
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
expr0: relationalExpr CMP_WITH_OP relationalExpr | relationalExpr;
CMP_WITH_OP:  LESS_THAN | GREATER_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL;

relationalExpr: logicalExpr CMP_OP logicalExpr | logicalExpr;
CMP_OP: EQUAL | NOT_EQUAL;

logicalExpr: logicalExpr AND_OR_OP addSubExpr | addSubExpr;
AND_OR_OP: LOGICAL_AND | LOGICAL_OR;

addSubExpr: addSubExpr ADD_SUB_OP mulDivModExpr | mulDivModExpr;
ADD_SUB_OP: PLUS | MINUS;

mulDivModExpr: mulDivModExpr MUL_DIV_MOD_OP strConcatExpr | strConcatExpr;
MUL_DIV_MOD_OP: MULTIPLY | FLOAT_DIVISION | INTEGER_DIVISION | MODULO;

strConcatExpr: strConcatExpr STR_CONCAT_OP logicalNotExpr | logicalNotExpr;
STR_CONCAT_OP: STR_CONCAT;

logicalNotExpr: NOT logicalNotExpr | unaryAddSubExpr;

unaryAddSubExpr: ADD_SUB_OP unaryAddSubExpr | arrayAccessExpr;

arrayAccessExpr: arrayAccessExpr arrayAccess | memberAccessExpr;
arrayAccess: LBRACKET expr0 RBRACKET;

memberAccessExpr: memberAccessExpr DOT (methodInvocation | ID) | fact;

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
blockStatement: LBRACE varDeclNulist stmtNulist RBRACE;

varDeclNulist: varDecl varDeclNulist | ;

stmtNulist: stmt stmtNulist | ;

stmt
    : assignStmt
    | ifStmt
    | forStmt
    | breakStmt
    | continueStmt
    | returnStmt
    | methodInvoStmt
    | blockStatement
    ;

varDecl: isFinal typeRef variableNameList SEMI;
variableNameList: variableName COMMA variableNameList | variableName;
variableName: ID ASSIGN expr0 | ID;

assignStmt: lhs ASSIGN expr0 SEMI;
lhs: ID | arrayAccessExpr;

ifStmt: IF expr0 THEN stmt (ELSE stmt | );
forStmt: FOR ID /*(scalar var)*/ ASSIGN expr0 (TO | DOWNTO) expr0 DO stmt;
breakStmt: BREAK SEMI;
continueStmt: CONTINUE SEMI;
returnStmt: RETURN expr0 SEMI;
methodInvoStmt: ((ID | THIS) DOT | ) methodInvocation SEMI;
/* === === === */

type: (INT | FLOAT | BOOLEAN | STRING | ID) arrayDecl | VOID;
arrayDecl: LBRACKET INTEGER_LITERAL RBRACKET | ;

literals: INTEGER_LITERAL | FLOAT_LITERAL | BOOLEAN_LITERAL | STRING_LITERAL | arrayLiteral;

arrayLiteral: floatArray | intArray | boolArray | idArray | strArray;
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

// IDENTIFIER
/* rule which can be read as KEYWORDS must be at below KEYWORDS */
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// ERRORS
ILLEGAL_ESCAPE: '"' ~[\n\r"]*? ('\\' ~[btnfr"'\\]) { self.text = self.text[1:] };
UNCLOSE_STRING: '"' ~[\n\r"]*? (EOF | '\n' | '\r') { self.text = self.text[1:] };
ERROR_CHAR: .;
