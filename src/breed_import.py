



class b_import:
	def __init__(self):
		#import module list
		self.import_list = {}

	def add(self,token,stat):
		pass
		#call component

def compile(token,stat):
	if token.value not in g_import.import_list:
		g_import.import_list[token.value] = g_import.add(token.value,stat)


g_import = b_import()
