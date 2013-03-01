# *-* coding=utf-8 *-*

import sys
sys.path.append("./src")

from global_var import g_project_dir
import breed_debug as debug



import breed_intep

def main():
    breed_intep.compile(g_project_dir+"component/interface/plc.brd")

if __name__ == "__main__":
	#try:
		main()
	#except Exception,ex:
	#	print u"异常 %s " % ( ex )
