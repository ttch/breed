# *-* coding=utf-8 *-*

import sys
sys.path.append(".\\src")

from global_var import g_project_dir



import breed_intep


if __name__ == "__main__":
	#try:
	breed_intep.Compile(g_project_dir+"component\\interface\\plc.brd")
	#except Exception,ex:
	#	print u"异常 %s " % ( ex)
