# *.* coding=utf-8 *.*

import ply.yacc as yacc
import lex
from collections import deque

tokens = lex.tokens

def p_compilationUnit(p):
	'''
	 compilationUnit : annotations expr_1
		| packageDeclaration expt_1 expt_2
		| packageDeclaration expt_1 
		| packageDeclaration  expt_2
		| packageDeclaration  
		|  expt_1 expt_2
		|  expt_1 
		|   expt_2
	'''

	pass


def p_packageDeclaration(p):
	'''
	 packageDeclaration :  PACKAGE qualifiedName SEMI
	'''

	pass


def p_importDeclaration(p):
	'''
	 importDeclaration : IMPORT STATIC qualifiedName DOT MULT SEMI
		| IMPORT STATIC qualifiedName  SEMI
		| IMPORT  qualifiedName DOT MULT SEMI
		| IMPORT  qualifiedName  SEMI
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
	 classOrInterfaceDeclaration : classOrInterfaceModifiers expr_2
		|  expr_2
	'''

	pass


def p_classOrInterfaceModifiers(p):
	'''
	 classOrInterfaceModifiers : expt_3
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
	 modifiers : expt_4
	'''

	pass


def p_classDeclaration(p):
	'''
	 classDeclaration :  normalClassDeclaration 
	| enumDeclaration
	'''

	pass


def p_normalClassDeclaration(p):
	'''
	 normalClassDeclaration : CLASS Identifier typeParameters EXTENDS type IMPLEMENTS typeList classBody
		| CLASS Identifier typeParameters EXTENDS type  classBody
		| CLASS Identifier typeParameters  IMPLEMENTS typeList classBody
		| CLASS Identifier typeParameters   classBody
		| CLASS Identifier  EXTENDS type IMPLEMENTS typeList classBody
		| CLASS Identifier  EXTENDS type  classBody
		| CLASS Identifier   IMPLEMENTS typeList classBody
		| CLASS Identifier    classBody
	'''

	pass


def p_typeParameters(p):
	'''
	 typeParameters : LESS typeParameter expt_5 MORE
		| LESS typeParameter  MORE
	'''

	pass


def p_typeParameter(p):
	'''
	 typeParameter : Identifier EXTENDS typeBound
		| Identifier 
	'''

	pass


def p_typeBound(p):
	'''
	 typeBound : type expt_6
		| type 
	'''

	pass


def p_enumDeclaration(p):
	'''
	 enumDeclaration : ENUM Identifier IMPLEMENTS typeList enumBody
		| ENUM Identifier  enumBody
	'''

	pass


def p_enumBody(p):
	'''
	 enumBody : BLPAREN enumConstants COMMA enumBodyDeclarations BRPAREN
		| BLPAREN enumConstants COMMA  BRPAREN
		| BLPAREN enumConstants  enumBodyDeclarations BRPAREN
		| BLPAREN enumConstants   BRPAREN
		| BLPAREN  COMMA enumBodyDeclarations BRPAREN
		| BLPAREN  COMMA  BRPAREN
		| BLPAREN   enumBodyDeclarations BRPAREN
		| BLPAREN    BRPAREN
	'''

	pass


def p_enumConstants(p):
	'''
	 enumConstants : enumConstant expt_7
		| enumConstant 
	'''

	pass


def p_enumConstant(p):
	'''
	 enumConstant : annotations Identifier arguments classBody
		| annotations Identifier arguments 
		| annotations Identifier  classBody
		| annotations Identifier  
		|  Identifier arguments classBody
		|  Identifier arguments 
		|  Identifier  classBody
		|  Identifier  
	'''

	pass


def p_enumBodyDeclarations(p):
	'''
	 enumBodyDeclarations : SEMI expt_8
		| SEMI 
	'''

	pass


def p_interfaceDeclaration(p):
	'''
	 interfaceDeclaration :  normalInterfaceDeclaration 
	| annotationTypeDeclaration
	'''

	pass


