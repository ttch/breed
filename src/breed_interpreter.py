# *-* coding=utf-8 *-*
import simplejson as json
import string

def error_print(object,str):
	print( "%s %s" % (object,str) )
def _replace(str,old,new):
	return str.replace(old, new)

#
# 特殊环境模块
#
#
class breed_tilde:
	def __init__(self):
		self.env_token = ""
		self.env_system = ""
		self.tokens = []
	def compile(self,tokens,compiler):
		i = 0
		atoken = tokens[i]
		if atoken.type == "TILDE":
			i = i+1
			self.env_token = tokens[i].value
			i = i+2
			self.env_system = tokens[i].value
			i = i+1
			if tokens[i].type == "BLPAREN":
				while (True):
					i = i+1
					if tokens[i].type == "BRPAREN":
						break
					self.tokens.append(tokens[i])
				#收集import生成一个import类
				#如果词汇不是import而是id的话直接走赋值式记录行程
				#特殊处理代码，需要细化

		#TO-DO 首先确认tokens中所有的对象中是否含有import
		
		i = 0
		l = len(self.tokens)
		while ( True ) :
			if self.tokens[i].type == "IMPORT":
				str_import = ""
				#导入一个import
				a_import = breed_import()
				a_import.append(self.tokens[i])
				while( True ):
					if self.tokens[i].type == "ID" or self.tokens[i].type == "DOT":
						str_import = str_import + self.tokens[i].value
					i = i+1
					a_import.append(self.tokens[i])
					if self.tokens[i].type == "SEMI":
						compiler.import_list[str_import] = a_import
						break
			i = i + 1
			if i >= l :
				break
	def debug(self):
		pass#print self.env_token
		#print self.env_system
		#print self.tokens


class breed_import:
	import_tokens = []
	def __init__(self):
		pass
	def compile(self,tokens):
		pass
	def append(self,obj):
		self.import_tokens.append(obj)
	@classmethod
	def parser_atoken( cls , data , parentCompile ):
		TokenName = ""
		TokenString = ""
		TokenList = []
		if data.type == 'IMPORT':
			while ( True ) :
				TokenString = TokenString + str(data.value)
				TokenList.append(data)
				if data.type == "SEMI":
					break;
				if data.type != 'IMPORT':
					TokenName = TokenName + str(data.value)
				data = parentCompile.getNextToken()
		return (TokenName,TokenString,data)
		

#------------------------------------------------------------------------------
#	field处理类 
#
#					#左按对象处理
#
#						内部存储结构按如下处理：
#						first_id : {
#							"letf":[id . id . id ],
#							"optertion": " = ",
#							right: object
#						}
#						object 可能是值 也可能是一个函数调用
#这里面有3种情况
#1 字段赋值
#2 特殊系统处理赋值
#3 函数调用
#4 函数定义
#------------------------------------------------------------------------------
class breed_field:
	def __init__(self):
		#字段名
		self.fieldname = ""
		#继承组件名称
		self.extend = ""
		#属性赋值表达式列表
		self.expressions = {}
		self.functions = {}
		self.call = {}
		self.special_system_process = {}
	def compile(self,tokens):
		#字段名
		self.fieldname = tokens[0]
		self.extend = tokens[4]
		i = 0
		l = len(tokens)
		ibegin_read = False
		while( True ) :
			if i == l-1 : break
			i = i+1
			#进入主体代码
			if tokens[i].type == "BLPAREN":
				ibegin_read = True
			if ibegin_read == True :
				i =	self.process_body(tokens,i)
	def getTokens(proCompile):
		pass
	def process_body(self,tokens,index):
		i = index+1
		l = len(tokens)
		while(True):
			if i == l-1 : break
			i = i+1
			if tokens[i].type == "BLPAREN":
				self.process_body(tokens,i)
			
			# syntax begin
			if tokens[i].type == "ID":
				field = {}
				field_body = {}
				
				id = tokens[i]
				field[id] = field_body

				left_stack = []
				right_stack = []
				j = i
				while (True):
					if tokens[j].type in ["ID","DOT"]:
						left_stack.append(tokens[j])
					else:
						break
					j = j+1
				i = j

				if left_stack != [] :
					field_body["left"] = left_stack
				if tokens[i].type == "EQUALS":
					field_body["optertion"] = tokens[i]
					i = i + 1
				if token[i].type == "LPAREN":
					pass
					#开始函数计算
				j = i
				while (True):
					if tokens[j].type in ["ID","DOT","STRING","NUMBER"]:
						right_stack.append(tokens[j])
					else:
						break
					j = j+1
				i = j
				if right_stack != []:
					field_body["right"] = right_stack
				#print field , ";"
		return i
