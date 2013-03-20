# *.* coding=utf-8 *.*

import ply.yacc as yacc
import lex
from collections import deque

tokens = lex.tokens
def p_compilationUnit(p):
	'''
	 compilationUnit :  expr_1 expr_2 expr_3
	'''

	pass

def p_packageDeclaration(p):
	'''
	 packageDeclaration :  PACKAGE qualifiedName SEMI
	'''

	pass

def p_importDeclaration(p):
	'''
	 importDeclaration :  IMPORT expr_4 IDENTIFIER DOT MULT SEMI 
	| IMPORT expr_5 IDENTIFIER expr_6 expr_7 SEMI
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
	 classOrInterfaceDeclaration :  classDeclaration 
	| interfaceDeclaration
	'''

	pass

def p_modifiers(p):
	'''
	 modifiers :  expr_8
	'''

	pass

def p_variableModifiers(p):
	'''
	 variableModifiers :  expr_9
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
	 normalClassDeclaration :  modifiers CLASS IDENTIFIER expr_10 expr_11 expr_12 classBody
	'''

	pass

def p_typeParameters(p):
	'''
	 typeParameters :  LESS typeParameter expr_13 MORE
	'''

	pass

def p_typeParameter(p):
	'''
	 typeParameter :  IDENTIFIER expr_14
	'''

	pass

def p_typeBound(p):
	'''
	 typeBound :  type expr_15
	'''

	pass

def p_enumDeclaration(p):
	'''
	 enumDeclaration :  modifiers expr_16 IDENTIFIER expr_17 enumBody
	'''

	pass

def p_enumBody(p):
	'''
	 enumBody :  BLPAREN expr_18 expr_19 expr_20 BRPAREN
	'''

	pass

def p_enumConstants(p):
	'''
	 enumConstants :  enumConstant expr_21
	'''

	pass

def p_enumConstant(p):
	'''
	 enumConstant :  expr_22 IDENTIFIER expr_23 expr_24
	'''

	pass

def p_enumBodyDeclarations(p):
	'''
	 enumBodyDeclarations :  SEMI expr_25
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
	 normalInterfaceDeclaration :  modifiers INTERFACE IDENTIFIER expr_26 expr_27 interfaceBody
	'''

	pass

def p_typeList(p):
	'''
	 typeList :  type expr_28
	'''

	pass

def p_classBody(p):
	'''
	 classBody :  BLPAREN expr_29 BRPAREN
	'''

	pass

def p_interfaceBody(p):
	'''
	 interfaceBody :  BLPAREN expr_30 BRPAREN
	'''

	pass

def p_classBodyDeclaration(p):
	'''
	 classBodyDeclaration :  SEMI 
	| expr_31 block 
	| memberDecl
	'''

	pass

def p_memberDecl(p):
	'''
	 memberDecl :  fieldDeclaration 
	| methodDeclaration 
	| classDeclaration 
	| interfaceDeclaration
	'''

	pass

def p_methodDeclaration(p):
	'''
	 methodDeclaration :  modifiers expr_32 IDENTIFIER formalParameters expr_33 BLPAREN expr_34 expr_35 BRPAREN 
	| modifiers expr_36 expr_37 IDENTIFIER formalParameters expr_38 expr_39 expr_40
	'''

	pass

def p_fieldDeclaration(p):
	'''
	 fieldDeclaration :  modifiers type variableDeclarator expr_41 SEMI
	'''

	pass

def p_variableDeclarator(p):
	'''
	 variableDeclarator :  IDENTIFIER expr_42 expr_43
	'''

	pass

def p_interfaceBodyDeclaration(p):
	'''
	 interfaceBodyDeclaration :  interfaceFieldDeclaration 
	| interfaceMethodDeclaration 
	| interfaceDeclaration 
	| classDeclaration 
	| SEMI
	'''

	pass

def p_interfaceMethodDeclaration(p):
	'''
	 interfaceMethodDeclaration :  modifiers expr_44 expr_45 IDENTIFIER formalParameters expr_46 expr_47 SEMI
	'''

	pass

def p_interfaceFieldDeclaration(p):
	'''
	 interfaceFieldDeclaration :  modifiers type variableDeclarator expr_48 SEMI
	'''

	pass

