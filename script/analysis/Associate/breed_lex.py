# *-* coding=utf-8 *-*
"""
breed 语言词法分析器


"""

from ply import *

keywords = {
    #unit keyword define
   'page'    : 'PAGE',
   'component': 'COMPONENT',
   #field keyword define
   'extends' : 'EXTENDS',
   'extend' : 'EXTEND',
   'display' : 'DISPLAY',
   'fields'  : 'FIELDS',
   'field'   : 'FIELD',
   'params'  : 'PARAMS',
   #lib keyword define
   'import'  : 'IMPORT',

   #block keyword define

   #输出描述
   'out' : 'OUT',
   #库包含描述
   'lib' : 'LIB',
   #控件
   'control' :  'CONTROL',
   #表单
   'form' : 'FORM',
   #数据库读取和存储
   'servlet' : 'SERVLET',

   #结束符号
   'end' :  'END',
   #函数
   'function' : 'FUNCTION',
   #变量
   'var'    :    'VAR',
}


tokens = [
     'STRING','EQUALS','LPAREN','RPAREN','BLPAREN','BRPAREN','DOT',
     'SEMI','FLPAREN','FRPAREN','NEWLINE','QUES',
     'COMMENT','ID','PLUS',
     #'QUOTES',,#'DQUOTES',
     'COMMA','COLON','MLINECOMMENT'
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
    t.type = keywords.get(t.value,'ID')    # Check for reserved words
    return t
def t_STRING(t):
    r'\'([^\\\n]|(\\.))*?\''
    #r'\'([^\\|\n]|\\.)*\''
    return t

t_PLUS    = r'\+'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_BLPAREN = r'\{'
t_BRPAREN = r'\}'
t_DOT     = r'\.'
t_SEMI    = r';'
t_FLPAREN = r'\['
t_FRPAREN = r'\]'
t_COLON = r'\:'
t_COMMA = r'\,'
t_QUES  = r'\?'


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += 1
    return t


def t_error(t):
    print "Illegal character", repr(t.value[0]),t.lineno
    t.lexer.skip(1)
    print t

lex.lex()
