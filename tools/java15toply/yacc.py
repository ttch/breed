# *.* coding=utf-8 *.*

import ply.yacc as yacc
import lex
from collections import deque

tokens = lex.tokens

rules = deque()
rule = deque()

extends = deque()
keys = []

expt_extends = deque()
expt_keys = []
Number = -1
expt_number = -1

class expr:
	def __init__(self,t):
		self.t = t
	def __str__(self):
		return "expr:%s" % (str(self.t))
	def __repr__(self):
		return "expr:%s" % (str(self.t))
	def __radd__(self, other):
		return other + self.t
	def add_extends( self, key ,new_expr ):
		global Number
		if key not in keys:
			extends.append(new_expr)
			keys.append(key)
			return True
		else:
			Number = Number-1
			return "expr_%d" % (keys.index(key))
	def add_expt( self, key ,new_expr ):
		global expt_number
		if key not in expt_keys:
			expt_extends.append(new_expr)
			expt_keys.append(key)
			return True
		else:
			print expt_number
			expt_number = expt_number-1
			return "expt_%d" % (expt_keys.index(key))
	def process_plus(self):
		if self.t[0] == '(' and self.t[-2] == ')' and self.t[-1] == '+':
			new_label = inc_number()
			new_expr =  [ new_label , ':'] + self.t[1:-2 ] + \
						[ '|' , new_label ] + self.t[1:-2 ]
			key = self.add_extends( self.t[1:-2] , new_expr )
			if key == True:
				self.t = [ new_label ]
			else:
				self.t = [ key ]
		else:
			pass
		return self
	def process_mult(self):
		if self.t[0] == '(' and self.t[-2] == ')' and self.t[-1] == '*':
			new_label = inc_expt()

			new_expr =  [ new_label , ':'] + self.t[1:-2 ] + \
						[ '|' , new_label ] + self.t[1:-2]

			key = self.add_expt( self.t[1:-2] , new_expr )
			if key == True:
				self.t = [ new_label ]
			else:
				self.t = [ key ]
	def process_ques(self):
		if self.t[0] == '(' and self.t[-2] == ')' and self.t[-1] == '?':
			new_label = inc_expt()

			new_expr =  [ new_label , ':'] + self.t[1:-2 ] + \
						[ '|','empty' ]

			key = self.add_expt( self.t[1:-2] , new_expr )

			if key == True:
				self.t = [ new_label ]
			else:
				self.t = [ key ]
	
	def process(self):
		for x in self.t:
			if x == '?':
				return self.process_ques()
			elif x=='+':
				return self.process_plus()
			elif x == '*':
				return self. process_mult()
		return self.t
	def process_sub(self):
		if self.t[0] == '(':

			flag = False
			if self.t[-1] == ')':
				flag = False
			elif self.t[-2] == ')' :
				flag = True
			if flag == True:
				flag = False
				for x in self.t :
					if x == '|': flag = True
				if flag == True:
					new_label = inc_number()
					new_expr = [ new_label , ':' ] + self.t[1:-2]

					key = self.add_extends( self.t[1:-2] , new_expr )
					if key == True:
						self.t = [ new_label ]
					else:
						self.t = [ key ]
			else:
				new_label = inc_number()
				new_expr = [ new_label , ':' ] + self.t[1:-1]

				key = self.add_extends( self.t[1:-1] , new_expr )

				if key == True:
					self.t = [ new_label ]
				else:
					self.t = [ key ]
	def process_no(self):
		for x in self.t:
			if x == '?':
				new_label = inc_expt()
				#print self.t
				new_expr =  [ new_label , ':'] + [ self.t[0] ] + [ '|' , 'empty' ]

				key = self.add_expt( self.t[0] , new_expr )
				if key == True:
					self.t = [ new_label ]
				else:
					self.t = [ key ]
				break
			elif x == '+':
				pass
			elif x == '*':
				print "hello"
				
'''
class rule:
	def __init__(self,t):
		self.t = t
	def __str__(self):
		return "rule:%s" % (str(self.t))
	def __repr__(self):
		return "rule:%s" % (str(self.t))
'''

