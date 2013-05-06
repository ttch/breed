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

# author by zhao_nf ( ttchgm@gmail.com)
# lex for java v0.0.1

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
#	'operator'				:'OPERATOR',
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
	'LONG_NUMBER' , 'LONG_HEX_NUMBER',
	'NON_INTEGER_1' , 'NON_INTEGER_2','NON_INTEGER_4','NON_INTEGER_3','NON_INTEGER_5','NON_INTEGER_6',

	'MCOMMENT','LCOMMENT',
	'Identifier',
	'OP_NE','OP_EQ', 'OP_LE', 'OP_GE', 
	'OP_LOR', 'OP_LAND', 'OP_INC', 'OP_DEC',
	'OP_SHL','OP_ARRAY',
	 'OP_SHRR' , 'OP_SHR',
	'ASS',
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

	'CharacterLiteral','StringLiteral'

	#'NUMBER','HEX_NUMBER',


]+ keywords.values()

t_ASS		=	r'='
t_OP_LE		=	r'<='
t_OP_GE		=	r'>='
t_OP_NE		= 	r'\!='
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

t_PLUS	= r'\+'
t_OP_EQ  = r'=='
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
t_VERTICAL = r'\|'
t_CARET = r'\^'
t_PERCENT = r'\%'
t_EXCLAMATION = r'!'

t_ignore = ' \t\r'

def t_MCOMMENT( t ):
	r'/\*(.|\n)*?\*/'
	t.lexer.lineno += t.value.count("\n")			
	pass

def t_LCOMMENT( t ):
	r'[\/][\/].*'
	pass

#def t_NUMBER(t):
#	r'([0123456789])+'
#	return t


def t_CharacterLiteral(t):
	r'(L)?\'([^\\\n]|(\\.))*?\''
	return t

def t_StringLiteral(t):
	r'\"([^\\\n]|(\\.))*?\"'
	return t

#def t_HEX_NUMBER(t):
#	r'[0][x|X][0-9a-fA-F]+'
#	return t

def t_LONG_NUMBER(t):
	r'([0123456789])+[l|L]'
	return t

def t_LONG_HEX_NUMBER(t):
	r'[0][x|X][0-9a-fA-F]+[l|L]'
	return t

def t_Identifier(t):
	r'[A-Za-z_][\w_]*'
	t.type = keywords.get(t.value,'Identifier')
	return t

def t_NON_INTEGER_1(t):
	r'[0-9]+[.][0-9]+[e|E|d|D]?[\+|\-]?[0-9]*'
	return t

def t_NON_INTEGER_2(t):
	r'[.][0-9]+[e|E]?[\+|\-]?[0-9]*'
	return t


def t_NON_INTEGER_4(t):
	r'[0-9]+[x][f]'
	return t

def t_NON_INTEGER_5(t):
	r'[0-9]+[d|D]'
	return t
def t_NON_INTEGER_6(t):
	r'[0-9]+[.][0-9]+[d|D]'
	return t

def t_NON_INTEGER_3(t):
	r'[0-9]+'
	return t




def t_NEWLINE(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")


def t_error(t):
	print "Illegal character", repr(t.value[0]),t.lineno
	t.lexer.skip(1)
	print t

def getlex():
	return lex.lex()

def input(lx,s):
	lx.input(s)
	return lx

