# *-* coding=utf-8 *-*


import collector

#struct 有两种结构
#一种是单体，一种是列表
#结构体应该是一种公用基础单位。


class json_struct:
	def __init__(self,a_list,tbl_name):
		self.__list = a_list
		self.__tblname = tbl_name
	#处理列表 此方法暂时不用,等出现需求现开发
	def process_list(self):
		pass
	#生成函数
	def make(self):
		self.process_item()
	#处理单表
	"""
		此处无法生成真正的代码，只能生成伪代码并加到colect中
		到后期根据模板来生成
	"""
	def process_item(self):
		tbl_name = self.__tblname
		print tbl_name
		tbl = {}
		tbl[tbl_name] = []
		for x in self.__list:
			tbl[tbl_name].append(x)
		#a_line = ""
		#a_line = "{\"\",\"value\"}"
		collector.struList.append(tbl)

