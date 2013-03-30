# *.* coding=utf-8 *.*

import ply.yacc as yacc
import lex
from collections import deque

tokens = lex.tokens
# deque(['compilationUnit', ':', ['annotations', 'expr_0', '|', 'expt_2', 'expt_0', 'expt_1']]) 
def p_compilationUnit(p):
	'''
	 compilationUnit : expt_2 expt_0 expt_1
		| expt_2 expt_0 empty
		| expt_2 empty expt_1
		| expt_2 empty empty
		| empty expt_0 expt_1
		| empty expt_0 empty
		| empty empty expt_1
		| empty empty empty
		| annotations expr_0
	'''

	pass

# deque(['packageDeclaration', ':', ['PACKAGE', 'qualifiedName', 'SEMI']]) 
def p_packageDeclaration(p):
	'''
	 packageDeclaration :  PACKAGE qualifiedName SEMI
	'''

	pass

# deque(['importDeclaration', ':', ['IMPORT', 'expt_3', 'qualifiedName', 'expt_4', 'SEMI']]) 
def p_importDeclaration(p):
	'''
	 importDeclaration : IMPORT expt_3 qualifiedName expt_4 SEMI
		| IMPORT expt_3 qualifiedName SEMI
		| IMPORT qualifiedName expt_4 SEMI
		| IMPORT qualifiedName SEMI
	'''

	pass

# deque(['typeDeclaration', ':', ['classOrInterfaceDeclaration', '|', 'SEMI']]) 
def p_typeDeclaration(p):
	'''
	 typeDeclaration :  classOrInterfaceDeclaration 
	| SEMI
	'''

	pass

# deque(['classOrInterfaceDeclaration', ':', ['classOrInterfaceModifiers', 'expr_1']]) 
def p_classOrInterfaceDeclaration(p):
	'''
	 classOrInterfaceDeclaration :  classOrInterfaceModifiers expr_1
	 							| expr_1
	'''

	pass

# deque(['classOrInterfaceModifiers', ':', ['expt_5']]) 
def p_classOrInterfaceModifiers(p):
	'''
	 classOrInterfaceModifiers : expt_5
		| empty
	'''

	pass

# deque(['classOrInterfaceModifier', ':', ['annotation', '|', 'PUBLIC', '|', 'PROTECTED', '|', 'PRIVATE', '|', 'ABSTRACT', '|', 'STATIC', '|', 'FINAL', '|', 'STRICTFP']]) 
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

# deque(['modifiers', ':', ['expt_6']]) 
def p_modifiers(p):
	'''
	 modifiers : expt_6
		| empty
	'''

	pass

# deque(['classDeclaration', ':', ['normalClassDeclaration', '|', 'enumDeclaration']]) 
def p_classDeclaration(p):
	'''
	 classDeclaration :  normalClassDeclaration 
	| enumDeclaration
	'''

	pass

# deque(['normalClassDeclaration', ':', ['CLASS', 'Identifier', 'expt_7', 'expt_8', 'expt_9', 'classBody']]) 
def p_normalClassDeclaration(p):
	'''
	 normalClassDeclaration : CLASS Identifier typeParameters expt_8 expt_9 classBody
		| CLASS Identifier typeParameters expt_8 empty classBody
		| CLASS Identifier typeParameters empty expt_9 classBody
		| CLASS Identifier typeParameters empty empty classBody
		| CLASS Identifier empty expt_8 expt_9 classBody
		| CLASS Identifier empty expt_8 empty classBody
		| CLASS Identifier empty empty expt_9 classBody
		| CLASS Identifier empty empty empty classBody
	'''

	pass

# deque(['typeParameters', ':', ['LESS', 'typeParameter', 'expt_10', 'MORE']]) 
def p_typeParameters(p):
	'''
	 typeParameters : LESS typeParameter expt_10 MORE
		| LESS typeParameter empty MORE
	'''

	pass

# deque(['typeParameter', ':', ['Identifier', 'expt_11']]) 
def p_typeParameter(p):
	'''
	 typeParameter : Identifier expt_11
		| Identifier empty
	'''

	pass

# deque(['typeBound', ':', ['type', 'expt_12']]) 
def p_typeBound(p):
	'''
	 typeBound : type expt_12
		| type empty
	'''

	pass

# deque(['enumDeclaration', ':', ['ENUM', 'Identifier', 'expt_9', 'enumBody']]) 
def p_enumDeclaration(p):
	'''
	 enumDeclaration : ENUM Identifier expt_9 enumBody
		| ENUM Identifier empty enumBody
	'''

	pass

# deque(['enumBody', ':', ['BLPAREN', 'expt_13', 'expt_14', 'expt_15', 'BRPAREN']]) 
def p_enumBody(p):
	'''
	 enumBody : BLPAREN expt_13 expt_14 expt_15 BRPAREN
		| BLPAREN expt_13 expt_14 empty BRPAREN
		| BLPAREN expt_13 empty expt_15 BRPAREN
		| BLPAREN expt_13 empty empty BRPAREN
		| BLPAREN empty expt_14 expt_15 BRPAREN
		| BLPAREN empty expt_14 empty BRPAREN
		| BLPAREN empty empty expt_15 BRPAREN
		| BLPAREN empty empty empty BRPAREN
	'''

	pass

# deque(['enumConstants', ':', ['enumConstant', 'expt_16']]) 
def p_enumConstants(p):
	'''
	 enumConstants : enumConstant expt_16
		| enumConstant empty
	'''

	pass

# deque(['enumConstant', ':', ['expt_17', 'Identifier', 'expt_18', 'expt_19']]) 
def p_enumConstant(p):
	'''
	 enumConstant : expt_17 Identifier expt_18 classBody
		| expt_17 Identifier expt_18 
		| expt_17 Identifier  classBody
		| expt_17 Identifier  
		| Identifier expt_18 classBody
		| Identifier expt_18 
		| Identifier  classBody
		| Identifier 
	'''

	pass

# deque(['enumBodyDeclarations', ':', ['SEMI', 'expt_20']]) 
def p_enumBodyDeclarations(p):
	'''
	 enumBodyDeclarations : SEMI classBodyDeclarations
		| SEMI
	'''

	pass

# deque(['interfaceDeclaration', ':', ['normalInterfaceDeclaration', '|', 'annotationTypeDeclaration']]) 
def p_interfaceDeclaration(p):
	'''
	 interfaceDeclaration :  normalInterfaceDeclaration 
	| annotationTypeDeclaration
	'''

	pass

# deque(['normalInterfaceDeclaration', ':', ['INTERFACE', 'Identifier', 'expt_7', 'expt_21', 'interfaceBody']]) 
def p_normalInterfaceDeclaration(p):
	'''
	 normalInterfaceDeclaration : INTERFACE Identifier typeParameters expt_21 interfaceBody
		| INTERFACE Identifier typeParameters empty interfaceBody
		| INTERFACE Identifier empty expt_21 interfaceBody
		| INTERFACE Identifier empty empty interfaceBody
	'''

	pass

