#*.* coding=utf-8 *.*

import sys

sys.path.append("../../src")
sys.path.append("../../")

import lex
import file_
import yacc

def main(filename):
	lexer = lex.getlex()
	#f = open("./result.txt","w")
	#sys.stderr = f
	#try:
	s = file_.getSource( filename )

	lexer.input(s)
	yacc.get_yacc(lexer)
	#finally:
		#f.close()
	#for x in file_.getTokenList(lexer):
	#	print x
if __name__ == "__main__":
	main('./Java.y')
