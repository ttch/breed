# *.* coding=utf-8 *.*


def printAll():
	print "hello"

class Name:
	def __init__(self,t):
		self.nameList = t
	def __radd__(self, other):
		return Name(self.nameList + other.nameList)

class ImportObject:

	def __init__(self):
		self.namesList = {}
	def addName(name):
		self.namesList.append(name)

class ClassList:
	"""
		class Object 
		this is define and collections class
	"""
	def __init__(self , className):
		self.className = className
		self.ImportList = []

	def addImport(self,ImportObject):
		self.ImportList.append(ImportObject)


class classObject:
	"""
		class Object
	"""
	def __init__(self, className):
		self.className = className


"""
	声明无需要计算。
	声明内部的需要计算。
	##çç≈Ωåß∂ƒ©†∑œ¡™£¢∞§¶•ªº–≠·÷æ…¬˚π“‘ø©˙ƒ√∫çµ≈≤Ω≤åß∂ƒ©
"""