def p_program( p ):
	'''
		program : grammar_statment options_statment rule_statments 
	'''
	pass

def p_grammar_statment( p ):
	'''
		grammar_statment : GRAMMAR ID SEMI
	'''
	pass

def p_options_statment( p ):
	'''
		options_statment : OPTIONS BLPAREN option_statments BRPAREN
						| empty
	'''
	pass

def p_option_statments( p ):
	'''
		option_statments : option_statment
						| option_statments option_statment
	'''
	pass

def p_option_statment( p ):
	'''
		option_statment : ID EQUALS ID SEMI
	'''
	pass

def p_rule_statments( p ):
	'''
		rule_statments : rule_statment
					| rule_statments rule_statment
	'''
	pass
def p_rule_statment( p ):
	'''
		rule_statment : ID COLON rules SEMI

	'''
	rule.appendleft(p[2])
	rule.appendleft(p[1])
	rules.append(deque(rule))
	rule.clear()
	pass


def p_rules( p ):
	'''
		rules : rule
			| rules rule
	'''
	if len(p) == 2:
		rule.appendleft(p[1])
	if p[0] == None : p[0] = []
	
	p[0] = p[0] + p[1]

def p_rule( p ):
	'''
		rule : expr
			| rule expr
			| rule VERTICAL expr
			| empty
	'''
	if p[0] == None : p[0] = []
	if len(p) == 2:
		p[0] = p[0] + p[1]
	if len(p) == 3:
		p[0] =  p[1] + p[2]
	if len(p) == 4:
		p[0] = p[1] +  [ p[2] ] + p[3]

def p_expr( p ):
	'''
		expr : ptoken
			| s_expr
	'''
	if p[0] == None: p[0] = []
	p[0] = p[0] + p[1]

def p_sub_expr( p ):
	'''
		sub_expr :  LPAREN rule RPAREN
			| LPAREN rule RPAREN operator
	'''
	if len(p) == 4:
		if p[2] !=None:
			p[0] = expr( [ p[1] ] + p[2] +[ p[3] ]  )
			p[0].process_sub()
	if len(p) == 5:
		if p[2] != None:
			p[0] = expr( [ p[1] ] + p[2] + [ p[3] ] + p[4] )
			p[0].process_sub()
			p[0].process()

def p_s_expr( p ):
	'''
		s_expr :
				| expr operator
				| expr
				| LPAREN RPAREN
				| expr sub_expr
				| sub_expr
	'''
	if len(p) == 3:
		if p[1] != None and p[1] != '(':

			if p[0] == None : p[0] = []
			p[0] = expr(  p[0] + p[1] + p[2] )

			#operator
			print p[2]
			if p[2] in [["?"],["+"],["*"]] :
				p[0].process_no()

	if len(p) == 2:
		if p[1] != None:
			if p[0] == None: p[0] = []
			p[0] = p[0] + p[1]

def p_operator( p ):
	'''
		operator : PLUS
				| MULT
				| QUES
	'''
	p[0] = [ p[1] ]

def p_ptoken( p ):
	'''
		ptoken : ID
				| SPE_TOKEN
	'''
	p[0] = [ get_ID(p[1]) ]


#### Empty

def p_empty( p ):
    '''empty : '''

#### Catastrophic error handler

def p_error(p):
	if p:
		print "Syntax error at '%s' lineno = %i linepos=%i" %  ( p.value , p.lineno , p.lexpos )
	else:
		print "Syntax error at EOF"


def get_ID(p):
	if p == None:return p
	if p[0] == "'" and p[-1] == "'":
		if lex.tokenNameList.has_key(p[1:-1]):
			return lex.tokenNameList[p[1:-1]]
		if lex.key_list.has_key(p[1:-1]):
			return lex.key_list[p[1:-1]]
	return p


def split_lower(p):
	import re
	if len(p) == 1 : return lex.tokenNameList[p]
	if len( re.findall('[A-Z_]' , p ) ) == len( p ):
		return p
	else:
		return ( "_".join(re.findall('[A-Z][a-z]+',p)) ).lower()

def inc_number():
	global Number
	Number = Number+1
	return 'expr_%d' % (Number)

