# *-* coding=utf-8 *-*

import sys
sys.path.append("./script/struct/JSON.struct")

from jinja2 import Template
import jstruct

class form:
	def __init__(self,main_config,page_config):
		self.__config = {}
		self.__page_config = page_config
		self.__main_config = main_config

	def __del__ (self):
		x=1

	def read_config(self):
		for x in self.__page_config.get_form():
			aline = x.split("=")
			self.__config[aline[0]] = aline[1]

		tpl_tab_list = []
		var_f = open(self.__main_config.get_tpldir()+"UI\\form\\form.tpl")

		tpl_str = ""
		for x in var_f.readlines():
			tpl_str = tpl_str+x

		template = Template(tpl_str)
		m = template.module
		self.__form_tpl_str = template.render( name = self.__config["FORM_NAME"] )

		#SendAction.js FORM_FILETYPE
		"""
		print self.__config["FORM_NAME"]
		print self.__config["BUTTON_NAME"]
		print self.__config["FORM_SEND_FILE"]
		print self.__config["FORM_RECV_FILE"]
		print self.__config["AJAX_RECV_Struct"]
		print self.__config["AJAX_RECV_FILE"]
		print self.__config["SERVELT_NAME"]
		print self.__config["URL_PATH"]
		print self.__config["SAVE_PATH"]
		"""
		x = jstruct.jstruct("","")
		x.read_config()

