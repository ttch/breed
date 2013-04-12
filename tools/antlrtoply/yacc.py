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

import ply.yacc as yacc
import lex
from collections import deque

tokens = lex.tokens

rules = deque()
rule = deque()


class QuesList:
	def __init__(self):
		self.l = {}
		self.v = {}
		self.k = 0
	def isin(self,value):
		for x in self.v:
			if self.v[x] == value:
				return True
		return False
	
	def get_key(self,value):
		for x in self.v:
			if self.v[x] == value:
				return x
		return 'key_error'

	def get_value(self,key):
		return self.l[key]

	def add(self,value):
		if not self.isin(value):
			self.k = self.k + 1
			key =  "ques_%d" % self.k
			self.l[key] = value
			self.v[key] = value
			return key

		else:
			return self.get_key(value)

class MutlList:
	def __init__(self):
		self.l = {}
		self.v = {}
		self.k = 0
	def isin(self,value):
		for x in self.v:
			if self.v[x] == value:
				return True
		return False
	
	def get_key(self,value):
		for x in self.v:
			if self.v[x] == value:
				return x
		return 'key_error'		

	def get_value(self,key):
		return self.l[key]

	def add(self,value):
		if not self.isin(value):
			self.k = self.k + 1
			key =  "expt_%d" % self.k
			new_expr = [ key , ':'] + value + [ '|' , key ] + value
			self.l[key] = new_expr
			self.v[key] = value
			return key

		else:
			return self.get_key(value)
	def echo( self , sf ):
		for x in self.l:
			body = ""
			slist = []
			for item in [item.split("<?>") for item in ("<?>".join(self.l[x][2:]) ).split("|") ]:
				pitem = [ i for i in item if i != '' ]
				slist.append(process_expr(pitem))
			body = "\n\t\t| ".join( [" ".join(o) for o in slist ] )
			print_p(sf, x, body)

class ExprList:
	def __init__(self):
		self.l = {}
		self.v = []
		self.k = 0
	
	def get_value(self,key):
		return self.l[key]

	def add(self,value):
		if value not in self.v:
			self.k = self.k + 1
			key =  "expr_%d" % self.k
			
			l = len(value)
			for i in range(l):
				if value[i] == 'new_label':
					value[i] = key

			self.l[key] = value
			self.v.append(value)
			return key

		else:
			return "expr_%d" % self.k
	def echo( self , sf ):
		for x in self.l:
			body = ""
			for y in self.l[x][2:]:
				if y == "|":
					body = body + " " + ( "\n\t" + y )
				else:
					body = body + " "+ y
			print_p(sf, x, body)

exprlist = ExprList()
queslist = QuesList()
multlist = MutlList()


class Expr:
	def __init__(self,t):
		self.t = t
	def __str__(self):
		return "expr:%s" % (str(self.t))
	def __repr__(self):
		return "expr:%s" % (str(self.t))
	def __radd__(self, other):
		return other + self.t

	def process_plus(self):
		if self.t[0] == '(' and self.t[-2] == ')' and self.t[-1] == '+':

			value =  [ 'new_label' , ':'] + self.t[1:-2 ] + \
						[ '|' , 'new_label' ] + self.t[1:-2 ]
			self.t = [ exprlist.add( value ) ]
		else:
			pass
		return self
	def process_mult(self):
		if self.t[0] == '(' and self.t[-2] == ')' and self.t[-1] == '*':
			self.t = [ multlist.add( self.t[1:-2] ) ]
	
	def process_ques(self):
		if self.t[0] == '(' and self.t[-2] == ')' and self.t[-1] == '?':
			self.t = [ queslist.add( self.t[1:-2] ) ]
	
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
					if self.t[-1] == '?':
						value = [ 'new_label' , ':' ] + self.t[1:-2]
						self.t = [ exprlist.add( value ) , '?' ]
						self.t = [  queslist.add( [ self.t[0] ] ) ]
					else:
						value = [ 'new_label' , ':' ] + self.t[1:-1]
						self.t = [ exprlist.add( value ) ]
				else:
					for x in self.t:
						if x == '?':
							return self.process_ques()
						elif x=='+':
							return self.process_plus()
						elif x == '*':
							return self. process_mult()
					return self.t
			else:
				value = [ 'new_label' , ':' ] + self.t[1:-1]
				self.t = [ exprlist.add( value ) ]

	def process_no(self):
		for x in self.t:
			if x == '?':
				self.t = [ queslist.add( self.t[0:-1] ) ]
				break
			elif x == '+':
				pass
			elif x == '*':
				pass

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
			p[0] = Expr( [ p[1] ] + p[2] +[ p[3] ]  )
			p[0].process_sub()
	if len(p) == 5:
		if p[2] != None:
			p[0] = Expr( [ p[1] ] + p[2] + [ p[3] ] + p[4] )
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
			p[0] = Expr(  p[0] + p[1] + p[2] )

			#operator
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