# deque(['typeList', ':', ['type', 'expt_22']]) 
def p_typeList(p):
	'''
	 typeList : type expt_22
		| type empty
	'''

	pass

# deque(['classBody', ':', ['BLPAREN', 'expt_20', 'BRPAREN']]) 
def p_classBody(p):
	'''
	 classBody : BLPAREN classBodyDeclarations BRPAREN
		| BLPAREN  BRPAREN
	'''

	pass

# deque(['interfaceBody', ':', ['BLPAREN', 'expt_23', 'BRPAREN']]) 
def p_interfaceBody(p):
	'''
	 interfaceBody : BLPAREN expt_23 BRPAREN
		| BLPAREN empty BRPAREN
	'''

	pass

# deque(['classBodyDeclaration', ':', ['SEMI', '|', 'expt_3', 'block', '|', 'modifiers', 'memberDecl']]) 
def p_classBodyDeclaration(p):
	'''
	 classBodyDeclaration : modifiers memberDecl
		| expt_3 block
		| empty block
		| SEMI
	'''

	pass

# deque(['memberDecl', ':', ['genericMethodOrConstructorDecl', '|', 'memberDeclaration', '|', 'VOID', 'Identifier', 'voidMethodDeclaratorRest', '|', 'Identifier', 'constructorDeclaratorRest', '|', 'interfaceDeclaration', '|', 'classDeclaration']]) 
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

# deque(['memberDeclaration', ':', ['type', 'expr_2']]) 
def p_memberDeclaration(p):
	'''
	 memberDeclaration :  type expr_2
	'''

	pass

# deque(['genericMethodOrConstructorDecl', ':', ['typeParameters', 'genericMethodOrConstructorRest']]) 
def p_genericMethodOrConstructorDecl(p):
	'''
	 genericMethodOrConstructorDecl :  typeParameters genericMethodOrConstructorRest
	'''

	pass

# deque(['genericMethodOrConstructorRest', ':', ['expr_3', 'Identifier', 'methodDeclaratorRest', '|', 'Identifier', 'constructorDeclaratorRest']]) 
def p_genericMethodOrConstructorRest(p):
	'''
	 genericMethodOrConstructorRest :  expr_3 Identifier methodDeclaratorRest 
	| Identifier constructorDeclaratorRest
	'''

	pass

# deque(['methodDeclaration', ':', ['Identifier', 'methodDeclaratorRest']]) 
def p_methodDeclaration(p):
	'''
	 methodDeclaration :  Identifier methodDeclaratorRest
	'''

	pass

# deque(['fieldDeclaration', ':', ['variableDeclarators', 'SEMI']]) 
def p_fieldDeclaration(p):
	'''
	 fieldDeclaration :  variableDeclarators SEMI
	'''

	pass

# deque(['interfaceBodyDeclaration', ':', ['modifiers', 'interfaceMemberDecl', '|', 'SEMI']]) 
def p_interfaceBodyDeclaration(p):
	'''
	 interfaceBodyDeclaration :  modifiers interfaceMemberDecl 
	| SEMI
	'''

	pass

# deque(['interfaceMemberDecl', ':', ['interfaceMethodOrFieldDecl', '|', 'interfaceGenericMethodDecl', '|', 'VOID', 'Identifier', 'voidInterfaceMethodDeclaratorRest', '|', 'interfaceDeclaration', '|', 'classDeclaration']]) 
def p_interfaceMemberDecl(p):
	'''
	 interfaceMemberDecl :  interfaceMethodOrFieldDecl 
	| interfaceGenericMethodDecl 
	| VOID Identifier voidInterfaceMethodDeclaratorRest 
	| interfaceDeclaration 
	| classDeclaration
	'''

	pass

# deque(['interfaceMethodOrFieldDecl', ':', ['type', 'Identifier', 'interfaceMethodOrFieldRest']]) 
def p_interfaceMethodOrFieldDecl(p):
	'''
	 interfaceMethodOrFieldDecl :  type Identifier interfaceMethodOrFieldRest
	'''

	pass

# deque(['interfaceMethodOrFieldRest', ':', ['constantDeclaratorsRest', 'SEMI', '|', 'interfaceMethodDeclaratorRest']]) 
def p_interfaceMethodOrFieldRest(p):
	'''
	 interfaceMethodOrFieldRest :  constantDeclaratorsRest SEMI 
	| interfaceMethodDeclaratorRest
	'''

	pass

# deque(['methodDeclaratorRest', ':', ['formalParameters', 'expt_24', 'expt_25', 'expr_4']]) 
def p_methodDeclaratorRest(p):
	'''
	 methodDeclaratorRest : formalParameters expt_24 expt_25 expr_4
		| formalParameters expt_24 empty expr_4
		| formalParameters empty expt_25 expr_4
		| formalParameters empty empty expr_4
	'''

	pass

# deque(['voidMethodDeclaratorRest', ':', ['formalParameters', 'expt_25', 'expr_4']]) 
def p_voidMethodDeclaratorRest(p):
	'''
	 voidMethodDeclaratorRest : formalParameters expt_25 expr_4
		| formalParameters empty expr_4
	'''

	pass

# deque(['interfaceMethodDeclaratorRest', ':', ['formalParameters', 'expt_24', 'expt_25', 'SEMI']]) 
def p_interfaceMethodDeclaratorRest(p):
	'''
	 interfaceMethodDeclaratorRest : formalParameters expt_24 expt_25 SEMI
		| formalParameters expt_24 empty SEMI
		| formalParameters empty expt_25 SEMI
		| formalParameters empty empty SEMI
	'''

	pass

# deque(['interfaceGenericMethodDecl', ':', ['typeParameters', 'expr_3', 'Identifier', 'interfaceMethodDeclaratorRest']]) 
def p_interfaceGenericMethodDecl(p):
	'''
	 interfaceGenericMethodDecl :  typeParameters expr_3 Identifier interfaceMethodDeclaratorRest
	'''

	pass

# deque(['voidInterfaceMethodDeclaratorRest', ':', ['formalParameters', 'expt_25', 'SEMI']]) 
def p_voidInterfaceMethodDeclaratorRest(p):
	'''
	 voidInterfaceMethodDeclaratorRest : formalParameters expt_25 SEMI
		| formalParameters empty SEMI
	'''

	pass

# deque(['constructorDeclaratorRest', ':', ['formalParameters', 'expt_25', 'constructorBody']]) 
def p_constructorDeclaratorRest(p):
	'''
	 constructorDeclaratorRest : formalParameters expt_25 constructorBody
		| formalParameters empty constructorBody
	'''

	pass

# deque(['constantDeclarator', ':', ['Identifier', 'constantDeclaratorRest']]) 
def p_constantDeclarator(p):
	'''
	 constantDeclarator :  Identifier constantDeclaratorRest
	'''

	pass

