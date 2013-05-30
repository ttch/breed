# *.* coding=utf-8 *.*
# convert by The Java Language Specification
#
# the part of code was reference by plyj(http://travis-ci.org/musiKk/plyj)
# 
#
# [The "BSD licence"]
# Copyright (c) 2013 zhao_nf
# All rights reserved.
#
# author by zhao_nf ( ttchgm@gmail.com )
#

import ply.yacc as yacc
import lex
from collections import deque
import objectTree

tokens = lex.tokens

# package 
# ## Compilation Units begin
def p_compilationUnit(p):
	'''
		compilationUnit : packageDeclaration importDeclarations typeDeclarations
		| packageDeclaration importDeclarations 
		| packageDeclaration typeDeclarations
		| packageDeclaration
		| typeDeclarations
		| importDeclarations
		| importDeclarations typeDeclarations
		| empty
	'''

def p_importDeclarations(p):
	'''
		importDeclarations : importDeclaration
		| importDeclarations importDeclaration
	'''

def p_typeDeclarations(p):
	'''
		typeDeclarations : typeDeclaration
		| typeDeclarations typeDeclaration
	'''

def p_packageDeclaration(p):
	'''
		packageDeclaration : packageDeclarationName SEMI
	'''

def p_packageDeclarationName1(p):
	'''
		packageDeclarationName : modifiers PACKAGE name
	'''

def p_packageDeclarationName2(p):
	'''
		packageDeclarationName : PACKAGE name
	'''

def p_importDeclaration(p):
	'''
    	importDeclaration : singleTypeImportDeclaration
		| typeImportOnDemandDeclaration	
		| singleStaticImportDeclaration	
		| staticImportOnDemandDeclaration
	'''

def p_singleTypeImportDeclaration(p):
	'''
		singleTypeImportDeclaration : IMPORT name SEMI
	'''
	print p[2].nameList
	#objectTree.cl.addImport(ImportObject().addName())

def p_typeImportOnDemandDeclaration(p):
	'''
		typeImportOnDemandDeclaration : IMPORT name DOT MULT SEMI
	'''
	#print p[0], p[1] , p[2], p[3], p[4]


def p_singleStaticImportDeclaration(p):
	'''
		singleStaticImportDeclaration : IMPORT STATIC name SEMI
	'''

def p_staticImportOnDemandDeclaration(p):
	'''
		staticImportOnDemandDeclaration : IMPORT STATIC name DOT MULT SEMI
	'''

def p_typeDeclaration(p):
	'''
		typeDeclaration : classDeclaration
		| interfaceDeclaration
		| annotationTypeDeclaration
		| enumDeclaration
		| SEMI
	'''
# ## Compilation Units end

# name begin

def p_name(p):
	'''
		name : simpleName
		| qualifiedName
	'''
	p[0] = p[1]

def p_simpleName(p):
	'''
		simpleName : Identifier
	'''
	#if p[0] == None : p[0] = objectTree.Name()
	p[0] = objectTree.Name( [ p[1] ] )

def p_qualifiedName(p):
	'''
		qualifiedName : name DOT simpleName		

	'''
	#p[0] = "%s.%s" % ( p[1] , p[3] )
	p[0] = p[1] + p[3]
# name end

# Types, Values, and Variables * begin

# ## type begin

def p_type(p):
	'''
		type : primitiveType
		| referenceType
	'''


def p_primitiveType(p):
	'''
		primitiveType : BOOLEAN
		| VOID
		| BYTE
		| SHORT
		| INT
		| LONG
		| CHAR
		| FLOAT
		| DOUBLE
	'''
def p_referenceType(p):
	'''
		referenceType : classOrInterfaceType
		| arrayType
	'''

def p_classOrInterfaceType(p):
	'''
		classOrInterfaceType : classOrInterface
		| genericType
	'''

def p_classOrInterface(p):
	'''
		classOrInterface : name
		| genericType DOT name
	'''

def p_genericType(p):
	'''
		genericType : classOrInterface typeArguments
		| classOrInterface LESS MORE
	'''

def p_classType(p):
	'''
		classType : classOrInterfaceType	
	'''

def p_interfaceType(p):
	'''
		interfaceType : classOrInterfaceType
	'''

def p_arrayType (p):
	'''
		arrayType : genericType arrays
		| genericType DOT name arrays
		| primitiveType arrays
		| name arrays
	'''

def p_array(p):
	'''
		array : FLPAREN FRPAREN
	'''
def p_arrays(p):
	'''
		arrays : array_loop
	'''

def p_array_loop(p):
	'''
		array_loop : array
		| array_loop array
	'''

def p_arrays_opt(p):
	'''
		arrays_opt : arrays
		| empty
	'''

# ## type end

# ## Type Parameter - begin

def p_typeParametersHeaderName(p):
	'''
		typeParametersHeaderName : Identifier
	'''

def p_typeParameters(p):
	'''
		typeParameters : LESS typeParameterList1
	'''

def p_typeParameterList(p):
	'''
		typeParameterList : typeParameter
		| typeParameterList COMMA typeParameter
	'''

def p_typeParameter(p):
	'''
		typeParameter : typeParametersHeaderName
		| typeParametersHeaderName EXTENDS referenceType
		| typeParametersHeaderName EXTENDS referenceType additionalBoundList
	'''

def p_additionalBoundList(p):
	'''
		additionalBoundList : additionalBound
		| additionalBoundList additionalBound
	'''

def p_additionalBound(p):
	'''
		additionalBound : AND referenceType
	'''
def p_typeParameterList1(p):
	'''
		typeParameterList1 : typeParameter1
		| typeParameterList COMMA typeParameter1
	'''

