# *-* coding=utf-8 *-* 

from jinja2 import Template
from jinja2 import Environment

class out_ctrl:
	def __init__(self):
		self.__out_list = {}
		self.__tab_list = []
		self.initjs_list = []

	def append(self,out_dest,str_in):
		__out_list[out_dest] = str_in

	def exec_out(self,ctrl_tree):
		
		panel_str = ""
		
		self.__tab_list = []
		
		for aCtrl in ctrl_tree:
			if aCtrl["id"] == "main":
				for aline in aCtrl["mainlist"]:
					panel_str = ""
					for a_panel in aline["panellist"]:
						panel_str = panel_str + self.make_panel(a_panel)

					self.__tab_list.append({"id":aline["id"],"rep_str":panel_str})

		return	self.make_all(aCtrl["tpl"])
	def make_panel(self,panel_str):
		
		field_html = ""
		i = 0
		for a_field in panel_str["fieldlist"]:
			if a_field["tpl"] != None:
				if i == 0:
					field_html = field_html+"""<div class="box">"""+a_field["tpl"]["html"]
					i = i+1
				elif i > 1:
					field_html = field_html+a_field["tpl"]["html"]+"""</div>"""
					i = 0
				else:
					field_html = field_html + a_field["tpl"]["html"]
					i = i+1
				self.initjs_list.append(a_field["tpl"]["js"])

		field_reder = Template(panel_str["tpl"]) 
		return field_reder.render({panel_str["id"]:field_html})

	def make_all(self,tpl):
		a_render_dict = {}
		for a_tab in self.__tab_list:
			a_render_dict[a_tab["id"]] = a_tab["rep_str"]
		field_reder = Template(tpl) 
		return field_reder.render(a_render_dict)
		