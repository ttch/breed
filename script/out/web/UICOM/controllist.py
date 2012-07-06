# *-* coding=utf-8 *-*

import combbox
import text
import intctrl
import floatctrl
import button
import panel
import frame
import menu

class ControlFactory:
	def __init__(self,field):
		self.__field = field
	def query(self,child):
		if self.__field["fieldtype"] == "PANEL":
			aCtrlVar = panel.panel_control(self.__field)
			return aCtrlVar.make(child)
		if self.__field["fieldtype"] == "TAB":
			aCtrlVar = panel.panel_control(self.__field)
			return aCtrlVar.make(child)
		elif self.__field["fieldtype"] == "input.text":
			aCtrlVar = text.text(self.__field)
			return aCtrlVar.make()
		elif self.__field["fieldtype"] == "FRAMESET":
			aCtrlVar = frame.frameset(self.__field)
			return aCtrlVar.make(child)
		elif self.__field["fieldtype"] == "FRAME":
			aCtrlVar = frame.frame(self.__field)
			return aCtrlVar.make()
		elif self.__field["fieldtype"] == "MENUITEM":
			aCtrlVar = menu.menuitem(self.__field)
			return aCtrlVar.make(child)
		elif self.__field["fieldtype"] == "MENUSET":
			aCtrlVar = menu.menuset(self.__field)
			return aCtrlVar.make(child)
		elif self.__field["fieldtype"] == "SUBMENU":
			aCtrlVar = menu.submenu(self.__field)
			return aCtrlVar.make(child)
		else:
			print u"不支持此控件定义 %s " % self.__field["fieldtype"] ; assert 0