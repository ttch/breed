# *.* coding=utf-8 *.*

from collections import deque

import breed_import
import breed_function
import breed_debug as debug

from g.gy import *
	
class component:
	def __init__(self):
		self.lex = None
		self.ID = None
		self.fullname = None
		self.recvlist = deque()
	
	def readNext(self):
		if ( len(self.lex) == 0 ): return None
		return poptoaddbyleft(self.lex,self.recvlist)
	
	def recvNext(self):
		return poptoaddbyleft(self.recvlist,self.lex)

	def p_import(self,token):
		""" 调用 breed_import 模块编译 """
		self.lex.appendleft(token)
		breed_import.compile(self.fullname,self.lex)

	def p_function(self,token):
		debug.logs("编译function %s " , ( token ))
		self.recvNext()
		self.recvNext()
		breed_function.compile(token,self.lex)

	def p_at(self,token):
		{
			"DEFINE": lambda token : token,
			"FUNCTION": lambda token : self.p_function(token)
		}.get(token.type,self.p_default)(token)
	
	def p_default(self,token):
		#print "error token_id : " + token.value
		return None

	def p_getID(self,token):
		# get lib id  first search to libs directory and search to project component directory
		return token
	

	# Compile Component source
	def compile(self,fullname,lex):
		self.lex = lex
		self.fullname = fullname
		
		token = self.readNext()

		self.ID ={
			"ID" : lambda token : self.p_getID(token)
		
		}.get(token.type,self.p_default)(token)

		#processing statment	
		while(True):
			token = self.readNext()

			if token == None: break
			#syn begin
			{
			
				"AT" : lambda token : self.p_at(self.readNext()),
				"IMPORT": lambda token : self.p_import(token)

			}.get(token.type,self.p_default)(token)

import g_class
g_class.ADD("component",component)