def p_type(p):
	'''
	 type :  classOrInterfaceType expr_49 
	| primitiveType expr_50
	'''

	pass

def p_classOrInterfaceType(p):
	'''
	 classOrInterfaceType :  IDENTIFIER expr_51 expr_53
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

def p_typeArguments(p):
	'''
	 typeArguments :  LESS typeArgument expr_54 MORE
	'''

	pass

def p_typeArgument(p):
	'''
	 typeArgument :  type 
	| QUES expr_56
	'''

	pass

def p_qualifiedNameList(p):
	'''
	 qualifiedNameList :  qualifiedName expr_57
	'''

	pass

def p_formalParameters(p):
	'''
	 formalParameters :  LPAREN expr_58 RPAREN
	'''

	pass

def p_formalParameterDecls(p):
	'''
	 formalParameterDecls :  ellipsisParameterDecl 
	| normalParameterDecl expr_59 
	| expr_60 ellipsisParameterDecl
	'''

	pass

def p_normalParameterDecl(p):
	'''
	 normalParameterDecl :  variableModifiers type IDENTIFIER expr_61
	'''

	pass

def p_ellipsisParameterDecl(p):
	'''
	 ellipsisParameterDecl :  variableModifiers type OP_ARRAY IDENTIFIER
	'''

	pass

def p_explicitConstructorInvocation(p):
	'''
	 explicitConstructorInvocation :  expr_62 expr_63 arguments SEMI 
	| primary DOT expr_64 SUPER arguments SEMI
	'''

	pass

def p_qualifiedName(p):
	'''
	 qualifiedName :  IDENTIFIER expr_65
	'''

	pass

def p_annotations(p):
	'''
	 annotations :  expr_66
	'''

	pass

def p_annotation(p):
	'''
	 annotation :  AT qualifiedName expr_68
	'''

	pass

def p_elementValuePairs(p):
	'''
	 elementValuePairs :  elementValuePair expr_69
	'''

	pass

def p_elementValuePair(p):
	'''
	 elementValuePair :  IDENTIFIER EQUALS elementValue
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
	 elementValueArrayInitializer :  BLPAREN expr_71 expr_72 BRPAREN
	'''

	pass

def p_annotationTypeDeclaration(p):
	'''
	 annotationTypeDeclaration :  modifiers AT INTERFACE IDENTIFIER annotationTypeBody
	'''

	pass

def p_annotationTypeBody(p):
	'''
	 annotationTypeBody :  BLPAREN expr_73 BRPAREN
	'''

	pass

def p_annotationTypeElementDeclaration(p):
	'''
	 annotationTypeElementDeclaration :  annotationMethodDeclaration 
	| interfaceFieldDeclaration 
	| normalClassDeclaration 
	| normalInterfaceDeclaration 
	| enumDeclaration 
	| annotationTypeDeclaration 
	| SEMI
	'''

	pass

def p_annotationMethodDeclaration(p):
	'''
	 annotationMethodDeclaration :  modifiers type IDENTIFIER LPAREN RPAREN expr_74 SEMI
	'''

	pass

def p_block(p):
	'''
	 block :  BLPAREN expr_75 BRPAREN
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
	 localVariableDeclaration :  variableModifiers type variableDeclarator expr_76
	'''

	pass

def p_statement(p):
	'''
	 statement :  block 
	| expr_77 expression expr_78 SEMI 
	| ASSERT expression expr_79 SEMI 
	| IF parExpression statement expr_80 
	| forstatement 
	| WHILE parExpression statement 
	| DO statement WHILE parExpression SEMI 
	| trystatement 
	| SWITCH parExpression BLPAREN switchBlockStatementGroups BRPAREN 
	| SYNCHRONIZED parExpression block 
	| RETURN expr_81 SEMI 
	| THROW expression SEMI 
	| BREAK expr_82 SEMI 
	| CONTINUE expr_83 SEMI 
	| expression SEMI 
	| IDENTIFIER COLON statement 
	| SEMI
	'''

	pass

def p_switchBlockStatementGroups(p):
	'''
	 switchBlockStatementGroups :  expr_84
	'''

	pass

def p_switchBlockStatementGroup(p):
	'''
	 switchBlockStatementGroup :  switchLabel expr_85
	'''

	pass

def p_switchLabel(p):
	'''
	 switchLabel :  CASE expression COLON 
	| DEFAULT COLON
	'''

	pass

def p_trystatement(p):
	'''
	 trystatement :  TRY block expr_86
	'''

	pass

def p_catches(p):
	'''
	 catches :  catchClause expr_87
	'''

	pass

def p_catchClause(p):
	'''
	 catchClause :  CATCH LPAREN formalParameter RPAREN block
	'''

	pass

def p_formalParameter(p):
	'''
	 formalParameter :  variableModifiers type IDENTIFIER expr_88
	'''

	pass

def p_forstatement(p):
	'''
	 forstatement :  FOR LPAREN variableModifiers type IDENTIFIER COLON expression RPAREN statement 
	| FOR LPAREN expr_89 SEMI expr_90 SEMI expr_91 RPAREN statement
	'''

	pass

def p_forInit(p):
	'''
	 forInit :  localVariableDeclaration 
	| expressionList
	'''

	pass

def p_parExpression(p):
	'''
	 parExpression :  LPAREN expression RPAREN
	'''

	pass

def p_expressionList(p):
	'''
	 expressionList :  expression expr_92
	'''

	pass

def p_expression(p):
	'''
	 expression :  conditionalExpression expr_93
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
	| LESS LESS EQUALS 
	| MORE MORE MORE EQUALS 
	| MORE MORE EQUALS
	'''

	pass

def p_conditionalExpression(p):
	'''
	 conditionalExpression :  conditionalOrExpression expr_94
	'''

	pass

def p_conditionalOrExpression(p):
	'''
	 conditionalOrExpression :  conditionalAndExpression expr_95
	'''

	pass

def p_conditionalAndExpression(p):
	'''
	 conditionalAndExpression :  inclusiveOrExpression expr_96
	'''

	pass

def p_inclusiveOrExpression(p):
	'''
	 inclusiveOrExpression :  exclusiveOrExpression expr_97
	'''

	pass

def p_exclusiveOrExpression(p):
	'''
	 exclusiveOrExpression :  andExpression expr_98
	'''

	pass

def p_andExpression(p):
	'''
	 andExpression :  equalityExpression expr_99
	'''

	pass

def p_equalityExpression(p):
	'''
	 equalityExpression :  instanceOfExpression expr_101
	'''

	pass

def p_instanceOfExpression(p):
	'''
	 instanceOfExpression :  relationalExpression expr_102
	'''

	pass

def p_relationalExpression(p):
	'''
	 relationalExpression :  shiftExpression expr_103
	'''

	pass

def p_relationalOp(p):
	'''
	 relationalOp :  LESS EQUALS 
	| MORE EQUALS 
	| LESS 
	| MORE
	'''

	pass

def p_shiftExpression(p):
	'''
	 shiftExpression :  additiveExpression expr_104
	'''

	pass

def p_shiftOp(p):
	'''
	 shiftOp :  LESS LESS 
	| MORE MORE MORE 
	| MORE MORE
	'''

	pass

def p_additiveExpression(p):
	'''
	 additiveExpression :  multiplicativeExpression expr_106
	'''

	pass

def p_multiplicativeExpression(p):
	'''
	 multiplicativeExpression :  unaryExpression expr_108
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
	 unaryExpressionNotPlusMinus :  TILDE unaryExpression 
	| EXCLAMATION unaryExpression 
	| castExpression 
	| primary expr_109 expr_110
	'''

	pass

def p_castExpression(p):
	'''
	 castExpression :  LPAREN primitiveType RPAREN unaryExpression 
	| LPAREN type RPAREN unaryExpressionNotPlusMinus
	'''

	pass

def p_primary(p):
	'''
	 primary :  parExpression 
	| THIS expr_111 expr_112 
	| IDENTIFIER expr_113 expr_114 
	| SUPER superSuffix 
	| literal 
	| creator 
	| primitiveType expr_115 DOT CLASS 
	| VOID DOT CLASS
	'''

	pass

def p_superSuffix(p):
	'''
	 superSuffix :  arguments 
	| DOT expr_116 IDENTIFIER expr_117
	'''

	pass

def p_identifierSuffix(p):
	'''
	 identifierSuffix :  expr_118 DOT CLASS 
	| expr_119 
	| arguments 
	| DOT CLASS 
	| DOT nonWildcardTypeArguments IDENTIFIER arguments 
	| DOT THIS 
	| DOT SUPER arguments 
	| innerCreator
	'''

	pass

def p_selector(p):
	'''
	 selector :  DOT IDENTIFIER expr_120 
	| DOT THIS 
	| DOT SUPER superSuffix 
	| innerCreator 
	| FLPAREN expression FRPAREN
	'''

	pass

def p_creator(p):
	'''
	 creator :  NEW nonWildcardTypeArguments classOrInterfaceType classCreatorRest 
	| NEW classOrInterfaceType classCreatorRest 
	| arrayCreator
	'''

	pass

def p_arrayCreator(p):
	'''
	 arrayCreator :  NEW createdName FLPAREN FRPAREN expr_121 arrayInitializer 
	| NEW createdName FLPAREN expression FRPAREN expr_122 expr_123
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
	 arrayInitializer :  BLPAREN expr_125 expr_126 BRPAREN
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
	 innerCreator :  DOT NEW expr_127 IDENTIFIER expr_128 classCreatorRest
	'''

	pass

def p_classCreatorRest(p):
	'''
	 classCreatorRest :  arguments expr_129
	'''

	pass

def p_nonWildcardTypeArguments(p):
	'''
	 nonWildcardTypeArguments :  LESS typeList MORE
	'''

	pass

def p_arguments(p):
	'''
	 arguments :  LPAREN expr_130 RPAREN
	'''

	pass

def p_literal(p):
	'''
	 literal :  INTLITERAL 
	| LONGLITERAL 
	| FLOATLITERAL 
	| DOUBLELITERAL 
	| CHARLITERAL 
	| STRINGLITERAL 
	| TRUE 
	| FALSE 
	| NULL
	'''

	pass

def p_expr_0(p):
	'''
	 expr_0 :  annotations 
	| empty
	'''
	pass

def p_expr_1(p):
	'''
	 expr_1 :  expr_0 packageDeclaration 
	| empty
	'''
	pass

def p_expr_2(p):
	'''
	 expr_2 :  importDeclaration 
	| expr_2 importDeclaration 
	| empty
	'''
	pass

def p_expr_3(p):
	'''
	 expr_3 :  typeDeclaration 
	| expr_3 typeDeclaration 
	| empty
		'''
	pass

def p_expr_4(p):
	'''
	 expr_4 :  STATIC 
	| empty
		'''
	pass

def p_expr_5(p):
	'''
	 expr_5 :  STATIC 
	| empty
		'''
	pass

def p_expr_6(p):
	'''
	 expr_6 :  DOT IDENTIFIER 
	| expr_6 DOT IDENTIFIER
		'''
	pass

def p_expr_7(p):
	'''
	 expr_7 :  DOT MULT 
	| empty
		'''
	pass

def p_expr_8(p):
	'''
	 expr_8 :  annotation 
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

