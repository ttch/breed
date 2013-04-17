# *.* coding=utf-8 *.*

#/*
# [The "BSD licence"]
# Copyright (c) 2007-2008 Terence Parr
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. The name of the author may not be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#*/
#/** A Java 1.5 grammar for ANTLR v3 derived from the spec
# *
# *  This is a very close representation of the spec; the changes
# *  are comestic (remove left recursion) and also fixes (the spec
# *  isn't exactly perfect).  I have run this on the 1.4.2 source
# *  and some nasty looking enums from 1.5, but have not really
# *  tested for 1.5 compatibility.
# *
# *  I built this with: java -Xmx100M org.antlr.Tool java.g 
# *  and got two errors that are ok (for now):
# *  java.g:691:9: Decision can match input such as
# *    "'0'..'9'{'E', 'e'}{'+', '-'}'0'..'9'{'D', 'F', 'd', 'f'}"
# *    using multiple alternatives: 3, 4
# *  As a result, alternative(s) 4 were disabled for that input
# *  java.g:734:35: Decision can match input such as "{'$', 'A'..'Z',
# *    '_', 'a'..'z', '\u00C0'..'\u00D6', '\u00D8'..'\u00F6',
# *    '\u00F8'..'\u1FFF', '\u3040'..'\u318F', '\u3300'..'\u337F',
# *    '\u3400'..'\u3D2D', '\u4E00'..'\u9FFF', '\uF900'..'\uFAFF'}"
# *    using multiple alternatives: 1, 2
# *  As a result, alternative(s) 2 were disabled for that input
# *
# *  You can turn enum on/off as a keyword :)
# *
# *  Version 1.0 -- initial release July 5, 2006 (requires 3.0b2 or higher)
# *
# *  Primary author: Terence Parr, July 2006
# *
# *  Version 1.0.1 -- corrections by Koen Vanderkimpen & Marko van Dooren,
# *      October 25, 2006;
# *      fixed normalInterfaceDeclaration: now uses typeParameters instead
# *          of typeParameter (according to JLS, 3rd edition)
# *      fixed castExpression: no longer allows expression next to type
# *          (according to semantics in JLS, in contrast with syntax in JLS)
# *
# *  Version 1.0.2 -- Terence Parr, Nov 27, 2006
# *      java spec I built this from had some bizarre for-loop control.
# *          Looked weird and so I looked elsewhere...Yep, it's messed up.
# *          simplified.
# *
# *  Version 1.0.3 -- Chris Hogue, Feb 26, 2007
# *      Factored out an annotationName rule and used it in the annotation rule.
# *          Not sure why, but typeName wasn't recognizing references to inner
# *          annotations (e.g. @InterfaceName.InnerAnnotation())
# *      Factored out the elementValue section of an annotation reference.  Created 
# *          elementValuePair and elementValuePairs rules, then used them in the 
# *          annotation rule.  Allows it to recognize annotation references with 
# *          multiple, comma separated attributes.
# *      Updated elementValueArrayInitializer so that it allows multiple elements.
# *          (It was only allowing 0 or 1 element).
# *      Updated localVariableDeclaration to allow annotations.  Interestingly the JLS
# *          doesn't appear to indicate this is legal, but it does work as of at least
# *          JDK 1.5.0_06.
# *      Moved the Identifier portion of annotationTypeElementRest to annotationMethodRest.
# *          Because annotationConstantRest already references variableDeclarator which 
# *          has the Identifier portion in it, the parser would fail on constants in 
# *          annotation definitions because it expected two identifiers.  
# *      Added optional trailing ';' to the alternatives in annotationTypeElementRest.
# *          Wouldn't handle an inner interface that has a trailing ';'.
# *      Swapped the expression and type rule reference order in castExpression to 
# *          make it check for genericized casts first.  It was failing to recognize a
# *          statement like  "Class<Byte> TYPE = (Class<Byte>)...;" because it was seeing
# *          'Class<Byte' in the cast expression as a less than expression, then failing 
# *          on the '>'.
# *      Changed createdName to use typeArguments instead of nonWildcardTypeArguments.
# *          Again, JLS doesn't seem to allow this, but java.lang.Class has an example of
# *          of this construct.
# *      Changed the 'this' alternative in primary to allow 'identifierSuffix' rather than
# *          just 'arguments'.  The case it couldn't handle was a call to an explicit
# *          generic method invocation (e.g. this.<E>doSomething()).  Using identifierSuffix
# *          may be overly aggressive--perhaps should create a more constrained thisSuffix rule?
# *      
# *  Version 1.0.4 -- Hiroaki Nakamura, May 3, 2007
# *
# *  Fixed formalParameterDecls, localVariableDeclaration, forInit,
# *  and forVarControl to use variableModifier* not 'final'? (annotation)?
# *
# *  Version 1.0.5 -- Terence, June 21, 2007
# *  --a[i].foo didn't work. Fixed unaryExpression
# *
# *  Version 1.0.6 -- John Ridgway, March 17, 2008
# *      Made "assert" a switchable keyword like "enum".
# *      Fixed compilationUnit to disallow "annotation importDeclaration ...".
# *      Changed "Identifier ('.' Identifier)*" to "qualifiedName" in more 
# *          places.
# *      Changed modifier* and/or variableModifier* to classOrInterfaceModifiers,
# *          modifiers or variableModifiers, as appropriate.
# *      Renamed "bound" to "typeBound" to better match language in the JLS.
# *      Added "memberDeclaration" which rewrites to methodDeclaration or 
# *      fieldDeclaration and pulled type into memberDeclaration.  So we parse 
# *          type and then move on to decide whether we're dealing with a field
# *          or a method.
# *      Modified "constructorDeclaration" to use "constructorBody" instead of
# *          "methodBody".  constructorBody starts with explicitConstructorInvocation,
# *          then goes on to blockStatement*.  Pulling explicitConstructorInvocation
# *          out of expressions allowed me to simplify "primary".
# *      Changed variableDeclarator to simplify it.
# *      Changed type to use classOrInterfaceType, thus simplifying it; of course
# *          I then had to add classOrInterfaceType, but it is used in several 
# *          places.
# *      Fixed annotations, old version allowed "@X(y,z)", which is illegal.
# *      Added optional comma to end of "elementValueArrayInitializer"; as per JLS.
# *      Changed annotationTypeElementRest to use normalClassDeclaration and 
# *          normalInterfaceDeclaration rather than classDeclaration and 
# *          interfaceDeclaration, thus getting rid of a couple of grammar ambiguities.
# *      Split localVariableDeclaration into localVariableDeclarationStatement
# *          (includes the terminating semi-colon) and localVariableDeclaration.  
# *          This allowed me to use localVariableDeclaration in "forInit" clauses,
# *           simplifying them.
# *      Changed switchBlockStatementGroup to use multiple labels.  This adds an
# *          ambiguity, but if one uses appropriately greedy parsing it yields the
# *           parse that is closest to the meaning of the switch statement.
# *      Renamed "forVarControl" to "enhancedForControl" -- JLS language.
# *      Added semantic predicates to test for shift operations rather than other
# *          things.  Thus, for instance, the string "< <" will never be treated
# *          as a left-shift operator.
# *      In "creator" we rule out "nonWildcardTypeArguments" on arrayCreation, 
# *          which are illegal.
# *      Moved "nonWildcardTypeArguments into innerCreator.
# *      Removed 'super' superSuffix from explicitGenericInvocation, since that
# *          is only used in explicitConstructorInvocation at the beginning of a
# *           constructorBody.  (This is part of the simplification of expressions
# *           mentioned earlier.)
# *      Simplified primary (got rid of those things that are only used in
# *          explicitConstructorInvocation).
# *      Lexer -- removed "Exponent?" from FloatingPointLiteral choice 4, since it
# *          led to an ambiguity.
# *
# *      This grammar successfully parses every .java file in the JDK 1.5 source 
# *          tree (excluding those whose file names include '-', which are not
# *          valid Java compilation units).
# *
# *  Known remaining problems:
# *      "Letter" and "JavaIDDigit" are wrong.  The actual specification of
# *      "Letter" should be "a character for which the method
# *      Character.isJavaIdentifierStart(int) returns true."  A "Java 
# *      letter-or-digit is a character for which the method 
# *      Character.isJavaIdentifierPart(int) returns true."
# */
#
# convert by openjdk 1.5 grammar file
#
# author by zhao_nf ( ttchgm@gmail.com )
#
# [The "BSD licence"]
# Copyright (c) 2011- zhao_nf
# All rights reserved.

