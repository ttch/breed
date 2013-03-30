# *.* coding=utf-8 *.*

import ply.yacc as yacc
import lex
from collections import deque

tokens = lex.tokens


def p_compilationUnit( p ):
	'''
		p_compilationUnit : annotations packageDeclaration importDeclarations typeDeclarations
		| annotations packageDeclaration typeDeclarations
		| annotations packageDeclaration importDeclarations
		| annotations packageDeclaration
		| annotations classOrInterfaceDeclaration typeDeclarations
		| packageDeclaration importDeclarations typeDeclarations
		| packageDeclaration  typeDeclarations
		| packageDeclaration importDeclarations 
		| packageDeclaration
		| importDeclarations typeDeclarations
		| importDeclarations
		| typeDeclarations
		| empty

	'''
	pass

def p_importDeclarations( p ):
	'''
		importDeclarations : importDeclaration
						| importDeclarations importDeclaration
	'''
	pass

def p_typeDeclarations( p ):
	'''
		typeDeclarations : typeDeclaration
					| typeDeclarations typeDeclaration
	'''
	pass

def p_packageDeclaration( p ):
    '''
		packageDeclaration :   PACKAGE qualifiedName SEMI
    '''

def p_importDeclaration( p ):
	'''
		importDeclaration : IMPORT STATIC qualifiedName importDle SEMI
						|  IMPORT qualifiedName SEMI
						|  IMPORT STATIC qualifiedName SEMI
						|  IMPORT qualifiedName importDle SEMI
	'''

def p_typeDeclaration( p ):
	'''
		typeDeclaration : classOrInterfaceDeclaration
						| SEMI
	'''

def p_classOrInterfaceDeclaration( p ):
	'''
		classOrInterfaceDeclaration : classOrInterfaceModifiers classOrInterfaceBody
	'''

def p_classOrInterfaceBody( p ):
	'''
		classOrInterfaceBody : classDeclaration
							| interfaceDeclaration
	'''
def p_classOrInterfaceModifiers( p ):
	'''
		classOrInterfaceModifiers : classOrInterfaceModifier
								| empty
	'''
def p_classOrInterfaceModifier( p ):
	'''
	 	classOrInterfaceModifier :  annotation 
							| PUBLIC 
							| PROTECTED 
							| PRIVATE 
							| ABSTRACT 
							| STATIC 
							| FINAL 
							| STRICTFP
	'''
	pass

def p_modifiers( p ):
	'''
		modifiers : modifier
				| empty
	'''
def p_classDeclaration( p ):
	'''
		classDeclaration : normalClassDeclaration
    					|   enumDeclaration	
	'''

def p_normalClassDeclaration( p ):
    '''
	normalClassDeclaration : CLASS Identifier typeParameters extend_expr implement_expr  classBody
		| CLASS Identifier   classBody
		| CLASS Identifier typeParameters   classBody
		| CLASS Identifier typeParameters extend_expr  classBody
		| CLASS Identifier typeParameters implement_expr  classBody
		| CLASS Identifier  extend_expr implement_expr  classBody
		| CLASS Identifier  extend_expr  classBody
		| CLASS Identifier  implement_expr  classBody
	'''

def p_typeParameters
	'''
    	typeParameters :   LESS typeParameter typeParameter_extend MORE
    '''
def p_typeParameter_extend( p ):
	'''
		typeParameter_extend : DOT typeParameter
		| typeParameter_extend DOT typeParameter
		| empty
	'''



def p_extend_expr( p ):
	'''
		extend_expr : EXTENDS type
	'''

def p_implement_expr(p ):
	'''
		implement_expr : IMPLEMENTS typeList
	'''

def p_importDle( p ):
	'''
		importDle : '.' '*'
	'''





def p_FloatingPointLiteral( p ):
	'''
		FloatingPointLiteral : NON_INTEGER_1
					| NON_INTEGER_2
					| NON_INTEGER_3
	'''
	pass

def p_integerLiteral(p):
	'''
		integerLiteral : NUMBER 
					| HEX_NUMBER
					| LONG_NUMBER
					| LONG_HEX_NUMBER
	'''
	pass


	#### Empty
   
def p_empty( p ):
	'''empty : '''

#### Catastrophic error handler

def p_error(p):
	if p:
		print "Syntax error at '%s' lineno = %i linepos=%i" %  ( p.value , p.lineno , p.lexpos )
	else:
		print "Syntax error at EOF"

def get_yacc(l):
	b = yacc.yacc()

	b.error = 0
	result = b.parse(lexer = l , debug=2)
	if b.error : return None
