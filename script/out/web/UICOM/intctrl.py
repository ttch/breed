# *-* coding=utf-8 *-*


#menu ����
"""
intctrl  ����
		id
		isred
		name
"""

from jinja2 import Template



class intctrl:

	def __init__(self,main_config):
		self.control_list = []
		self.__tpl_mkd_str = ""
		self.__main_config = main_config

	def read_tpl(self):
		return

	def read_config(self,config_str):

		var_f = open(self.__main_config.get_tpldir()+"UI\\com\\intctrl.tpl")

		tpl_str = ""
		for x in var_f.readlines():
			tpl_str = tpl_str+x

		template = Template(tpl_str)

		if config_str[6] == "Y":
			self.__tpl_mkd_str = template.render(id=config_str[1].decode("utf-8"),name=config_str[3].decode("utf-8"),isred="red")
		else:
			self.__tpl_mkd_str = template.render(id=config_str[1].decode("utf-8"),name=config_str[3].decode("utf-8"),isred="")

		var_f.close

		#js
		var_f = open(self.__main_config.get_tpldir()+"UI\\com\\intctrl_js.tpl")

		tpl_str = ""
		for x in var_f.readlines():
			tpl_str = tpl_str+x

		template = Template(tpl_str)
		self.__tpl_mkd_js_str = template.render(name=config_str[1])
		var_f.close

		return

	def flush_(self):
		return

	def make(self):
		return {"html":self.__tpl_mkd_str,"js":self.__tpl_mkd_js_str,"css":""}