# *-* coding=utf-8 *-*

# page read config
class page_config:

	
	def __init__(self,page_object,main_config):
		self.page_object = page_object
		self.__main_config = main_config
		self.__file_dict = []
		
		self.__tab_panel = []
		self.__panel = []
		self.__field = []
		self.__form = []
		
		self.__out_name = []
		self.__pageconfig = {}
	def __del__ (self):
		self.__file_dict = []
	
	def __init(self):
		page_str = self.page_object.split("|")
		self.name = page_str[0]
	def __read__form(self):
		iread = 0
		self.__form = []
		for x in self.__file_dict:
			if x == "--form--":
				iread = 1
				continue
			if iread == 1:
				if x == "--end--":
					return
				else:
					self.__form.append(x)
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
	def __read__tab(self):
		iread = 0
		self.__tab_panel = []
		for x in self.__file_dict:
			if x == "--maintab--":
				iread = 1
				continue
			if iread == 1:
				if x == "--end--":
					return
				else:
					self.__tab_panel.append(x)

	def __read__panel(self):
		iread = 0
		self.__panel = []
		for x in self.__file_dict:
			if x == "--mainpanel--":
				iread = 1
				continue
			if iread == 1:
				if x == "--end--":
					return
				else:
					self.__panel.append(x)

	def __read__field(self):
		iread = 0
		self.__field = []
		for x in self.__file_dict:
			if x == "--fieldpanel--":
				iread = 1
				continue
			if iread == 1:
				if x == "--end--":
					return
				else:
					self.__field.append(x)
	
	def read_all(self):
		self.__init()
		var_file = open(self.__main_config.get_page_config_dir()+"page\\"+self.name)
		for var_line in var_file.readlines():
			if var_line[0] == "#":
				continue
			else:
				self.__file_dict.append(var_line[0:-1])
		
		self.__read__outname()
		self.__read__tab()
		self.__read__panel()
		self.__read__field()
		self.__read__form()

		for x in self.__out_name:
			aline = x.split("=")
			self.__pageconfig[aline[0]] = aline[1]
			
		
		var_file.close
		var_file = None
	
	def get_tab(self):
		return self.__tab_panel
		
	def get_panel(self):
		return self.__panel

	def get_field(self):
		return self.__field
	def get_form(self):
		return self.__form

	def get_outname(self):
		return self.__pageconfig["out_dir"]+self.__pageconfig["out_name"]
	
	def get_js_init_outname(self):
		return self.__pageconfig["out_dir"]+self.__pageconfig["init_js"]
	
	def add_js_init(self):
		return "<script src=\""+self.__pageconfig["init_js"]+"\"></script>"