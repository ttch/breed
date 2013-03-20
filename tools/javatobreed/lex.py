# *.* coding=utf-8 *.*
# author by zhao_nf
# lex for java



from ply import *

keywords = {
	'double'				:'DOUBLE',
	'import'				:'IMPORT',
	'private'				:'PRIVATE',
	'throws'				:'THROWS',
	'throw'					:'THROW',
	'break'					:'BREAK',
	'else'					:'ELSE',
	'inner'					:'INNER',
	'protected'				:'PROTECTED',
	'transient'				:'TRANSIENT',
	'byte'					:'BYTE',
	'extends'				:'EXTENDS',
	'instanceof'			:'INSTANCEOF',
	'public'				:'PUBLIC',
	'try'					:'TRY',
	'case'					:'CASE',
	'final'					:'FINAL',
	'int'					:'INT',
	'rest'					:'REST',
	'var'					:'VAR',
	'cast'					:'CAST',
	'finally'				:'FINALLY',
	'interface'				:'INTERFACE',
	'return'				:'RETURN',
	'void'					:'VOID',
	'catch'					:'CATCH',
	'float'					:'FLOAT',
	'long'					:'LONG',
	'short'					:'SHORT',
	'volatile'				:'VOLATILE',
	'char'					:'CHAR',
	'for'					:'FOR',
	'native'				:'NATIVE',
	'static'				:'STATIC',
	'while'					:'WHILE',
	'class'					:'CLASS',
	'future'				:'FUTURE',
	'new'					:'NEW',
	'super'					:'SUPER',
	'const'					:'CONST',
	'generic'				:'GENERIC',
	'null'					:'NULL',
	'switch'				:'SWITCH',
	'continue'				:'CONTINUE',
	'goto'					:'GOTO',
	'operator'				:'OPERATOR',
	'synchronized'			:'SYNCHRONIZED',
	'default'				:'DEFAULT',
	'if'					:'IF',
	'outer'					:'OUTER',
	'this'					:'THIS',
	'package'				:'PACKAGE',
	'abstract'				:'ABSTRACT',
	'boolean'				:'BOOLEAN',
	'implements'			:'IMPLEMENTS',
	'do'					:'DO',
	'enum'					:'ENUM',
	'strictfp'				:'STRICTFP',
	'assert'				:'ASSERT',
	'true'					:'TRUE',
	'false'					:'FALSE'
}


tokens = [
	'MCOMMENT','LCOMMENT',
	'IDENTIFIER',
	'OP_EQ', 'OP_LE', 'OP_GE', 'OP_NE', 
	'OP_LOR', 'OP_LAND', 'OP_INC', 'OP_DEC',
	'OP_SHR', 'OP_SHL', 'OP_SHRR','OP_ARRAY',
	
	'ASS_ADD',
	'ASS_SUB', 'ASS_MUL', 'ASS_DIV', 'ASS_AND',
	'ASS_OR', 'ASS_XOR', 'ASS_MOD', 'ASS_SHL',
	'ASS_SHR', 'ASS_SHRR', 'NEWLINE',

	'PLUS','EQUALS','LPAREN','RPAREN',
	'BLPAREN','BRPAREN','DOT','SEMI',
	'FLPAREN','FRPAREN','COLON','COMMA',
	'QUES','TILDE','AT','LESS','MORE',
	'MULT','DASH','AND','SLASH','EXCLAMATION',
	'VERTICAL','CARET','PERCENT',

	'CHARLITERAL','STRINGLITERAL',

	'NUMBER','HEX_NUMBER',
	'LONG_NUMBER' , 'LONG_HEX_NUMBER',
	'NON_INTEGER_1' , 'NON_INTEGER_2' , 'NON_INTEGER_3'

]+ keywords.values()


t_PLUS	= r'\+'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_BLPAREN = r'\{'
t_BRPAREN = r'\}'
t_DOT	 = r'\.'
t_SEMI	= r';'
t_FLPAREN = r'\['
t_FRPAREN = r'\]'
t_COLON = r'\:'
t_COMMA = r'\,'
t_QUES  = r'\?'
t_TILDE = r'\~'
t_AT = r'@'
t_LESS = r'<'
t_MORE = r'>'
t_MULT = r'\*'
t_DASH = r'\-'
t_AND = r'\&'
t_SLASH = r'\/'
t_EXCLAMATION = r'\!'
t_VERTICAL = r'\|'
t_CARET = r'\^'
t_PERCENT = r'\%'


t_ignore = ' \t\r'

def t_MCOMMENT( t ):
	r'/\*(.|\n)*?\*/'
	pass

def t_LCOMMENT( t ):
	r'[\/][\/].*'
	pass

def t_NUMBER(t):
	r'([0123456789])+'
	return t


def t_CHARLITERAL(t):
	r'(L)?\'([^\\\n]|(\\.))*?\''
	return t

def t_STRINGLITERAL(t):
	r'\"([^\\\n]|(\\.))*?\"'
	return t

def t_HEX_NUMBER(t):
	r'[0][x|X][0-9a-fA-F]+'
	return t

def t_LONG_NUMBER(t):
	r'([0123456789])+[l|L]'
	return t

def t_LONG_HEX_NUMBER(t):
	r'[0][x|X][0-9a-fA-F]+[l|L]'
	return t

def t_IDENTIFIER(t):
	r'[A-Za-z_][\w_]*'
	#t.type = keywords.get(t.value,'ID')
	return t

def t_NON_INTEGER_1(t):
	r'[0-9]+[.][0-9]+[e|E]?[\+|\-]?[0-9]*'
	return t

def t_NON_INTEGER_2(t):
	r'[.][0-9]+[e|E]?[\+|\-]?[0-9]*'
	return t

def t_NON_INTEGER_3(t):
	r'[0-9]+'
	return t

t_OP_EQ		=	r'=='
t_OP_LE		=	r'<='
t_OP_GE		=	r'>='
t_OP_NE		= 	r'!='
t_OP_LOR	=	r'\|\|'
t_OP_LAND	=	r'\&\&'
t_OP_INC	=	r'\+\+'
t_OP_DEC	=	r'--'
t_OP_SHR	=	r'>>'
t_OP_SHL	=	r'<<'
t_OP_SHRR	=	r'\>\>\>'
t_OP_ARRAY  =   r'\.\.\.'

t_ASS_ADD	=	r'\+='
t_ASS_SUB	=	r'-='
t_ASS_MUL	=	r'\*\='
t_ASS_DIV	=	r'/='
t_ASS_AND		=	r"&="
t_ASS_OR		=	r"\|\="
t_ASS_XOR		=	r"^="
t_ASS_MOD		=	r"%="
t_ASS_SHL		=	r"\<\<\="
t_ASS_SHR		=	r"\>\>\="
t_ASS_SHRR		=	r"\>\>\>\="





def t_NEWLINE(t):
	r'\n+'
	t.lexer.lineno += 1
	return t


def t_error(t):
	print "Illegal character", repr(t.value[0]),t.lineno
	t.lexer.skip(1)
	print t

def getlex():
	return lex.lex()

def input(lx,s):
	lx.input(s)
	return lx

