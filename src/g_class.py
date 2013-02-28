# *-* coding=utf-8 *-
#a global class list
#这个 list 暂时只包含 component
import global_var
import os
from file_ import *
import breed_lex
import breed_debug as debug
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
			pass
		else:
			s = getSource( isExistFile(file_name) )
			print s
			lexer = breed_lex.getlex()
			lexer.input(s)
			tokenList = getTokenList(lexer)
			name = getImportNameByFileName(file_name)
			class_list[class_name]().compile(name,tokenList)
			#import import_
			#return import_.package(modulename)


