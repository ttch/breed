# *.* coding=utf-8 *.*

class func_arg:
	def __init__(self ,type , name , action ):
		self.type = type
		self.name = name
		self.action = action

class function:
	def __init__( self ):
		self.funcname = ""
		self.arglist = []
	def set_name( name ):
		self.funcname = name
	def set_arg( arglist):
		for x in arglist:
			self.arglist.append(x)