def p_expr_9(p):
	'''
	 expr_9 :  FINAL 
	| annotation
		'''
	pass

def p_expr_10(p):
	'''
	 expr_10 :  typeParameters 
	| empty
		'''
	pass

def p_expr_11(p):
	'''
	 expr_11 :  EXTENDS type 
	| empty
		'''
	pass

def p_expr_12(p):
	'''
	 expr_12 :  IMPLEMENTS typeList 
	| empty
		'''
	pass

def p_expr_13(p):
	'''
	 expr_13 :  COMMA typeParameter 
	| expr_13 COMMA typeParameter 
	| empty
		'''
	pass

def p_expr_14(p):
	'''
	 expr_14 :  EXTENDS typeBound 
	| empty
		'''
	pass

def p_expr_15(p):
	'''
	 expr_15 :  AND type 
	| expr_15 AND type 
	| empty
		'''
	pass

def p_expr_16(p):
	'''
	 expr_16 :  ENUM
		'''
	pass

def p_expr_17(p):
	'''
	 expr_17 :  IMPLEMENTS typeList 
	| empty
		'''
	pass

def p_expr_18(p):
	'''
	 expr_18 :  enumConstants 
	| empty
		'''
	pass

def p_expr_19(p):
	'''
	 expr_19 :  COMMA 
	| empty
		'''
	pass

