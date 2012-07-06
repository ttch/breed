# *-* coding=utf-8 *-*

"""
tab  属性 tab_id_name
					tab_title_name
					tab_contenxt
"""

from jinja2 import Template
from jinja2 import Environment

import global_var

var_main = global_var.var_main

class frame:

	def __init__(self,field):
		self.__field = field

	def read_tpl(self):
		tpl_str = ""
		for x in open(var_main.get_tpldir()+"UI\\com\\frame.tpl").readlines():
			tpl_str = tpl_str+x
		self.__tpl_str = tpl_str

	def read_config(self):

		self.read_tpl()

		template = Template(self.__tpl_str)
		m = template.module
		self.__tpl_mkd_str = template.render(
											 name = self.__field["fieldname"],src = self.__field["src"],
											 )
		return self.__tpl_mkd_str

	def flush_(self):
		return

	def make(self):
		return self.read_config()


class frameset:

	def __init__(self,field):
		self.__field = field

	def read_tpl(self):
		tpl_str = ""
		for x in open(var_main.get_tpldir()+"UI\\com\\frameset.tpl").readlines():
			tpl_str = tpl_str+x
		self.__tpl_str = tpl_str

	def read_config(self):

		self.read_tpl()

		template = Template(self.__tpl_str)
		m = template.module
		self.__tpl_mkd_str = template.render(
											 frames=self.__child
											 )
		return self.__tpl_mkd_str

	def flush_(self):
		return

	def make(self,child):
		self.__child = child
		return self.read_config()
