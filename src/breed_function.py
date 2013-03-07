# *.* coding=utf-8 *.*


import function_
from g.gy import *
from collections import deque

"""
functions_expersion_list : 
	@function stat @end
	| @function @end
	;
"""

def p_at_function(stat):
	alist = deque()
	while True :
		token = poptoaddbyleft(stat,alist)
		if token.type == "AT":	
			token = poptoaddbyleft( stat , alist )
			if token.type == "FUNCTION":
				while True:
					token = poptoaddbyleft(stat,alist)
					if token == None:
						"exception to yacc error"
						return None
					if token.type == "END":
						return alist

def p_statment(stat):
	pass

def p_arg_list(stat):
	pass

"""
	yacc
	function
		:
		ID LPAREN para_list RPAREN BLPAREN STAT BRPAREN 
		| ID LPAREN RPAREN BLPAREN STAT BRPAREN
		| ID LPAREN para_list PRAREN SEMI
		| ID LPAREN RPAREN SEMI
		;
"""
def p_function(fn,stat):
	# delete @ function | @ end
	stat.pop();stat.pop();stat.popleft();stat.popleft()


	while True:
		if len(stat) == 0 : break
		token = stat.pop()
		if token.type == "COMMENT":
			continue
		if token.type == "FUNCTION":
			if token.type == "ID":
				fn.set_name = token.value
			else :
				"exception to yacc error"
				return
			token = stat.pop()
			if token.type == "LPAREN":
				arg = p_arg_list(stat)
			else:
				"exception "
				return
			token = stat.pop()
			if token.type == "BLPAREN":
				p_statment(stat)
			else:
				"exception"
				return
			token = stat.pop()
			if token.type == "BRPAREN":
				return
			else:
				"exception"
				return


		print token

	return None


def compile( name, stat ):
	cp = deque()
	cp = p_at_function(stat)
	
	fn = function_.function()
	p_function(fn,cp)

	pass