def p_expr_20(p):
	'''
	 expr_20 :  enumBodyDeclarations 
	| empty
		'''
	pass

def p_expr_21(p):
	'''
	 expr_21 :  COMMA enumConstant 
	| expr_21 COMMA enumConstant 
	| empty
		'''
	pass

def p_expr_22(p):
	'''
	 expr_22 :  annotations 
	| empty
		'''
	pass

def p_expr_23(p):
	'''
	 expr_23 :  arguments 
	| empty
		'''
	pass

def p_expr_24(p):
	'''
	 expr_24 :  classBody 
	| empty
		'''
	pass

def p_expr_25(p):
	'''
	 expr_25 :  classBodyDeclaration 
	| expr_25 classBodyDeclaration 
	| empty
		'''
	pass

def p_expr_26(p):
	'''
	 expr_26 :  typeParameters 
	| empty
		'''
	pass

def p_expr_27(p):
	'''
	 expr_27 :  EXTENDS typeList 
	| empty
		'''
	pass

def p_expr_28(p):
	'''
	 expr_28 :  COMMA type 
	| expr_28 COMMA type 
	| empty
		'''
	pass

def p_expr_29(p):
	'''
	 expr_29 :  classBodyDeclaration 
	| expr_29 classBodyDeclaration 
	| empty
		'''
	pass

