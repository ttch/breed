# *.* encoding=utf-8 *.*


import breed_debug as debug



# 运行时内容收集器
class brdRuntime:
	# 编译过的列表
	# 暂时只支持 component
	compiledObj = {}

	def __init__( self ) :
		pass
	
	# package 为import_.py中的
	def addPackage( self , name , package ) :
		self.compiledObj[name] = package
	
	def getPackage( self , name ):
		debug.logs( " breed_runtime 传入名字是 %s  " , ( name ) )
		return ( self.compiledObj[name] if name in self.compiledObj else None )
	
	def isCompiled( self , name ):
		return ( True if name in self.compiledObj else False )

def echo():
	for x in runtime.compiledObj:
		print x


runtime = brdRuntime()
	