def p_normalInterfaceDeclaration(p):
	'''
	 normalInterfaceDeclaration : INTERFACE Identifier typeParameters EXTENDS typeList interfaceBody
		| INTERFACE Identifier typeParameters  interfaceBody
		| INTERFACE Identifier  EXTENDS typeList interfaceBody
		| INTERFACE Identifier   interfaceBody
	'''

	pass


def p_typeList(p):
	'''
	 typeList : type expt_9
		| type 
	'''

	pass


def p_classBody(p):
	'''
	 classBody : BLPAREN expt_8 BRPAREN
		| BLPAREN  BRPAREN
	'''

	pass


def p_interfaceBody(p):
	'''
	 interfaceBody : BLPAREN expt_10 BRPAREN
		| BLPAREN  BRPAREN
	'''

	pass


def p_classBodyDeclaration(p):
	'''
	 classBodyDeclaration : SEMI
		| STATIC block
		|  block
		| modifiers memberDecl
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
	 memberDeclaration :  type expr_3
	'''

	pass


def p_genericMethodOrConstructorDecl(p):
	'''
	 genericMethodOrConstructorDecl :  typeParameters genericMethodOrConstructorRest
	'''

	pass


def p_genericMethodOrConstructorRest(p):
	'''
	 genericMethodOrConstructorRest :  expr_4 Identifier methodDeclaratorRest 
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
	 interfaceBodyDeclaration :  modifiers interfaceMemberDecl 
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


def p_methodDeclaratorRest(p):
	'''
	 methodDeclaratorRest : formalParameters expt_11 THROWS qualifiedNameList expr_5
		| formalParameters expt_11  expr_5
		| formalParameters  THROWS qualifiedNameList expr_5
		| formalParameters   expr_5
	'''

	pass


def p_voidMethodDeclaratorRest(p):
	'''
	 voidMethodDeclaratorRest : formalParameters THROWS qualifiedNameList expr_6
		| formalParameters  expr_6
	'''

	pass


def p_interfaceMethodDeclaratorRest(p):
	'''
	 interfaceMethodDeclaratorRest : formalParameters expt_11 THROWS qualifiedNameList SEMI
		| formalParameters expt_11  SEMI
		| formalParameters  THROWS qualifiedNameList SEMI
		| formalParameters   SEMI
	'''

	pass


def p_interfaceGenericMethodDecl(p):
	'''
	 interfaceGenericMethodDecl :  typeParameters expr_7 Identifier interfaceMethodDeclaratorRest
	'''

	pass


def p_voidInterfaceMethodDeclaratorRest(p):
	'''
	 voidInterfaceMethodDeclaratorRest : formalParameters THROWS qualifiedNameList SEMI
		| formalParameters  SEMI
	'''

	pass


def p_constructorDeclaratorRest(p):
	'''
	 constructorDeclaratorRest : formalParameters THROWS qualifiedNameList constructorBody
		| formalParameters  constructorBody
	'''

	pass


def p_constantDeclarator(p):
	'''
	 constantDeclarator :  Identifier constantDeclaratorRest
	'''

	pass


def p_variableDeclarators(p):
	'''
	 variableDeclarators : variableDeclarator expt_12
		| variableDeclarator 
	'''

	pass


def p_variableDeclarator(p):
	'''
	 variableDeclarator : variableDeclaratorId EQUALS variableInitializer
		| variableDeclaratorId 
	'''

	pass


def p_constantDeclaratorsRest(p):
	'''
	 constantDeclaratorsRest : constantDeclaratorRest expt_13
		| constantDeclaratorRest 
	'''

	pass


def p_constantDeclaratorRest(p):
	'''
	 constantDeclaratorRest : expt_11 EQUALS variableInitializer
		|  EQUALS variableInitializer
	'''

	pass


def p_variableDeclaratorId(p):
	'''
	 variableDeclaratorId : Identifier expt_11
		| Identifier 
	'''

	pass


def p_variableInitializer(p):
	'''
	 variableInitializer :  arrayInitializer 
	| expression
	'''

	pass


def p_arrayInitializer(p):
	'''
	 arrayInitializer : BLPAREN  BRPAREN
		| BLPAREN variableInitializer expt_14 COMMA BRPAREN
		| BLPAREN variableInitializer expt_14  BRPAREN
		| BLPAREN variableInitializer  COMMA BRPAREN
		| BLPAREN variableInitializer   BRPAREN
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
	 type : classOrInterfaceType expt_11
		| classOrInterfaceType 
		| primitiveType expt_11
		| primitiveType 
	'''

	pass


def p_classOrInterfaceType(p):
	'''
	 classOrInterfaceType : Identifier typeArguments expt_15
		| Identifier typeArguments 
		| Identifier  expt_15
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