#------------------------------------------------------------------------------
#	field处理类 
#
#------------------------------------------------------------------------------
class breed_set:

	def __init__(self):
		pass
	def compile(self,tokens):
		pass
#------------------------------------------------------------------------------
#	field处理类 
#
#------------------------------------------------------------------------------
class breed_function:

	def __init__(self):
		pass
	def compile(self,tokens):
		pass
#------------------------------------------------------------------------------
#	field处理类 
#
#------------------------------------------------------------------------------
class breed_fieldset:

	def __init__(self):
		pass
	def compile(self,tokens):
		pas
#------------------------------------------------------------------------------
#	field处理类 
#
#------------------------------------------------------------------------------
class breed_sec:

	def __init__(self):
		pass
	def compile(self,tokens):
		pas
#------------------------------------------------------------------------------
#		breed 语言解析模块
#------------------------------------------------------------------------------
class BreedInterpreter:
	def __init__(self,tokens):
		self.__tokens = tokens
		self.__nameStack= []
		self.name = ""
		
		#调用组件的名字表
		#self.lib_import = breed_lib()
		
		#字段表
		self.field_list = {} 


		self.lib_sys = []
		self.lib_componet = []
		self.lib_custom = []

		self.out = {}
		#field字段
		
		self.import_list = {}


		#组件
		self.function = {}

		self.com_desc = ""
	def debug(self):
		for x in self.import_list:
			pass
			#print self.import_list[x].import_tokens
			print x
			print self.import_list[x].import_tokens
	#------------------------------------------------------------------------------
	#	编译函数
	#------------------------------------------------------------------------------
	def Compile(self):
		adata = self.getNextToken()
		if adata.type == 'PAGE' :
			self.process_page()
		#elif adata.type == "COMPONENT":
			#self.com_desc = self.process_component()
	
	#递归读词
	def read_tokens(self,tokens):
		two_flag = 0;
		while ( True ) :
			adata = self.getNextToken()
			if adata == None: 
				return
			if adata.type == "BLPAREN":
				tokens.append(adata)
				two_flag = two_flag+1
				if two_flag == 2:
					self.read_tokens(tokens)
				continue
			if adata.type == "BRPAREN":
				tokens.append(adata)
				return
			tokens.append(adata)
	#------------------------------------------------------------------------------
	#	处理组件模块部分
	#------------------------------------------------------------------------------
	def process_component(self):
		adata = self.getNextToken()
		if adata == None:
			print "ERROR PAGE IS NULL on lineno:%s - 0001" % (adata.lineno)
			return
		elif adata.type != "ID":
			print "ERROR PAGE IS NOT ID on lineno:%s - 00002" % (adata.lineno)
			return
		else:
			self.name = adata.value
		return self.process_lib()
	#------------------------------------------------------------------------------
	#	处理页函数
	#------------------------------------------------------------------------------
	def process_page(self):
		adata = self.getNextToken()
		if adata == None:
			print "ERROR PAGE IS NULL on lineno:%s - 0001" % (adata.lineno)
			return
		elif adata.type != "ID":
			print "ERROR PAGE IS NOT ID on lineno:%s - 00002" % (adata.lineno)
			return
		else:
			self.name = adata.value
		self.process_body()

	#------------------------------------------------------------------------------
	#	处理库部分函数
	#------------------------------------------------------------------------------
	def process_lib(self):
		a_var = Component(self.__tokens,self.function)
		return a_var.make()
			#处理component数据
	#------------------------------------------------------------------------------
	#					处理公用部分
	#------------------------------------------------------------------------------
	def process_body(self):
		while(True):
			
			adata = self.getNextToken()
			
			if adata == None:
				break
			#一层特殊处理
			#  ~  符号处理模式
			#TO-DO 需要筹划这种模式
			if adata.type == "TILDE":
				tilde_tokens_list = []
				while(True):
					tilde_tokens_list.append(adata)
					if adata.type == "BRPAREN":
						break
					adata = self.getNextToken()
				aTilde = breed_tilde()
				aTilde.compile(tilde_tokens_list,self)
				aTilde.debug()
			#lib段
			if adata.type == 'IMPORT':
				#read Import
				aImport = breed_import()
				TokenName = ""
				TokenString = ""
				(TokenName,TokenString,adata)  = breed_import().parser_atoken(adata,self)
				aImport.compile(TokenString)
				self.import_list[TokenName] = aImport
			if adata.type == 'FIELD':
				afield = breed_field()
				afield.compiles(Toekn)
				
			if adata.type == 'SET':
				pass#print adata
			if adata.type == "FIELDSET":
				pass#print adata
			if adata.type == "SEC":
				pass#print adata
			if adata.type == "FUNCTION":
				pass#print adata
			if adata.type == "ASSIOC":
				pass#print adata
				#alib_token = []
				#while ( True ) : 
				#	adata = self.getNextToken()
				#	print adata
				#	if adata.type == "END": break
				#	alib_token.append(adata)
				#self.lib_import.compile(alib_token)
			
			#主程序部分
			#收集
			#if adata.type == "FIELD":
			#	afield = breed_field()
			#	tokens = []
			#	#读词
			#	self.read_tokens(tokens)
			#	afield.compile(tokens)
			#self.field_list.append[afield.fieldname] = afiled

			#解析control段

			#if adata.type == 'CONTROL':
			#	self.process_control()


	#------------------------------------------------------------------------------
	#						获得下一个词
	#------------------------------------------------------------------------------
	def getNextToken(self):
		return self.__tokens.token()
	#------------------------------------------------------------------------------
	#						分析库代码
	#------------------------------------------------------------------------------
	def read_lib(self,lib_type):
		while (True):
			adata = self.getNextToken()
			if adata.type == "COMMA":
				continue
			if adata == None or adata.type == "RPAREN":
				break
			if lib_type == "sys":
				self.lib_sys.append(adata.value)
			if lib_type == "aoc":
				self.lib_componet.append(adata.value)
			if lib_type == "custom":
				self.lib_custom.append(adata.value)

	#------------------------------------------------------------------------------
	#				分析控件代码
	#------------------------------------------------------------------------------
	def process_control(self):
		adata = self.getNextToken()
		while adata.type != 'END':
			adata = self.getNextToken()
			if adata.type == 'FIELD':
				adata = self.getNextToken()
				if (adata.type != 'DOT'):
					error_print(a,"this site is a dot")
					break
				adata = self.getNextToken()
				if adata.type == 'STRING':
					self.field_list.append(adata.value)
				elif adata.type == "EXTENDS":
					while(True):
						adata = self.getNextToken()
						if adata.type == "SEMI": break
						self.__nameStack.append(adata)

					self.process_function()
					self.__nameStack = []
			if adata == None:
				return
	#------------------------------------------------------------------------------
	#		处理函数
	#------------------------------------------------------------------------------
	def process_function(self):
		i = 0
		l = len(self.__nameStack)
		while ( True):
			#(object . func ( param ) )
			adata = self.__nameStack[i]
			if adata.type == 'DOT':
				obj = self.__nameStack[i-1].value
				func = self.__nameStack[i+1].value
				i = i+1
			if adata.type == "LPAREN":
				adata = self.__nameStack[i+1]
				if adata.type == "ID":
					param = adata.value
				if adata.type == "STRING":
					param = adata.value
			i = i+1
			if i == l:
				break
		self.field_extends.append({"object":obj,"function":func,"param":param})
		isfunc = False

