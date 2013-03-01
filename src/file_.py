# *.* coding=utf-8 *.*
import os
import global_var
from collections import deque
import itertools


def all_dir_cache():
	pass
	#做一个全缓存路径

def importname_filename(modulename):
	return "/".join( modulename.split(".") )+".brd"

def getSource(filename):
	return "".join( open(filename).readlines() )

def isExistFile(filename):
	if ( os.path.isfile(global_var.g_libs_dir+filename) == True ):
		return global_var.g_libs_dir+filename
	elif ( os.path.isfile(global_var.g_project_dir+filename) == True ):
		return global_var.g_project_dir+filename
	else:
		return None

def getTokenList(lexer):
	tokenList = []
	while (True):
		token = lexer.token()
		if token == None: return deque( tokenList )
		tokenList.append(token)

def getNameListInName( name ):
	name = [x for x in itertools.ifilter( ( lambda x : ( x != ".") and ( x != "" ) and ( x != "brd" ) ), name.split(".") ) ] [0]
	
	return [x for x in  name.split("/") if x != "" ]


def isInLib( names , libs ):
	i = 0
	for x in itertools.izip( names , libs ):
		if x[0] != x[1]:
			return (i , False )
		else:
			i = i+1
	
	return ( i , ( True if i == len( libs ) else False) )

#通过名字获取到完整的import路径
def getImportNameByFileName( name ):
	names =  getNameListInName(name)

	(l ,isIn) = isInLib( names , getNameListInName(global_var.g_libs_dir) )

	if isIn == True:
		return ".".join( names[l:len(names)] )

	(l , isIn) = isInLib( names , getNameListInName(global_var.g_project_dir ) )
	if isIn == True:
		return ".".join( names[l:len(names)] )

	return None
