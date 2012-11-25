
import breed_import

class component:
	def __init__(self):
		self.lex = None
		self.ID = None
		self.process_pack()
	
	def readNext(self):
		return self.lex.token()
	
	def process_pack(self):
		def p_at(token):
			print token
			print "hello"
		self.p_pack = {"AT":p_at}
	
	def p_import(self,token):
		breed_import.compile(token,self.lex)

	def p_at(self,token):
		{
			"DEFINE": lambda token : token,
			"FUNCTION": lambda token : token 
				
		}.get(token.type,self.p_default)(token)
	
	def p_default(self,token):
		print "error token_id : " + token.value

	# Compile Component source
	def Compile(self,lex):
		self.lex = lex
		token = self.readNext()
		#process and save component ID
		if token.type == "ID":
			self.ID = token
		#processing statment	
		while(True):
			token = self.readNext()
			if token == None: break
			#syn begin
			{
				"AT" : lambda token : self.p_at(token),
				"IMPORT": lambda token : self.p_import(token) 
			}.get(token.type,self.p_default)(token)
