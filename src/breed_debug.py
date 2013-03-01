# *.* coding=utf-8 *.*
import global_var


def log( s ):
	if global_var.is_debug == True:
		print s

def logs( s , t ):
	if global_var.is_debug == True:
		print s % t