def p_typeArguments(p):
	'''
	 typeArguments : LESS typeArgument expt_16 MORE
		| LESS typeArgument  MORE
	'''

	pass


def p_typeArgument(p):
	'''
	 typeArgument : type
		| QUES expr_8 type
		| QUES 
	'''

	pass


def p_qualifiedNameList(p):
	'''
	 qualifiedNameList : qualifiedName expt_17
		| qualifiedName 
	'''

	pass


def p_formalParameters(p):
	'''
	 formalParameters : LPAREN formalParameterDecls RPAREN
		| LPAREN  RPAREN
	'''

	pass


def p_formalParameterDecls(p):
	'''
	 formalParameterDecls : variableModifiers type formalParameterDeclsRest
		|  type formalParameterDeclsRest
	'''

	pass


def p_formalParameterDeclsRest(p):
	'''
	 formalParameterDeclsRest : variableDeclaratorId COMMA formalParameterDecls
		| variableDeclaratorId 
		| OP_ARRAY variableDeclaratorId
	'''

	pass


def p_methodBody(p):
	'''
	 methodBody :  block
	'''

	pass


def p_constructorBody(p):
	'''
	 constructorBody : BLPAREN explicitConstructorInvocation expt_18 BRPAREN
		| BLPAREN explicitConstructorInvocation  BRPAREN
		| BLPAREN  expt_18 BRPAREN
		| BLPAREN   BRPAREN
	'''

	pass


def p_explicitConstructorInvocation(p):
	'''
	 explicitConstructorInvocation : nonWildcardTypeArguments expr_9 arguments SEMI
		|  expr_9 arguments SEMI
		| primary DOT nonWildcardTypeArguments SUPER arguments SEMI
		| primary DOT  SUPER arguments SEMI
	'''

	pass


def p_qualifiedName(p):
	'''
	 qualifiedName : Identifier expt_19
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
	 annotations :  expr_10
	'''

	pass


def p_annotation(p):
	'''
	 annotation : AT annotationName 
		| AT annotationName LPAREN expr_11 RPAREN
		| AT annotationName LPAREN  RPAREN
	'''

	pass


def p_annotationName(p):
	'''
	 annotationName : Identifier expt_19
		| Identifier 
	'''

	pass