import ply.yacc as yacc
import lex
from collections import deque

tokens = lex.tokens


#compilationUnit
#    :   annotations
#        (   packageDeclaration (importDeclaration)* (typeDeclaration)*
#        |   classOrInterfaceDeclaration (typeDeclaration)*
#        )
#    |   (packageDeclaration)? (importDeclaration)* (typeDeclaration)*
#    ;
def p_compilationUnit(p):
	'''
	 compilationUnit : annotations packageDeclaration importDeclarations typeDeclarations
		| annotations packageDeclaration importDeclarations
		| annotations packageDeclaration typeDeclarations
		| annotations packageDeclaration
		| annotations classOrInterfaceDeclaration typeDeclarations
		| annotations classOrInterfaceDeclaration
		| packageDeclaration importDeclarations typeDeclarations
		| packageDeclaration importDeclarations 
		| packageDeclaration typeDeclarations
		| packageDeclaration
		|
	'''

	pass

def p_importDeclarations(p):
	'''
	 importDeclarations : importDeclaration
		| importDeclarations importDeclaration
	'''

	pass


def p_typeDeclarations(p):
	'''
	 typeDeclarations : typeDeclaration
		| typeDeclarations typeDeclaration
	'''

	pass

def p_packageDeclaration_once(p):
	'''
		packageDeclaration_once : packageDeclaration
								| 
	'''


def p_packageDeclaration(p):
	'''
	 packageDeclaration :  PACKAGE qualifiedName SEMI
	'''

	pass

def p_STATIC_empty(p):
	'''
		STATIC_empty : STATIC
					 | 
	'''

def p_DOT_MULT(p):
	'''
		DOT_MULT : DOT MULT 
	'''

#   'import' ('static')? qualifiedName ('.' '*')? ';'
def p_importDeclaration(p):
	'''
	 importDeclaration : IMPORT STATIC qualifiedName SEMI
						| IMPORT qualifiedName SEMI
	'''

	pass


def p_typeDeclaration(p):
	'''
	 typeDeclaration :  classOrInterfaceDeclaration 
	| SEMI
	'''

	pass


def p_classOrInterfaceDeclaration(p):
	'''
	 classOrInterfaceDeclaration : classOrInterfaceModifiers classDeclaration
	 							| classDeclaration
	 							| classOrInterfaceModifiers interfaceDeclaration
								| interfaceDeclaration
	'''

	pass

def p_classOrInterfaceModifiers(p):
	'''
	 classOrInterfaceModifiers : classOrInterfaceModifier
	 							| classOrInterfaceModifiers classOrInterfaceModifier
	'''

	pass


def p_classOrInterfaceModifier(p):
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

def p_modifiers(p):
	'''
	 modifiers : modifier
	 		| modifiers modifier
	'''

	pass


def p_classDeclaration(p):
	'''
	 classDeclaration :  normalClassDeclaration 
	| enumDeclaration
	'''

	pass

def p_ExtendType(p):
	'''
		ExtendType : EXTENDS type
					|
	'''

def p_IMPLEMENTS_typeList(p):
	'''
		IMPLEMENTS_typeList : IMPLEMENTS typeList
							|
	'''

def p_normalClassDeclaration(p):
	'''
	 normalClassDeclaration : CLASS Identifier typeParameters ExtendType IMPLEMENTS_typeList  classBody
	'''

	pass


def p_dotTypeParameter(p):
	'''
		dotTypeParameter : COMMA typeParameter
	'''
def p_dotTypeParameters(p):
	'''
		dotTypeParameters : dotTypeParameter
						| dotTypeParameters dotTypeParameter
	'''

def p_typeParameters(p):
	'''
	 typeParameters : LESS typeParameter dotTypeParameters MORE
		| LESS typeParameter MORE
		|
	'''

	pass

def p_EXTENDS_typeBound(p):
	'''
		EXTENDS_typeBound : EXTENDS typeBound
						| 
	'''