# deque(['variableDeclarators', ':', ['variableDeclarator', 'expt_26']]) 
def p_variableDeclarators(p):
	'''
	 variableDeclarators : variableDeclarator expt_26
		| variableDeclarator empty
	'''

	pass

# deque(['variableDeclarator', ':', ['variableDeclaratorId', 'expt_27']]) 
def p_variableDeclarator(p):
	'''
	 variableDeclarator : variableDeclaratorId expt_27
		| variableDeclaratorId empty
	'''

	pass

# deque(['constantDeclaratorsRest', ':', ['constantDeclaratorRest', 'expt_28']]) 
def p_constantDeclaratorsRest(p):
	'''
	 constantDeclaratorsRest : constantDeclaratorRest expt_28
		| constantDeclaratorRest empty
	'''

	pass

# deque(['constantDeclaratorRest', ':', ['expt_24', 'EQUALS', 'variableInitializer']]) 
def p_constantDeclaratorRest(p):
	'''
	 constantDeclaratorRest : expt_24 EQUALS variableInitializer
		| empty EQUALS variableInitializer
	'''

	pass

# deque(['variableDeclaratorId', ':', ['Identifier', 'expt_24']]) 
def p_variableDeclaratorId(p):
	'''
	 variableDeclaratorId : Identifier expt_24
		| Identifier empty
	'''

	pass

# deque(['variableInitializer', ':', ['arrayInitializer', '|', 'expression']]) 
def p_variableInitializer(p):
	'''
	 variableInitializer :  arrayInitializer 
	| expression
	'''

	pass

# deque(['arrayInitializer', ':', ['BLPAREN', 'expt_31', 'BRPAREN']]) 
def p_arrayInitializer(p):
	'''
	 arrayInitializer : BLPAREN expt_31 BRPAREN
		| BLPAREN empty BRPAREN
	'''

	pass

# deque(['modifier', ':', ['annotation', '|', 'PUBLIC', '|', 'PROTECTED', '|', 'PRIVATE', '|', 'STATIC', '|', 'ABSTRACT', '|', 'FINAL', '|', 'NATIVE', '|', 'SYNCHRONIZED', '|', 'TRANSIENT', '|', 'VOLATILE', '|', 'STRICTFP']]) 
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


# deque(['enumConstantName', ':', ['Identifier']]) 
def p_enumConstantName(p):
	'''
	 enumConstantName :  Identifier
	'''

	pass

# deque(['type', ':', ['classOrInterfaceType', 'expt_24', '|', 'primitiveType', 'expt_24']]) 
def p_type(p):
	'''
	 type : primitiveType expt_24
		| primitiveType empty
		| classOrInterfaceType expt_24
		| classOrInterfaceType empty
	'''

	pass

# deque(['classOrInterfaceType', ':', ['Identifier', 'expt_32', 'expt_33']]) 
def p_classOrInterfaceType(p):
	'''
	 classOrInterfaceType : Identifier expt_32 expt_33
		| Identifier expt_32 empty
		| Identifier empty expt_33
		| Identifier empty empty
	'''

	pass

# deque(['primitiveType', ':', ['BOOLEAN', '|', 'CHAR', '|', 'BYTE', '|', 'SHORT', '|', 'INT', '|', 'LONG', '|', 'FLOAT', '|', 'DOUBLE']]) 
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

# deque(['variableModifier', ':', ['FINAL', '|', 'annotation']]) 
def p_variableModifier(p):
	'''
	 variableModifier :  FINAL 
	| annotation
	'''

	pass

# deque(['typeArguments', ':', ['LESS', 'typeArgument', 'expt_34', 'MORE']]) 
def p_typeArguments(p):
	'''
	 typeArguments : LESS typeArgument expt_34 MORE
		| LESS typeArgument MORE
	'''

	pass

# deque(['typeArgument', ':', ['type', '|', 'QUES', 'expt_35']]) 
def p_typeArgument(p):
	'''
	 typeArgument : QUES expt_35
		| QUES empty
		| type
	'''

	pass

# deque(['qualifiedNameList', ':', ['qualifiedName', 'expt_36']]) 
def p_qualifiedNameList(p):
	'''
	 qualifiedNameList : qualifiedName expt_36
		| qualifiedName empty
	'''

	pass

# deque(['formalParameters', ':', ['LPAREN', 'expt_37', 'RPAREN']]) 
def p_formalParameters(p):
	'''
	 formalParameters : LPAREN expt_37 RPAREN
		| LPAREN empty RPAREN
	'''

	pass

# deque(['formalParameterDecls', ':', ['variableModifiers', 'type', 'formalParameterDeclsRest']]) 
def p_formalParameterDecls(p):
	'''
	 formalParameterDecls :  variableModifiers type formalParameterDeclsRest
	 					| type formalParameterDeclsRest
	'''

	pass

# deque(['formalParameterDeclsRest', ':', ['variableDeclaratorId', 'expt_38', '|', 'OP_ARRAY', 'variableDeclaratorId']]) 
def p_formalParameterDeclsRest(p):
	'''
	 formalParameterDeclsRest : OP_ARRAY variableDeclaratorId
		| variableDeclaratorId expt_38
		| variableDeclaratorId empty
	'''

	pass

# deque(['methodBody', ':', ['block']]) 
def p_methodBody(p):
	'''
	 methodBody :  block
	'''

	pass

# deque(['constructorBody', ':', ['BLPAREN', 'expt_39', 'expt_40', 'BRPAREN']]) 
def p_constructorBody(p):
	'''
	 constructorBody : BLPAREN expt_39 expt_40 BRPAREN
		| BLPAREN expt_39 empty BRPAREN
		| BLPAREN empty expt_40 BRPAREN
		| BLPAREN empty empty BRPAREN
	'''

	pass

# deque(['explicitConstructorInvocation', ':', ['expt_41', 'expr_6', 'arguments', 'SEMI', '|', 'primary', 'DOT', 'expt_41', 'SUPER', 'arguments', 'SEMI']]) 
def p_explicitConstructorInvocation(p):
	'''
	 explicitConstructorInvocation : primary DOT expt_41 SUPER arguments SEMI
		| primary DOT empty SUPER arguments SEMI
		| expt_41 expr_6 arguments SEMI
		| empty expr_6 arguments SEMI
	'''

	pass

# deque(['qualifiedName', ':', ['Identifier', 'expt_42']]) 
def p_qualifiedName(p):
	'''
	 qualifiedName : Identifier expt_42
		| Identifier empty
	'''

	pass

# deque(['literal', ':', ['integerLiteral', '|', 'FloatingPointLiteral', '|', 'CharacterLiteral', '|', 'StringLiteral', '|', 'booleanLiteral', '|', 'NULL']]) 
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

# deque(['booleanLiteral', ':', ['TRUE', '|', 'FALSE']]) 
def p_booleanLiteral(p):
	'''
	 booleanLiteral :  TRUE 
	| FALSE
	'''

	pass

