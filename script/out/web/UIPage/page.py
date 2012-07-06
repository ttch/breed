# *-* coding=utf-8 *-*

import sys

from jinja2 import Template
import controllist
import tab
import panel
import form
import collector
import head

import reader
import simplejson as json

ContainControl = ["PANEL",
				  "TAB",
				  "FRAMESET",
				  "MENUITEM",
				  "MENUSET"
				  ]


class page:
	#control list
	__ctrl_list = []
	#attr view pattern
	# [tab , list]
	__view_pattern = ""

	def __init__(self,compiler,PageName):
		self.__compiler = compiler
		self.__name = PageName
		self.out = self.__strConfigToJSON(self.__compiler[self.__name].out["out_dir"].replace("\\\\","\\")) +self.__name+".jsp"
	def make(self):
		return self.__make()

	#------------------------------------------------------------------------------
	#	库部分生成
	#------------------------------------------------------------------------------
	def __makelib(self):
		for asys in self.__compiler[self.__name].lib_sys:
			compilerObj = self.__compiler[asys]


	#------------------------------------------------------------------------------
	#	还原成json格式
	#	把配置文件中的文件格式还原成 JSON字符串格式
	#------------------------------------------------------------------------------
	def __strConfigToJSON(self,Str):
		return Str.split("'")[1]

	#------------------------------------------------------------------------------
	#	读取函数
	#	this function is set page view pattern
	#------------------------------------------------------------------------------
	def __read_pattern(self):
		#读取页面root
		main_str = ""
		all_str = ""

		field_list = self.__compiler[self.__name].field_list
		field_extends = self.__compiler[self.__name].field_extends
		#普通录入字段
		for aStr in field_list:
			res = json.loads( self.__strConfigToJSON( aStr ) )
			if res["parent"] == "" and res["fieldtype"] in ContainControl:
				#递归子树
				main_str = self.find_child(field_list,res)
				#构建root
				main_str = self.make_root(res,main_str)
				break

		ahead = head.head( self.__compiler , main_str , self.__name)
		ahead.flush(field_extends)

		return ahead.make()
	"""
			#继承的字段方法
			for afield in field_extends:
				#res = json.loads( aStr )
				ahead = head.head(self.__compiler[afield["object"]] , afield , main_str )
				#这个函数需要判断在根之上还是在根之下
				main_str = ahead.make()
				#调用这个对象的解析函数
				print main_str.encode("utf-8")
	"""
	#------------------------------------------------------------------------------
	#	顶层元素输出
	#------------------------------------------------------------------------------
	def make_root(self,root_res,child):
		strFields = ""
		aFactory = controllist.ControlFactory(root_res)
		return aFactory.query(child)
	#------------------------------------------------------------------------------
	#	控件树构造算法
	#   author by zhao_nf
	#   2012 06 15
	#	从下向上构造树控件
	#------------------------------------------------------------------------------
	def find_child(self,fieldList,field):
		strHtml = ""
		#是否是底层
		for aStr in fieldList:
			res = json.loads( self.__strConfigToJSON( aStr ) )
			if res["parent"] == field["fieldname"]:
				#print"parent: %s" % name
				#print "child: %s " % res["fieldname"]
				if res["fieldtype"] in ContainControl:
					#每进一层，清空临时表
					#把子层的数据加到父层中
					strFields = ""
					strFields = self.find_child(fieldList,res)

					aFactory = controllist.ControlFactory(res)
					strHtml = strHtml + aFactory.query(strFields)
				else:
					#处理这一层
					return self.get_html(fieldList,field)
		return strHtml

	#------------------------------------------------------------------------------
	#获得底层一组数据。
	#------------------------------------------------------------------------------
	def get_html(self,fieldList,field):
		strHtml = ""
		for aStr in fieldList:
			res = json.loads( self.__strConfigToJSON( aStr ))
			if res["parent"] == field["fieldname"]:
					aFactory = controllist.ControlFactory(res)
					strHtml = strHtml + aFactory.query("")
		return strHtml
	#------------------------------------------------------------------------------
	#	构造函数调用点
	#------------------------------------------------------------------------------
	def __make(self):
		self.__makelib()
		return self.__read_pattern()


