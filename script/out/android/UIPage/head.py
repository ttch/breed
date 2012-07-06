# *-* coding=utf-8 *-*



from jinja2 import Template
import simplejson as json

import func_support

#------------------------------------------------------------------------------
#	头部分处理
#
#------------------------------------------------------------------------------
class head:
	def __init__(self,compiler,control_str,pagename):
		self.__compiler = compiler
		self.__control_str = control_str
		self.__pagename = pagename
		self.__res = None

	#------------------------------------------------------------------------------
	#	flush函数
	#------------------------------------------------------------------------------
	def flush(self,func_fields):
		#建立json母体对象
		if self.__res == None:
			res = json.loads(self.__compiler["stander"].com_desc)
		else:
			res = self.__res
		"""
		control_str是基层所有的内容

		首先对所有的func对象进行遍历，然后每个func都会有一个组件。先找到组件，然后调用组件里的代码
		现在首要问题是没有调用顺序，那么解决方法 规定一个一顺序标签 由
		"""
		#第一步计算出left 第二步计算出=号，然后计算出右边的部分
		for afunc_obj in func_fields:
			com_compiler = self.__compiler[afunc_obj["object"]]
			print afunc_obj
			func_call_obj = com_compiler.function[afunc_obj["function"]][1][0]


			left_stack = []
			right_stack = []
			self.stack_process(func_call_obj,left_stack,right_stack)
			str = self.get_rightobj(right_stack, afunc_obj)

			res = self.get_leftobj(left_stack,res,str)
		self.__res  = res
	#------------------------------------------------------------------------------
	#	make函数
	#	判断在根之上的独立生成，并把跟内容复写进去，如果再根之下的写入树里
	#------------------------------------------------------------------------------

	def make(self):
		var_f = open(".\\tpl\\jjs_java\\UI\\stander\\component.tpl")
		try:
			tpl_str = ""

			for x in var_f.readlines():
				tpl_str = tpl_str+x
			template = Template(tpl_str)

			return template.render(token=self.__res['token'])
		finally:
			var_f.close()
	def get_rightobj(self,rightstack,funcobj):
		if len(rightstack) == 1:
			#现在只支持一个函数
			if funcobj["param"][0] == "'":
				return funcobj["param"]
			else:
				return self.__control_str
		else:
			print "错误，系统只支持一个函数"
	def get_leftobj(self,leftstack,res,content):
		obj = res
		i = 0
		l = len(leftstack)
		while (True):
			obj = obj[leftstack[i]]
			if i>= l-2:
				obj[leftstack[i+1]] = content
				break
			i = i+1
		return res
	def stack_process(self,obj,left,right):
		i = 0
		l = len(obj)
		isleft = True
		while(True):
			if i == l:
				break;
			if obj[i].type == "EQUALS":
				isleft = False

			if isleft:
				if obj[i].type == "ID":
					left.append(obj[i].value)
			else:
				if obj[i].type == "ID":
					right.append(obj[i].value)
			i = i+1
