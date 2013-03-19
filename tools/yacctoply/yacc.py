# *.* coding=utf-8 *.*

import ply.yacc as yacc
import lex
from collections import deque

tokens = lex.tokens

rules_list = deque()

rule_stack = deque()

rule = deque()
def p_program( p ):
	'''
		program : token_statments start_statment rule_statments end_statment
	'''
	pass

def p_token_statments( p ):
	'''
		token_statments : token_statment
				| token_statments token_statment
	'''
	pass

def p_token_statment( p ):
	'''
		token_statment : TOKEN_ID token_list
	'''
	pass

def p_token_list( p ):
	'''
		token_list : ID
					| token_list ID
	'''
	pass

def p_start_statment( p ):
	'''
		start_statment : YACC_START ID BLOCK
	'''
	pass

def p_end_statment( p ):
	'''
		end_statment : BLOCK
	'''
	pass

def p_rule_statments( p ):
	'''
		rule_statments : rule_statment
					| rule_statments rule_statment
	'''
	rules_list.append( deque( rule_stack ))
	rule_stack.clear()
	pass

def p_rule_statment( p ):
	'''
		rule_statment : ID COLON rules SEMI

	'''
	rule_stack.append(p[2])
	rule_stack.append(p[1])
	pass

def p_rules( p ):
	'''
		rules : rule
			| rules VERTICAL rule
	'''
	rule_stack.append( deque(rule) )
	rule.clear()
	pass

def p_rule( p ):
	'''
		rule : rule_token
			| rule rule_token
			| rule LPAREN rule_token RPAREN
	'''
	pass

def p_rule_token( p ):
	'''
		rule_token : ID
					| rule_symbol
	'''
	if p[1] != None :
		rule.append(p[1])
	pass

def p_rule_symbol( p ):
	'''
		rule_symbol :  APOSTROPHE rule_spe_symbol APOSTROPHE
	'''
	rule.append(p[2])

def p_rule_spe_symbol( p ):
	'''
		rule_spe_symbol : VERTICAL
						| PLUS
						| EQUALS
						| LPAREN
						| RPAREN
						| BLPAREN
						| BRPAREN
						| DOT
						| SEMI
						| FLPAREN
						| FRPAREN
						| COLON
						| COMMA
						| QUES
						| TILDE
						| AT
						| LESS
						| MORE
						| MULT
						| DASH
						| EXCLAMATION
						| SLASH
						| PERCENT
						| AND
						| CARET
						| ID
	'''
	p[0] = p[1]

#### Empty
   
def p_empty( p ):
    '''empty : '''

#### Catastrophic error handler

def p_error(p):
	if p:
		print "Syntax error at '%s' lineno = %i linepos=%i" %  ( p.value , p.lineno , p.lexpos )
	else:
		print "Syntax error at EOF"

def split_lower(p):
	import re
	if len(p) == 1 : return lex.tokenNameList[p]
	if len( re.findall('[A-Z_]' , p ) ) == len( p ):
		return p
	else:
		return ( "_".join(re.findall('[A-Z][a-z]+',p)) ).lower()

def get_yacc(l):
	b = yacc.yacc()

	b.error = 0
	result = b.parse(lexer = l , debug=1)

	for x in rules_list:
		z = x.pop()
		print "def p_%s( p ):" % ( split_lower(z) )
		print "	''' "
		x.pop()
		d = x.pop()
		if isinstance( d,deque):
			s = ""
			for q in d:
				s = s + " " + split_lower( q )
			print "	%s : %s " % ( split_lower( z ) , s )
		else:
			print " %s : %s " % ( split_lower ( z ) , split_lower( d ) )

		l = len(x)
		i = 0
		while i < l:
			z = x.pop()
			if isinstance(z , deque ) :
				s = ""
				for q in z :
					s = s + " " + split_lower( q )
				print "	|%s " % ( s)
			else:
				print " |%s " %s ( split_lower ( z ) ) 
			i += 1
		print "	'''\n	pass"
		print ""
	if b.error : return None



