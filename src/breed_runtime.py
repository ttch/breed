# *.* encoding=utf-8 *.*


import breed_debug as debug

from collections import deque

# 运行时内容收集器
class brdRuntime:
	# 编译过的列表
	# 暂时只支持 component
	pckList = {}

	#当前编译的curPkg
	curPkg = None
	curFunction = None
	#临时使用的栈
	stack = deque()

	def __init__( self ) :
		pass
	
	def __getitem__(self,n):
		return self.pckList[n]

	def __setitem__(self,n,v):
		self.pckList[n] = v

	# package 为import_.py中的
	def addPackage( self , name , package ) :
		self.pckList[name] = package
		return package
	
	def getPackage( self , name ):
		debug.logs( " breed_runtime 传入名字是 %s  " , ( name ) )
		return ( self.pckList[name] if name in self.pckList else None )
	
	def isCompiled( self , name ):
		return ( True if name in self.pckList else False )

	def getStack(self):
		return self.stack

def echo():
	for x in runtime.PackageList:
		print x
		print runtime.PackageList[x].requrelist
		for y in runtime.PackageList[x].requrelist:
			print y

runtime = brdRuntime()
	
