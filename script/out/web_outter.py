# *-* coding=utf-8 *-*

#新版本程序分析输出器

from jinja2 import Template
from jinja2 import Environment
import interface_outter

def new_outer(col_list):
	avar = outter(col_list)

def write_file(filename,write_str):
	x = open(filename,"w")
	x.write(write_str)
	x.close

#类web_outter
#用途：输出成web用的网页格式代码

class web_outter(interface_outter.abs_outter):
	def __init__(self,col_list):
		for x in col_list.get_list():
			self.__out_list = {}
			self.__tab_list = {}

			#暂时只支持一个tab 暂时不支持分TAB
			self.__tab_str = ""
			self.initjs_list = []
			self.initjs_filename = ""
			self.head_begin = ""
			self.head_end = ""
			self.change(x)
	def change(self,aPage):
		for a in aPage.items:
			if a["type"] == "tab":
				self.ay_tab(a["id"],a["contents"])
			elif a["type"] == "panel":
				self.ay_panel(a["id"],a["ownerid"],a["contents"])
			elif a["type"] == "field":
				self.ay_field(a["id"],a["ownerid"],a["contents"])
			elif a["type"] == "file":
				self.initjs_filename = a["file_name"]
			elif a["type"] == "head_begin":
				self.head_begin = a["contents"]
			elif a["type"] == "head_end":
				self.head_end = a["contents"]
			"""
			elif a["type"] == "form":
				print "form"
			elif a["type"] == "js":
				print "js"
			elif a["type"] == "owner_js":
				print "owner_js"
			elif a["type"] == "button":
				print "button"
			elif a["type"] == "menu":
				print "menu"
			elif a["type"] == "treemenu":
				print "treemenu"
			elif a["type"] == "WEB_INF":
				print "WEB_INF"
			elif a["type"] == "sevlet":
				print "sevlet"
			elif a["type"] == "table":
				print "table"
			elif a["type"] == "struct":
				print "struct"
			"""
		self.make(aPage)
	#系统支持以下多种程序
	def ay_tab(self,tab_id,tab_str):
		for x in tab_id:
			self.__tab_list[x] = []
		self.__tab_str = tab_str
		self.initjs_list.append(tab_str["js"])

	def ay_panel(self,panel_id,owner_id,panel_str):
		for x in self.__tab_list:
			if x == owner_id:
				self.__tab_list[x].append({"id":panel_id,"contents":panel_str,"field":[]})

	def ay_form():
		pass
	def ay_js():
		pass
	def ay_owner_js():
		pass
	def ay_field(self,field_id,owner_id,field_str):
		for x in self.__tab_list:
			for y in self.__tab_list[x]:
				if y["id"] == owner_id:
					y["field"].append({"id":field_id,"contents":field_str})
	def ay_button():
		pass
	def ay_menu():
		pass
	def ay_treemenu():
		pass
	def ay_WEB_INF():
		pass
	def ay_sevlet():
		pass
	def ay_struct():
		pass
	def ay_table():
		pass
	def make(self):
		pass
	def make(self,aPageObj):
		tab_list = {}
		for a_tab in self.__tab_list:
			a_panel_str = ""
			for a_panel in self.__tab_list[a_tab]:
				a_str = ""
				i = 0
				for a_field in a_panel["field"]:
					if a_field["contents"] != None:
						if i == 0:
							a_str = a_str+"""<div class="box">"""+a_field["contents"]["html"]
							i = i+1
						elif i > 1:
							a_str = a_str+a_field["contents"]["html"]+"""</div>"""
							i = 0
						else:
							a_str = a_str+a_field["contents"]["html"]
							i = i+1
						self.initjs_list.append(a_field["contents"]["js"])
				a_panel_str = a_panel_str+self.replace_id(a_panel["id"],a_panel["contents"],a_str)
			tab_list[a_tab] = a_panel_str
		#写文件
		page_str = self.head_begin + self.replace_tab(tab_list,self.__tab_str) + self.head_end
		write_file(aPageObj.root_name,page_str.encode("utf-8"))
		write_file(self.initjs_filename,self.get_init_js())

	def replace_id (self,id,str,tpl_str):
		field_reder = Template(tpl_str)
		return field_reder.render({id:str})

	def replace_tab(self,ids,tpl_str):
		field_reder = Template(tpl_str["html"])
		return field_reder.render(ids)

	def get_init_js(self):
		str = ""
		str = "$(function() {"
		for x in self.initjs_list:
			str = str + x
		str = str + "});"
		return str
	def out(self):
		pass