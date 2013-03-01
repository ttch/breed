
# *.* coding=utf-8 *.*
import breed_import
	
class component:
	def __init__(self):
		self.lex = None
		self.ID = None
		self.fullname = None
	
	def readNext(self):
		count = 0
		if ( len(self.lex) == 0 ): return None
		return self.lex.popleft()

	
	def p_import(self,token):
		""" 调用 breed_import 模块编译 """
		self.lex.appendleft(token)
		breed_import.compile(self.fullname,self.lex)

	def p_at(self,token):
		{
			"DEFINE": lambda token : token,
			"FUNCTION": lambda token : token 
				
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
			
				"AT" : lambda token : self.p_at(token),
				"IMPORT": lambda token : self.p_import(token) 

			}.get(token.type,self.p_default)(token)

import g_class
g_class.ADD("component",component)
