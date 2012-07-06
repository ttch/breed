# *-* coding=utf-8 *-*

import panel
import input


class ControlFactory:
	def __init__(self,field):
		self.__field = field
	def query(self,child):
		if self.__field["fieldtype"] == "LinearLayout":
			aCtrlVar = panel.LinearLayout(self.__field)
			return aCtrlVar.make(child)
		if self.__field["fieldtype"] == "TableLayout":
			aCtrlVar = panel.TableLayout(self.__field)
			return aCtrlVar.make(child)
		elif self.__field["fieldtype"] == "TableRow":
			aCtrlVar = panel.TableRow(self.__field)
			return aCtrlVar.make(child)
		elif self.__field["fieldtype"] == "ScrollView":
			aCtrlVar = panel.ScrollView(self.__field)
			return aCtrlVar.make(child)
		elif self.__field["fieldtype"] == "input.select":
			aCtrlVar = input.select(self.__field)
			return aCtrlVar.make()
		elif self.__field["fieldtype"] == "input.text":
			aCtrlVar = input.text(self.__field)
			return aCtrlVar.make()
		else:
			return ""
			#print u"不支持此控件定义 %s " % self.__field["fieldtype"] ; assert 0