# deque(['annotations', ':', ['expr_7']]) 
def p_annotations(p):
	'''
	 annotations :  annotation
	 			| annotations annotation
	'''

	pass

# deque(['annotation', ':', ['AT', 'annotationName', 'expt_43']]) 
def p_annotation(p):
	'''
	 annotation : AT annotationName LPAREN elementValuePairs RPAREN
	 	|  AT annotationName LPAREN elementValue RPAREN
	 	| AT annotationName LPAREN RPAREN
		| AT annotationName 
	'''

	pass

# deque(['annotationName', ':', ['Identifier', 'expt_42']]) 
def p_annotationName(p):
	'''
	 annotationName : Identifier expt_42
		| Identifier empty
	'''

	pass

# deque(['elementValuePairs', ':', ['elementValuePair', 'expt_44']]) 
def p_elementValuePairs(p):
	'''
	 elementValuePairs : elementValuePair expt_44
		| elementValuePair empty
	'''

	pass

# deque(['elementValuePair', ':', ['Identifier', 'EQUALS', 'elementValue']]) 
def p_elementValuePair(p):
	'''
	 elementValuePair :  Identifier EQUALS elementValue
	'''

	pass

# deque(['elementValue', ':', ['conditionalExpression', '|', 'annotation', '|', 'elementValueArrayInitializer']]) 
def p_elementValue(p):
	'''
	 elementValue :  conditionalExpression 
	| annotation 
	| elementValueArrayInitializer
	'''

	pass

# deque(['elementValueArrayInitializer', ':', ['BLPAREN', 'expt_46', 'expt_30', 'BRPAREN']]) 
def p_elementValueArrayInitializer(p):
	'''
	 elementValueArrayInitializer : BLPAREN expt_46 expt_30 BRPAREN
		| BLPAREN expt_46 empty BRPAREN
		| BLPAREN empty expt_30 BRPAREN
		| BLPAREN empty empty BRPAREN
	'''

	pass

# deque(['annotationTypeDeclaration', ':', ['AT', 'INTERFACE', 'Identifier', 'annotationTypeBody']]) 
def p_annotationTypeDeclaration(p):
	'''
	 annotationTypeDeclaration :  AT INTERFACE Identifier annotationTypeBody
	'''

	pass

# deque(['annotationTypeBody', ':', ['BLPAREN', 'expt_47', 'BRPAREN']]) 
def p_annotationTypeBody(p):
	'''
	 annotationTypeBody : BLPAREN expt_47 BRPAREN
		| BLPAREN empty BRPAREN
	'''

	pass

# deque(['annotationTypeElementDeclaration', ':', ['modifiers', 'annotationTypeElementRest']]) 
def p_annotationTypeElementDeclaration(p):
	'''
	 annotationTypeElementDeclaration :  modifiers annotationTypeElementRest
	'''

	pass

# deque(['annotationTypeElementRest', ':', ['type', 'annotationMethodOrConstantRest', 'SEMI', '|', 'normalClassDeclaration', 'expt_48', '|', 'normalInterfaceDeclaration', 'expt_48', '|', 'enumDeclaration', 'expt_48', '|', 'annotationTypeDeclaration', 'expt_48']]) 
def p_annotationTypeElementRest(p):
	'''
	 annotationTypeElementRest : annotationTypeDeclaration expt_48
		| annotationTypeDeclaration empty
		| enumDeclaration expt_48
		| enumDeclaration empty
		| normalInterfaceDeclaration expt_48
		| normalInterfaceDeclaration empty
		| normalClassDeclaration expt_48
		| normalClassDeclaration empty
		| type annotationMethodOrConstantRest SEMI
	'''

	pass

# deque(['annotationMethodOrConstantRest', ':', ['annotationMethodRest', '|', 'annotationConstantRest']]) 
def p_annotationMethodOrConstantRest(p):
	'''
	 annotationMethodOrConstantRest :  annotationMethodRest 
	| annotationConstantRest
	'''

	pass

# deque(['annotationMethodRest', ':', ['Identifier', 'LPAREN', 'RPAREN', 'expt_49']]) 
def p_annotationMethodRest(p):
	'''
	 annotationMethodRest : Identifier LPAREN RPAREN expt_49
		| Identifier LPAREN RPAREN empty
	'''

	pass

# deque(['annotationConstantRest', ':', ['variableDeclarators']]) 
def p_annotationConstantRest(p):
	'''
	 annotationConstantRest :  variableDeclarators
	'''

	pass

# deque(['defaultValue', ':', ['DEFAULT', 'elementValue']]) 
def p_defaultValue(p):
	'''
	 defaultValue :  DEFAULT elementValue
	'''

	pass

# deque(['block', ':', ['BLPAREN', 'expt_40', 'BRPAREN']]) 
def p_block(p):
	'''
	 block : BLPAREN expt_40 BRPAREN
		| BLPAREN empty BRPAREN
	'''

	pass

# deque(['blockStatement', ':', ['localVariableDeclarationStatement', '|', 'classOrInterfaceDeclaration', '|', 'statement']]) 
def p_blockStatement(p):
	'''
	 blockStatement :  localVariableDeclarationStatement 
	| classOrInterfaceDeclaration 
	| statement
	'''

	pass

# deque(['localVariableDeclarationStatement', ':', ['localVariableDeclaration', 'SEMI']]) 
def p_localVariableDeclarationStatement(p):
	'''
	 localVariableDeclarationStatement :  localVariableDeclaration SEMI
	 |	SEMI
	'''

	pass

# deque(['localVariableDeclaration', ':', ['variableModifiers', 'type', 'variableDeclarators']]) 
def p_localVariableDeclaration(p):
	'''
	 localVariableDeclaration :  variableModifiers type variableDeclarators
	 						| type variableDeclarators
	'''

	pass

# deque(['variableModifiers', ':', ['expt_50']]) 
def p_variableModifiers(p):
	'''
	 variableModifiers : expt_50
	'''

	pass