#------------------------------------------------------------------------------
#
# 处理控件格式类，1.0
# 需要把大部分数据都处理成json数据 格式。然后在模版中进行替换
#------------------------------------------------------------------------------
class Component:
	def __init__(self,tokens,function):
		self.__tokens = tokens
		self.__tokenStack = []
		self.__json_str = ""
		self.function =function
	#------------------------------------------------------------------------------
	#	获得下一个词
	#------------------------------------------------------------------------------
	def getNextToken(self):
		return self.__tokens.token()
	#------------------------------------------------------------------------------
	#	生成需要的格式
	#------------------------------------------------------------------------------
	def make(self):
		#读取lib中的内容
		while ( True ) :
			adata = self.getNextToken()
			if adata == None:
				break
			if adata.type == "FUNCTION":
				self.process_function()
			self.__tokenStack.append(adata)
		i = 0
		l = len ( self.__tokenStack )
		i,value = self.submake(self.__tokenStack,i,l)
		return value

	#------------------------------------------------------------------------------
	# 处理函数的函数
	# 只处理单语句 变量赋值
	# 暂时不支持跳转，函数调用，循环，循环嵌套等高级用法
	#------------------------------------------------------------------------------
	def process_function(self):
		func_name = ""
		param = []
		is_block = False
		while ( True):
			adata = self.getNextToken()
			#参数
			if adata.type == "ID":
				self.function[adata.value] = ""
				func_name = adata.value
			#参数
			if adata.type == "LPAREN":
				while(True):
					adata = self.getNextToken()
					if adata.type == "RPAREN":
						break
					if adata.type == "ID":
						param.append(adata.value)
			if adata.type == "BLPAREN":
				while(True):
					( result,body ) = self.process_function_body()
					if result == "BRPAREN":
						self.function[func_name] = (param,body)
						return



	#------------------------------------------------------------------------------
	#
	#	处理函数体
	#------------------------------------------------------------------------------
	def process_function_body(self):
		body = []
		body_stack = []
		while (True):
			adata = self.getNextToken()
			if adata.type == "BRPAREN":
				break
			body_stack.append(adata)
		i = 0
		l = len(body_stack)
		token = []

		while( True ):
			if i == l:
				break
			if body_stack[i].type == "SEMI":
				body.append(token)
				token = []
			token.append(body_stack[i])
			i = i+1
		return "BRPAREN" , body

	#------------------------------------------------------------------------------
	#	递归制作分析词组成JSON格式串
	#------------------------------------------------------------------------------
	def submake(self,tokenStack,i,l):
		jStr = "{"
		__json_token = []
		while ( True ) :
			#组装key

			if i >= l or i ==l-1 :
				jl = len(__json_token)
				ji = 0
				for atoken in __json_token:
					if ji == jl-1:
						jStr = jStr + atoken
					else:
						jStr = jStr +atoken+ " , "
					ji = ji+1
				jStr = jStr + "}"
				return ( i , jStr)
			if tokenStack[i+1].type == "BRPAREN" and tokenStack[i+2].type == "SEMI":
				jl = len(__json_token)
				ji = 0
				for atoken in __json_token:
					if ji == jl-1:
						jStr = jStr + atoken
					else:
						jStr = jStr +atoken+ " , "
					ji = ji+1
				jStr = jStr + "}"
				return ( i , jStr)
			adata = tokenStack[i]
			if adata.type == "EQUALS":
				if tokenStack[i+1].type == "STRING":
					key = ""
					value = ""
					if i < l-1 and tokenStack[i+2].type == "PLUS":
						key = _replace(_replace(tokenStack[i-1].value,"\"", "\\\""),"\'","\"")
						value = ""
						j = i+1
						while (True):
							if tokenStack[j].type == "STRING":
								value = value + tokenStack[j].value
							if tokenStack[j].type == "SEMI":
								break
							j = j+1
						value = _replace(_replace(_replace(value,"\'",""),"\t",""),"\"","\\\"")
						value = "\""+value+"\""
						i = j
					else:
						key = _replace(_replace(tokenStack[i-1].value,"\"", "\\\""),"\'","\"")
						value = _replace(_replace(tokenStack[i+1].value,"\"", "\\\""),"\'","\"")
					__json_token.append("\"%s\":%s " % (
												 key,
												 value
												  )
										)
				if tokenStack[i+1].type == "BLPAREN":
					key = tokenStack[i-1].value
					value = ""
					i,value = self.submake(tokenStack,i+1,l)
					__json_token.append( "\"%s\": %s " % (key , value) )
			i = i+1





