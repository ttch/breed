# *.* coding=utf-8 *.*

# author by zhao_nf
# yacc lex v 0.0.1



from ply import *

keywords = {
}


tokens = [
	'MCOMMENT','CMCOMENT','LCOMMENT','NMBER','ID','NEWLINE','TOKEN_ID','YACC_START','BLOCK',

	'PLUS','EQUALS','LPAREN','RPAREN',
	'BLPAREN','BRPAREN','DOT','SEMI',
	'FLPAREN','FRPAREN','COLON','COMMA',
	'QUES','TILDE','AT','LESS','MORE',
	'MULT','VERTICAL','APOSTROPHE','EXCLAMATION','DASH',
	'SLASH','PERCENT','AND','CARET'
]+ keywords.values()

tokenNameList = {
	"|" : "VERTICAL",
	"+" : "PLUS",
	"=" : "EQUALS",
	"(" : "LPAREN",
	")" : "RPAREN",
	"{" : "BLPAREN",
	"}" : "BRPAREN",
	"." : "DOT",
	";" : "SEMI",
	"[" : "FLPAREN",
	"]" : "FRPAREN",
	":" : "COLON",
	"," : "COMMA",
	"?" : "QUES",
	"~" : "TILDE",
	"@" : "AT",
	"<" : "LESS",
	">" : "MORE",
	"*" : "MULT",
	"'" : "APOSTROPHE",
	"!" : "EXCLAMATION",
	"-" : "DASH",
	"/" : "SLASH",
	"%" : "PERCENT",
	"&" : "AND",
	"^" : "CARET"
}

t_VERTICAL = r'\|'
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
t_APOSTROPHE = r'\''
t_EXCLAMATION = r'!'
t_DASH = r'-'
t_SLASH = r'/'
t_PERCENT = r'%'
t_AND = '&'
t_CARET = r'\^'

t_ignore = ' \t\r'

def t_BLOCK( t ):
	r'\%\%'
	return t

def t_YACC_START( t ):
	r'\%start'
	return t

def t_TOKEN_ID( t ):
	r'\%token'
	return t

def t_MCOMMENT( t ):
	r'\%\{(.|\n)*?\%\}'
	for x in t.value:
		if x == '\n':
			t.lexer.lineno += 1
	pass

def t_CMCOMMENT( t ):
	r'\/\*(.|\n)*?\*\/'
	for x in t.value:
		if x == '\n':
			t.lexer.lineno += 1
	pass

def t_LCOMMENT( t ):
	r'[\/][\/].*'
	for x in t.value:
		if x == '\n':
			t.lexer.lineno += 1
	pass

def t_NUMBER(t):
	r'([0123456789])+'
	return t
#def t_HEX_NUMBER(t):
#	r'[0]([x]|[X])1([0123456789])+'
#	return t

#def t_literal ( t ):


def t_ID(t):
	r'[A-Za-z_][\w_]*'
	t.type = keywords.get(t.value,'ID')
	return t

def t_NEWLINE(t):
	r'\n+'
	t.lexer.lineno += 1
	pass


def t_error(t):
	print "Illegal character", repr(t.value[0]),t.lineno
	t.lexer.skip(1)
	print t

def getlex():
	return lex.lex()

def input(lx,s):
	lx.input(s)
	return lx