def p_typeParameter(p):
	'''
	 typeParameter : Identifier EXTENDS_typeBound
	'''

	pass

def p_and_type(p):
	'''
		and_type : AND type
	'''

def p_and_types(p):
	'''
	 and_types : and_type
		| and_types and_type
	'''

	pass

def p_typeBound(p):
	'''
	 typeBound : type and_types
		| type
	'''

	pass


def p_enumDeclaration(p):
	'''
	 enumDeclaration : ENUM Identifier IMPLEMENTS_typeList enumBody
	'''

	pass

#enumBody
#    :   '{' (enumConstants)? ','? enumBodyDeclarations? '}'
#    ;

def p_enumBody(p):
	'''
	 enumBody : BLPAREN enumConstants enumBodyDeclarations BRPAREN
	 		| BLPAREN enumConstants BRPAREN
			| BLPAREN enumBodyDeclarations BRPAREN
			| BLPAREN BRPAREN
	'''

	pass

def p_COMMA_enumConstant(p):
	'''
		COMMA_enumConstant : COMMA enumConstant
							| COMMA
	'''

def p_COMMA_enumConstants(p):
	'''
	 COMMA_enumConstants : COMMA_enumConstant
		| COMMA_enumConstant COMMA_enumConstants
	'''

	pass


def p_enumConstants(p):
	'''
	 enumConstants : enumConstant COMMA_enumConstants
		| enumConstant 
	'''

	pass


def p_annotations_once(p):
	'''
		annotations_once : annotations
						| empty
	'''

def p_arguments_once(p):
	'''
		arguments_once : arguments
						| 
	'''

def p_classBody_once(p):
	'''
		classBody_once : classBody
						| 
	'''

def p_enumConstant(p):
	'''
	 enumConstant : annotations_once Identifier arguments_once classBody_once
	'''

	pass

def p_classBodyDeclarations(p):
	'''
	 classBodyDeclarations : classBodyDeclaration
		| classBodyDeclarations classBodyDeclaration
	'''

	pass

def p_enumBodyDeclarations(p):
	'''
	 enumBodyDeclarations : SEMI classBodyDeclarations
		| SEMI 
	'''

	pass


def p_interfaceDeclaration(p):
	'''
	 interfaceDeclaration :  normalInterfaceDeclaration 
	| annotationTypeDeclaration
	'''

	pass


def p_typeParameters_once(p):
	'''
		typeParameters_once : typeParameters
							| 
	'''

def p_EXTENDS_typeList(p):
	'''
		EXTENDS_typeList : EXTENDS typeList
						|
	'''

def p_normalInterfaceDeclaration(p):
	'''
	 normalInterfaceDeclaration : INTERFACE Identifier typeParameters_once EXTENDS_typeList interfaceBody
	'''

	pass

def p_COMMA_type(p):
	'''
	 COMMA_type : COMMA type
	'''

	pass

def p_COMMA_types(p):
	'''
		COMMA_types : COMMA_type
					| COMMA_types COMMA_type
	'''

def p_typeList(p):
	'''
	 typeList : type COMMA_types
		| type 
	'''

	pass


def p_classBody(p):
	'''
	 classBody : BLPAREN classBodyDeclarations BRPAREN
		| BLPAREN BRPAREN
	'''

	pass

def p_interfaceBodyDeclarations(p):
	'''
	 interfaceBodyDeclarations : interfaceBodyDeclaration
		| interfaceBodyDeclarations interfaceBodyDeclaration
	'''

	pass


def p_interfaceBody(p):
	'''
	 interfaceBody : BLPAREN interfaceBodyDeclarations BRPAREN
		| BLPAREN BRPAREN
	'''

	pass


def p_classBodyDeclaration(p):
	'''
	 classBodyDeclaration : SEMI
		| STATIC block
		| block
		| modifiers memberDecl
		| memberDecl
	'''

	pass


def p_memberDecl(p):
	'''
	 memberDecl :  genericMethodOrConstructorDecl 
	| memberDeclaration 
	| VOID Identifier voidMethodDeclaratorRest 
	| Identifier constructorDeclaratorRest 
	| interfaceDeclaration 
	| classDeclaration
	'''

	pass


def p_memberDeclaration(p):
	'''
	 memberDeclaration :  type methodDeclaration
	 					| type fieldDeclaration
	'''

	pass


def p_genericMethodOrConstructorDecl(p):
	'''
	 genericMethodOrConstructorDecl :  typeParameters genericMethodOrConstructorRest
	'''

	pass


def p_genericMethodOrConstructorRest(p):
	'''
	 genericMethodOrConstructorRest :  type Identifier methodDeclaratorRest
									| VOID Identifier methodDeclaratorRest
									| Identifier constructorDeclaratorRest
	'''

	pass


def p_methodDeclaration(p):
	'''
	 methodDeclaration :  Identifier methodDeclaratorRest
	'''

	pass


def p_fieldDeclaration(p):
	'''
	 fieldDeclaration :  variableDeclarators SEMI
	'''

	pass


def p_interfaceBodyDeclaration(p):
	'''
	 interfaceBodyDeclaration :  modifiers_empty interfaceMemberDecl 
	| SEMI
	'''

	pass


def p_interfaceMemberDecl(p):
	'''
	 interfaceMemberDecl :  interfaceMethodOrFieldDecl 
	| interfaceGenericMethodDecl 
	| VOID Identifier voidInterfaceMethodDeclaratorRest 
	| interfaceDeclaration 
	| classDeclaration
	'''

	pass


def p_interfaceMethodOrFieldDecl(p):
	'''
	 interfaceMethodOrFieldDecl :  type Identifier interfaceMethodOrFieldRest
	'''

	pass


def p_interfaceMethodOrFieldRest(p):
	'''
	 interfaceMethodOrFieldRest :  constantDeclaratorsRest SEMI 
	| interfaceMethodDeclaratorRest
	'''

	pass

def p_throwList(p):
	'''
		throwList : THROWS qualifiedNameList
	'''
	pass

def p_array(p):
	'''
		array : FLPAREN FRPAREN
	'''
	pass

def p_arrays(p):
	'''
		arrays : arrays array
				| array
	'''