def p_expr_30(p):
	'''
	 expr_30 :  interfaceBodyDeclaration 
	| expr_30 interfaceBodyDeclaration 
	| empty
		'''
	pass

def p_expr_31(p):
	'''
	 expr_31 :  STATIC 
	| empty
		'''
	pass

def p_expr_32(p):
	'''
	 expr_32 :  typeParameters 
	| empty
		'''
	pass

def p_expr_33(p):
	'''
	 expr_33 :  THROWS qualifiedNameList 
	| empty
		'''
	pass

def p_expr_34(p):
	'''
	 expr_34 :  explicitConstructorInvocation 
	| empty
		'''
	pass

def p_expr_35(p):
	'''
	 expr_35 :  blockStatement 
	| expr_35 blockStatement 
	| empty
		'''
	pass

def p_expr_36(p):
	'''
	 expr_36 :  typeParameters 
	| empty
		'''
	pass

def p_expr_37(p):
	'''
	 expr_37 :  type 
	| VOID
		'''
	pass

def p_expr_38(p):
	'''
	 expr_38 :  FLPAREN FRPAREN 
	| expr_38 FLPAREN FRPAREN 
	| empty
		'''
	pass

def p_expr_39(p):
	'''
	 expr_39 :  THROWS qualifiedNameList 
	| empty
		'''
	pass

def p_expr_40(p):
	'''
	 expr_40 :  block 
	| SEMI
		'''
	pass

def p_expr_41(p):
	'''
	 expr_41 :  COMMA variableDeclarator 
	| expr_41 COMMA variableDeclarator 
	| empty
		'''
	pass

def p_expr_42(p):
	'''
	 expr_42 :  FLPAREN FRPAREN 
	| expr_42 FLPAREN FRPAREN 
	| empty
		'''
	pass

def p_expr_43(p):
	'''
	 expr_43 :  EQUALS variableInitializer 
	| empty
		'''
	pass

def p_expr_44(p):
	'''
	 expr_44 :  typeParameters 
	| empty
		'''
	pass

def p_expr_45(p):
	'''
	 expr_45 :  type 
	| VOID
		'''
	pass

def p_expr_46(p):
	'''
	 expr_46 :  FLPAREN FRPAREN 
	| expr_46 FLPAREN FRPAREN 
	| empty
		'''
	pass

def p_expr_47(p):
	'''
	 expr_47 :  THROWS qualifiedNameList 
	| empty
		'''
	pass

def p_expr_48(p):
	'''
	 expr_48 :  COMMA variableDeclarator 
	| expr_48 COMMA variableDeclarator 
	| empty
		'''
	pass

