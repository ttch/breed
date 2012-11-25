# *-* coding=utf-8 *-*
"""
breed 语言词法分析器


"""

from ply import *

keywords = {
	'component'	:	'COMPONENT',
	
	'import'	:	'IMPORT',

	'extend'	:	'EXTEND',

	'end'		:	'END',

	#function
	'function'	:	'FUNCTION',

	'in'		:	'IN',
	
	'out'		:	'OUT',
	
	'return'	:	'RETURN',

	'in_out'	:	'IN_OUT',

	#define segment 
	'define'	:	'DEFINE',

	#struct
	'struct'	:	'STRUCT'
}


tokens = [
	 'STRING','EQUALS','LPAREN','RPAREN','BLPAREN','BRPAREN','DOT',
	 'SEMI','FLPAREN','FRPAREN','NEWLINE','QUES',
	 'COMMENT','ID','PLUS',
	 #'QUOTES',,#'DQUOTES',
	 'COMMA','COLON','MLINECOMMENT','TILDE','NUMBER','AT'
]+ keywords.values()

t_ignore = ' \t'

def t_COMMENT(t):
	r'\#.*'
	return t
def t_MLINECOMMENT(t):
	r'/\*(.|\n)*?\*/'
	return t
	#t.lexer.lineno += t.value.count('\n')

def t_ID(t):
	r'[A-Za-z_][\w_]*'
	t.type = keywords.get(t.value,'ID')
	# Check for reserved words
	return t
def t_STRING(t):
	r'\'([^\\\n]|(\\.))*?\''
	#r'\'([^\\|\n]|\\.)*\''
	return t
def t_NUMBER(t):
	r'([0123456789])+'
	return t

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

def t_NEWLINE(t):
	r'\n+'
	t.lexer.lineno += 1
	return t


def t_error(t):
	print "Illegal character", repr(t.value[0]),t.lineno
	t.lexer.skip(1)
	print t

lex.lex()