#methodDeclaratorRest
#    :   formalParameters ('[' ']')*
#        ('throws' qualifiedNameList)?
#        (   methodBody
#        |   ';'
#        )
#    ;

def p_methodDeclaratorRest(p):
	'''
	 methodDeclaratorRest : formalParameters arrays throwList methodBody
	 					| formalParameters arrays throwList SEMI
						| formalParameters throwList SEMI
						| formalParameters throwList methodBody
						| formalParameters arrays methodBody
	 					| formalParameters arrays SEMI
						| formalParameters methodBody
						| formalParameters SEMI
	'''

	pass


def p_voidMethodDeclaratorRest(p):
	'''
	 voidMethodDeclaratorRest : formalParameters throwList methodBody
		| formalParameters throwList SEMI
		| formalParameters methodBody
		| formalParameters SEMI
	'''

	pass


def p_interfaceMethodDeclaratorRest(p):
	'''
	 interfaceMethodDeclaratorRest : formalParameters arrays throwList SEMI
	 								| formalParameters throwList SEMI
									| formalParameters arrays SEMI
									| formalParameters SEMI

	'''

	pass


def p_interfaceGenericMethodDecl(p):
	'''
	 interfaceGenericMethodDecl :  typeParameters type Identifier interfaceMethodDeclaratorRest
	 		| typeParameters VOID Identifier interfaceMethodDeclaratorRest
	'''

	pass


def p_voidInterfaceMethodDeclaratorRest(p):
	'''
	 voidInterfaceMethodDeclaratorRest : formalParameters throwList SEMI
	 								| formalParameters SEMI
	'''

	pass

#constructorDeclaratorRest
#    :   formalParameters ('throws' qualifiedNameList)? constructorBody
#    ;

def p_constructorDeclaratorRest(p):
	'''
	 constructorDeclaratorRest : formalParameters throwList constructorBody
	 							| formalParameters constructorBody
	'''

	pass


def p_constantDeclarator(p):
	'''
	 constantDeclarator :  Identifier constantDeclaratorRest
	'''

	pass

def p_COMMA_VAR(p):
	'''
		COMMA_VAR : COMMA variableDeclarator
	'''

def p_COMMA_VARS(p):
	'''
	 COMMA_VARS : COMMA_VAR
		| COMMA_VARS COMMA_VAR
	'''

	pass

def p_variableDeclarators(p):
	'''
	 variableDeclarators : variableDeclarator COMMA_VARS
		| variableDeclarator 
	'''

	pass


def p_EQUALS_variableInitializer(p):
	'''
		EQUALS_variableInitializer : EQUALS variableInitializer
	'''

def p_variableDeclarator(p):
	'''
	 variableDeclarator : variableDeclaratorId EQUALS_variableInitializer
		| variableDeclaratorId 
	'''

	pass

def p_COMMA_const(p):
	'''
		COMMA_const : COMMA constantDeclarator
	'''

def p_COMMA_consts(p):
	'''
	 COMMA_consts : COMMA_const
		| COMMA_consts COMMA_const
	'''

	pass

def p_constantDeclaratorsRest(p):
	'''
	 constantDeclaratorsRest : constantDeclaratorRest COMMA_consts
		| constantDeclaratorRest 
	'''

	pass


def p_constantDeclaratorRest(p):
	'''
	 constantDeclaratorRest : arrays EQUALS variableInitializer
		|  EQUALS variableInitializer
	'''

	pass


def p_variableDeclaratorId(p):
	'''
	 variableDeclaratorId : Identifier arrays
		| Identifier 
	'''

	pass


def p_variableInitializer(p):
	'''
	 variableInitializer :  arrayInitializer 
	| expression
	'''

	pass



def p_COMMA_variableInitializer( p ):
	'''
		COMMA_variableInitializer : COMMA variableInitializer
	'''

def p_COMMA_variableInitializers(p):
	'''
	 COMMA_variableInitializers : COMMA_variableInitializer
							| COMMA_variableInitializers COMMA variableInitializer
	'''

	pass


def p_COMMA_once(p):
	'''
		COMMA_once : COMMA
				| 
	'''

def p_array_body(p):
	'''
		array_body : variableInitializer COMMA_variableInitializers COMMA_once
					| variableInitializer COMMA_once
	'''

#arrayInitializer
#    :   '{' (variableInitializer (',' variableInitializer)* (',')? )? '}'
#    ;

def p_arrayInitializer(p):
	'''
		arrayInitializer : BLPAREN array_body BRPAREN
						| BLPAREN BRPAREN
	'''

	pass


def p_modifier(p):
	'''
	 modifier :  annotation 
	| PUBLIC 
	| PROTECTED 
	| PRIVATE 
	| STATIC 
	| ABSTRACT 
	| FINAL 
	| NATIVE 
	| SYNCHRONIZED 
	| TRANSIENT 
	| VOLATILE 
	| STRICTFP
	'''

	pass


def p_packageOrTypeName(p):
	'''
	 packageOrTypeName :  qualifiedName
	'''

	pass


def p_enumConstantName(p):
	'''
	 enumConstantName :  Identifier
	'''

	pass


def p_typeName(p):
	'''
	 typeName :  qualifiedName
	'''

	pass


def p_type(p):
	'''
	 type : type_body
		| primitiveType arrays
		| primitiveType 
	'''

	pass

def p_type_body(p):
	'''
		type_body : Identifier classOrInterfaceTypeBody arrays
				| Identifier classOrInterfaceTypeBody
				| Identifier arrays
				| Identifier
	'''

def p_classOrInterfaceTypeBody(p):
	'''
		classOrInterfaceTypeBody : typeArguments classOrInterfaceTypeStatements
						| typeArguments
						| classOrInterfaceTypeStatements
	'''


def p_classOrInterfaceTypeStatement(p):
	'''
		classOrInterfaceTypeStatement : CallBody typeArguments
									| CallBody
	'''

def p_classOrInterfaceTypeStatements(p):
	'''
		classOrInterfaceTypeStatements : classOrInterfaceTypeStatement
			| classOrInterfaceTypeStatements classOrInterfaceTypeStatement
	'''

#classOrInterfaceType
#	:	Identifier typeArguments? ('.' Identifier typeArguments? )*
def p_classOrInterfaceType(p):
	'''
	 classOrInterfaceType : Identifier classOrInterfaceTypeBody
						| Identifier
	'''

	pass