def inc_expt():
	global expt_number
	expt_number = expt_number+1
	return 'expt_%d' % (expt_number)

def print_p(sf,name,body,mate=None):
		sf.write( '# %s ' % mate)
		sf.write( '\ndef p_%s(p):' % name )
		sf.write( "\n\t'''\n")
		sf.write( "\t %s : %s" % (name , body) )
		sf.write( "\n\t'''\n")
		sf.write( "\n\tpass\n")
		sf.write( "\n")

class Node:
	def __init__(self,Item):
		self.rItem = Item
		self.parent = None
		if Item[0:4] != 'expt':
			self.item = Item
		else:
			self.item = (Item,'empty')
#	def __str__(self):
#		return str(self.rItem)
#	def __repr__(self):
#		return str(self.rItem)
	def __radd__(self, other):
		return other + self.rItem
	def __len__(self):
		if self.is_str() :
			return 1
		else:
			return len(self.item)
	def is_str(self):
		if ( isinstance(self.item , (str, unicode)) or isinstance(self.item,(str))):
			return True
		else:
			return False

		

def process_tree(l):
	#print l
	s = "<?>".join(l)
	x = s.split("|")
	result = []
	for o in x:
		l = deque( [ Node(z) for z in o.split("<?>") if z !=''] )
		h = len(l)
		d = deque()
		for z in l:
			if len(z) == 1:
				if len(d) == 0: d.append( deque([]) )
				for y in d:
					y.append(z.item)
			else:
				if len(d) == 0: d.append( deque([]) )
				f = deque()
				for y in d:
					o1 = deque(y)
					o1.append(z.item[0])
					o2 = deque(y)
					o2.append(z.item[1])
					f.append(deque(o1))
					f.append(deque(o2))
				d = f
		result.append(d)
	return result

def get_yacc(l):
	b = yacc.yacc()

	b.error = 0
	result = b.parse(lexer = l , debug=1)
	#"""
	sf = open("../javatobreed/yacc.py","w")
	sf.write("# *.* coding=utf-8 *.*\n")
	sf.write("""
import ply.yacc as yacc
import lex
from collections import deque

tokens = lex.tokens
""")
	for x in  rules:
		if x[0] == 'integerLiteral': continue
		body = ""
		flag = False
		for y in x[2]:
			if y[0:4] == 'expt':
				flag = True
				break
		if flag == True:
			d = process_tree(x[2])
			#print d
			for z in d:
				if body == "":
					body = "\n\t\t| ".join( [" ".join(o) for o in z ] )
				else:
					body = "\n\t\t| ".join( [" ".join(o) for o in z ] )+"\n\t\t| "+body
		else:
			for y in x[2]:
				if y == "|":
					body = body + " " +  ( "\n\t" + y )
				else:
					body = body + " "+ y
		print_p(sf, x[0], body,x)
	for x in extends:
		body = ""
		for y in x[2:]:
			if y == "|":
				body = body + " " + ( "\n\t" + y )
			else:
				body = body + " "+ y
		print_p(sf, x[0], body)

	for x in expt_extends:
		body = ""
		for y in x[2:]:
			if y == "|":
				body = body + " " + ( "\n\t" + y )
			else:
				body = body + " "+ y
		print_p(sf, x[0], body)
	sf.write("""

def p_FloatingPointLiteral( p ):
	'''
		FloatingPointLiteral : NON_INTEGER_1
					| NON_INTEGER_2
					| NON_INTEGER_3
	'''
	pass

def p_integerLiteral(p):
	'''
		integerLiteral : NUMBER 
					| HEX_NUMBER
					| LONG_NUMBER
					| LONG_HEX_NUMBER
	'''
	pass


	#### Empty
   
def p_empty( p ):
	'''empty : '''

#### Catastrophic error handler

def p_error(p):
	if p:
		print "Syntax error at '%s' lineno = %i linepos=%i" %  ( p.value , p.lineno , p.lexpos )
	else:
		print "Syntax error at EOF"

def get_yacc(l):
	b = yacc.yacc()

	b.error = 0
	result = b.parse(lexer = l , debug=2)
	if b.error : return None
	""")
	sf.close()
	#"""
	if b.error : return None



