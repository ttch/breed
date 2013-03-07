# *.* coding=utf-8 *.*

# 处理import 段的程序

import g_class
import import_
from breed_runtime import runtime
import breed_debug as debug

class b_import:
	def compile(self,name):
		return g_class.CALL("component",name)

#to-do getimportlist
def get_import_list(stat):
	token = ""
	begin = False
	while True:
		x = stat.popleft()
		if begin == False:
			if x.type == "IMPORT":
				begin = True
				token = ""
				continue
			else:
				stat.appendleft(x)
				return
		if begin == True:
			if x.type != "SEMI" :
				token = token + x.value
			elif x.type == "SEMI":
				begin = False
				yield token

def compile(name,stat):
	#获得包名字
	ilist = [ y for y in get_import_list(stat)]
	debug.log( list )
	pkg = runtime.getPackage( name )
	if pkg == None:
		pkg = import_.package(name)
		runtime.addPackage( name , pkg )
	for x in ilist:
		if not runtime.isCompiled( x ):
			npkg = runtime.addPackage( x ,g.compile( x ))
			pkg.add_requre(npkg)


#公用的import list 模块
g = b_import()
