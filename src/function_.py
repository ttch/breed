# *.* coding=utf-8 *.*

class func_arg:
	def __init__(self ,type , name , action ):
		self.type = type
		self.name = name
		self.action = action

class function:
	def __init__( self , name ):
		self.funcname = name
		self.arglist = []
	def set_arg(self , arg_type,arg_name,arg_action):
		self.arglist.append( func_arg( arg_type,arg_name,arg_action ] ) )
