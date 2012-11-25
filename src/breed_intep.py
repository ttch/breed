# *-* coding=utf-8 *-*

import breed_lex


#compileing function
def Compile( filename ):
	s = ""
	f = open(filename)
	for x in f.readlines():
		s = s+ x
	breed_lex.lex.input(s)
	"""
	这地方分四大词组，我们这里只处理两个，一个是component 一个是datastruct



	"""


	token = breed_lex.lex.token()
	#raise Exception("test",u"错误啊错误")
	if token.type == "COMPONENT":
		import breed_component
		component = breed_component.component()
		component.Compile(breed_lex.lex)
		print "this id = "+ component.ID.value
	elif token.type == "DATASTRUCT":
		import breed_datastruct
		print u"这个是数据结构"
	else:
		raise u"错误"