def p_elementValuePairs(p):
	'''
	 elementValuePairs : elementValuePair expt_20
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


def p_elementValueArrayInitializer(p):
	'''
	 elementValueArrayInitializer : BLPAREN elementValue expt_21 COMMA BRPAREN
		| BLPAREN elementValue expt_21  BRPAREN
		| BLPAREN  COMMA BRPAREN
		| BLPAREN   BRPAREN
	'''

	pass


def p_annotationTypeDeclaration(p):
	'''
	 annotationTypeDeclaration :  AT INTERFACE Identifier annotationTypeBody
	'''

	pass


def p_annotationTypeBody(p):
	'''
	 annotationTypeBody : BLPAREN expt_22 BRPAREN
		| BLPAREN  BRPAREN
	'''

	pass


def p_annotationTypeElementDeclaration(p):
	'''
	 annotationTypeElementDeclaration :  modifiers annotationTypeElementRest
	'''

	pass


def p_annotationTypeElementRest(p):
	'''
	 annotationTypeElementRest : type annotationMethodOrConstantRest SEMI
		| normalClassDeclaration SEMI
		| normalClassDeclaration 
		| normalInterfaceDeclaration SEMI
		| normalInterfaceDeclaration 
		| enumDeclaration SEMI
		| enumDeclaration 
		| annotationTypeDeclaration SEMI
		| annotationTypeDeclaration 
	'''

	pass


def p_annotationMethodOrConstantRest(p):
	'''
	 annotationMethodOrConstantRest :  annotationMethodRest 
	| annotationConstantRest
	'''

	pass


def p_annotationMethodRest(p):
	'''
	 annotationMethodRest : Identifier LPAREN RPAREN defaultValue
		| Identifier LPAREN RPAREN 
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
	 block : BLPAREN expt_18 BRPAREN
		| BLPAREN  BRPAREN
	'''

	pass


def p_blockStatement(p):
	'''
	 blockStatement :  localVariableDeclarationStatement 
	| classOrInterfaceDeclaration 
	| statement
	'''

	pass


def p_localVariableDeclarationStatement(p):
	'''
	 localVariableDeclarationStatement :  localVariableDeclaration SEMI
	'''

	pass


def p_localVariableDeclaration(p):
	'''
	 localVariableDeclaration : variableModifiers type variableDeclarators
		|  type variableDeclarators
	'''

	pass


def p_variableModifiers(p):
	'''
	 variableModifiers : expt_23
	'''

	pass


def p_statement(p):
	'''
	 statement : block
		| ASSERT expression COLON expression SEMI
		| ASSERT expression  SEMI
		| IF parExpression statement ELSE statement
		| IF parExpression statement 
		| FOR LPAREN forControl RPAREN statement
		| WHILE parExpression statement
		| DO statement WHILE parExpression SEMI
		| TRY block expr_12
		| SWITCH parExpression BLPAREN switchBlockStatementGroups BRPAREN
		| SYNCHRONIZED parExpression block
		| RETURN expression SEMI
		| RETURN  SEMI
		| THROW expression SEMI
		| BREAK Identifier SEMI
		| BREAK  SEMI
		| CONTINUE Identifier SEMI
		| CONTINUE  SEMI
		| SEMI
		| statementExpression SEMI
		| Identifier COLON statement
	'''

	pass


def p_catches(p):
	'''
	 catches : catchClause expt_24
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
	 formalParameter : variableModifiers type variableDeclaratorId
		|  type variableDeclaratorId
	'''

	pass


def p_switchBlockStatementGroups(p):
	'''
	 switchBlockStatementGroups : expt_25
	'''

	pass


def p_switchBlockStatementGroup(p):
	'''
	 switchBlockStatementGroup : expr_13 expt_18
		| expr_13 
	'''

	pass


def p_switchLabel(p):
	'''
	 switchLabel :  CASE constantExpression COLON 
	| CASE enumConstantName COLON 
	| DEFAULT COLON
	'''

	pass


def p_forControl(p):
	'''
	 forControl : enhancedForControl
		| forInit SEMI expression SEMI forUpdate
		| forInit SEMI expression SEMI 
		| forInit SEMI  SEMI forUpdate
		| forInit SEMI  SEMI 
		|  SEMI expression SEMI forUpdate
		|  SEMI expression SEMI 
		|  SEMI  SEMI forUpdate
		|  SEMI  SEMI 
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
	 enhancedForControl : variableModifiers type Identifier COLON expression
		|  type Identifier COLON expression
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


