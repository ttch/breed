# *-* coding=utf-8 *-*


from jinja2 import Template

import global_var

var_main = global_var.var_main

class LinearLayout:
	def __init__(self,field):
		self.__field = field

	def read_tpl(self):
		tpl_str = ""
		for x in open(var_main.get_tpldir()+"UI\\com\\LinearLayout.tpl").readlines():
			tpl_str = tpl_str+x
		self.__tpl_str = tpl_str

	def read_config(self):

		self.read_tpl()

		template = Template(self.__tpl_str)
		m = template.module


		self.__tpl_mkd_str = template.render(
											 id = self.__field["fieldname"],
											 orientation = self.__field["orientation"],
											 layout_width = self.__field["layout_width"],
											 layout_height = self.__field["layout_height"],
											 layout_weight = self.__field["layout_weight"],
											 content=self.__child
											 )
		return self.__tpl_mkd_str

	def flush_(self):
		return

	def make(self,child):
		self.__child = child
		return self.read_config()
class TableLayout:
	def __init__(self,field):
		self.__field = field

	def read_tpl(self):
		tpl_str = ""
		for x in open(var_main.get_tpldir()+"UI\\com\\TableLayout.tpl").readlines():
			tpl_str = tpl_str+x
		self.__tpl_str = tpl_str

	def read_config(self):

		self.read_tpl()

		template = Template(self.__tpl_str)
		m = template.module
		self.__tpl_mkd_str = template.render(
											 id = self.__field["fieldname"],
											 layout_width = self.__field["layout_width"],
											 layout_height = self.__field["layout_height"],
											 content=self.__child
											 )
		return self.__tpl_mkd_str

	def flush_(self):
		return

	def make(self,child):
		self.__child = child
		return self.read_config()
class TableRow:
	def __init__(self,field):
		self.__field = field

	def read_tpl(self):
		tpl_str = ""
		for x in open(var_main.get_tpldir()+"UI\\com\\TableRow.tpl").readlines():
			tpl_str = tpl_str+x
		self.__tpl_str = tpl_str

	def read_config(self):

		self.read_tpl()

		template = Template(self.__tpl_str)
		m = template.module
		self.__tpl_mkd_str = template.render(
											 id = self.__field["fieldname"],
											 layout_width = self.__field["layout_width"],
											 layout_height = self.__field["layout_height"],
											 content=self.__child
											 )
		return self.__tpl_mkd_str

	def flush_(self):
		return

	def make(self,child):
		self.__child = child
		return self.read_config()
class ScrollView:
	def __init__(self,field):
		self.__field = field

	def read_tpl(self):
		tpl_str = ""
		for x in open(var_main.get_tpldir()+"UI\\com\\ScrollView.tpl").readlines():
			tpl_str = tpl_str+x
		self.__tpl_str = tpl_str

	def read_config(self):

		self.read_tpl()

		template = Template(self.__tpl_str)
		m = template.module
		self.__tpl_mkd_str = template.render(
											 id = self.__field["fieldname"],
											 layout_width = self.__field["layout_width"],
											 layout_height = self.__field["layout_height"],
											 content=self.__child
											 )
		return self.__tpl_mkd_str

	def flush_(self):
		return

	def make(self,child):
		self.__child = child
		return self.read_config()


class panel_control:
	def __init__(self,field):
		self.__field = field

	def read_tpl(self):
		tpl_str = ""
		for x in open(var_main.get_tpldir()+"UI\\com\\panel.tpl").readlines():
			tpl_str = tpl_str+x
		self.__tpl_str = tpl_str

	def read_config(self):

		self.read_tpl()

		template = Template(self.__tpl_str)
		m = template.module
		self.__tpl_mkd_str = template.render(
											 panel_title = self.__field["fieldchnname"],
											 panel_id=self.__child
											 )
		return self.__tpl_mkd_str

	def flush_(self):
		return

	def make(self,child):
		self.__child = child
		return self.read_config()
