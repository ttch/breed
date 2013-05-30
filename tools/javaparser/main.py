#*.* coding=utf-8 *.*

import sys

sys.path.append("../../src")
sys.path.append("../../")

import lex
import file_
import yacc
def help():
	print """
java parser v0.0.2
author by zhao_nf
command line is main.py -shortoptions args
example : python main.py --file $HOME/project/xxxx.java
	"""
def getopts():
	try:
		import getopt
		opts, args = getopt.getopt(sys.argv[1:], "", ["file=", "version","help","debug"])
	except getopt.GetoptError as err:
		# print help information and exit:
		print str(err) # will print something like "option -a not recognized"
		sys.exit(2)
	filename = ""
	debug = False
	for o,a in opts:
		if o == "--file":
			filename = a
		if o == "--help":
			help()
		if o == "--version":
			help()
		if o == "--debug":
			debug = True

	main(filename,debug)

def main(filename,debug=False):
	lexer = lex.getlex()

	s = file_.getSource( filename )

	lexer.input(s)
	yacc.get_yacc(lexer,filename,debug)

	#for x in file_.getTokenList(lexer):
	#	print x
if __name__ == "__main__":
	getopts()