def p_expressionList(p):
	'''
	 expressionList : expression expt_26
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


def p_expression(p):
	'''
	 expression : conditionalExpression assignmentOperator expression
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
	 conditionalExpression : conditionalOrExpression QUES expression COLON expression
		| conditionalOrExpression 
	'''

	pass


def p_conditionalOrExpression(p):
	'''
	 conditionalOrExpression : conditionalAndExpression expt_27
		| conditionalAndExpression 
	'''

	pass


def p_conditionalAndExpression(p):
	'''
	 conditionalAndExpression : inclusiveOrExpression expt_28
		| inclusiveOrExpression 
	'''

	pass


def p_inclusiveOrExpression(p):
	'''
	 inclusiveOrExpression : exclusiveOrExpression expt_29
		| exclusiveOrExpression 
	'''

	pass


def p_exclusiveOrExpression(p):
	'''
	 exclusiveOrExpression : andExpression expt_30
		| andExpression 
	'''

	pass


def p_andExpression(p):
	'''
	 andExpression : equalityExpression expt_31
		| equalityExpression 
	'''

	pass


def p_equalityExpression(p):
	'''
	 equalityExpression : instanceOfExpression expt_32
		| instanceOfExpression 
	'''

	pass


def p_instanceOfExpression(p):
	'''
	 instanceOfExpression : relationalExpression INSTANCEOF type
		| relationalExpression 
	'''

	pass


def p_relationalExpression(p):
	'''
	 relationalExpression : shiftExpression expt_33
		| shiftExpression 
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


def p_shiftExpression(p):
	'''
	 shiftExpression : additiveExpression expt_34
		| additiveExpression 
	'''

	pass


def p_shiftOp(p):
	'''
	 shiftOp :  OP_SHR 
	| OP_SHRR 
	| OP_SHL
	'''

	pass


def p_additiveExpression(p):
	'''
	 additiveExpression : multiplicativeExpression expt_35
		| multiplicativeExpression 
	'''

	pass


def p_multiplicativeExpression(p):
	'''
	 multiplicativeExpression : unaryExpression expt_36
		| unaryExpression 
	'''

	pass


def p_unaryExpression(p):
	'''
	 unaryExpression :  PLUS unaryExpression 
	| DASH unaryExpression 
	| OP_INC unaryExpression 
	| OP_DEC unaryExpression 
	| unaryExpressionNotPlusMinus
	'''

	pass


def p_unaryExpressionNotPlusMinus(p):
	'''
	 unaryExpressionNotPlusMinus : TILDE unaryExpression
		| EXCLAMATION unaryExpression
		| castExpression
		| primary expt_37 expr_17
		| primary expt_37 
		| primary  expr_17
		| primary  
	'''

	pass


def p_castExpression(p):
	'''
	 castExpression :  LPAREN primitiveType RPAREN unaryExpression 
	| LPAREN expr_18 RPAREN unaryExpressionNotPlusMinus
	'''

	pass


def p_primary(p):
	'''
	 primary : parExpression
		| THIS expt_19 identifierSuffix
		| THIS expt_19 
		| THIS  identifierSuffix
		| THIS  
		| SUPER superSuffix
		| literal
		| NEW creator
		| Identifier expt_19 identifierSuffix
		| Identifier expt_19 
		| Identifier  identifierSuffix
		| Identifier  
		| primitiveType expt_11 DOT CLASS
		| primitiveType  DOT CLASS
		| VOID DOT CLASS
	'''

	pass


def p_identifierSuffix(p):
	'''
	 identifierSuffix :  expr_19 DOT CLASS 
	| expr_20 
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
	| createdName expr_21
	'''

	pass


def p_createdName(p):
	'''
	 createdName :  classOrInterfaceType 
	| primitiveType
	'''

	pass


def p_innerCreator(p):
	'''
	 innerCreator : nonWildcardTypeArguments Identifier classCreatorRest
		|  Identifier classCreatorRest
	'''

	pass


def p_arrayCreatorRest(p):
	'''
	 arrayCreatorRest :  FLPAREN expr_22
	'''

	pass


def p_classCreatorRest(p):
	'''
	 classCreatorRest : arguments classBody
		| arguments 
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
		| LPAREN  RPAREN
	'''

	pass


def p_expt_38(p):
	'''
	 expt_38 : FLPAREN expression FRPAREN
		| expt_38 FLPAREN expression FRPAREN
	'''

	pass


def p_expt_34(p):
	'''
	 expt_34 : shiftOp additiveExpression
		| expt_34 shiftOp additiveExpression
	'''

	pass


def p_expt_35(p):
	'''
	 expt_35 : expr_15 multiplicativeExpression
		| expt_35 expr_15 multiplicativeExpression
	'''

	pass