def p_typeParameter1(p):
	'''
		typeParameter1 : typeParametersHeaderName MORE
		| typeParametersHeaderName EXTENDS referenceType1
		| typeParametersHeaderName EXTENDS referenceType additionalBoundList1
	'''

def p_additionalBoundList1(p):
	'''
		additionalBoundList1 : additionalBound1
		| additionalBoundList additionalBound1
	'''

def p_additionalBound1(p):
	'''
		additionalBound1 : AND referenceType1
	'''

# ## Type Parameter - end


# ## Type Argument - begin
def p_typeArguments(p):
	'''
		typeArguments : LESS typeArgumentList1
	'''

def p_typeArgument(p):
	'''
		typeArgument : referenceType
		| wildcard
	'''

def p_typeArgumentList(p):
	'''
		typeArgumentList : typeArgument
		| typeArgumentList COMMA typeArgument
	'''


def p_typeArgumentList1(p):
	'''
		typeArgumentList1 : typeArgument1
		| typeArgumentList COMMA typeArgument1
	'''

def p_typeArgument1(p):
	'''
		typeArgument1 : referenceType1
		| wildcard1
	'''

def p_referenceType1(p):
	'''
		referenceType1 : referenceType MORE
		| classOrInterface LESS typeArgumentList2
	'''

def p_typeArgumentList2(p):
	'''
		typeArgumentList2 : typeArgument2
		| typeArgumentList COMMA typeArgument2
	'''

def p_typeArgument2(p):
	'''
		typeArgument2 : referenceType2
		| wildcard2
	'''

def p_referenceType2(p):
	'''
		referenceType2 : referenceType OP_SHR
		| classOrInterface LESS typeArgumentList3
	'''

def p_typeArgumentList3(p):
	'''
		typeArgumentList3 : typeArgument3
		| typeArgumentList COMMA typeArgument3
	'''

def p_typeArgument3(p):
	'''
		typeArgument3 : referenceType3
		| wildcard3
	'''

def p_referenceType3(p):
	'''
		referenceType3 : referenceType OP_SHRR
	'''

def p_wildcard(p):
	'''
		wildcard : QUES
		| QUES wildcardBounds
	'''

def p_wildcardBounds(p):
	'''
		wildcardBounds : EXTENDS referenceType
		| SUPER referenceType
	'''

def p_wildcard1(p):
	'''
		wildcard1 : QUES MORE
		| QUES wildcardBounds1
	'''

def p_wildcardBounds1(p):
	'''
		wildcardBounds1 : EXTENDS referenceType1
		| SUPER referenceType1
	'''

def p_wildcard2(p):
	'''
		wildcard2 : QUES OP_SHR
		| QUES wildcardBounds2
	'''

def p_wildcardBounds2(p):
	'''
		wildcardBounds2 : EXTENDS referenceType2
		| SUPER referenceType2
	'''

def p_wildcard3(p):
	'''
		wildcard3 : QUES OP_SHRR
		| QUES wildcardBounds3
	'''

def p_wildcardBounds3(p):
	'''
		wildcardBounds3 : EXTENDS referenceType3
		| SUPER referenceType3
	'''

# ## Type Argument - end

def p_modifiers_opt(p):
	'''
		modifiers_opt : modifiers
		| empty
	'''
	

def p_modifiers(p):
	'''
		modifiers : modifier
		| modifiers modifier
	'''

def p_modifier(p):
	'''
		modifier : PUBLIC
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
		| annotation
	'''

# class begin

def p_classDeclaration(p):
	'''
		classDeclaration : classHead classBody
	'''
def p_classHead(p):
	'''
		classHead : className classExtends_opt classImpls_opt
	'''

def p_className(p):
	'''
		className : classHeadName1 typeParameters
		| classHeadName1
	'''

def p_classHeadName1(p):
	'''
		classHeadName1 :  modifiers_opt CLASS Identifier
	'''



def p_classExtends_opt(p):
	'''
		classExtends_opt : classExtends
		| empty
	'''
def p_classImpls_opt(p):
	'''
		classImpls_opt : classImpls
		| empty
	'''

def p_classExtends(p):
	'''
		classExtends : EXTENDS classType
	'''

def p_classImpls(p):
	'''
		classImpls : IMPLEMENTS interfaceTypeList
	'''

def p_interfaceTypeList(p):
	'''
		interfaceTypeList : interfaceType
		| interfaceTypeList COMMA interfaceType
	'''

def p_typeParameters_opt(p):
	'''
		typeParameters_opt : typeParameters
		| empty
	'''

def p_classBody(p):
	'''
		classBody : BLPAREN classBodyDeclarations_opt BRPAREN
	'''

def p_classBodyDeclarations_opt(p):
	'''
		classBodyDeclarations_opt : classBodyDeclarations
		| empty
	'''

def p_classBodyDeclarations(p):
	'''
		classBodyDeclarations : classBodyDeclaration
		| classBodyDeclarations classBodyDeclaration
	'''

def p_classBodyDeclaration(p):
	'''
		classBodyDeclaration : classMemberDeclaration
		| staticInitializer
		| constructorDeclaration
		| block
	'''

def p_staticInitializer(p):
	'''
		staticInitializer : STATIC block
	'''

def p_constructorDeclaration(p):
	'''
		constructorDeclaration : constructorHead methodBody
	'''

def p_constructorHead(p):
	'''
		constructorHead : constructorName formalParameterList_opt RPAREN methodHeadThrowList_opt
	'''

def p_constructorName(p):
	'''
		constructorName : modifiers_opt typeParameters Identifier LPAREN
		| modifiers_opt Identifier LPAREN
	'''

