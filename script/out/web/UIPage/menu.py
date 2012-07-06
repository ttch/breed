# *-* coding=utf-8 *-*


from jinja2 import Template
import global_var

var_main = global_var.var_main


class menuitem:
	def __init__(self,field):
		self.__field = field

	def read_tpl(self):
		tpl_str = ""
		for x in open(var_main.get_tpldir()+"UI\\com\\menuitem.tpl").readlines():
			tpl_str = tpl_str+x
		self.__tpl_str = tpl_str

	def read_config(self):

		self.read_tpl()

		template = Template(self.__tpl_str)
		m = template.module
		self.__tpl_mkd_str = template.render(
											 name = self.__field["fieldchnname"],
											 href = self.__field["url"],
											 target = self.__field["target"],
											 submenus = self.__child
											 )
		return self.__tpl_mkd_str

	def flush_(self):
		return

	def make(self,child):
		self.__child = child
		return self.read_config()

class submenu:
	def __init__(self,field):
		self.__field = field

	def read_tpl(self):
		tpl_str = ""
		for x in open(var_main.get_tpldir()+"UI\\com\\submenu.tpl").readlines():
			tpl_str = tpl_str+x
		self.__tpl_str = tpl_str

	def read_config(self):

		self.read_tpl()

		template = Template(self.__tpl_str)
		m = template.module
		self.__tpl_mkd_str = template.render(
											 name = self.__field["fieldchnname"],
											 href = self.__field["url"],
											 target = self.__field["target"],
											 submenus = self.__child
											 )
		return self.__tpl_mkd_str

	def flush_(self):
		return

	def make(self,child):
		self.__child = child
		return self.read_config()

class menuset:
	def __init__(self,field):
		self.__field = field

	def read_tpl(self):
		tpl_str = ""
		for x in open(var_main.get_tpldir()+"UI\\com\\menuset.tpl").readlines():
			tpl_str = tpl_str+x
		self.__tpl_str = tpl_str

	def read_config(self):

		self.read_tpl()

		template = Template(self.__tpl_str)
		m = template.module
		self.__tpl_mkd_str = template.render(
											 name = self.__field["fieldname"],
											 menus=self.__child
											 )
		return self.__tpl_mkd_str

	def flush_(self):
		return

	def make(self,child):
		self.__child = child
		return self.read_config()