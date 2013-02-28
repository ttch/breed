# *-* coding=utf-8 *-*

import breed_lex
import file_

import breed_debug as debug


#compileing function
def compile( filename ):
	s = file_.getSource(filename)
	lexer = breed_lex.getlex()
	lexer.input(s)
	tokenList =  file_.getTokenList(lexer)

	token = tokenList.popleft()
	#raise Exception("test",u"错误啊错误")
	
	if token.type == "COMPONENT":
		debug.logs(" breed _ intep 开始编译......... [ %s ] ",(filename))
		import breed_component
		component = breed_component.component()
		debug.logs("获取程序的完全import路径名 ....[ %s ]" , (file_.getImportNameByFileName(filename) ))
		component.compile( file_.getImportNameByFileName(filename) , tokenList )
	elif token.type == "DATASTRUCT":
		import breed_datastruct
		u"这个是数据结构"
	else:
		raise u"错误"
	import breed_runtime
	breed_runtime.echo()
