#*.* coding=utf-8 *.*

import sys

sys.path.append("../../src")
sys.path.append("../../")

import lex
import file_

def main(filename):
	lexer = lex.getlex()

	s = file_.getSource( filename )

	lexer.input(s)
	for x in file_.getTokenList(lexer):
		print x
if __name__ == "__main__":
	main('/Users/zhaonf/program/insurance/src/main/java/com/itec/stis/dao/as/CertNoChangeDao.java')
