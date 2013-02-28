# *.* coding=utf-8 *.*

import file_


# import package datastruct
class package:
	def __init__( self , name ):
		self.requrelist = []
		self.packagename = name.split(".")[-1]
		self.packagefile = file_.importname_filename(name)
		self.packageFullName = name

	def isrequre( self , name ):
		return ( name in self.requrelist )

	def add_requre( self , pkgname ):
		self.requrelist.append( pkgname )
