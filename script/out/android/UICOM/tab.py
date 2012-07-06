# *-* coding=utf-8 *-* 

"""
tab  属性 tab_id_name
					tab_title_name
					tab_contenxt
"""

from jinja2 import Template
from jinja2 import Environment


class tab_control:
	
	def __init__(self,main_config):
		self.__main_config = main_config
		self.control_list = []
		self.ids = []

	#读取模版
	def read_tpl(self):
		return

	def read_config(self,config_str):
		tpl_tab_list = []

		var_f = open(self.__main_config.get_tpldir()+"UI\\com\\tab.tpl")
		
		tpl_str = ""
		for x in var_f.readlines():
			tpl_str = tpl_str+x
		
		for x in config_str:
			aline = x[0:-1].split("|")
			tpl_tab_list.append({"tab_id_name":aline[0].decode("utf-8"),"tab_contenxt_id":"{{"+aline[0].decode("utf-8")+"}}","tab_title_name":aline[1].decode("utf-8")})
			self.ids.append(aline[0])
		template = Template(tpl_str)
		m = template.module

		self.__tpl_mkd_str = template.render(tabs = tpl_tab_list)
		
		var_f.close
		
		#js
		var_f = open(self.__main_config.get_tpldir()+"UI\\com\\tab_js.tpl")
		
		tpl_str = ""
		for x in var_f.readlines():
			tpl_str = tpl_str+x
		
		template = Template(tpl_str)
		
		self.__tpl_mkd_js_str = template.render(name=".tab")
		
		var_f.close
		
		return

	def flush_(self):
		return

	def make(self):
		return {"html":self.__tpl_mkd_str,"js":self.__tpl_mkd_js_str,"css":""}
	
	def get_ids(self):
		return self.ids