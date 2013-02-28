# *.* coding=utf-8 *.*

# 处理import 段的程序

import g_class
import import_
from breed_runtime import runtime
import breed_debug as debug

class b_import:
	def compile(self,name):
		return g_class.CALL("component",name)


def compile(curComponentName,stat):
	#获得包名字
	name = ""
	while (True):
		token = stat.popleft()
		if token == None or token.type == "SEMI":
			break
		name = name + token.value
	debug.logs( " breed_import 获取模块  %s " , ( name ) )
	pkg = runtime.getPackage( name )
	#debug.logs( "编译模块 %s 的 子列表为： %s " , ( curComponentName , pkg.requredList) )

	if pkg != None or runtime.isCompiled( pkg ):
		if name not in pkg.requredList :
			return
		else:
			npkg = runtime.getpackage( name )
			if npkg == None:
				debug.logs( " breed_import 编译模块 not requred %s " , ( name ) )
				npkg = runtime.addPackage( name , g.compile(name) )
			else :
				return
	else:
		debug.logs( " breed_import 编译模块 no Compiled %s " , ( name ) )
		runtime.addPackage( name  , g.compile(name) ) 	

#公用的import list 模块
g = b_import()