def p_expt_36(p):
	'''
	 expt_36 : expr_16 unaryExpression
		| expt_36 expr_16 unaryExpression
	'''

	pass


def p_expt_37(p):
	'''
	 expt_37 : selector
		| expt_37 selector
	'''

	pass


def p_expt_30(p):
	'''
	 expt_30 : CARET andExpression
		| expt_30 CARET andExpression
	'''

	pass


def p_expt_31(p):
	'''
	 expt_31 : AND equalityExpression
		| expt_31 AND equalityExpression
	'''

	pass


def p_expt_32(p):
	'''
	 expt_32 : expr_14 instanceOfExpression
		| expt_32 expr_14 instanceOfExpression
	'''

	pass


def p_expt_33(p):
	'''
	 expt_33 : relationalOp shiftExpression
		| expt_33 relationalOp shiftExpression
	'''

	pass


def p_expt_8(p):
	'''
	 expt_8 : classBodyDeclaration
		| expt_8 classBodyDeclaration
	'''

	pass


def p_expt_9(p):
	'''
	 expt_9 : COMMA type
		| expt_9 COMMA type
	'''

	pass


def p_expt_4(p):
	'''
	 expt_4 : modifier
		| expt_4 modifier
	'''

	pass


def p_expt_5(p):
	'''
	 expt_5 : COMMA typeParameter
		| expt_5 COMMA typeParameter
	'''

	pass


def p_expt_6(p):
	'''
	 expt_6 : AND type
		| expt_6 AND type
	'''

	pass


def p_expt_7(p):
	'''
	 expt_7 : COMMA enumConstant
		| expt_7 COMMA enumConstant
	'''

	pass


def p_expt_1(p):
	'''
	 expt_1 : importDeclaration
		| expt_1 importDeclaration
	'''

	pass


def p_expt_2(p):
	'''
	 expt_2 : typeDeclaration
		| expt_2 typeDeclaration
	'''

	pass


def p_expt_3(p):
	'''
	 expt_3 : classOrInterfaceModifier
		| expt_3 classOrInterfaceModifier
	'''

	pass


def p_expt_29(p):
	'''
	 expt_29 : VERTICAL exclusiveOrExpression
		| expt_29 VERTICAL exclusiveOrExpression
	'''

	pass


def p_expt_28(p):
	'''
	 expt_28 : OP_LAND inclusiveOrExpression
		| expt_28 OP_LAND inclusiveOrExpression
	'''

	pass


def p_expt_27(p):
	'''
	 expt_27 : OP_LOR conditionalAndExpression
		| expt_27 OP_LOR conditionalAndExpression
	'''

	pass


def p_expt_26(p):
	'''
	 expt_26 : COMMA expression
		| expt_26 COMMA expression
	'''

	pass


def p_expt_25(p):
	'''
	 expt_25 : switchBlockStatementGroup
		| expt_25 switchBlockStatementGroup
	'''

	pass


def p_expt_24(p):
	'''
	 expt_24 : catchClause
		| expt_24 catchClause
	'''

	pass


def p_expt_23(p):
	'''
	 expt_23 : variableModifier
		| expt_23 variableModifier
	'''

	pass


def p_expt_22(p):
	'''
	 expt_22 : annotationTypeElementDeclaration
		| expt_22 annotationTypeElementDeclaration
	'''

	pass


def p_expt_21(p):
	'''
	 expt_21 : COMMA elementValue
		| expt_21 COMMA elementValue
	'''

	pass


def p_expt_20(p):
	'''
	 expt_20 : COMMA elementValuePair
		| expt_20 COMMA elementValuePair
	'''

	pass


def p_expt_16(p):
	'''
	 expt_16 : COMMA typeArgument
		| expt_16 COMMA typeArgument
	'''

	pass


def p_expt_17(p):
	'''
	 expt_17 : COMMA qualifiedName
		| expt_17 COMMA qualifiedName
	'''

	pass


def p_expt_14(p):
	'''
	 expt_14 : COMMA variableInitializer
		| expt_14 COMMA variableInitializer
	'''

	pass