def p_primitiveType(p):
	'''
	 primitiveType :  BOOLEAN 
	| CHAR 
	| BYTE 
	| SHORT 
	| INT 
	| LONG 
	| FLOAT 
	| DOUBLE
	'''

	pass


def p_variableModifier(p):
	'''
	 variableModifier :  FINAL 
	| annotation
	'''

	pass

def p_COMMA_typeArgument( p ):
	'''
		COMMA_typeArgument : COMMA typeArgument
	'''

def p_COMMA_typeArguments(p):
	'''
	 COMMA_typeArguments : COMMA_typeArgument
		| COMMA_typeArguments COMMA_typeArgument
	'''

	pass

def p_typeArguments(p):
	'''
	 typeArguments : LESS typeArgument COMMA_typeArguments MORE
		| LESS typeArgument MORE
	'''

	pass

def p_typeArgumentStatment(p):
	'''
	 typeArgumentStatment :  EXTENDS type
	| SUPER type
	| empty
	'''

	pass

def p_typeArgument(p):
	'''
	 typeArgument : type
		| QUES typeArgumentStatment
	'''

	pass

def p_COMMA_qualifiedName(p):
	'''
		COMMA_qualifiedName : COMMA qualifiedName
	'''

def p_COMMA_qualifiedNames(p):
	'''
	 COMMA_qualifiedNames : COMMA_qualifiedName
	 	| COMMA_qualifiedNames COMMA_qualifiedName
	'''

	pass


def p_qualifiedNameList(p):
	'''
	 qualifiedNameList : qualifiedName COMMA_qualifiedNames
		| qualifiedName 
	'''

	pass


def p_formalParameters(p):
	'''
	 formalParameters : LPAREN formalParameterDecls RPAREN
	'''

	pass

def p_variableModifiers_empty(p):
	'''
		variableModifiers_empty : variableModifiers
								|
	'''

def p_formalParameterDecls(p):
	'''
	 formalParameterDecls :  variableModifiers_empty type formalParameterDeclsRest
						| empty
	'''

	pass

def p_formalParameterDeclsRestBody(p):
	'''
		formalParameterDeclsRestBody :  COMMA formalParameterDecls
		|
	'''
def p_formalParameterDeclsRest(p):
	'''
	 formalParameterDeclsRest : variableDeclaratorId formalParameterDeclsRestBody
		| OP_ARRAY variableDeclaratorId
	'''

	pass


def p_methodBody(p):
	'''
	 methodBody :  block
	'''

	pass


def p_blockStatements(p):
	'''
	 blockStatements : blockStatement
		| blockStatements blockStatement
	'''

	pass

#constructorBody
#    :   '{' (explicitConstructorInvocation)? (blockStatement)* '}'
#    ;

def p_constructorBody(p):
	'''
	 constructorBody : BLPAREN explicitConstructorInvocation blockStatements BRPAREN
		| BLPAREN explicitConstructorInvocation BRPAREN
		| BLPAREN blockStatements BRPAREN
		| BLPAREN BRPAREN
	'''

	pass


def p_explicitConstructorInvocation(p):
	'''
	 explicitConstructorInvocation : nonWildcardTypeArguments THIS arguments SEMI
	 				| nonWildcardTypeArguments SUPER arguments SEMI
	 				| THIS arguments SEMI
					| SUPER arguments SEMI
					| primary DOT nonWildcardTypeArguments SUPER arguments SEMI
					| primary DOT SUPER arguments SEMI
	'''

	pass

def p_DOT_Identifier(p):
	'''
		DOT_Identifier : DOT Identifier
					| DOT MULT
	'''

def p_DOT_Identifiers(p):
	'''
		DOT_Identifiers : DOT_Identifier
						| DOT_Identifiers DOT_Identifier
	'''

def p_qualifiedName(p):
	'''
	 qualifiedName : Identifier DOT_Identifiers
		| Identifier
	'''

	pass


def p_literal(p):
	'''
	 literal :  integerLiteral 
	| FloatingPointLiteral 
	| CharacterLiteral 
	| StringLiteral 
	| booleanLiteral 
	| NULL
	'''

	pass


def p_booleanLiteral(p):
	'''
	 booleanLiteral :  TRUE 
	| FALSE
	'''

	pass


def p_annotations(p):
	'''
	 annotations :  annotation
	 			| annotations annotation
	'''

	pass

def p_annotationBody(p):
	'''
		annotationBody :  LPAREN elementValuePairs RPAREN
					| LPAREN elementValue RPAREN
					| LPAREN RPAREN
					|
	'''

def p_annotation(p):
	'''
	 annotation : AT annotationName annotationBody
	'''

	pass


def p_annotationName(p):
	'''
	 annotationName : Identifier DOT_Identifiers
		| Identifier 
	'''

	pass

def p_elementValuePairsBody(p):
	'''
		elementValuePairsBody :  COMMA elementValuePair
	'''

def p_elementValuePairsBodys(p):
	'''
	 elementValuePairsBodys : elementValuePairsBody
		| elementValuePairsBodys elementValuePairsBody
	'''

	pass


def p_elementValuePairs(p):
	'''
	 elementValuePairs : elementValuePair elementValuePairsBodys
		| elementValuePair 
	'''

	pass


def p_elementValuePair(p):
	'''
	 elementValuePair :  Identifier EQUALS elementValue
	'''

	pass


def p_elementValue(p):
	'''
	 elementValue :  conditionalExpression 
	| annotation 
	| elementValueArrayInitializer
	'''

	pass


def p_elementValueBody(p):
	'''
		elementValueBody : COMMA elementValue
	'''

def p_elementValueBodys(p):
	'''
	 elementValueBodys : elementValueBody
		| elementValueBodys elementValueBody
	'''

	pass

def p_elementValueStatement(p):
	'''
		elementValueStatement : elementValue elementValueBodys
							| elementValue
							|
	'''

def p_COMMA_OR_empty(p):
	'''
		COMMA_OR_empty : COMMA
					| 
	'''

def p_elementValueArrayInitializer(p):
	'''
	 elementValueArrayInitializer : BLPAREN elementValueStatement COMMA_OR_empty BRPAREN
	'''

	pass