# deque(['statement', ':', ['block', '|', 'ASSERT', 'expression', 'expt_51', 'SEMI', '|', 'IF', 'parExpression', 'statement', 'expt_52', '|', 'FOR', 'LPAREN', 'forControl', 'RPAREN', 'statement', '|', 'WHILE', 'parExpression', 'statement', '|', 'DO', 'statement', 'WHILE', 'parExpression', 'SEMI', '|', 'TRY', 'block', 'expr_9', '|', 'SWITCH', 'parExpression', 'BLPAREN', 'switchBlockStatementGroups', 'BRPAREN', '|', 'SYNCHRONIZED', 'parExpression', 'block', '|', 'RETURN', 'expt_53', 'SEMI', '|', 'THROW', 'expression', 'SEMI', '|', 'BREAK', 'expt_54', 'SEMI', '|', 'CONTINUE', 'expt_54', 'SEMI', '|', 'SEMI', '|', 'statementExpression', 'SEMI', '|', 'Identifier', 'COLON', 'statement']]) 
def p_statement(p):
	'''
	 statement : Identifier COLON statement
		| statementExpression SEMI
		| SEMI
		| CONTINUE Identifier SEMI
		| CONTINUE SEMI
		| BREAK Identifier SEMI
		| BREAK  SEMI
		| THROW expression SEMI
		| RETURN expt_53 SEMI
		| RETURN SEMI
		| SYNCHRONIZED parExpression block
		| SWITCH parExpression BLPAREN switchBlockStatementGroups BRPAREN
		| TRY block expr_9
		| DO statement WHILE parExpression SEMI
		| WHILE parExpression statement
		| FOR LPAREN forControl RPAREN statement
		| IF parExpression statement ELSE statement
		| IF parExpression statement 
		| ASSERT expression expt_51 SEMI
		| ASSERT expression SEMI
		| block
	'''

	pass

# deque(['catches', ':', ['catchClause', 'expt_55']]) 
def p_catches(p):
	'''
	 catches : catchClause expt_55
		| catchClause empty
	'''

	pass

# deque(['catchClause', ':', ['CATCH', 'LPAREN', 'formalParameter', 'RPAREN', 'block']]) 
def p_catchClause(p):
	'''
	 catchClause :  CATCH LPAREN formalParameter RPAREN block
	'''

	pass

# deque(['formalParameter', ':', ['variableModifiers', 'type', 'variableDeclaratorId']]) 
def p_formalParameter(p):
	'''
	 formalParameter :  variableModifiers type variableDeclaratorId
	'''

	pass

# deque(['switchBlockStatementGroups', ':', ['expt_56']]) 
def p_switchBlockStatementGroups(p):
	'''
	 switchBlockStatementGroups : expt_56
		| empty
	'''

	pass

# deque(['switchBlockStatementGroup', ':', ['expr_10', 'expt_40']]) 
def p_switchBlockStatementGroup(p):
	'''
	 switchBlockStatementGroup : expr_10 expt_40
		| expr_10 empty
	'''

	pass

# deque(['switchLabel', ':', ['CASE', 'constantExpression', 'COLON', '|', 'CASE', 'enumConstantName', 'COLON', '|', 'DEFAULT', 'COLON']]) 
def p_switchLabel(p):
	'''
	 switchLabel :  CASE constantExpression COLON 
	| CASE enumConstantName COLON 
	| DEFAULT COLON
	'''

	pass

# deque(['forControl', ':', ['enhancedForControl', '|', 'expt_57', 'SEMI', 'expt_58', 'SEMI', 'expt_59']]) 
def p_forControl(p):
	'''
	 forControl : expt_57 SEMI expt_58 SEMI expt_59
		| expt_57 SEMI expt_58 SEMI empty
		| expt_57 SEMI empty SEMI expt_59
		| expt_57 SEMI empty SEMI empty
		| empty SEMI expt_58 SEMI expt_59
		| empty SEMI expt_58 SEMI empty
		| empty SEMI empty SEMI expt_59
		| empty SEMI empty SEMI empty
		| enhancedForControl
	'''

	pass

# deque(['forInit', ':', ['localVariableDeclaration', '|', 'expressionList']]) 
def p_forInit(p):
	'''
	 forInit :  localVariableDeclaration 
	| expressionList
	'''

	pass

# deque(['enhancedForControl', ':', ['variableModifiers', 'type', 'Identifier', 'COLON', 'expression']]) 
def p_enhancedForControl(p):
	'''
	 enhancedForControl :  variableModifiers type Identifier COLON expression
	'''

	pass

# deque(['forUpdate', ':', ['expressionList']]) 
def p_forUpdate(p):
	'''
	 forUpdate :  expressionList
	'''

	pass

# deque(['parExpression', ':', ['LPAREN', 'expression', 'RPAREN']]) 
def p_parExpression(p):
	'''
	 parExpression :  LPAREN expression RPAREN
	'''

	pass

# deque(['expressionList', ':', ['expression', 'expt_60']]) 
def p_expressionList(p):
	'''
	 expressionList : expression expt_60
		| expression 
	'''

	pass

# deque(['statementExpression', ':', ['expression']]) 
def p_statementExpression(p):
	'''
	 statementExpression :  expression
	'''

	pass

# deque(['constantExpression', ':', ['expression']]) 
def p_constantExpression(p):
	'''
	 constantExpression :  expression
	'''

	pass

# deque(['expression', ':', ['conditionalExpression', 'expt_61']]) 
def p_expression(p):
	'''
	 expression : conditionalExpression assignmentOperator expression
				| conditionalExpression 
	'''

	pass

