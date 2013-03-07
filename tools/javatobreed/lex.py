# *.* coding=utf-8 *.*
# author by zhao_nf
# lex for java



from ply import *

keywords = {
	'double'				:' DOUBLE',
	'import'				:' IMPORT',
	'private'				:' PRIVATE',
	'throws'				:' THROWS',
	'break'					:' BREAK',
	'else'					:' ELSE',
	'inner'					:' INNER',
	'protected'				:' PROTECTED',
	'transient'				:' TRANSIENT',
	'byte'					:' BYTE',
	'extends'				:' EXTENDS',
	'instanceof'			:' INSTANCEOF',
	'public'				:' PUBLIC',
	'try'					:' TRY',
	'case'					:' CASE',
	'final'					:' FINAL',
	'int'					:' INT',
	'rest'					:' REST',
	'var'					:' VAR',
	'cast'					:' CAST',
	'finally'				:' FINALLY',
	'interface'				:' INTERFACE',
	'return'				:' RETURN',
	'void'					:' VOID',
	'catch'					:' CATCH',
	'float'					:' FLOAT',
	'long'					:' LONG',
	'short'					:' SHORT',
	'volatile'				:' VOLATILE',
	'char'					:' CHAR',
	'for'					:' FOR',
	'native'				:' NATIVE',
	'static'				:' STATIC',
	'while'					:' WHILE',
	'class'					:' CLASS',
	'future'				:' FUTURE',
	'new'					:' NEW',
	'super'					:' SUPER',
	'const'					:' CONST',
	'generic'				:' GENERIC',
	'null'					:' NULL',
	'switch'				:' SWITCH',
	'continue'				:' CONTINUE',
	'goto'					:' GOTO',
	'operator'				:' OPERATOR',
	'synchronized'			:' SYNCHRONIZED',
	'default'				:' DEFAULT',
	'if'					:' IF',
	'outer'					:' OUTER',
	'this'					:' THIS'
}


tokens = [


]+ keywords.values()

t_ignore = ' \t\n\r\b\f':
	pass

def t_comment1( t ):
	r'/\*(.|\n)*?\*/'
	pass

def t_comment2( t ):
	r'[\/][\/].*'
	pass

def t_NUMBER(t):
	r'([0123456789])+'
	return t
def t_HEX_NUMBER(t):
	r'[0]([x]|[X])1([0123456789])+'
	return t

def t_literal ( t ):


def t_ID(t):
	r'[A-Za-z_][\w_]*'
	t.type = keywords.get(t.value,'ID')
	return t


t_OP_EQ		=	r'=='
t_OP_LE		=	r'<='
t_OP_GE		=	r'>='
t_OP_NE		= 	r'!='
t_OP_LOR	=	r'||'
t_OP_LAND	=	r'&&'
t_OP_INC	=	r'++'
t_OP_DEC	=	r'--'
t_OP_SHR	=	r'>>'
t_OP_SHL	=	r'<<'
t_OP_SHRR	=	r'>>>'

t_ASS_ADD	=	r'+='
t_ASS_SUB	=	r'-='
t_ASS_MUL	=	r'*='
t_ASS_DIV	=	r'/='
t_ASS_AND		=	r"&="
t_ASS_OR		=	r"|="
t_ASS_XOR		=	r"^="
t_ASS_MOD		=	r"%="
t_ASS_SHL		=	r"<<="
t_ASS_SHR		=	r">>="
t_ASS_SHRR	=	r">>>="





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