def p_formalParameterList_opt(p):
	'''
		formalParameterList_opt : formalParameterList
		| empty
	'''

def p_formalParameterList(p):
	'''
		formalParameterList : formalParameter
		| formalParameterList COMMA formalParameter
	'''
def p_formalParameter(p):
	'''
		formalParameter : modifiers_opt type variableDeclaratorId
		| modifiers_opt type OP_ARRAY variableDeclaratorId
	'''
def p_methodHeadThrowList_opt(p):
	'''
		methodHeadThrowList_opt : methodHeadThrowList
		| empty
	'''

def p_methodHeadThrowList(p):
	'''
		methodHeadThrowList : THROWS exceptionTypeList
	'''

def p_exceptionTypeList(p):
	'''
		exceptionTypeList : exceptionType
		| exceptionTypeList exceptionType
	'''

def p_exceptionType(p):
	'''
		exceptionType : classType
	'''

def p_classMemberDeclaration(p):
	'''
		classMemberDeclaration : fieldDeclaration
		| methodDeclaration
		| classDeclaration
		| interfaceDeclaration
		| enumDeclaration
		| annotationTypeDeclaration
		| SEMI
	'''

def p_fieldDeclaration(p):
	'''
		fieldDeclaration : modifiers_opt type variableDeclarators SEMI
	'''
def p_variableDeclarators(p):
	'''
		variableDeclarators : variableDeclarator
		| variableDeclarators COMMA variableDeclarator
	'''

def p_variableDeclarator(p):
	'''
		variableDeclarator : variableDeclaratorId
		| variableDeclaratorId ASS variableInitializer
	'''

def p_variableDeclaratorId(p):
	'''
		variableDeclaratorId : Identifier arrays_opt
	'''

def p_variableInitializer(p):
	'''
		variableInitializer : expression
		| arrayInitializer
	'''

def p_methodDeclaration(p):
	'''
		methodDeclaration : abstractMethodDeclaration
		| methodHeader methodBody
	'''

def p_abstractMethodDeclaration(p):
	'''
		abstractMethodDeclaration : methodHeader SEMI
	'''

def p_methodHeader(p):
	'''
		methodHeader : methodName formalParameterList_opt RPAREN methodHeadExtendedDims methodHeadThrowList_opt
	'''

def p_methodName(p):
	'''
		methodName : modifiers_opt typeParameters type Identifier LPAREN
		| modifiers_opt type Identifier LPAREN
	'''
def p_methodHeadExtendedDims(p):
	'''
		methodHeadExtendedDims : arrays_opt
	'''

def p_methodHeadThrowList_opt(p):
	'''
		methodHeadThrowList_opt : methodHeadThrowList
		| empty
	'''

def p_methodHeadThrowList(p):
	'''
		methodHeadThrowList : THROWS classTypeList
	'''
def p_classTypeList(p):
	'''
		classTypeList : classType
		| classTypeList COMMA classType
	'''

def p_methodBody(p):
	'''
		methodBody : BLPAREN blockStatements_opt BRPAREN
	'''

def p_interfaceDeclaration(p):
	'''
		interfaceDeclaration : interfaceHead InterfaceBody
	'''
def p_interfaceHead(p):
	'''
		interfaceHead : interfaceHeadName interfaceHeadExtends_opt
	'''
def p_interfaceHeadName(p):
	'''
		interfaceHeadName : modifiers_opt INTERFACE Identifier typeParameters
		| modifiers_opt INTERFACE Identifier
	'''

def p_interfaceHeadExtends_opt(p):
	'''
		interfaceHeadExtends_opt : interfaceHeadExtends
		| empty
	'''

def p_interfaceHeadExtends(p):
	'''
		interfaceHeadExtends : EXTENDS interfaceTypeList
	'''

def p_interfaceBody(p):
	'''
		InterfaceBody : BLPAREN interfaceMemberDeclarations_opt BRPAREN
	'''

def p_interfaceMemberDeclarations_opt(p):
	'''
		interfaceMemberDeclarations_opt : interfaceMemberDeclarations
		| empty
	'''
def p_interfaceMemberDeclarations(p):
	'''
		interfaceMemberDeclarations : interfaceMemberDeclaration
		| interfaceMemberDeclarations interfaceMemberDeclaration
	'''

def p_interfaceMemberDeclaration(p):
	'''
		interfaceMemberDeclaration : constantDeclaration
		| abstractMethodDeclaration
		| classDeclaration
		| interfaceDeclaration
		| enumDeclaration
		| annotationTypeDeclaration
		| SEMI
	'''

def p_constantDeclaration(p):
	'''
		constantDeclaration : fieldDeclaration
	'''

def p_enumDeclaration(p):
	'''
		enumDeclaration : enumHead enumBody
	'''

def p_enumHead(p):
	'''
		enumHead : enumHeadName classImpls_opt
	'''

def p_enumHeadName(p):
	'''
		enumHeadName : modifiers_opt ENUM Identifier
		| modifiers_opt ENUM Identifier typeParameters
	'''

def p_enumBody(p):
	'''
		enumBody : BLPAREN enumBodyDeclarations_opt BRPAREN
		| BLPAREN COMMA enumBodyDeclarations_opt BRPAREN
		| BLPAREN enumConstants COMMA enumBodyDeclarations_opt BRPAREN
		| BLPAREN enumConstants enumBodyDeclarations_opt BRPAREN
	'''

def p_enumConstants(p):
	'''
		enumConstants : enumConstant
		| enumConstants COMMA enumConstant
	'''

def p_enumConstant(p):
	'''
		enumConstant : enumConstantHead classBody
		| enumConstantHead
	'''

