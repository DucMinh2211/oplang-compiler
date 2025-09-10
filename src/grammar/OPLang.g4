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

program: class_decl_list EOF; // write for program rule here using vardecl and funcdecl

/* === CLASS DECLARATION === */
class_decl_list: class_decl class_decl_list | class_decl;
class_decl: CLASS ID class_extends LBRACE member_nulist RBRACE;

class_extends: EXTENDS ID | ;
member_nulist: member member_nulist | ;
member: is_static attribute_decl | method_decl;
is_static: STATIC | ;
/* === === === */

/* === ATTRIBUTE DECLARATION === */
attribute_decl: is_final type attribute_name_list SEMI;
attribute_name_list: attribute_name COMMA attribute_name_list | attribute_name;

is_final: FINAL | ;
attribute_name: ID MEMBER_ASSIGN value | ID;
/* === === === */

/* === METHOD DECLARATION === */
method_decl: type is_ref ID LPAREN param_nulist RPAREN block_statement;

param_nulist: param_prime | ;
param_prime: param SEMI param_prime | ;
param: type is_ref id_list;
id_list: ID COMMA id_list | ID;

is_ref: AMPERSAND | ;
/* === === === */

/* === CONSTRUCTOR DECLARATION === */
def_constructor: ID LPAREN RPAREN block_statement;
copy_constructor: ID LPAREN ID 'other' RPAREN block_statement;
custom_constructor: ID LPAREN param_nulist RPAREN block_statement;

destructor: TILDE ID LPAREN RPAREN block_statement;
/* === === === */

/* === EXPRESSION === */
expr0: expr1 CMP_WITH_OP expr1 | expr1;
CMP_WITH_OP:  LESS_THAN | GREATER_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL;

expr1: expr2 CMP_OP expr2 | expr2;
CMP_OP: EQUAL | NOT_EQUAL;

expr2: expr2 AND_OR_OP expr3 | expr3;
AND_OR_OP: LOGICAL_AND | LOGICAL_OR;

expr3: expr3 ADD_SUB_BINOP expr4 | expr4;
ADD_SUB_BINOP: PLUS | MINUS;

expr4: expr4 MUL_DIV_MOD_OP expr5 | expr5;
MUL_DIV_MOD_OP: MULTIPLY | FLOAT_DIVISION | INTEGER_DIVISION | MODULO;

expr5: expr5 STR_CONCAT_OP expr6 | expr6;
STR_CONCAT_OP: STR_CONCAT;

expr6: NOT expr6 | expr7;

expr7: ADD_SUB_UNOP expr7 | expr8;
ADD_SUB_UNOP: PLUS | MINUS;

expr8: expr8 array_access | expr9;
array_access: LBRACKET expr0 RBRACKET;

expr9: expr9 DOT (method_invocation | ID) | fact;

fact: literals
    | ID
    | THIS
    | NIL
    | method_invocation
    | obj_creation
    | THIS
    | LPAREN expr0 RPAREN
    ;

obj_creation: NEW ID LPAREN expr_nulist RPAREN;
expr_nulist: expr_prime | ;
expr_prime: expr0 COMMA expr_prime | expr0;

method_invocation: (ID | THIS) LPAREN expr_nulist RPAREN;
/* === === === */

/* === BLOCK STATEMENT === */
block_statement: LBRACE var_decl_nulist stmt_nulist RBRACE;

stmt_nulist: stmt stmt_nulist | ;
var_decl_nulist: var_decl var_decl_nulist | ;

var_decl: is_final type id_list SEMI;

stmt: assign_stmt
    | if_stmt
    | for_stmt
    | break_stmt
    | continue_stmt
    | return_stmt
    | method_invocation SEMI
    | block_statement
    ;

assign_stmt: lhs ASSIGN expr0 SEMI;
lhs: ID | ID array_access;

if_stmt: IF expr0 THEN stmt (ELSE stmt | );

for_stmt: FOR ID /*(scalar var)*/ ASSIGN expr0 LPAREN (TO | DOWNTO) expr0 RPAREN DO stmt;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

return_stmt: RETURN expr0 SEMI | RETURN SEMI;
/* === === === */

type: literals | ID | VOID;

literals: INTEGER_LITERAL | FLOAT_LITERAL | BOOLEAN_LITERAL | STRING_LITERAL;


/*
###################
### LEXER RULES ###
###################
 */

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
array_literal: LBRACE (value (COMMA value)*)? RBRACE;
value: INTEGER_LITERAL | FLOAT_LITERAL | BOOLEAN_LITERAL | STRING_LITERAL;

// ERRORS
ILLEGAL_ESCAPE: '"' ~[\n\r"]*? ('\\' ~[btnfr"'\\]) { self.text = self.text[1:] };
UNCLOSE_STRING: '"' ~[\n\r"]*? (EOF | '\n' | '\r') { self.text = self.text[1:] };
ERROR_CHAR: .;
