# *-* coding=utf-8 *-*


from jinja2 import Template

import global_var

var_main = global_var.var_main


class text:

	def __init__(self,field):
		self.__field = field

	def read_tpl(self):
		tpl_str = ""
		for x in open(var_main.get_tpldir()+"UI\\com\\text.tpl").readlines():
			tpl_str = tpl_str+x
		self.__tpl_str = tpl_str

	def read_config(self):

		self.read_tpl()

		template = Template(self.__tpl_str)
		m = template.module

		self.__tpl_mkd_str = template.render(
											 id = self.__field["fieldchnname"],
											 name = self.__field["fieldchnname"],
											 color = self.__field["labelcolor"]
											 )
		return self.__tpl_mkd_str

	def flush_(self):
		return

	def make(self):
		return self.read_config()