# deque(['assignmentOperator', ':', ['EQUALS', '|', 'ASS_ADD', '|', 'ASS_SUB', '|', 'ASS_MUL', '|', 'ASS_DIV', '|', 'ASS_AND', '|', 'ASS_OR', '|', 'ASS_XOR', '|', 'ASS_MOD', '|', 'LESS', 'LESS', 'EQUALS', '|', 'MORE', 'MORE', 'MORE', 'EQUALS', '|', 'MORE', 'MORE', 'EQUALS']]) 
def p_assignmentOperator(p):
	'''
	 assignmentOperator : EQUALS 
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

# deque(['conditionalExpression', ':', ['conditionalOrExpression', 'expt_62']]) 
def p_conditionalExpression(p):
	'''
	 conditionalExpression : conditionalOrExpression QUES expression COLON expression 
		| conditionalOrExpression 
	'''

	pass

# deque(['conditionalOrExpression', ':', ['conditionalAndExpression', 'expt_63']]) 
def p_conditionalOrExpression(p):
	'''
	 conditionalOrExpression : conditionalAndExpression expt_63
		| conditionalAndExpression  
	'''

	pass

# deque(['conditionalAndExpression', ':', ['inclusiveOrExpression', 'expt_64']]) 
def p_conditionalAndExpression(p):
	'''
	 conditionalAndExpression : inclusiveOrExpression expt_64
		| inclusiveOrExpression 
	'''

	pass

# deque(['inclusiveOrExpression', ':', ['exclusiveOrExpression', 'expt_65']]) 
def p_inclusiveOrExpression(p):
	'''
	 inclusiveOrExpression : exclusiveOrExpression expt_65
		| exclusiveOrExpression 
	'''

	pass

# deque(['exclusiveOrExpression', ':', ['andExpression', 'expt_66']]) 
def p_exclusiveOrExpression(p):
	'''
	 exclusiveOrExpression : andExpression expt_66
		| andExpression 
	'''

	pass

# deque(['andExpression', ':', ['equalityExpression', 'expt_67']]) 
def p_andExpression(p):
	'''
	 andExpression : equalityExpression expt_67
		| equalityExpression 
	'''

	pass

# deque(['equalityExpression', ':', ['instanceOfExpression', 'expt_68']]) 
def p_equalityExpression(p):
	'''
	 equalityExpression : instanceOfExpression expt_68
		| instanceOfExpression 
	'''

	pass

# deque(['instanceOfExpression', ':', ['relationalExpression', 'expt_69']]) 
def p_instanceOfExpression(p):
	'''
	 instanceOfExpression : relationalExpression INSTANCEOF type
		| relationalExpression
	'''

	pass

# deque(['relationalExpression', ':', ['shiftExpression', 'expt_70']]) 
def p_relationalExpression(p):
	'''
	 relationalExpression : shiftExpression expt_70
		| shiftExpression 
	'''

	pass

# deque(['relationalOp', ':', ['LESS', 'EQUALS', '|', 'MORE', 'EQUALS', '|', 'LESS', '|', 'MORE']]) 
def p_relationalOp(p):
	'''
	 relationalOp : OP_LE
	| OP_GE 
	| LESS 
	| MORE
	'''

	pass

# deque(['shiftExpression', ':', ['additiveExpression', 'expt_71']]) 
def p_shiftExpression(p):
	'''
	 shiftExpression : additiveExpression expt_71
		| additiveExpression 
	'''

	pass

# deque(['shiftOp', ':', ['LESS', 'LESS', '|', 'MORE', 'MORE', 'MORE', '|', 'MORE', 'MORE']]) 
def p_shiftOp(p):
	'''
	 shiftOp :  OP_SHR 
	| OP_SHL
	| OP_SHRR
	'''

	pass

# deque(['additiveExpression', ':', ['multiplicativeExpression', 'expt_72']]) 
def p_additiveExpression(p):
	'''
	 additiveExpression : multiplicativeExpression expt_72
		| multiplicativeExpression 
	'''

	pass

# deque(['multiplicativeExpression', ':', ['unaryExpression', 'expt_73']]) 
def p_multiplicativeExpression(p):
	'''
	 multiplicativeExpression : unaryExpression expt_73
		| unaryExpression 
	'''

	pass

# deque(['unaryExpression', ':', ['PLUS', 'unaryExpression', '|', 'DASH', 'unaryExpression', '|', 'OP_INC', 'unaryExpression', '|', 'OP_DEC', 'unaryExpression', '|', 'unaryExpressionNotPlusMinus']]) 
def p_unaryExpression(p):
	'''
	 unaryExpression :  PLUS unaryExpression 
	| DASH unaryExpression 
	| OP_INC unaryExpression 
	| OP_DEC unaryExpression 
	| unaryExpressionNotPlusMinus
	'''

	pass

# deque(['unaryExpressionNotPlusMinus', ':', ['TILDE', 'unaryExpression', '|', 'EXCLAMATION', 'unaryExpression', '|', 'castExpression', '|', 'primary', 'expt_74', 'expr_14']]) 
def p_unaryExpressionNotPlusMinus(p):
	'''
	 unaryExpressionNotPlusMinus : primary expt_74 expr_14
		| primary expr_14
		| primary expt_74
		| primary
		| castExpression
		| EXCLAMATION unaryExpression
		| TILDE unaryExpression
	'''

	pass

# deque(['castExpression', ':', ['LPAREN', 'primitiveType', 'RPAREN', 'unaryExpression', '|', 'LPAREN', 'expr_15', 'RPAREN', 'unaryExpressionNotPlusMinus']]) 
def p_castExpression(p):
	'''
	 castExpression :  LPAREN primitiveType RPAREN unaryExpression 
	| LPAREN expr_15 RPAREN unaryExpressionNotPlusMinus
	'''

	pass

# deque(['primary', ':', ['parExpression', '|', 'THIS', 'expt_42', 'expt_75', '|', 'SUPER', 'superSuffix', '|', 'literal', '|', 'NEW', 'creator', '|', 'Identifier', 'expt_42', 'expt_75', '|', 'primitiveType', 'expt_24', 'DOT', 'CLASS', '|', 'VOID', 'DOT', 'CLASS']]) 
def p_primary(p):
	'''
	 primary : VOID DOT CLASS
		| primitiveType expt_24 DOT CLASS
		| primitiveType DOT CLASS
		| Identifier expt_42 identifierSuffix
		| Identifier expt_42
		| Identifier identifierSuffix
		| Identifier
		| NEW creator
		| literal
		| SUPER superSuffix
		| THIS expt_42 identifierSuffix
		| THIS expt_42 
		| THIS identifierSuffix
		| THIS 
		| parExpression
	'''

	pass

# deque(['identifierSuffix', ':', ['expr_16', 'DOT', 'CLASS', '|', 'expr_17', '|', 'arguments', '|', 'DOT', 'CLASS', '|', 'DOT', 'explicitGenericInvocation', '|', 'DOT', 'THIS', '|', 'DOT', 'SUPER', 'arguments', '|', 'DOT', 'NEW', 'innerCreator']]) 
def p_identifierSuffix(p):
	'''
	 identifierSuffix :  suffixStatements DOT CLASS 
	| suffixExprStatements 
	| arguments 
	| DOT CLASS 
	| DOT explicitGenericInvocation 
	| DOT THIS 
	| DOT SUPER arguments 
	| DOT NEW innerCreator
	'''

	pass

# deque(['creator', ':', ['nonWildcardTypeArguments', 'createdName', 'classCreatorRest', '|', 'createdName', 'expr_18']]) 
def p_creator(p):
	'''
	 creator :  nonWildcardTypeArguments createdName classCreatorRest 
	| createdName classCreatorRest
	| createdName arrayCreatorRest
	'''

	pass

# deque(['createdName', ':', ['classOrInterfaceType', '|', 'primitiveType']]) 
def p_createdName(p):
	'''
	 createdName :  classOrInterfaceType 
	| primitiveType
	'''

	pass

# deque(['innerCreator', ':', ['expt_41', 'Identifier', 'classCreatorRest']]) 
def p_innerCreator(p):
	'''
	 innerCreator : expt_41 Identifier classCreatorRest
		| empty Identifier classCreatorRest
	'''

	pass

# deque(['arrayCreatorRest', ':', ['FLPAREN', 'expr_19']]) 
def p_arrayCreatorRest(p):
	'''
	 arrayCreatorRest :  FLPAREN expr_19
	'''

	pass

# deque(['classCreatorRest', ':', ['arguments', 'expt_19']]) 
def p_classCreatorRest(p):
	'''
	 classCreatorRest : arguments 
		| arguments classBody
	'''

	pass

# deque(['explicitGenericInvocation', ':', ['nonWildcardTypeArguments', 'Identifier', 'arguments']]) 
def p_explicitGenericInvocation(p):
	'''
	 explicitGenericInvocation :  nonWildcardTypeArguments Identifier arguments
	'''

	pass

# deque(['nonWildcardTypeArguments', ':', ['LESS', 'typeList', 'MORE']]) 
def p_nonWildcardTypeArguments(p):
	'''
	 nonWildcardTypeArguments :  LESS typeList MORE
	'''

	pass

# deque(['selector', ':', ['DOT', 'Identifier', 'expt_18', '|', 'DOT', 'THIS', '|', 'DOT', 'SUPER', 'superSuffix', '|', 'DOT', 'NEW', 'innerCreator', '|', 'FLPAREN', 'expression', 'FRPAREN']]) 
def p_selector(p):
	'''
	 selector : FLPAREN expression FRPAREN
		| DOT NEW innerCreator
		| DOT SUPER superSuffix
		| DOT THIS
		| DOT Identifier expt_18
		| DOT Identifier empty
	'''

	pass

# deque(['superSuffix', ':', ['arguments', '|', 'DOT', 'Identifier', 'expt_18']]) 
def p_superSuffix(p):
	'''
	 superSuffix : DOT Identifier expt_18
		| DOT Identifier empty
		| arguments
	'''

	pass

# deque(['arguments', ':', ['LPAREN', 'expt_77', 'RPAREN']]) 
def p_arguments(p):
	'''
	 arguments : LPAREN expressionList RPAREN
		| LPAREN  RPAREN
	'''

	pass

# None 
def p_expr_0(p):
	'''
	 expr_0 :  packageDeclaration expt_0 expt_1 
	| classOrInterfaceDeclaration expt_1
	'''

	pass

# None 
def p_expr_1(p):
	'''
	 expr_1 :  classDeclaration 
	| interfaceDeclaration
	'''

	pass

# None 
def p_expr_2(p):
	'''
	 expr_2 :  methodDeclaration 
	| fieldDeclaration
	'''

	pass

# None 
def p_expr_3(p):
	'''
	 expr_3 :  type 
	| VOID
	'''

	pass

# None 
def p_expr_4(p):
	'''
	 expr_4 :  methodBody 
	| SEMI
	'''

	pass

# None 
def p_expr_5(p):
	'''
	 expr_5 :  EXTENDS 
	| SUPER
	'''

	pass

# None 
def p_expr_6(p):
	'''
	 expr_6 :  THIS 
	| SUPER
	'''

	pass



# None 
def p_expr_9(p):
	'''
	 expr_9 :  catches FINALLY block 
	| catches 
	| FINALLY block

	'''

	pass

# None 
def p_expr_10(p):
	'''
	 expr_10 :  switchLabel 
	| expr_10 switchLabel
	'''

	pass

# None 
def p_expr_11(p):
	'''
	 expr_11 :  OP_EQ 
	| OP_NE
	'''

	pass

# None 
def p_expr_12(p):
	'''
	 expr_12 :  PLUS 
	| DASH
	'''

	pass

# None 
def p_expr_13(p):
	'''
	 expr_13 :  MULT 
	| SLASH 
	| PERCENT
	'''

	pass

# None 
def p_expr_14(p):
	'''
	 expr_14 :  OP_INC 
	| OP_DEC
	'''

	pass

# None 
def p_expr_15(p):
	'''
	 expr_15 :  type 
	| expression
	'''

	pass

# None 
def p_suffixStatements(p):
	'''
	 suffixStatements :  FLPAREN FRPAREN 
	| suffixStatements FLPAREN FRPAREN
	'''

	pass

# None 
def p_suffixExprStatements(p):
	'''
	 suffixExprStatements :  FLPAREN expression FRPAREN 
	| suffixExprStatements FLPAREN expression FRPAREN
	'''

	pass


# None 
def p_expr_19(p):
	'''
	 expr_19 :  FRPAREN expt_24 arrayInitializer 
	| expression FRPAREN expt_76 expt_24
	'''

	pass

# None 
def p_expt_0(p):
	'''
	 expt_0 :  importDeclaration 
	| expt_0 importDeclaration
	'''

	pass

# None 
def p_expt_1(p):
	'''
	 expt_1 :  typeDeclaration 
	| expt_1 typeDeclaration
	'''

	pass

# None 
def p_expt_2(p):
	'''
	 expt_2 :  packageDeclaration 
	| empty
	'''

	pass

# None 
def p_expt_3(p):
	'''
	 expt_3 :  STATIC 
	| empty
	'''

	pass

# None 
def p_expt_4(p):
	'''
	 expt_4 :  DOT MULT 
	| empty
	'''

	pass

# None 
def p_expt_5(p):
	'''
	 expt_5 :  classOrInterfaceModifier 
	| expt_5 classOrInterfaceModifier
	'''

	pass

# None 
def p_expt_6(p):
	'''
	 expt_6 :  modifier 
	| expt_6 modifier
	'''

	pass

# None 
def p_expt_7(p):
	'''
	 expt_7 :  typeParameters 
	| empty
	'''

	pass

# None 
def p_expt_8(p):
	'''
	 expt_8 :  EXTENDS type
	'''

	pass

# None 
def p_expt_9(p):
	'''
	 expt_9 :  IMPLEMENTS typeList 
	| empty
	'''

	pass

# None 
def p_expt_10(p):
	'''
	 expt_10 :  COMMA typeParameter 
	| expt_10 COMMA typeParameter
	'''

	pass

# None 
def p_expt_11(p):
	'''
	 expt_11 :  EXTENDS typeBound 
	| empty
	'''

	pass

# None 
def p_expt_12(p):
	'''
	 expt_12 :  AND type 
	| expt_12 AND type
	'''

	pass

# None 
def p_expt_13(p):
	'''
	 expt_13 :  enumConstants 
	| empty
	'''

	pass

# None 
def p_expt_14(p):
	'''
	 expt_14 :  COMMA 
	| empty
	'''

	pass

# None 
def p_expt_15(p):
	'''
	 expt_15 :  enumBodyDeclarations 
	| empty
	'''

	pass

# None 
def p_expt_16(p):
	'''
	 expt_16 :  COMMA enumConstant 
	| expt_16 COMMA enumConstant
	'''

	pass

# None 
def p_expt_17(p):
	'''
	 expt_17 :  annotations 
	| empty
	'''

	pass

# None 
def p_expt_18(p):
	'''
	 expt_18 :  arguments 
	| empty
	'''

	pass


# None 
def p_classBodyDeclarations(p):
	'''
	 classBodyDeclarations :  classBodyDeclaration 
	| classBodyDeclarations classBodyDeclaration
	'''

	pass

# None 
def p_expt_21(p):
	'''
	 expt_21 :  EXTENDS typeList 
	| empty
	'''

	pass

# None 
def p_expt_22(p):
	'''
	 expt_22 :  COMMA type 
	| expt_22 COMMA type
	'''

	pass

# None 
def p_expt_23(p):
	'''
	 expt_23 :  interfaceBodyDeclaration 
	| expt_23 interfaceBodyDeclaration
	'''

	pass

# None 
def p_expt_24(p):
	'''
	 expt_24 :  FLPAREN FRPAREN 
	| expt_24 FLPAREN FRPAREN
	'''

	pass

# None 
def p_expt_25(p):
	'''
	 expt_25 :  THROWS qualifiedNameList 
	| empty
	'''

	pass

# None 
def p_expt_26(p):
	'''
	 expt_26 :  COMMA variableDeclarator 
	| expt_26 COMMA variableDeclarator
	'''

	pass

# None 
def p_expt_27(p):
	'''
	 expt_27 :  EQUALS variableInitializer 
	| empty
	'''

	pass

# None 
def p_expt_28(p):
	'''
	 expt_28 :  COMMA constantDeclarator 
	| expt_28 COMMA constantDeclarator
	'''

	pass

# None 
def p_expt_29(p):
	'''
	 expt_29 :  COMMA variableInitializer 
	| expt_29 COMMA variableInitializer
	'''

	pass

# None 
def p_expt_30(p):
	'''
	 expt_30 :  COMMA 
	| empty
	'''

	pass

# None 
def p_expt_31(p):
	'''
	 expt_31 :  variableInitializer expt_29 expt_30 
	| empty
	'''

	pass

# None 
def p_expt_32(p):
	'''
	 expt_32 :  typeArguments 
	| empty
	'''

	pass

# None 
def p_expt_33(p):
	'''
	 expt_33 :  DOT Identifier expt_32 
	| expt_33 DOT Identifier expt_32
	'''

	pass

# None 
def p_expt_34(p):
	'''
	 expt_34 :  COMMA typeArgument 
	| expt_34 COMMA typeArgument
	'''

	pass

# None 
def p_expt_35(p):
	'''
	 expt_35 :  expr_5 type 
	| empty
	'''

	pass

# None 
def p_expt_36(p):
	'''
	 expt_36 :  COMMA qualifiedName 
	| expt_36 COMMA qualifiedName
	'''

	pass

# None 
def p_expt_37(p):
	'''
	 expt_37 :  formalParameterDecls 
	| empty
	'''

	pass

# None 
def p_expt_38(p):
	'''
	 expt_38 :  COMMA formalParameterDecls 
	| empty
	'''

	pass

# None 
def p_expt_39(p):
	'''
	 expt_39 :  explicitConstructorInvocation 
	| empty
	'''

	pass

# None 
def p_expt_40(p):
	'''
	 expt_40 :  blockStatement 
	| expt_40 blockStatement
	'''

	pass

# None 
def p_expt_41(p):
	'''
	 expt_41 :  nonWildcardTypeArguments 
	| empty
	'''

	pass

# None 
def p_expt_42(p):
	'''
	 expt_42 :  DOT Identifier
	| expt_42 DOT Identifier
	'''

	pass


# None 
def p_expt_44(p):
	'''
	 expt_44 :  COMMA elementValuePair 
	| expt_44 COMMA elementValuePair
	'''

	pass

# None 
def p_expt_45(p):
	'''
	 expt_45 :  COMMA elementValue 
	| expt_45 COMMA elementValue
	| empty
	'''

	pass

# None 
def p_expt_46(p):
	'''
	 expt_46 :  elementValue expt_45
	'''

	pass

# None 
def p_expt_47(p):
	'''
	 expt_47 :  annotationTypeElementDeclaration 
	| expt_47 annotationTypeElementDeclaration
	'''

	pass

# None 
def p_expt_48(p):
	'''
	 expt_48 :  SEMI 
	| empty
	'''

	pass

# None 
def p_expt_49(p):
	'''
	 expt_49 :  defaultValue 
	| empty
	'''

	pass

# None 
def p_expt_50(p):
	'''
	 expt_50 :  variableModifier 
	| expt_50 variableModifier
	'''

	pass

# None 
def p_expt_51(p):
	'''
	 expt_51 :  COLON expression 
	| empty
	'''

	pass


# None 
def p_expt_53(p):
	'''
	 expt_53 :  expression 
	| empty
	'''

	pass

# None 
def p_expt_55(p):
	'''
	 expt_55 :  catchClause 
	| expt_55 catchClause
	'''

	pass

# None 
def p_expt_56(p):
	'''
	 expt_56 :  switchBlockStatementGroup 
	| expt_56 switchBlockStatementGroup
	'''

	pass

# None 
def p_expt_57(p):
	'''
	 expt_57 :  forInit 
	| empty
	'''

	pass

# None 
def p_expt_58(p):
	'''
	 expt_58 :  expression 
	| empty
	'''

	pass

# None 
def p_expt_59(p):
	'''
	 expt_59 :  forUpdate 
	| empty
	'''

	pass

# None 
def p_expt_60(p):
	'''
	 expt_60 :  COMMA expression 
	| expt_60 COMMA expression
	'''

	pass



# None 
def p_expt_63(p):
	'''
	 expt_63 :  OP_LOR conditionalAndExpression 
	| expt_63 OP_LOR conditionalAndExpression
	'''

	pass

# None 
def p_expt_64(p):
	'''
	 expt_64 :  OP_LAND inclusiveOrExpression 
	| expt_64 OP_LAND inclusiveOrExpression
	'''

	pass

# None 
def p_expt_65(p):
	'''
	 expt_65 :  VERTICAL exclusiveOrExpression 
	| expt_65 VERTICAL exclusiveOrExpression
	'''

	pass

# None 
def p_expt_66(p):
	'''
	 expt_66 :  CARET andExpression 
	| expt_66 CARET andExpression
	'''

	pass

# None 
def p_expt_67(p):
	'''
	 expt_67 :  AND equalityExpression 
	| expt_67 AND equalityExpression
	'''

	pass

# None 
def p_expt_68(p):
	'''
	 expt_68 :  expr_11 instanceOfExpression 
	| expt_68 expr_11 instanceOfExpression
	'''

	pass



# None 
def p_expt_70(p):
	'''
	 expt_70 :  relationalOp shiftExpression 
	| expt_70 relationalOp shiftExpression
	'''

	pass

# None 
def p_expt_71(p):
	'''
	 expt_71 :  shiftOp additiveExpression 
	| expt_71 shiftOp additiveExpression
	'''

	pass

# None 
def p_expt_72(p):
	'''
	 expt_72 :  expr_12 multiplicativeExpression 
	| expt_72 expr_12 multiplicativeExpression
	'''

	pass

def p_sub_expt_73(p):
	'''
	sub_expt_73 : expr_13 unaryExpression
	'''
# None 
def p_expt_73(p):
	'''
	 expt_73 : sub_expt_73
	| expt_73 sub_expt_73
	'''

	pass

# None 
def p_expt_74(p):
	'''
	 expt_74 :  selector 
	| expt_74 selector
	'''

	pass


# None 
def p_expt_76(p):
	'''
	 expt_76 :  FLPAREN expression FRPAREN 
	| expt_76 FLPAREN expression FRPAREN
	'''

	pass


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
	
