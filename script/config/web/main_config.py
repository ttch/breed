# *-* coding=utf-8 *-*
import sys
sys.path.append("./script/out")

import out

class main_config:
	def __init__(self,config_dir):
		self.__file_dict = []
		self.__main = []
		self.__pages = []
		self.__mainconfig = {}
		self.__structs = []
		self.__associate = []
		print config_dir
		self.file_handle = open(config_dir+"main.config")
		self.out_obj = out.out_ctrl()

	def __del__ (self):
		pass

	def __init(self):
		self.__target = ""
		for x in self.file_handle.readlines():
			if x[0] == "#":
				continue
			else:
				self.__file_dict.append(x[0:-1])

		self.__init_main()
		self.__init_page()
		self.__init_structs()
		self.__init_associate()

	def __init_main(self):
		iread = 0

		for x in self.__file_dict:
			if x == "--main--":
				iread = 1
				continue
			if iread == 1:
				if x == "--end--":
					return
				else:
					self.__main.append(x)


	def __init_page(self):
		iread = 0

		for x in self.__file_dict:
			if x == "--page--":
				iread = 1
				continue
			if iread == 1:
				if x == "--end--":
					return
				else:
					self.__pages.append(x)

	def __init_structs(self):
		iread = 0

		for x in self.__file_dict:
			if x == "--struct--":
				iread = 1
				continue
			if iread == 1:
				if x == "--end--":
					return
				else:
					self.__structs.append(x)

	def __init_associate(self):
		iread = 0

		for x in self.__file_dict:
			if x == "--associate--":
				iread = 1
				continue
			if iread == 1:
				if x == "--end--":
					return
				else:
					self.__associate.append(x)

	def get_pages(self):
		return self.__pages

	def get_main(self):
		return self.__main

	def read_all(self):
		self.__init()
		for x in self.__main:
			aline = x.split("=")
			self.__mainconfig[aline[0]] = aline[1]

	def get_machine_type(self):
		return self.__mainconfig["machine"]

	def get_tpldir(self):
		tpl_dir = self.__mainconfig["main_dir"]+"\\"+self.__mainconfig["tpl_dir"]+"\\"+self.__mainconfig["tpl_name"]+"\\"
		return tpl_dir

	def get_page_config_dir(self):
		return self.__mainconfig["main_dir"]+"\\"+self.__mainconfig["config_dir"]+"\\"+self.__mainconfig["project_name"]+"\\"

	def get_strcuts(self):
		return self.__structs

	def get_associate(self):
		return self.__associate
	def get_outdir(self):
		return self.__mainconfig["out_dir"]



