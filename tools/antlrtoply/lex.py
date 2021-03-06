# *.* coding=utf-8 *.*

#[The "BSD licence"]
# Copyright (c) 2012- zhao_nf
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. The name of the author may not be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# convert antlr 3 to ply tools v0.0.1
# author by zhao_nf( ttchgm@gmail.com)


from ply import *

keywords = {
	'grammar' : 'GRAMMAR',
	'options' : 'OPTIONS'
}


tokens = [
	'MCOMMENT','CMCOMENT','LCOMMENT','NMBER','ID','NEWLINE','TOKEN_ID','YACC_START','BLOCK','TEST_TOKEN','SPE_TOKEN',
	'PLUS','EQUALS','LPAREN','RPAREN',
	'BLPAREN','BRPAREN','DOT','SEMI',
	'FLPAREN','FRPAREN','COLON','COMMA',
	'QUES','TILDE','AT','LESS','MORE',
	'MULT','VERTICAL','EXCLAMATION','DASH',
	'SLASH','PERCENT','AND','CARET'
]+ keywords.values()


key_list = {
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
	"&lt;" : "LESS",
	">" : "MORE",
	"&gt;" : "MORE",
	"*" : "MULT",
	"'" : "APOSTROPHE",
	"!" : "EXCLAMATION",
	"-" : "DASH",
	"/" : "SLASH",
	"%" : "PERCENT",
	"&" : "AND",
	"&amp;" : "AND",
	"^" : "CARET",
	"||" : "OP_LOR",
	"+=" : "ASS_ADD",
	"-=" : "ASS_SUB",
	"*=" : "ASS_MUL",
	"/=" : "ASS_DIV",
	"&amp;=" : "ASS_AND",
	"|=" : "ASS_OR",
	"^=" : "ASS_XOR",
	"%=" : "ASS_MOD",
	"++" : "OP_INC",
	"--" : "OP_DEC",
	"&amp;&amp;" : "OP_LAND",
	"&&" : "OP_LAND",
	"==" : "OP_EQ",
	"...": "OP_ARRAY",
	"!=" : "OP_NE",
	">>" : "OP_SHR",
	"<<" : "OP_SHL",
	">>>": "OP_SHRR",
	"<<=": "ASS_SHL",
	">>=": "ASS_SHR",
	">>>=": "ASS_SHRR",
	">=" : "OP_GE",
	"<=" : "OP_LE"
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
t_EXCLAMATION = r'!'
t_DASH = r'-'
t_SLASH = r'/'
t_PERCENT = r'%'
t_AND = '&'
t_CARET = r'\^'



t_ignore = ' \t\r'

def t_SPE_TOKEN( t ):
	r'\'[^\']+\'';
	return t

def t_TEST_TOKEN( t ):
	r'\&[a-z]+;'
	return t

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