def p_expr_49(p):
	'''
	 expr_49 :  FLPAREN FRPAREN 
	| expr_49 FLPAREN FRPAREN 
	| empty
		'''
	pass

def p_expr_50(p):
	'''
	 expr_50 :  FLPAREN FRPAREN 
	| expr_50 FLPAREN FRPAREN 
	| empty
		'''
	pass

def p_expr_51(p):
	'''
	 expr_51 :  typeArguments 
	| empty
		'''
	pass

def p_expr_52(p):
	'''
	 expr_52 :  typeArguments 
	| empty
		'''
	pass

def p_expr_53(p):
	'''
	 expr_53 :  DOT IDENTIFIER expr_52 
	| expr_53 DOT IDENTIFIER expr_52 
	| empty
		'''
	pass

def p_expr_54(p):
	'''
	 expr_54 :  COMMA typeArgument 
	| expr_54 COMMA typeArgument 
	| empty
		'''
	pass

def p_expr_55(p):
	'''
	 expr_55 :  EXTENDS 
	| SUPER
		'''
	pass

def p_expr_56(p):
	'''
	 expr_56 :  expr_55 type 
	| empty
		'''
	pass

def p_expr_57(p):
	'''
	 expr_57 :  COMMA qualifiedName 
	| expr_57 COMMA qualifiedName 
	| empty
		'''
	pass

def p_expr_58(p):
	'''
	 expr_58 :  formalParameterDecls 
	| empty
		'''
	pass

def p_expr_59(p):
	'''
	 expr_59 :  COMMA normalParameterDecl 
	| expr_59 COMMA normalParameterDecl 
	| empty
		'''
	pass

def p_expr_60(p):
	'''
	 expr_60 :  normalParameterDecl COMMA 
	| expr_60 normalParameterDecl COMMA
		'''
	pass

def p_expr_61(p):
	'''
	 expr_61 :  FLPAREN FRPAREN 
	| expr_61 FLPAREN FRPAREN 
	| empty
		'''
	pass

def p_expr_62(p):
	'''
	 expr_62 :  nonWildcardTypeArguments 
	| empty
		'''
	pass

def p_expr_63(p):
	'''
	 expr_63 :  THIS 
	| SUPER
		'''
	pass

def p_expr_64(p):
	'''
	 expr_64 :  nonWildcardTypeArguments 
	| empty
		'''
	pass

def p_expr_65(p):
	'''
	 expr_65 :  DOT IDENTIFIER 
			| expr_65 DOT IDENTIFIER 
			| empty
	'''
	pass

def p_expr_66(p):
	'''
	 expr_66 :  annotation 
	| expr_66 annotation
		'''
	pass

def p_expr_67(p):
	'''
	 expr_67 :  elementValuePairs 
	| elementValue
		'''
	pass

def p_expr_68(p):
	'''
	 expr_68 :  LPAREN expr_67 RPAREN 
	| empty
		'''
	pass

def p_expr_69(p):
	'''
	 expr_69 :  COMMA elementValuePair 
	| expr_69 COMMA elementValuePair 
	| empty
		'''
	pass

def p_expr_70(p):
	'''
	 expr_70 :  COMMA elementValue 
	| expr_70 COMMA elementValue 
	| empty
		'''
	pass

def p_expr_71(p):
	'''
	 expr_71 :  elementValue expr_70 
	| empty
		'''
	pass

def p_expr_72(p):
	'''
	 expr_72 :  COMMA 
	| empty
		'''
	pass

def p_expr_73(p):
	'''
	 expr_73 :  annotationTypeElementDeclaration 
	| expr_73 annotationTypeElementDeclaration 
	| empty
		'''
	pass

def p_expr_74(p):
	'''
	 expr_74 :  DEFAULT elementValue 
	| empty
		'''
	pass

def p_expr_75(p):
	'''
	 expr_75 :  blockStatement 
	| expr_75 blockStatement 
	| empty
		'''
	pass

def p_expr_76(p):
	'''
	 expr_76 :  COMMA variableDeclarator 
	| expr_76 COMMA variableDeclarator 
	| empty
		'''
	pass

