# *.* coding=utf-8 *.*

import file_
import breed_debug as debug


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
		debug.logs( " add to package : %s " , ( pkgname ))
		self.requrelist.append( pkgname )

	def isRequred( self , name ):
		return ( name in self.requrelist )