def p_enumConstantHead(p):
	'''
		enumConstantHead : enumConstantHeadName arguments_opt
	'''

def p_enumConstantHeadName(p):
	'''
		enumConstantHeadName : modifiers_opt Identifier
	'''

def p_arguments_opt(p):
	'''
		arguments_opt : arguments
		| empty
	'''

def p_arguments(p):
	'''
		arguments : LPAREN argumentList_opt RPAREN
	'''

def p_argumentList_opt(p):
	'''
		argumentList_opt : argumentList
		| empty
	'''

def p_argumentList(p):
	'''
		argumentList : expression
		| argumentList COMMA expression
	'''

def p_enumBodyDeclarations_opt(p):
	'''
		enumBodyDeclarations_opt : enumDeclarations
		| empty

	'''

def p_enumDeclarations(p):
	'''
		enumDeclarations : SEMI classBodyDeclarations_opt
	'''

def p_annotationTypeDeclaration(p):
	'''
		annotationTypeDeclaration : annotationTypeDeclarationHead annotationTypeBody
	'''

def p_annotationTypeDeclarationHead(p):
	'''
		annotationTypeDeclarationHead : annotationTypeDeclarationHeadName classExtends_opt classImpls_opt
	'''

def p_annotationTypeDeclarationHeadName(p):
	'''
		annotationTypeDeclarationHeadName : modifiers AT INTERFACE Identifier
		| modifiers AT INTERFACE Identifier typeParameters
		| AT INTERFACE Identifier typeParameters
		| AT INTERFACE Identifier
	'''

def p_annotationTypeBody(p):
	'''
		annotationTypeBody : BLPAREN annotationTypeMemberDeclarations_opt BRPAREN
	'''

def p_annotationTypeMemberDeclarations_opt(p):
	'''
		annotationTypeMemberDeclarations_opt : annotationTypeMemberDeclarations
		| empty
	'''

def p_annotationTypeMemberDeclarations(p):
	'''
		annotationTypeMemberDeclarations : annotationTypeMemberDeclaration
		| annotationTypeMemberDeclarations annotationTypeMemberDeclaration
	'''

def p_annotationTypeMemberDeclaration(p):
	'''
		annotationTypeMemberDeclaration : annotationMethodHead SEMI
		| constantDeclaration
		| constructorDeclaration
		| typeDeclaration
	'''

def p_annotationMethodHead(p):
	'''
		annotationMethodHead : annotationMethodHeadName formalParameterList_opt RPAREN methodHeadExtendedDims annotationMethodHeadDefaultValue_opt
	'''

def p_annotationMethodHeadDefaultValue_opt(p):
	'''
		annotationMethodHeadDefaultValue_opt : defaultValue
		| empty
	'''

def p_annotationMethodHeadName(p):
	'''
		annotationMethodHeadName : modifiers_opt typeParameters type Identifier LPAREN
		| modifiers_opt type Identifier LPAREN
	'''

def p_defaultValue(p):
	'''
		defaultValue : DEFAULT memberValue
	'''

def p_memberValue(p):
	'''
		memberValue : conditionalExpressionNotName
		| name
		| annotation
		| memberValueArrayInitializer
	'''

def p_memberValueArrayInitializer(p):
	'''
		memberValueArrayInitializer : BLPAREN memberValues COMMA BRPAREN
		| BLPAREN memberValues BRPAREN
		| BLPAREN COMMA BRPAREN
		| BLPAREN BRPAREN
	'''

def p_memberValues(p):
	'''
		memberValues : memberValue
		| memberValues COMMA memberValue
	'''


# annotation begin
def p_annotation(p):
	'''
		annotation : normalAnnotation
		| markerAnnotation
		| singleMemberAnnotation
	'''

def p_normalAnnotation(p):
	'''
		normalAnnotation : annotationName LPAREN memberValuePairs_opt RPAREN
	'''

def p_annotationName(p):
	'''
		annotationName : AT name
	'''

def p_memberValuePairs_opt(p):
	'''
		memberValuePairs_opt : memberValuePairs
		| empty
	'''

def p_memberValuePairs(p):
	'''
		memberValuePairs : memberValuePair
		| memberValuePairs COMMA memberValuePair
	'''

def p_memberValuePair(p):
	'''
		memberValuePair : Identifier ASS memberValue
	'''

def p_markerAnnotation(p):
	'''
		markerAnnotation : annotationName
	'''

def p_singleMemberAnnotation(p):
	'''
		singleMemberAnnotation : annotationName LPAREN singleMemberAnnotationMemberValue RPAREN
	'''

def p_singleMemberAnnotationMemberValue(p):
	'''
		singleMemberAnnotationMemberValue : memberValue
	'''
# class end


# block begin
def p_block(p):
	'''
		block : BLPAREN blockStatements_opt BRPAREN
	'''

def p_blockStatements(p):
	'''
		blockStatements : blockStatement
		| blockStatements blockStatement
	'''

def p_blockStatements_opt(p):
	'''
		blockStatements_opt : blockStatements
		| empty
	'''

def p_blockStatement(p):
	'''
		blockStatement : localVariableDeclarationStatement
		| statement
		| classDeclaration
		| interfaceDeclaration
		| annotationTypeDeclaration
		| enumDeclaration
	'''

def p_localVariableDeclarationStatement(p):
	'''
		localVariableDeclarationStatement : localVariableDeclaration SEMI
	'''

def p_localVariableDeclaration(p):
	'''
		localVariableDeclaration : type variableDeclarators
		| modifiers type variableDeclarators
	'''

def p_variableDeclarators(p):
	'''
		variableDeclarators : variableDeclarator
		| variableDeclarators COMMA variableDeclarator
	'''

