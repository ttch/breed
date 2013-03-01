# *-* coding=utf-8 *-
#a global class list
#这个 list 暂时只包含 component
import global_var
import os
from file_ import *
import breed_lex
import breed_debug as debug
import import_

class_list = {}

def ADD ( classname ,classdef ):
	class_list[classname] = classdef


# 这是一个全局编译程序列表，
#当component 等关键词进入的时候，
#需要查找是否有编译结构，如果没有，即时编译他就可以。

def CALL(class_name,modulename):
	if class_name == "component":
		
		debug.logs( " g_class 调用的 模块名称是  %s" , ( modulename ) )

		file_name = importname_filename(modulename)
		if isExistFile(file_name) == None:
			debug.logs( " g_class 找不到模块文件 %s " , ( modulename ) )
			return None
		else:
			# new 一个组件对象，并调用编译新的代码
			class_list[class_name]().compile(	\
				getImportNameByFileName(file_name) , getTokenList(	\
				 	breed_lex.input( breed_lex.getlex() , getSource( isExistFile(file_name) ) \
				 	) ) )
			debug.logs( " 模块名字是： %s , 文件名字是： %s" , ( modulename,file_name ))
		return import_.package(modulename)		