def p_expt_15(p):
	'''
	 expt_15 : DOT Identifier typeArguments
		| expt_15 DOT Identifier typeArguments
	'''

	pass


def p_expt_12(p):
	'''
	 expt_12 : COMMA variableDeclarator
		| expt_12 COMMA variableDeclarator
	'''

	pass


def p_expt_13(p):
	'''
	 expt_13 : COMMA constantDeclarator
		| expt_13 COMMA constantDeclarator
	'''

	pass


def p_expt_10(p):
	'''
	 expt_10 : interfaceBodyDeclaration
		| expt_10 interfaceBodyDeclaration
	'''

	pass


def p_expt_11(p):
	'''
	 expt_11 : FLPAREN FRPAREN
		| expt_11 FLPAREN FRPAREN
	'''

	pass


def p_expt_18(p):
	'''
	 expt_18 : blockStatement
		| expt_18 blockStatement
	'''

	pass


def p_expt_19(p):
	'''
	 expt_19 : DOT Identifier
		| expt_19 DOT Identifier
	'''

	pass


def p_expr_21(p):
	'''
	 expr_21 :  arrayCreatorRest 
	| classCreatorRest
	'''

	pass


def p_expr_20(p):
	'''
	 expr_20 :  FLPAREN expression FRPAREN 
	| expr_20 FLPAREN expression FRPAREN
	'''

	pass


def p_expr_22(p):
	'''
	 expr_22 :  FRPAREN expt_11 arrayInitializer 
	| expression FRPAREN expt_38 expt_11
	'''

	pass


def p_expr_8(p):
	'''
	 expr_8 :  EXTENDS 
	| SUPER
	'''

	pass


def p_expr_9(p):
	'''
	 expr_9 :  THIS 
	| SUPER
	'''

	pass


def p_expr_6(p):
	'''
	 expr_6 :  methodBody 
	| SEMI
	'''

	pass


def p_expr_7(p):
	'''
	 expr_7 :  type 
	| VOID
	'''

	pass


def p_expr_4(p):
	'''
	 expr_4 :  type 
	| VOID
	'''

	pass


def p_expr_5(p):
	'''
	 expr_5 :  methodBody 
	| SEMI
	'''

	pass


def p_expr_2(p):
	'''
	 expr_2 :  classDeclaration 
	| interfaceDeclaration
	'''

	pass


def p_expr_3(p):
	'''
	 expr_3 :  methodDeclaration 
	| fieldDeclaration
	'''

	pass


def p_expr_1(p):
	'''
	 expr_1 :  packageDeclaration expt_1 expt_2 
	| classOrInterfaceDeclaration expt_2
	'''

	pass


def p_expr_18(p):
	'''
	 expr_18 :  type 
	| expression
	'''

	pass


def p_expr_19(p):
	'''
	 expr_19 :  FLPAREN FRPAREN 
	| expr_19 FLPAREN FRPAREN
	'''

	pass


def p_expr_14(p):
	'''
	 expr_14 :  OP_EQ 
	| OP_NE
	'''

	pass


def p_expr_15(p):
	'''
	 expr_15 :  PLUS 
	| DASH
	'''

	pass


def p_expr_16(p):
	'''
	 expr_16 :  MULT 
	| SLASH 
	| PERCENT
	'''

	pass


def p_expr_17(p):
	'''
	 expr_17 :  OP_INC 
	| OP_DEC
	'''

	pass


def p_expr_10(p):
	'''
	 expr_10 :  annotation 
	| expr_10 annotation
	'''

	pass


def p_expr_11(p):
	'''
	 expr_11 :  elementValuePairs 
	| elementValue
	'''

	pass


def p_expr_12(p):
	'''
	 expr_12 :  catches FINALLY block 
	| catches 
	| FINALLY block
	'''

	pass


def p_expr_13(p):
	'''
	 expr_13 :  switchLabel 
	| expr_13 switchLabel
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
		integerLiteral : LONG_NUMBER
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
	
