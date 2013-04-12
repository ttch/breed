#*.* coding=utf-8 *.*

import sys

sys.path.append("../../src")
sys.path.append("../../")

import lex
import file_
import yacc


def help():
	print """
antlr parser v0.0.1
author by zhao_nf
command line is convy.py -shortoptions args
example : python convy.py --file $HOME/project/xxxx.y $HOME/java/xxx.py
	"""
def getopts():
	try:
		import getopt
		opts, args = getopt.getopt(sys.argv[1:], "", ["file=","outfile=", "version","help"])
	except getopt.GetoptError as err:
		# print help information and exit:
		print str(err) # will print something like "option -a not recognized"
		sys.exit(2)
	filename = ""
	outfilename = ""
	for o,a in opts:
		if o == "--file":
			filename = a
		if o == "--outfile":
			outfilename = a
		if o == "--help":
			help()
		if o == "--version":
			help()
	if filename != "" and outfilename != "":
		main(filename,outfilename)
	else:
		help()


def main(filename,outfile):
	lexer = lex.getlex()
	#f = open("./result.txt","w")
	#sys.stderr = f
	#try:
	s = file_.getSource( filename )

	lexer.input(s)
	yacc.get_yacc(lexer,outfile)
	#finally:
		#f.close()
	#for x in file_.getTokenList(lexer):
	#	print x
if __name__ == "__main__":
	getopts()
