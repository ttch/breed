#*.* coding=utf-8 *.*

import sys

sys.path.append("../../src")
sys.path.append("../../")

import lex
import file_
import yacc

def main(filename):
	lexer = lex.getlex()

	s = file_.getSource( filename )

	lexer.input(s)
	yacc.get_yacc(lexer)

	#for x in file_.getTokenList(lexer):
	#	print x
if __name__ == "__main__":
	main('./java.y')