def p_expr_77(p):
	'''
	 expr_77 :  ASSERT
		'''
	pass

def p_expr_78(p):
	'''
	 expr_78 :  COLON expression 
	| empty
		'''
	pass

def p_expr_79(p):
	'''
	 expr_79 :  COLON expression 
	| empty
		'''
	pass

def p_expr_80(p):
	'''
	 expr_80 :  ELSE statement 
	| empty
		'''
	pass

def p_expr_81(p):
	'''
	 expr_81 :  expression 
	| empty
		'''
	pass

def p_expr_82(p):
	'''
	 expr_82 :  IDENTIFIER 
	| empty
		'''
	pass

def p_expr_83(p):
	'''
	 expr_83 :  IDENTIFIER 
	| empty
		'''
	pass

def p_expr_84(p):
	'''
	 expr_84 :  switchBlockStatementGroup 
	| expr_84 switchBlockStatementGroup 
	| empty
		'''
	pass

def p_expr_85(p):
	'''
	 expr_85 :  blockStatement 
	| expr_85 blockStatement 
	| empty
		'''
	pass

def p_expr_86(p):
	'''
	 expr_86 :  catches FINALLY block 
	| catches 
	| FINALLY block
		'''
	pass

def p_expr_87(p):
	'''
	 expr_87 :  catchClause 
	| expr_87 catchClause 
	| empty
		'''
	pass

def p_expr_88(p):
	'''
	 expr_88 :  FLPAREN FRPAREN 
	| expr_88 FLPAREN FRPAREN 
	| empty
		'''
	pass

def p_expr_89(p):
	'''
	 expr_89 :  forInit 
	| empty
		'''
	pass

def p_expr_90(p):
	'''
	 expr_90 :  expression 
	| empty
		'''
	pass

def p_expr_91(p):
	'''
	 expr_91 :  expressionList 
	| empty
		'''
	pass

def p_expr_92(p):
	'''
	 expr_92 :  COMMA expression 
	| expr_92 COMMA expression 
	| empty
		'''
	pass

def p_expr_93(p):
	'''
	 expr_93 :  assignmentOperator expression 
	| empty
		'''
	pass

def p_expr_94(p):
	'''
	 expr_94 :  QUES expression COLON conditionalExpression 
	| empty
		'''
	pass

def p_expr_95(p):
	'''
	 expr_95 :  OP_LOR conditionalAndExpression 
	| expr_95 OP_LOR conditionalAndExpression 
	| empty
		'''
	pass

def p_expr_96(p):
	'''
	 expr_96 :  OP_LAND inclusiveOrExpression 
	| expr_96 OP_LAND inclusiveOrExpression 
	| empty
		'''
	pass

def p_expr_97(p):
	'''
	 expr_97 :  VERTICAL exclusiveOrExpression 
	| expr_97 VERTICAL exclusiveOrExpression 
	| empty
		'''
	pass

def p_expr_98(p):
	'''
	 expr_98 :  CARET andExpression 
	| expr_98 CARET andExpression 
	| empty
		'''
	pass

def p_expr_99(p):
	'''
	 expr_99 :  AND equalityExpression 
	| expr_99 AND equalityExpression 
	| empty
		'''
	pass

def p_expr_100(p):
	'''
	 expr_100 :  OP_EQ 
	| OP_NE
		'''
	pass

def p_expr_101(p):
	'''
	 expr_101 :  expr_100 instanceOfExpression 
	| expr_101 expr_100 instanceOfExpression 
	| empty
		'''
	pass

def p_expr_102(p):
	'''
	 expr_102 :  INSTANCEOF type 
	| empty
		'''
	pass

def p_expr_103(p):
	'''
	 expr_103 :  relationalOp shiftExpression 
	| expr_103 relationalOp shiftExpression 
	| empty
		'''
	pass

def p_expr_104(p):
	'''
	 expr_104 :  shiftOp additiveExpression 
	| expr_104 shiftOp additiveExpression 
	| empty
		'''
	pass

def p_expr_105(p):
	'''
	 expr_105 :  PLUS 
	| DASH
		'''
	pass

def p_expr_106(p):
	'''
	 expr_106 :  expr_105 multiplicativeExpression 
	| expr_106 expr_105 multiplicativeExpression 
	| empty
		'''
	pass