def p_variableDeclarator(p):
	'''
		variableDeclarator : variableDeclaratorId
		| variableDeclaratorId ASS variableInitializer
	'''

def p_variableDeclaratorId(p):
	'''
		variableDeclaratorId : Identifier arrays_opt
	'''

def p_variableInitializer(p):
	'''
		variableInitializer : expression
		| arrayInitializer
	'''

# statement

def p_statement(p):
	'''
		statement : statementWithoutTrailingSubStatement
		| labeldStatement
		| ifThenStatement
		| ifThenElseStatement
		| whileStatement
		| forStatement
		| enhancedForStatement
	'''

def p_statementWithoutTrailingSubStatement(p):
	'''
		statementWithoutTrailingSubStatement : block
		| expressionStatement
		| assertStatement
		| emptyStatement
		| switchStatement
		| doStatement
		| breakStatement
		| continueStatement
		| returnStatement
		| synchronizedStatement
		| throwStatment
		| tryStatement
		| tryStatementWithResources

	'''



def p_ExpressionStatement(p):
	'''
		expressionStatement : statementExpression SEMI
		| explicitConstructorInvocation
	'''

def p_statementExpression(p):
	'''
		statementExpression : assignment
		| preIncrementExpression
		| preDecrementExpression
		| postIncrementExpression
		| postDecrementExpression
		| methodInvocation
		| classInstanceCreationExpression
	'''

def p_comma_opt(p):
	'''
		comma_opt : COMMA
		| empty
	'''

def p_arrayInitializer(p):
	'''
		arrayInitializer : BLPAREN comma_opt BRPAREN
		| BLPAREN variableInitializers BRPAREN
		| BLPAREN variableInitializers COMMA BRPAREN
	'''

def p_variableInitializers(p):
	'''
		variableInitializers : variableInitializer
		| variableInitializers COMMA variableInitializer
	'''

def p_methodInvocation(p):
	'''
		methodInvocation : name LPAREN argumentList_opt RPAREN
		| name DOT typeArguments Identifier LPAREN argumentList_opt RPAREN
		| primary DOT typeArguments Identifier LPAREN argumentList_opt RPAREN
		| SUPER DOT typeArguments Identifier LPAREN argumentList_opt RPAREN
		| primary DOT Identifier LPAREN argumentList_opt RPAREN
		| SUPER DOT Identifier LPAREN argumentList_opt RPAREN
	'''

def p_labeledStatement(p):
	'''
		labeldStatement : label COLON statement
	'''

def p_labeledStatementNoShortIf(p):
	'''
		labeledStatementNoShortIf : label COLON statementNoShortIf
	'''

def p_label(p):
	'''
		label : Identifier
	'''

def p_ifThenStatement(p):
	'''
		ifThenStatement : IF LPAREN expression RPAREN statement
	'''

def p_ifThenElseStatement(p):
	'''
		ifThenElseStatement : IF LPAREN expression RPAREN statementNoShortIf ELSE statement
	'''

def p_ifThenElseStatementNoShortIf(p):
	'''
		ifThenElseStatementNoShortIf : IF LPAREN expression RPAREN statementNoShortIf ELSE statementNoShortIf
	'''

def p_whileStatement(p):
	'''
		whileStatement : WHILE LPAREN expression RPAREN statement
	'''

def p_whileStatementNoShortIf(p):
	'''
		whileStatementNoShortIf : WHILE LPAREN expression RPAREN statementNoShortIf
	'''

def p_forStatement(p):
	'''
		forStatement : FOR LPAREN forInit_opt SEMI expression_opt SEMI forUpdate_opt RPAREN statement
	'''

def p_forStatementNoShortIf(p):
	'''
		forStatementNoShortIf : FOR LPAREN forInit_opt SEMI expression_opt SEMI forUpdate_opt RPAREN statementNoShortIf
	'''

def p_forInit_opt(p):
	'''
		forInit_opt : forInit
		| empty
	'''

def p_forInit(p):
	'''
		forInit : statementExpressionList
		| localVariableDeclaration
	'''

def p_statementExpressionList(p):
	'''
		statementExpressionList : statementExpression
		| statementExpressionList COMMA statementExpression
	'''

def p_expression_opt(p):
	'''
		expression_opt : expression
		| empty
	'''

def p_forUpdate_opt(p):
	'''
		forUpdate_opt : forUpdate
		| empty
	'''

def p_forUpdate(p):
	'''
		forUpdate : statementExpressionList
	'''

def p_enhancedForStatement(p):
	'''
		enhancedForStatement : enhancedForStatementHead statement
	'''

def p_enhancedForStatementNoShortIf(p):
	'''
		enhancedForStatementNoShortIf : enhancedForStatementHead statementNoShortIf
	'''

def p_enhancedForStatementHead(p):
	'''
		enhancedForStatementHead : enhancedForStatementHeadInit COLON expression RPAREN
	'''

def p_enhancedForStatementHeadInit(p):
	'''
		enhancedForStatementHeadInit : FOR LPAREN type Identifier arrays_opt
		| FOR LPAREN modifiers type Identifier arrays_opt
	'''

def p_statementNoShortIf(p):
	'''
		statementNoShortIf : statementWithoutTrailingSubStatement
		| labeledStatementNoShortIf
		| ifThenElseStatementNoShortIf
		| whileStatementNoShortIf
		| enhancedForStatementNoShortIf
	'''

def p_assertStatement(p):
	'''
		assertStatement : ASSERT expression SEMI
		| ASSERT expression COLON expression SEMI
	'''

def p_empty_statement(p):
	'''
		emptyStatement : SEMI
	'''