def p_annotationTypeDeclaration(p):
	'''
	 annotationTypeDeclaration :  AT INTERFACE Identifier annotationTypeBody
	'''

	pass

def p_annotationTypeElementDeclarations(p):
	'''
	 annotationTypeElementDeclarations : annotationTypeElementDeclaration
		| annotationTypeElementDeclarations annotationTypeElementDeclaration
	'''

	pass

def p_annotationTypeBody(p):
	'''
	 annotationTypeBody : BLPAREN annotationTypeElementDeclarations BRPAREN
		| BLPAREN  BRPAREN
	'''

	pass

def p_modifiers_empty(p):
	'''
		modifiers_empty : modifiers
						|
	'''

def p_annotationTypeElementDeclaration(p):
	'''
	 annotationTypeElementDeclaration :  modifiers annotationTypeElementRest
	 								| annotationTypeElementRest
	'''

	pass

def p_SEMI_OR_empty(p):
	'''
		SEMI_OR_empty : SEMI
					| 
	'''

def p_annotationTypeElementRest(p):
	'''
	 annotationTypeElementRest : type annotationMethodOrConstantRest SEMI
								| normalClassDeclaration SEMI
								| normalInterfaceDeclaration SEMI
								| enumDeclaration SEMI
								| annotationTypeDeclaration SEMI
								| normalClassDeclaration
								| normalInterfaceDeclaration
								| enumDeclaration
								| annotationTypeDeclaration
	'''

	pass


def p_annotationMethodOrConstantRest(p):
	'''
	 annotationMethodOrConstantRest :  annotationMethodRest 
									| annotationConstantRest
	'''

	pass

def p_defaultValue_or_empty(p):
	'''
		defaultValue_or_empty : defaultValue
								| 
	'''

def p_annotationMethodRest(p):
	'''
	 annotationMethodRest : Identifier LPAREN RPAREN defaultValue_or_empty
	'''

	pass


def p_annotationConstantRest(p):
	'''
	 annotationConstantRest :  variableDeclarators
	'''

	pass


def p_defaultValue(p):
	'''
	 defaultValue :  DEFAULT elementValue
	'''

	pass


def p_block(p):
	'''
	 block : BLPAREN blockStatements BRPAREN
		| BLPAREN BRPAREN
	'''

	pass


def p_blockStatement(p):
	'''
	 blockStatement :  statement
	| localVariableDeclarationStatement
	| classOrInterfaceDeclaration  
	'''

	pass


def p_localVariableDeclarationStatement(p):
	'''
	 localVariableDeclarationStatement :  localVariableDeclaration SEMI
	'''

	pass

def p_localVariableDeclarationModifBody(p):
	'''
		localVariableDeclarationModifBody : variableModifiers type variableDeclarators
											| type variableDeclarators
	'''

def p_localVariableDeclaration(p):
	'''
	 localVariableDeclaration : localVariableDeclarationModifBody
	'''

	pass


def p_variableModifiers(p):
	'''
	 variableModifiers : variableModifiers variableModifier
	 					| variableModifier
	'''

	pass

def p_expression_colon_or_empty(p):
	'''
		expression_colon_or_empty : COLON expression
							| 
	'''

def p_else_statement(p):
	'''
		else_statement : ELSE statement
						|
	'''

def p_expression_or_empty(p):
	'''
		expression_or_empty : expression
							| 
	'''

def p_Identifier_or_empty(p):
	'''
		Identifier_or_empty : Identifier
							|
	'''

def p_statement(p):
	'''
	 statement : block
	 			| ASSERT expression expression_colon_or_empty SEMI
				| IF parExpression statement else_statement
				| FOR LPAREN forControl RPAREN statement
	 			| WHILE parExpression statement
				| DO statement WHILE parExpression SEMI
				| TRY block catches FINALLY block
				| TRY block catches
				| TRY block FINALLY block
				| SWITCH parExpression BLPAREN switchBlockStatementGroups BRPAREN
				| SYNCHRONIZED parExpression block
				| RETURN expression_or_empty SEMI
				| THROW expression SEMI
				| BREAK Identifier_or_empty SEMI
				| CONTINUE  Identifier_or_empty SEMI
				| SEMI
				| statementExpression SEMI
				| Identifier COLON statement
	'''

	pass

def p_catchClauses(p):
	'''
		catchClauses : catchClause
					| catchClauses catchClause
	'''
def p_catches(p):
	'''
	 catches : catchClause catchClauses
		| catchClause 
	'''

	pass


def p_catchClause(p):
	'''
	 catchClause :  CATCH LPAREN formalParameter RPAREN block
	'''

	pass


def p_formalParameter(p):
	'''
	 formalParameter :  variableModifiers_empty type variableDeclaratorId
	'''

	pass


def p_switchBlockStatementGroupStats(p):
	'''
	 switchBlockStatementGroupStats : switchBlockStatementGroup
		| switchBlockStatementGroupStats switchBlockStatementGroup
	'''

	pass

def p_switchBlockStatementGroups(p):
	'''
		switchBlockStatementGroups : switchBlockStatementGroupStats
									|
	'''

	pass


def p_switchLabels(p):
	'''
	 switchLabels :  switchLabel 
	| switchLabels switchLabel
	'''

	pass

def p_switchBlockStatementGroup(p):
	'''
	 switchBlockStatementGroup : switchLabels blockStatements
		| switchLabels 
	'''

	pass


def p_switchLabel(p):
	'''
	 switchLabel :  CASE constantExpression COLON 
	| CASE enumConstantName COLON 
	| DEFAULT COLON
	'''

	pass

def p_forInit_or_empty(p):
	'''
		forInit_or_empty : forInit
						|
	'''
def p_forUpdate_empty(p):
	'''
		forUpdate_empty : forUpdate
						|
	'''

#forControl
#    :   enhancedForControl
#    |   (forInit)? ';' expression? ';' (forUpdate)?
#    ;
def p_forControl(p):
	'''
	 forControl : enhancedForControl
	 			| forInit SEMI expression SEMI forUpdate
				| forInit SEMI expression SEMI
				| forInit SEMI SEMI forUpdate
				| forInit SEMI SEMI
				| SEMI SEMI
				| SEMI expression SEMI forUpdate
				| SEMI expression SEMI
				| SEMI SEMI forUpdate
	'''

	pass