def p_expr_107(p):
	'''
	 expr_107 :  MULT 
	| SLASH 
	| PERCENT
		'''
	pass

def p_expr_108(p):
	'''
	 expr_108 :  expr_107 unaryExpression 
	| expr_108 expr_107 unaryExpression 
	| empty
		'''
	pass

def p_expr_109(p):
	'''
	 expr_109 :  selector 
	| expr_109 selector 
	| empty
		'''
	pass

def p_expr_110(p):
	'''
	 expr_110 :  OP_INC 
	| OP_DEC
		'''
	pass

def p_expr_111(p):
	'''
	 expr_111 :  DOT IDENTIFIER 
	| expr_111 DOT IDENTIFIER 
	| empty
		'''
	pass

def p_expr_112(p):
	'''
	 expr_112 :  identifierSuffix 
	| empty
		'''
	pass

def p_expr_113(p):
	'''
	 expr_113 :  DOT IDENTIFIER 
	| expr_113 DOT IDENTIFIER 
	| empty
		'''
	pass

def p_expr_114(p):
	'''
	 expr_114 :  identifierSuffix 
	| empty
		'''
	pass

def p_expr_115(p):
	'''
	 expr_115 :  FLPAREN FRPAREN 
	| expr_115 FLPAREN FRPAREN 
	| empty
		'''
	pass

def p_expr_116(p):
	'''
	 expr_116 :  typeArguments 
	| empty
		'''
	pass

def p_expr_117(p):
	'''
	 expr_117 :  arguments 
	| empty
		'''
	pass

def p_expr_118(p):
	'''
	 expr_118 :  FLPAREN FRPAREN 
	| expr_118 FLPAREN FRPAREN
		'''
	pass

def p_expr_119(p):
	'''
	 expr_119 :  FLPAREN expression FRPAREN 
	| expr_119 FLPAREN expression FRPAREN
		'''
	pass

def p_expr_120(p):
	'''
	 expr_120 :  arguments 
	| empty
		'''
	pass

def p_expr_121(p):
	'''
	 expr_121 :  FLPAREN FRPAREN 
	| expr_121 FLPAREN FRPAREN 
	| empty
		'''
	pass

def p_expr_122(p):
	'''
	 expr_122 :  FLPAREN expression FRPAREN 
	| expr_122 FLPAREN expression FRPAREN 
	| empty
		'''
	pass

def p_expr_123(p):
	'''
	 expr_123 :  FLPAREN FRPAREN 
	| expr_123 FLPAREN FRPAREN 
	| empty
		'''
	pass

def p_expr_124(p):
	'''
	 expr_124 :  COMMA variableInitializer 
	| expr_124 COMMA variableInitializer 
	| empty
		'''
	pass

def p_expr_125(p):
	'''
	 expr_125 :  variableInitializer expr_124 
	| empty
		'''
	pass

def p_expr_126(p):
	'''
	 expr_126 :  COMMA 
	| empty
		'''
	pass

def p_expr_127(p):
	'''
	 expr_127 :  nonWildcardTypeArguments 
	| empty
		'''
	pass

def p_expr_128(p):
	'''
	 expr_128 :  typeArguments 
	| empty
		'''
	pass

def p_expr_129(p):
	'''
	 expr_129 :  classBody 
	| empty
		'''
	pass

def p_expr_130(p):
	'''
	 expr_130 :  expressionList 
	| empty
		'''
	pass



def p_INTLITERAL(p):
	'''
		INTLITERAL : NUMBER 
					| HEX_NUMBER
	'''
	pass
def p_LONGLITERAL(p):
	'''
		LONGLITERAL : LONG_NUMBER 
					| LONG_HEX_NUMBER
	'''
	pass
def p_FLOATLITERAL( p ):
	'''
		FLOATLITERAL : NON_INTEGER_1
					| NON_INTEGER_2
					| NON_INTEGER_3
	'''
	pass
def p_DOUBLELITERAL( p ):
	'''
		DOUBLELITERAL : NON_INTEGER_1
					| NON_INTEGER_2
					| NON_INTEGER_3
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
	
