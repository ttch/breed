# *-* coding=utf-8 *-*
#main program
# breed system 1.0
# author by zhao_nf
#
import sys
import datetime




sys.path.append(".\\script\\analysis\\struct_processer")
sys.path.append(".\\script\\analysis\\database")
sys.path.append(".\\script\\analysis\\struct_processer\\JSON.struct")
sys.path.append(".\\script\\analysis\\struct_processer\\JSON.struct\\send")

#breed 关系语言模块
sys.path.append(".\\script\\analysis\\Associate")
sys.path.append(".\\script\\analysis\\Associate\\run_time")
#数据库模块
sys.path.append(".\\script\\database\\oracle_db")



#收集器模块
sys.path.append(".\\script\\collector")
#输出模块
sys.path.append(".\\script\\out")
sys.path.append(".\\script\\out\\json\\servlet")
sys.path.append(".\\script\\out\\json\\web")

#配置模块
sys.path.append('.\\script\\config\\web')
sys.path.append(".\\script\\config\\android")



import main_config,page_config,menu_config,database_config,struct_config,associate_config

import collector
import web_outter
import struct_processer,associate_processer
import oracle_db
import servlet_outter
import outter

#脚本系统
import breed_lex
import breed_yacc
import breed_interpreter
import reader





out_list = []


def new_web_process(var_main):
	for avar in var_main.get_pages():
		aPageStr = avar.split("|")
		print u"Compiling %s unit..............................." % aPageStr[0]
		d1 = datetime.datetime.now()

		var_page = page.page(
								 reader.Compile(var_main.get_page_config_dir()+"page\\"+aPageStr[1]),
								 aPageStr[0]
								 )


		f = open(var_page.out,"w")
		f.write( var_page.make().encode("utf-8") )
		f.close()
		d2 = datetime.datetime.now()
		d = d2-d1
		print u"Compiled %s unit..................................\nCompile Time is--%s" % ( aPageStr[0],str(d) )

def new_android_process(var_main):
	for avar in var_main.get_pages():
		aPageStr = avar.split("|")
		print u"Compiling %s unit..............................." % aPageStr[0]
		d1 = datetime.datetime.now()

		var_page = page.page(
								 reader.Compile(var_main.get_page_config_dir()+"page\\"+aPageStr[1]),
								 aPageStr[0]
								 )


		f = open(var_page.out,"w")
		f.write( var_page.make().encode("utf-8") )
		f.close()
		d2 = datetime.datetime.now()
		d = d2-d1
		print u"Compiled %s unit..................................\nCompile Time is--%s" % ( aPageStr[0],str(d) )


import global_var

var_main = global_var.var_main



if __name__ == "__main__":
	"""
		read main.config
		send main.config var to project
		project dit func page
	"""


	var_main.read_all()

	#android 处理
	if var_main.get_machine_type() == "android":
		sys.path.append('.\\script\\out\\android\\UIpage')
		sys.path.append(".\\script\\out\\android\\UICOM")
		import page
		import menu
		new_android_process(var_main)
	#web 处理
	else:
		#web界面模块
		sys.path.append('.\\script\\out\\web\\UIpage')
		sys.path.append(".\\script\\out\\web\\UICOM")
		import page
		import menu
		new_web_process(var_main)