def p_forInit(p):
	'''
	 forInit :  localVariableDeclaration 
	| expressionList
	'''

	pass


def p_enhancedForControl(p):
	'''
	 enhancedForControl :  variableModifiers type Identifier COLON expression
	 					| type Identifier COLON expression
	'''

	pass


def p_forUpdate(p):
	'''
	 forUpdate :  expressionList
	'''

	pass


def p_parExpression(p):
	'''
	 parExpression :  LPAREN expression RPAREN
	'''

	pass

def p_COMMA_expression(p):
	'''
	 COMMA_expression : COMMA expression
	'''

	pass

def p_COMMA_expressions(p):
	'''
		COMMA_expressions : COMMA_expression
						| COMMA_expressions COMMA_expression
	'''


# expression COMMA expression ....
def p_expressionList(p):
	'''
	 expressionList : expression COMMA_expressions
		| expression 
	'''

	pass


def p_statementExpression(p):
	'''
	 statementExpression :  expression
	'''

	pass


def p_constantExpression(p):
	'''
	 constantExpression :  expression
	'''

	pass

def p_assignmentOperator_expression(p):
	'''
		assignmentOperator_expression : assignmentOperator expression
	'''

# expression begin

def p_expression(p):
	'''
	 expression : conditionalExpression assignmentOperator_expression
	 			| conditionalExpression
	'''

	pass


def p_assignmentOperator(p):
	'''
	 assignmentOperator :  EQUALS 
	| ASS_ADD 
	| ASS_SUB 
	| ASS_MUL 
	| ASS_DIV 
	| ASS_AND 
	| ASS_OR 
	| ASS_XOR 
	| ASS_MOD 
	| ASS_SHL 
	| ASS_SHRR 
	| ASS_SHR
	'''

	pass

def p_conditionalExpression(p):
	'''
	 conditionalExpression : conditionalOrExpressions
						| conditionalOrExpressions QUES expression COLON expression
	'''

	pass


# begin

def p_conditionalOrExpressions(p):
	'''
		conditionalOrExpressions : conditionalOrExpression
								| conditionalOrExpressions conditionalOrExpression 
	'''

def p_conditionalOrExpression(p):
	'''
	 conditionalOrExpression : conditionalAndExpressions
	 						| OP_LOR conditionalAndExpression
	'''

	pass

def p_conditionalAndExpressions(p):
	'''
		conditionalAndExpressions : conditionalAndExpression
								| conditionalAndExpressions conditionalAndExpression
	'''

def p_conditionalAndExpression(p):
	'''
	 conditionalAndExpression : inclusiveOrExpressions
	 						| OP_LAND inclusiveOrExpressions
	'''

	pass

def p_inclusiveOrExpressions(p):
	'''
		inclusiveOrExpressions : inclusiveOrExpression
								| inclusiveOrExpressions inclusiveOrExpression
	'''

def p_inclusiveOrExpression(p):
	'''
	 inclusiveOrExpression : exclusiveOrExpressions
	 					| VERTICAL exclusiveOrExpressions
	'''

	pass

def p_exclusiveOrExpressions(p):
	'''
		exclusiveOrExpressions : exclusiveOrExpression
							| exclusiveOrExpressions exclusiveOrExpression
	'''

def p_exclusiveOrExpression(p):
	'''
	 exclusiveOrExpression : andExpressions
	 					| CARET andExpressions
	'''

	pass

def p_andExpressions(p):
	'''
		andExpressions : andExpression
					| andExpressions andExpression
	'''

def p_andExpression(p):
	'''
	 andExpression : equalityExpressions
	 			| AND equalityExpressions
	'''

	pass

def p_equalityExpressions(p):
	'''
		equalityExpressions : equalityExpression
						| equalityExpressions equalityExpression
	'''

def p_equalityExpression(p):
	'''
	 equalityExpression : instanceOfExpressions
	 					| OP_EQ instanceOfExpressions
						| OP_NE instanceOfExpressions
	'''

	pass

def p_instanceOfExpressions(p):
	'''
		instanceOfExpressions : instanceOfExpression
							| instanceOfExpressions instanceOfExpression
	'''


def p_instanceOfExpression(p):
	'''
	 instanceOfExpression : relationalExpressions INSTANCEOF type
	 					| relationalExpressions
	'''

	pass

def p_relationalOp(p):
	'''
	 relationalOp :  OP_LE 
	| OP_GE 
	| LESS 
	| MORE
	'''

	pass

def p_shiftOp(p):
	'''
	 shiftOp :  MORE MORE
	| MORE MORE MORE 
	| OP_SHL
	'''

def p_relationalExpressions(p):
	'''
		relationalExpressions : relationalExpression
						| relationalExpressions relationalExpression
	'''

def p_relationalExpression(p):
	'''
		relationalExpression : shiftExpressions
							| shiftExpressions shiftOp
	'''

def p_shiftExpressions(p):
	'''
		shiftExpressions : shiftExpression
						| shiftExpressions shiftExpression
	'''

def p_shiftExpression(p):
	'''
		shiftExpression : additiveExpressions
						| relationalOp additiveExpressions
	'''

def p_additiveExpressions(p):
	'''
		additiveExpressions : additiveExpression
						| additiveExpressions additiveExpression
	'''


def p_additiveExpression(p):
	'''
	 additiveExpression : multiplicativeExpressions
	 					| PLUS multiplicativeExpressions
						| DASH multiplicativeExpressions
	'''

	pass

def p_multiplicativeExpressions(p):
	'''
		multiplicativeExpressions : multiplicativeExpression
						| multiplicativeExpressions multiplicativeExpression
	'''

#multiplicativeExpression
#    :   unaryExpression ( ( '*' | '/' | '%' ) unaryExpression )*
#    ;
def p_multiplicativeExpression(p):
	'''
	 multiplicativeExpression : unaryExpressions
	 		| MULT unaryExpressions
			| SLASH unaryExpressions
			| PERCENT unaryExpressions
	'''

	pass

def p_unaryExpressions(p):
	'''
		unaryExpressions : unaryExpression
					| unaryExpressions unaryExpression
	'''

