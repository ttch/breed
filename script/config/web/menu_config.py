# *-* coding=utf-8 *-*


class menu_config:
	def __init__(self,main_object):
		self.__main_object = main_object
		self.__file_dict = []
		self.__menu_name = []
		self.__out_name = []
	def __del__ (self):
		self.__file_dict = []

	def __init(self):
		return
	def __read__outname(self):
		iread = 0
		self.__out_name = []
		for x in self.__file_dict:
			if x == "--out--":
				iread = 1
				continue
			if iread == 1:
				if x == "--end--":
					return
				else:
					self.__out_name.append(x)

	def __read__menu(self):
		iread = 0
		self.__tab_panel = []
		for x in self.__file_dict:
			if x == "--menu--":
				iread = 1
				continue
			if iread == 1:
				if x == "--end--":
					return
				else:
					self.__menu_name.append(x)


	def read_all(self):
		self.__init()

		var_file = open(self.__main_object.get_page_config_dir()+"menu\\""menu.config")
		for var_line in var_file.readlines():
			if var_line[0] == "#":
				continue
			else:
				self.__file_dict.append(var_line[0:-1])

		self.__read__outname()
		self.__read__menu()

		var_file.close

	def get_menu(self):
		return self.__menu_name