def p_switch_statement(p):
	'''
		switchStatement : SWITCH LPAREN expression RPAREN switchBlock
	'''

def p_switchBlock(p):
	'''
		switchBlock : BLPAREN BRPAREN
		| BLPAREN switchBlockStatements BRPAREN
		| BLPAREN switchLabels BRPAREN
		| BLPAREN switchBlockStatements switchLabels BRPAREN
	'''

def p_switchBlockStatements(p):
	'''
		switchBlockStatements : switchBlockStatement
		| switchBlockStatements switchBlockStatement
	'''

def p_switchBlockStatement(p):
	'''
		switchBlockStatement : switchLabels blockStatements
	'''

def p_switchLabels(p):
	'''
		switchLabels : switchLabel
		| switchLabels switchLabel
	'''

def p_switchLabel(p):
	'''
		switchLabel : CASE constantExpression COLON
		| DEFAULT COLON
	'''

def p_constantExpression(p):
	'''
		constantExpression : expression
	'''

def p_doStatement(p):
	'''
		doStatement : DO statement WHILE LPAREN expression RPAREN SEMI
	'''

def p_breakStatement(p):
	'''
		breakStatement : BREAK SEMI
		| BREAK Identifier SEMI
	'''

def p_continueStatement(p):
	'''
		continueStatement : CONTINUE SEMI
		| CONTINUE Identifier SEMI
	'''

def p_returnStatement(p):
	'''
		returnStatement : RETURN expression_opt SEMI
	'''

def p_synchronizedStatement(p):
	'''
		synchronizedStatement : SYNCHRONIZED LPAREN expression RPAREN block
	'''

def p_throwStatement(p):
	'''
		throwStatment : THROW expression SEMI
	'''

def p_tryStatement(p):
	'''
		tryStatement : TRY tryBlock catches
		| TRY tryBlock catches_opt finally
	'''

def p_tryBlock(p):
	'''
		tryBlock : block
	'''

def p_catches_opt(p):
	'''
		catches_opt : catches
		| empty
	'''

def p_catches(p):
	'''
		catches : catchClause
		| catches catchClause
	'''

def p_catchClause(p):
	'''
		catchClause : CATCH LPAREN catchFormalParameter RPAREN block
	'''

def p_catchFormalParameter(p):
	'''
		catchFormalParameter : modifiers_opt catchType variableDeclaratorId
	'''

def p_catchType(p):
	'''
		catchType : unionType
	'''

def p_unionType(p):
	'''
		unionType : type
		| unionType VERTICAL type
	'''

def p_tryStatementWithResources(p):
	'''
		tryStatementWithResources : TRY resourceSpecification tryBlock catches_opt
		| TRY resourceSpecification tryBlock catches_opt finally
	'''

def p_resourceSpecification(p):
	'''
		resourceSpecification : LPAREN resources semi_opt RPAREN
	'''

def p_semi_opt(p):
	'''
		semi_opt : SEMI
		| empty
	'''

def p_resources(p):
	'''
		resources : resource
		| resources trailingSemicolon resource
	'''

def p_trailingSemicolon(p):
	'''
		trailingSemicolon : SEMI
	'''

def p_resource(p):
	'''
		resource : type variableDeclaratorId ASS variableInitializer
		| modifiers type variableDeclaratorId ASS variableInitializer
	'''

def p_finally(p):
	'''
		finally : FINALLY block
	'''

def p_explicitConstructorInvocation(p):
	'''
		explicitConstructorInvocation : THIS LPAREN argumentList_opt RPAREN SEMI
		| SUPER LPAREN argumentList_opt RPAREN SEMI
		| typeArguments SUPER LPAREN argumentList RPAREN SEMI
		| typeArguments THIS LPAREN argumentList_opt RPAREN SEMI
		| primary DOT SUPER LPAREN argumentList_opt RPAREN SEMI
		| name DOT SUPER LPAREN argumentList_opt RPAREN SEMI
		| primary DOT THIS LPAREN argumentList_opt RPAREN SEMI
		| name DOT THIS LPAREN argumentList_opt RPAREN SEMI
		| primary DOT typeArguments SUPER LPAREN argumentList_opt RPAREN SEMI
		| name DOT typeArguments SUPER LPAREN argumentList_opt RPAREN SEMI
		| primary DOT typeArguments THIS LPAREN argumentList_opt RPAREN SEMI
		| name DOT typeArguments THIS LPAREN argumentList_opt RPAREN SEMI
	'''

def p_classInstanceCreationExpression(p):
	'''
		classInstanceCreationExpression : NEW typeArguments classType LPAREN argumentList_opt RPAREN classBody_opt
		| NEW classType LPAREN argumentList_opt RPAREN classBody_opt
		| primary DOT NEW typeArguments classType LPAREN argumentList_opt RPAREN classBody_opt
		| primary DOT NEW classType LPAREN argumentList_opt RPAREN classBody_opt
		| classInstanceCreationExpressionName NEW classType LPAREN argumentList_opt RPAREN classBody_opt
		| classInstanceCreationExpressionName NEW typeArguments classType LPAREN argumentList_opt RPAREN classBody_opt
	'''

def p_classInstanceCreationExpressionName(p):
	'''
		classInstanceCreationExpressionName : name DOT 
	'''

def p_classBody_opt(p):
	'''
		classBody_opt : classBody
		| empty
	'''

def p_fieldAccess(p):
	'''
		fieldAccess : primary DOT Identifier
		| SUPER DOT Identifier
	'''

def p_arrayAccess(p):
	'''
		arrayAccess : name FLPAREN expression FRPAREN
		| primaryNoNewArray FLPAREN expression FRPAREN
		| arrayCreationWithArrayInitializer FLPAREN expression FRPAREN
	'''