# multiplicativeExpression -- end

def p_unaryExpression(p):
	'''
	 unaryExpression :  PLUS unaryExpression 
	| DASH unaryExpression 
	| OP_INC unaryExpression 
	| OP_DEC unaryExpression 
	| unaryExpressionNotPlusMinus
	'''

	pass


def p_INC_DEC(p):
	'''
	 INC_DEC :  OP_INC 
	| OP_DEC
	'''

	pass

def p_selectors(p):
	'''
	 selectors : selector
		| selectors selector
	'''

	pass


def p_unaryExpressionNotPlusMinus(p):
	'''
	 unaryExpressionNotPlusMinus : TILDE unaryExpression
								 | EXCLAMATION unaryExpression
								 | castExpression
								 | primary selectors INC_DEC
								 | primary INC_DEC
								 | primary selectors
								 | primary
	'''

	pass

def p_castExpression(p):
	'''
	 castExpression :  LPAREN primitiveType RPAREN unaryExpression 
					| LPAREN type RPAREN unaryExpressionNotPlusMinus
					| LPAREN expression RPAREN unaryExpressionNotPlusMinus
	'''

	pass

def p_CallBody(p):
	'''
		CallBody : DOT Identifier
				| DOT CLASS
	'''

def p_CallBodys(p):
	'''
		CallBodys : CallBody
					| CallBody CallBodys
	'''

#primary
#    :   parExpression
#    |   'this' ('.' Identifier)* (identifierSuffix)?
#    |   'super' superSuffix
#    |   literal
#    |   'new' creator
#    |   Identifier ('.' Identifier)* (identifierSuffix)?
#    |   primitiveType ('[' ']')* '.' 'class'
#    |   'void' '.' 'class'
#    ;
def p_primary(p):
	'''
	 primary : parExpression
		| THIS CallBodys identifierSuffix
		| THIS CallBodys
		| THIS identifierSuffix
		| THIS
		| SUPER superSuffix
		| literal
		| NEW creator
		| Identifier CallBodys identifierSuffix
		| Identifier CallBodys
		| Identifier identifierSuffix
		| Identifier
		| primitiveType arrays DOT CLASS
		| primitiveType  DOT CLASS
		| VOID DOT CLASS
	'''

	pass

def p_FL_expression_FR(p):
	'''
		FL_expression_FR : FLPAREN expression FRPAREN
	'''

def p_FL_expression_FRs(p):
	'''
	 FL_expression_FRs : FL_expression_FR
		| FL_expression_FRs FL_expression_FR
	'''

	pass

def p_identifierSuffix(p):
	'''
	 identifierSuffix :  arrays DOT CLASS 
	| FL_expression_FRs
	| arguments 
	| DOT CLASS 
	| DOT explicitGenericInvocation 
	| DOT THIS 
	| DOT SUPER arguments 
	| DOT NEW innerCreator
	'''

	pass


def p_creator(p):
	'''
	 creator :  nonWildcardTypeArguments createdName classCreatorRest 
	| createdName arrayCreatorRest 
	| createdName classCreatorRest
	'''

	pass


def p_createdName(p):
	'''
	 createdName :  classOrInterfaceType 
	| primitiveType
	'''

	pass


def p_nonWildcardTypeArguments_empty(p):
	'''
		nonWildcardTypeArguments_empty : nonWildcardTypeArguments
										|
	'''


def p_innerCreator(p):
	'''
	 innerCreator : nonWildcardTypeArguments_empty Identifier classCreatorRest
	'''

	pass

#arrayCreatorRest
#    :   '['
#        (   ']' ('[' ']')* arrayInitializer
#        |   expression ']' ('[' expression ']')* ('[' ']')*
#        )
#    ;

def p_arrayCreatorRest(p):
	'''
	 arrayCreatorRest :  FLPAREN FRPAREN arrays arrayInitializer
						| FLPAREN FRPAREN arrayInitializer
						| FLPAREN expression FRPAREN FL_expression_FRs arrays
						| FLPAREN expression FRPAREN
						| FLPAREN expression FRPAREN FL_expression_FRs
						| FLPAREN expression FRPAREN arrays
	'''

	pass


def p_classCreatorRest(p):
	'''
	 classCreatorRest : arguments classBody_once
	'''

	pass


def p_explicitGenericInvocation(p):
	'''
	 explicitGenericInvocation :  nonWildcardTypeArguments Identifier arguments
	'''

	pass


def p_nonWildcardTypeArguments(p):
	'''
	 nonWildcardTypeArguments :  LESS typeList MORE
	'''

	pass


def p_selector(p):
	'''
	 selector : DOT Identifier arguments
		| DOT Identifier 
		| DOT THIS
		| DOT SUPER superSuffix
		| DOT NEW innerCreator
		| FLPAREN expression FRPAREN
	'''

	pass


def p_superSuffix(p):
	'''
	 superSuffix : arguments
		| DOT Identifier arguments
		| DOT Identifier
	'''

	pass

def p_arguments(p):
	'''
	 arguments : LPAREN expressionList RPAREN
	 			| LPAREN RPAREN
	'''

	pass

def p_FloatingPointLiteral( p ):
	'''
		FloatingPointLiteral : NON_INTEGER_1
					| NON_INTEGER_2
					| NON_INTEGER_3
					| NON_INTEGER_4
	'''
	pass

def p_integerLiteral(p):
	'''
		integerLiteral : LONG_NUMBER
					| LONG_HEX_NUMBER
	'''
	pass


	#### Empty
   
def p_empty( p ):
	'''empty : '''

#### Catastrophic error handler
is_pass = True
def p_error(p):
	global is_pass
	if p:
		print "Syntax error at '%s' lineno = %i linepos=%i" %  ( p.value , p.lineno , p.lexpos )
	else:
		print "Syntax error at EOF"
	is_pass = False

def get_yacc(l,filename,debug):
	b = yacc.yacc()

	b.error = 0

	if debug == True:
		result = b.parse(lexer = l , debug=2)
	else:
		result = b.parse(lexer = l , debug=0)

	if b.error : return None
	global is_pass

	#if is_pass:
	#	print "%s was successed" % filename
	if not is_pass :
		print "%s was failed" % filename
