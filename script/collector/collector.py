# *-* coding=utf-8 *-*

#用来收集控件和控件关联关系



class colletList:
	def __init__(self):
		self.__con_list = []
	def append(self,item):
		self.__con_list.append(item)
	def get_list(self):
		return self.__con_list

class colletItem:
	def __init__(self):
		#type
		#file_name
		#contents
		self.item = {}
	def add(self,outter,file_name,contents):
		self.item["outter"] = outter
		self.item["file_name"] = file_name
		self.item["contents"] = contents

class colletTreeItem:
	def __init__(self,filename):
		self.items = []
		self.root_name = filename
	def add(self,ownerid,id,type,aItem):
		self.items.append({"id":id,"ownerid":ownerid,"type":type,"contents":aItem})

	def add_file(self,id,js_name,aItem):
		self.items.append({"id":id,"type":"file","file_name":js_name,"contents":aItem})

#单元变量,全局列表
colList = colletList()
#结构体收集器
struList = colletList()