def p_arrayCreationWithArrayInitializer(p):
	'''
		arrayCreationWithArrayInitializer : NEW primitiveType arrayWithOrWithoutExprs arrayInitializer
		| NEW classOrInterfaceType arrayWithOrWithoutExprs arrayInitializer
	'''

def p_arrayWithOrWithoutExprs(p):
	'''
		arrayWithOrWithoutExprs : arrayWithOrWithoutExpr
		| arrayWithOrWithoutExprs arrayWithOrWithoutExpr
	'''

def p_arrayWithOrWithoutExpr(p):
	'''
		arrayWithOrWithoutExpr : FLPAREN expression FRPAREN
		| FLPAREN FRPAREN
	'''

# * expression begin

# * expression begin

def p_expression(p):
	'''
		expression : assignmentExpression
	'''

def p_expressionNotName(p):
	'''
		expressionNotName : assignmentExpressionNotName
	'''

def p_assignmentExpression(p):
	'''
		assignmentExpression : assignment
		| conditionalExpression
	'''

def p_assignmentExpressionNotName(p):
	'''
		assignmentExpressionNotName : assignment
		| conditionalExpressionNotName
	'''


def p_assignmentOperator(p):
	'''
	 assignmentOperator :  ASS 
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

def p_assignment(p):
	'''
		assignment : postfixExpression assignmentOperator assignmentExpression
	'''

def p_conditionalExpression(p):
	'''
		conditionalExpression : conditionalOrExpression
		| conditionalOrExpression QUES expression COLON conditionalExpression
	'''

def p_conditionalExpressionNotName(p):
	'''
		conditionalExpressionNotName : conditionalOrExpressionNotName
		| conditionalOrExpressionNotName QUES expression COLON conditionalExpression
		| name QUES expression COLON conditionalExpression
	'''

def p_conditionalOrExpression(p):
	'''
		conditionalOrExpression : conditionalAndExpression
		| conditionalOrExpression OP_LOR conditionalAndExpression
	'''

def p_conditionalOrExpressionNotName(p):
	'''
		conditionalOrExpressionNotName : conditionalAndExpressionNotName
		| conditionalOrExpressionNotName OP_LOR conditionalAndExpression
		| name OP_LOR conditionalAndExpression
	'''

def p_conditionalAndExpression(p):
	'''
		conditionalAndExpression : inclusiveOrExpression
		| conditionalAndExpression OP_LAND inclusiveOrExpression
	'''

def p_conditionalAndExpressionNotName(p):
	'''
		conditionalAndExpressionNotName : inclusiveOrExpressionNotName
		| conditionalAndExpressionNotName OP_LAND inclusiveOrExpression
		| name OP_LAND inclusiveOrExpression
	'''

def p_inclusiveOrExpression(p):
	'''
		inclusiveOrExpression : exclusiveOrExpression
		| inclusiveOrExpression VERTICAL exclusiveOrExpression
	'''
def p_inclusiveOrExpressionNotName(p):
	'''
		inclusiveOrExpressionNotName : exclusiveOrExpressionNotName
		| inclusiveOrExpressionNotName VERTICAL exclusiveOrExpression
		| name VERTICAL exclusiveOrExpression
	'''

def p_exclusiveOrExpression(p):
	'''
		exclusiveOrExpression : andExpression
		| exclusiveOrExpression CARET andExpression
	'''

def p_exclusiveOrExpressionNotName(p):
	'''
		exclusiveOrExpressionNotName : andExpressionNotName
		| exclusiveOrExpressionNotName CARET andExpression
		| name CARET andExpression
	'''


def p_andExpression(p):
	'''
		andExpression : equalityExpression
		| andExpression AND equalityExpression
	'''

def p_andExpressionNotName(p):
	'''
		andExpressionNotName : equalityExpressionNotName
		| andExpressionNotName AND equalityExpression
		| name AND equalityExpression
	'''


def p_equalityExpression(p):
	'''
		equalityExpression : instanceOfExpression
		| equalityExpression OP_EQ instanceOfExpression
		| equalityExpression OP_NE instanceOfExpression
	'''

def p_equalityExpressionNotName(p):
	'''
		equalityExpressionNotName : instanceOfExpressionNotName
		| equalityExpressionNotName OP_EQ instanceOfExpression
		| equalityExpressionNotName OP_NE instanceOfExpression
		| name OP_EQ instanceOfExpression
		| name OP_NE instanceOfExpression
	'''


def p_instanceOfExpression(p):
	'''
		instanceOfExpression : relationalExpression
		| instanceOfExpression INSTANCEOF referenceType
	'''

def p_instanceOfExpressionNotName(p):
	'''
		instanceOfExpressionNotName : relationalExpressionNotName
		| instanceOfExpressionNotName INSTANCEOF referenceType
		| name INSTANCEOF referenceType
	'''

def p_relationalExpression(p):
	'''
		relationalExpression : shiftExpression
		| relationalExpression LESS shiftExpression
		| relationalExpression OP_GE shiftExpression
		| relationalExpression MORE shiftExpression
		| relationalExpression OP_LE shiftExpression
	'''

def p_relationalExpressionNotName(p):
	'''
		relationalExpressionNotName : shiftExpressionNotName
		| relationalExpressionNotName LESS shiftExpression
		| relationalExpressionNotName OP_GE shiftExpression
		| relationalExpressionNotName MORE shiftExpression
		| relationalExpressionNotName OP_LE shiftExpression
		| name LESS shiftExpression
		| name OP_GE shiftExpression
		| name MORE shiftExpression
		| name OP_LE shiftExpression
	'''

def p_shiftExpression(p):
	'''
		shiftExpression : additiveExpression
		| shiftExpression OP_SHR additiveExpression
		| shiftExpression OP_SHL additiveExpression
		| shiftExpression OP_SHRR additiveExpression
	'''

def p_shiftExpressionNotName(p):
	'''
		shiftExpressionNotName : additiveExpressionNotName
		| shiftExpressionNotName OP_SHR additiveExpression
		| shiftExpressionNotName OP_SHL additiveExpression
		| shiftExpressionNotName OP_SHRR additiveExpression
		| name OP_SHR additiveExpression
		| name OP_SHL additiveExpression
		| name OP_SHRR additiveExpression
	'''


def p_additiveExpression(p):
	'''
		additiveExpression : multiplicativeExpression
		| additiveExpression PLUS multiplicativeExpression
		| additiveExpression DASH multiplicativeExpression
	'''

def p_additiveExpressionNotName(p):
	'''
		additiveExpressionNotName : multiplicativeExpressionNotName
		| additiveExpressionNotName PLUS multiplicativeExpression
		| additiveExpressionNotName DASH multiplicativeExpression
		| name PLUS multiplicativeExpression
		| name DASH multiplicativeExpression
	'''

def p_multiplicativeExpression(p):
	'''
		multiplicativeExpression : unaryExpression
	 	| multiplicativeExpression MULT unaryExpression
		| multiplicativeExpression SLASH unaryExpression
		| multiplicativeExpression PERCENT unaryExpression
	'''

def p_multiplicativeExpressionNotName(p):
	'''
		multiplicativeExpressionNotName : unaryExpressionNotName
	 	| multiplicativeExpressionNotName MULT unaryExpression
		| multiplicativeExpressionNotName SLASH unaryExpression
		| multiplicativeExpressionNotName PERCENT unaryExpression
	 	| name MULT unaryExpression
		| name SLASH unaryExpression
		| name PERCENT unaryExpression
	'''


def p_unaryExpression(p):
	'''
		unaryExpression : preIncrementExpression
		| preDecrementExpression
		| PLUS unaryExpression
		| DASH unaryExpression
		| unaryExpressionNotPlusMinus
	'''

def p_unaryExpressionNotName(p):
	'''
		unaryExpressionNotName : preIncrementExpression
		| preDecrementExpression
		| PLUS unaryExpression
		| DASH unaryExpression
		| unaryExpressionNotPlusMinusNotName
	'''


def p_preIncrementExpression(p):
	'''
		preIncrementExpression : OP_INC unaryExpression
	'''

def p_preDecrementExpression(p):
	'''
		preDecrementExpression : OP_DEC unaryExpression
	'''

def p_postIncrementExpression(p):
	'''
		postIncrementExpression : postfixExpression OP_INC
	'''

def p_postDecrementExpression(p):
	'''
		postDecrementExpression : postfixExpression OP_DEC
	'''


def p_unaryExpressionNotPlusMinus(p):
	'''
		unaryExpressionNotPlusMinus : TILDE unaryExpression
		| EXCLAMATION unaryExpression
		| postfixExpression
		| castExpression
	'''

def p_unaryExpressionNotPlusMinusNotName(p):
	'''
		unaryExpressionNotPlusMinusNotName : TILDE unaryExpression
		| EXCLAMATION unaryExpression
		| postfixExpressionNotName
		| castExpression
	'''

def p_postfixExpression(p):
	'''
		postfixExpression : primary
		| name
		| postIncrementExpression
		| postDecrementExpression
	'''

def p_postfixExpressionNotName(p):
	'''
		postfixExpressionNotName : primary
		| postIncrementExpression
		| postDecrementExpression
	'''

def p_primary(p):
	'''
		primary : primaryNoNewArray
		| arrayCreationWithArrayInitializer
		| arrayCreationWithoutArrayInitializer
	'''

def p_primaryNoNewArray(p):
	'''
		primaryNoNewArray : literal
		| THIS
		| classInstanceCreationExpression
		| fieldAccess
		| methodInvocation
		| arrayAccess
		| LPAREN name RPAREN
		| LPAREN expressionNotName RPAREN
		| name DOT THIS
		| name DOT SUPER
		| name DOT CLASS
		| name arrays DOT CLASS
		| primitiveType arrays DOT CLASS
		| primitiveType DOT CLASS
	'''

def p_castExpression(p):
	'''
	 	castExpression :  LPAREN primitiveType arrays_opt RPAREN unaryExpression
		| LPAREN name typeArguments arrays_opt RPAREN unaryExpressionNotPlusMinus
		| LPAREN name typeArguments DOT classOrInterfaceType arrays_opt RPAREN unaryExpressionNotPlusMinus
		| LPAREN name RPAREN unaryExpressionNotPlusMinus
		| LPAREN name arrays RPAREN unaryExpressionNotPlusMinus
	'''

def p_arrayCreationWithoutArrayInitializer(p):
	'''
		arrayCreationWithoutArrayInitializer : NEW primitiveType arrayWithOrWithoutExprs
		| NEW classOrInterfaceType arrayWithOrWithoutExprs
	'''

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

def p_FloatingPointLiteral( p ):
	'''
		FloatingPointLiteral : NON_INTEGER_1
		| NON_INTEGER_2
		| NON_INTEGER_3
		| NON_INTEGER_4
		| NON_INTEGER_5
		| NON_INTEGER_6
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


	objectTree.printAll()

	if b.error : return None
	global is_pass

	#if is_pass:
	#	print "%s was successed" % filename
	if not is_pass :
		print "%s was failed" % filename