def print_p(sf,name,body):
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
		if Item[0:4] != 'expt' and Item[0:5] != "ques_"and Item != "variableModifiers" and Item != "classOrInterfaceModifiers":
			self.item = Item
		else:
			self.item = (Item,'')
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

# function define
def insert(s ,i , d ):
	t = list(s)
	del t[i]
	for item in d :
		t.insert( i , item)
		i = i + 1
	s = deque(t)
	return s

def find_ques(d):
	l = len(d)
	for i in range(l):
		if d[i][0:5] == "ques_":
			yield (i , d[i])

def process_expr( expr ):
	l = [ (i , f ) for i,f in find_ques(expr) ]
			
	if len( l ) == 0 : return expr
	ilen = len(expr)
	for i,f in l:	
		i = (len(expr) - ilen ) + i
		d = queslist.get_value( expr[i] )
		expr = insert (expr , i ,d)
	return expr
# ------------------

def get_yacc(l,outfile):

	b = yacc.yacc()

	b.error = 0
	result = b.parse(lexer = l , debug=0)

	# begin

	sf = open(outfile,"w")
	sf.write("# *.* coding=utf-8 *.*\n")
	sf.write("""
import ply.yacc as yacc
import lex
from collections import deque

tokens = lex.tokens
""")


	for rule in  rules:
		if rule[0] == 'integerLiteral': continue
		body = ""
		flag = False
		for token in rule[2]:
			if token[0:4] == 'expt' or token[0:5] == 'ques_' or token == "classOrInterfaceModifiers" or token == "variableModifiers":
				flag = True
				break
		if flag == True:
			d = process_tree(rule[2])


			#process replace ques ........	
			b = deque( d )
			s_list = []
			for item in d:
				s_list.extend( [ process_expr( i ) for i in item ] )
			iFlag = False
			l = len(s_list)
			for i in range( l ):
				l = [ (k , f ) for k,f in find_ques(s_list[i]) ]
				
				if len(l) > 0:
					temp_list = process_tree(s_list[i])
					del s_list[i]
					s_list.extend( [ process_expr(item) for item in temp_list[0] ] )
					iFlag = True
			#if rule[0] == 'annotation':
			#	print s_list

			body = "\n\t\t| ".join( [" ".join(o) for o in s_list if "".join(o) != "" ] )
		else:
			l = len(rule[2])
			for i in xrange( l ):
				if rule[2][i][0:5] == "ques_":
					rule[2][i] = " ".join( queslist.get_value( rule[2][i] ) )
			for y in rule[2]:
				if y == "|":
					body = body + " " +  ( "\n\t" + y )
				else:
					body = body + " "+ y
		print_p(sf, rule[0], body)

	multlist.echo(sf)
	exprlist.echo(sf)
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
		integerLiteral : LONG_NUMBER
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

def get_yacc(l,filename,debug):
	b = yacc.yacc()

	b.error = 0

	if debug == True:
		result = b.parse(lexer = l , debug=2)
	else:
		result = b.parse(lexer = l , debug=0)

	if b.error : return None
	print "%s was successed" % filename
	""")
	sf.close()



