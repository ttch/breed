# *.* coding=utf-8 *.*

import ply.yacc as yacc
import lex
from collections import deque

tokens = lex.tokens
def p_compilationUnit(p):
	'''
	 compilationUnit :  expr_3 expr_2 expr_1
	'''

	pass

def p_packageDeclaration(p):
	'''
	 packageDeclaration :  PACKAGE qualifiedName SEMI
	'''

	pass

def p_importDeclaration(p):
	'''
	 importDeclaration :  expr_4 IMPORT IDENTIFIER DOT MULT SEMI 
	| expr_5 IMPORT expr_7 expr_6 IDENTIFIER SEMI
	'''

	pass

def p_qualifiedImportName(p):
	'''
	 qualifiedImportName :  expr_8 IDENTIFIER
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
	 modifiers :  expr_9
	'''

	pass

def p_variableModifiers(p):
	'''
	 variableModifiers :  expr_10
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
	 normalClassDeclaration :  modifiers CLASS expr_13 expr_12 expr_11 IDENTIFIER classBody
	'''

	pass

def p_typeParameters(p):
	'''
	 typeParameters :  LESS expr_14 typeParameter MORE
	'''

	pass

def p_typeParameter(p):
	'''
	 typeParameter :  expr_15 IDENTIFIER
	'''

	pass

def p_typeBound(p):
	'''
	 typeBound :  expr_16 type
	'''

	pass

def p_enumDeclaration(p):
	'''
	 enumDeclaration :  expr_17 modifiers expr_18 IDENTIFIER enumBody
	'''

	pass

def p_enumBody(p):
	'''
	 enumBody :  expr_19 BLPAREN expr_21 expr_20 BRPAREN
	'''

	pass

def p_enumConstants(p):
	'''
	 enumConstants :  expr_22 enumConstant
	'''

	pass

def p_enumConstant(p):
	'''
	 enumConstant :  expr_23 expr_25 expr_24 IDENTIFIER
	'''

	pass

def p_enumBodyDeclarations(p):
	'''
	 enumBodyDeclarations :  expr_26 SEMI
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
	 normalInterfaceDeclaration :  modifiers INTERFACE expr_28 expr_27 IDENTIFIER interfaceBody
	'''

	pass

def p_typeList(p):
	'''
	 typeList :  expr_29 type
	'''

	pass

def p_classBody(p):
	'''
	 classBody :  expr_30 BLPAREN BRPAREN
	'''

	pass

def p_interfaceBody(p):
	'''
	 interfaceBody :  expr_31 BLPAREN BRPAREN
	'''

	pass

def p_classBodyDeclaration(p):
	'''
	 classBodyDeclaration :  SEMI 
	| expr_32 block 
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
	 methodDeclaration :  expr_33 modifiers IDENTIFIER expr_34 formalParameters expr_36 expr_35 BLPAREN BRPAREN 
	| expr_38 expr_37 modifiers IDENTIFIER expr_41 expr_40 expr_39 formalParameters
	'''

	pass

def p_fieldDeclaration(p):
	'''
	 fieldDeclaration :  modifiers type expr_42 variableDeclarator SEMI
	'''

	pass

def p_variableDeclarator(p):
	'''
	 variableDeclarator :  expr_44 expr_43 IDENTIFIER
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
	 interfaceMethodDeclaration :  expr_46 expr_45 modifiers IDENTIFIER expr_48 expr_47 formalParameters SEMI
	'''

	pass

def p_interfaceFieldDeclaration(p):
	'''
	 interfaceFieldDeclaration :  modifiers type expr_49 variableDeclarator SEMI
	'''

	pass

def p_type(p):
	'''
	 type :  expr_50 classOrInterfaceType 
	| expr_51 primitiveType
	'''

	pass

def p_classOrInterfaceType(p):
	'''
	 classOrInterfaceType :  expr_54 expr_52 IDENTIFIER
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
	 typeArguments :  LESS expr_55 typeArgument MORE
	'''

	pass

def p_typeArgument(p):
	'''
	 typeArgument :  type 
	| expr_57 QUES
	'''

	pass

def p_qualifiedNameList(p):
	'''
	 qualifiedNameList :  expr_58 qualifiedName
	'''

	pass

def p_formalParameters(p):
	'''
	 formalParameters :  expr_59 LPAREN RPAREN
	'''

	pass

def p_formalParameterDecls(p):
	'''
	 formalParameterDecls :  ellipsisParameterDecl 
	| expr_60 normalParameterDecl 
	| expr_61 ellipsisParameterDecl
	'''

	pass

def p_normalParameterDecl(p):
	'''
	 normalParameterDecl :  variableModifiers type expr_62 IDENTIFIER
	'''

	pass

def p_ellipsisParameterDecl(p):
	'''
	 ellipsisParameterDecl :  variableModifiers type OP_ARRAY IDENTIFIER
	'''

	pass

def p_explicitConstructorInvocation(p):
	'''
	 explicitConstructorInvocation :  expr_64 expr_63 arguments SEMI 
	| primary expr_65 DOT SUPER arguments SEMI
	'''

	pass

def p_qualifiedName(p):
	'''
	 qualifiedName :  expr_66 IDENTIFIER
	'''

	pass

def p_annotations(p):
	'''
	 annotations :  expr_67
	'''

	pass

def p_annotation(p):
	'''
	 annotation :  AT expr_69 qualifiedName
	'''

	pass

def p_elementValuePairs(p):
	'''
	 elementValuePairs :  expr_70 elementValuePair
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
	 elementValueArrayInitializer :  expr_73 expr_72 BLPAREN BRPAREN
	'''

	pass

def p_annotationTypeDeclaration(p):
	'''
	 annotationTypeDeclaration :  modifiers AT INTERFACE IDENTIFIER annotationTypeBody
	'''

	pass

def p_annotationTypeBody(p):
	'''
	 annotationTypeBody :  expr_74 BLPAREN BRPAREN
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
	 annotationMethodDeclaration :  modifiers type IDENTIFIER LPAREN expr_75 RPAREN SEMI
	'''

	pass

def p_block(p):
	'''
	 block :  expr_76 BLPAREN BRPAREN
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
	 localVariableDeclaration :  variableModifiers type expr_77 variableDeclarator
	'''

	pass

def p_statement(p):
	'''
	 statement :  block 
	| expr_78 expr_79 expression SEMI 
	| ASSERT expr_80 expression SEMI 
	| IF parExpression expr_81 statement 
	| forstatement 
	| WHILE parExpression statement 
	| DO statement WHILE parExpression SEMI 
	| trystatement 
	| SWITCH parExpression BLPAREN switchBlockStatementGroups BRPAREN 
	| SYNCHRONIZED parExpression block 
	| expr_82 RETURN SEMI 
	| THROW expression SEMI 
	| expr_83 BREAK SEMI 
	| expr_84 CONTINUE SEMI 
	| expression SEMI 
	| IDENTIFIER COLON statement 
	| SEMI
	'''

	pass

def p_switchBlockStatementGroups(p):
	'''
	 switchBlockStatementGroups :  expr_85
	'''

	pass

def p_switchBlockStatementGroup(p):
	'''
	 switchBlockStatementGroup :  expr_86 switchLabel
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
	 trystatement :  TRY expr_87 block
	'''

	pass

def p_catches(p):
	'''
	 catches :  expr_88 catchClause
	'''

	pass

def p_catchClause(p):
	'''
	 catchClause :  CATCH LPAREN formalParameter RPAREN block
	'''

	pass

def p_formalParameter(p):
	'''
	 formalParameter :  variableModifiers type expr_89 IDENTIFIER
	'''

	pass

def p_forstatement(p):
	'''
	 forstatement :  FOR LPAREN variableModifiers type IDENTIFIER COLON expression RPAREN statement 
	| FOR expr_90 LPAREN expr_91 SEMI expr_92 SEMI RPAREN statement
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
	 expressionList :  expr_93 expression
	'''

	pass

def p_expression(p):
	'''
	 expression :  expr_94 conditionalExpression
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
	 conditionalExpression :  expr_95 conditionalOrExpression
	'''

	pass

def p_conditionalOrExpression(p):
	'''
	 conditionalOrExpression :  expr_96 conditionalAndExpression
	'''

	pass

def p_conditionalAndExpression(p):
	'''
	 conditionalAndExpression :  expr_97 inclusiveOrExpression
	'''

	pass

def p_inclusiveOrExpression(p):
	'''
	 inclusiveOrExpression :  expr_98 exclusiveOrExpression
	'''

	pass

def p_exclusiveOrExpression(p):
	'''
	 exclusiveOrExpression :  expr_99 andExpression
	'''

	pass

def p_andExpression(p):
	'''
	 andExpression :  expr_100 equalityExpression
	'''

	pass

def p_equalityExpression(p):
	'''
	 equalityExpression :  expr_102 instanceOfExpression
	'''

	pass

def p_instanceOfExpression(p):
	'''
	 instanceOfExpression :  expr_103 relationalExpression
	'''

	pass

def p_relationalExpression(p):
	'''
	 relationalExpression :  expr_104 shiftExpression
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
	 shiftExpression :  expr_105 additiveExpression
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
	 additiveExpression :  expr_107 multiplicativeExpression
	'''

	pass

def p_multiplicativeExpression(p):
	'''
	 multiplicativeExpression :  expr_109 unaryExpression
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
	| expr_111 expr_110 primary
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
	| expr_113 expr_112 THIS 
	| expr_115 expr_114 IDENTIFIER 
	| SUPER superSuffix 
	| literal 
	| creator 
	| expr_116 primitiveType DOT CLASS 
	| VOID DOT CLASS
	'''

	pass

def p_superSuffix(p):
	'''
	 superSuffix :  arguments 
	| expr_117 DOT expr_118 IDENTIFIER
	'''

	pass

def p_identifierSuffix(p):
	'''
	 identifierSuffix :  expr_119 DOT CLASS 
	| expr_120 
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
	 selector :  DOT expr_121 IDENTIFIER 
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
	 arrayCreator :  NEW createdName FLPAREN expr_122 FRPAREN arrayInitializer 
	| NEW createdName FLPAREN expression expr_124 expr_123 FRPAREN
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
	 arrayInitializer :  expr_127 expr_126 BLPAREN BRPAREN
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
	 innerCreator :  DOT expr_128 NEW expr_129 IDENTIFIER classCreatorRest
	'''

	pass

def p_classCreatorRest(p):
	'''
	 classCreatorRest :  expr_130 arguments
	'''

	pass

def p_nonWildcardTypeArguments(p):
	'''
	 nonWildcardTypeArguments :  LESS typeList MORE
	'''

	pass

def p_arguments(p):
	'''
	 arguments :  expr_131 LPAREN RPAREN
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

def p_classHeader(p):
	'''
	 classHeader :  modifiers CLASS IDENTIFIER
	'''

	pass

def p_enumHeader(p):
	'''
	 enumHeader :  expr_132 modifiers IDENTIFIER
	'''

	pass

def p_interfaceHeader(p):
	'''
	 interfaceHeader :  modifiers INTERFACE IDENTIFIER
	'''

	pass

def p_annotationHeader(p):
	'''
	 annotationHeader :  modifiers AT INTERFACE IDENTIFIER
	'''

	pass

def p_typeHeader(p):
	'''
	 typeHeader :  expr_135 modifiers IDENTIFIER
	'''

	pass

def p_methodHeader(p):
	'''
	 methodHeader :  modifiers expr_137 expr_136 IDENTIFIER LPAREN
	'''

	pass

def p_fieldHeader(p):
	'''
	 fieldHeader :  modifiers type expr_139 expr_138 IDENTIFIER
	'''

	pass

def p_localVariableHeader(p):
	'''
	 localVariableHeader :  variableModifiers type expr_141 expr_140 IDENTIFIER
	'''

	pass

def p_expr_0(p):
	'''
	 expr_0 :  annotations
		'''
	pass

def p_expr_1(p):
	'''
	 expr_1 :  expr_0 packageDeclaration
		'''
	pass

def p_expr_2(p):
	'''
	 expr_2 :  importDeclaration
		'''
	pass

def p_expr_3(p):
	'''
	 expr_3 :  typeDeclaration
		'''
	pass

def p_expr_4(p):
	'''
	 expr_4 :  STATIC
		'''
	pass

def p_expr_5(p):
	'''
	 expr_5 :  STATIC
		'''
	pass

def p_expr_6(p):
	'''
	 expr_6 :  DOT IDENTIFIER
		'''
	pass

def p_expr_7(p):
	'''
	 expr_7 :  DOT MULT
		'''
	pass

def p_expr_8(p):
	'''
	 expr_8 :  DOT IDENTIFIER
		'''
	pass

def p_expr_9(p):
	'''
	 expr_9 :  annotation 
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

def p_expr_10(p):
	'''
	 expr_10 :  FINAL 
	| annotation
		'''
	pass

def p_expr_11(p):
	'''
	 expr_11 :  typeParameters
		'''
	pass

def p_expr_12(p):
	'''
	 expr_12 :  EXTENDS type
		'''
	pass

def p_expr_13(p):
	'''
	 expr_13 :  IMPLEMENTS typeList
		'''
	pass

def p_expr_14(p):
	'''
	 expr_14 :  COMMA typeParameter
		'''
	pass

def p_expr_15(p):
	'''
	 expr_15 :  EXTENDS typeBound
		'''
	pass

def p_expr_16(p):
	'''
	 expr_16 :  AND type
		'''
	pass

def p_expr_17(p):
	'''
	 expr_17 :  ENUM
		'''
	pass

def p_expr_18(p):
	'''
	 expr_18 :  IMPLEMENTS typeList
		'''
	pass

def p_expr_19(p):
	'''
	 expr_19 :  enumConstants
		'''
	pass

def p_expr_20(p):
	'''
	 expr_20 :  COMMA 
	| empty
		'''
	pass

def p_expr_21(p):
	'''
	 expr_21 :  enumBodyDeclarations
		'''
	pass

def p_expr_22(p):
	'''
	 expr_22 :  COMMA enumConstant
		'''
	pass

def p_expr_23(p):
	'''
	 expr_23 :  annotations
		'''
	pass

def p_expr_24(p):
	'''
	 expr_24 :  arguments
		'''
	pass

def p_expr_25(p):
	'''
	 expr_25 :  classBody
		'''
	pass

def p_expr_26(p):
	'''
	 expr_26 :  classBodyDeclaration
		'''
	pass

def p_expr_27(p):
	'''
	 expr_27 :  typeParameters
		'''
	pass

def p_expr_28(p):
	'''
	 expr_28 :  EXTENDS typeList
		'''
	pass

def p_expr_29(p):
	'''
	 expr_29 :  COMMA type
		'''
	pass

def p_expr_30(p):
	'''
	 expr_30 :  classBodyDeclaration
		'''
	pass

def p_expr_31(p):
	'''
	 expr_31 :  interfaceBodyDeclaration
		'''
	pass

def p_expr_32(p):
	'''
	 expr_32 :  STATIC
		'''
	pass

def p_expr_33(p):
	'''
	 expr_33 :  typeParameters
		'''
	pass

def p_expr_34(p):
	'''
	 expr_34 :  THROWS qualifiedNameList
		'''
	pass

def p_expr_35(p):
	'''
	 expr_35 :  explicitConstructorInvocation
		'''
	pass

def p_expr_36(p):
	'''
	 expr_36 :  blockStatement
		'''
	pass

def p_expr_37(p):
	'''
	 expr_37 :  typeParameters
		'''
	pass

def p_expr_38(p):
	'''
	 expr_38 :  type 
	| VOID
		'''
	pass

def p_expr_39(p):
	'''
	 expr_39 :  FLPAREN FRPAREN
		'''
	pass

def p_expr_40(p):
	'''
	 expr_40 :  THROWS qualifiedNameList
		'''
	pass

def p_expr_41(p):
	'''
	 expr_41 :  block 
	| SEMI
		'''
	pass

def p_expr_42(p):
	'''
	 expr_42 :  COMMA variableDeclarator
	'''
	pass

def p_expr_43(p):
	'''
	 expr_43 :  FLPAREN FRPAREN
		'''
	pass

def p_expr_44(p):
	'''
	 expr_44 :  EQUALS variableInitializer
		'''
	pass

def p_expr_45(p):
	'''
	 expr_45 :  typeParameters
		'''
	pass

def p_expr_46(p):
	'''
	 expr_46 :  type 
	| VOID
		'''
	pass

def p_expr_47(p):
	'''
	 expr_47 :  FLPAREN FRPAREN
		'''
	pass

def p_expr_48(p):
	'''
	 expr_48 :  THROWS qualifiedNameList
		'''
	pass

def p_expr_49(p):
	'''
	 expr_49 :  COMMA variableDeclarator
		'''
	pass

def p_expr_50(p):
	'''
	 expr_50 :  FLPAREN FRPAREN
		'''
	pass

def p_expr_51(p):
	'''
	 expr_51 :  FLPAREN FRPAREN
		'''
	pass

def p_expr_52(p):
	'''
	 expr_52 :  typeArguments
		'''
	pass

def p_expr_53(p):
	'''
	 expr_53 :  typeArguments
		'''
	pass

def p_expr_54(p):
	'''
	 expr_54 :  DOT expr_53 IDENTIFIER
		'''
	pass

def p_expr_55(p):
	'''
	 expr_55 :  COMMA typeArgument
		'''
	pass

def p_expr_56(p):
	'''
	 expr_56 :  EXTENDS 
	| SUPER
		'''
	pass

def p_expr_57(p):
	'''
	 expr_57 :  expr_56 type
		'''
	pass

def p_expr_58(p):
	'''
	 expr_58 :  COMMA qualifiedName
		'''
	pass

def p_expr_59(p):
	'''
	 expr_59 :  formalParameterDecls
		'''
	pass

def p_expr_60(p):
	'''
	 expr_60 :  COMMA normalParameterDecl
		'''
	pass

def p_expr_61(p):
	'''
	 expr_61 :  normalParameterDecl COMMA
		'''
	pass

def p_expr_62(p):
	'''
	 expr_62 :  FLPAREN FRPAREN
		'''
	pass

def p_expr_63(p):
	'''
	 expr_63 :  nonWildcardTypeArguments
		'''
	pass

def p_expr_64(p):
	'''
	 expr_64 :  THIS 
	| SUPER
		'''
	pass

def p_expr_65(p):
	'''
	 expr_65 :  nonWildcardTypeArguments
		'''
	pass

def p_expr_66(p):
	'''
	 expr_66 :  DOT IDENTIFIER
		'''
	pass

def p_expr_67(p):
	'''
	 expr_67 :  annotation
		'''
	pass

def p_expr_68(p):
	'''
	 expr_68 :  elementValuePairs 
	| elementValue
		'''
	pass

def p_expr_69(p):
	'''
	 expr_69 :  expr_68 LPAREN RPAREN
		'''
	pass

def p_expr_70(p):
	'''
	 expr_70 :  COMMA elementValuePair
		'''
	pass

def p_expr_71(p):
	'''
	 expr_71 :  COMMA elementValue
		'''
	pass

def p_expr_72(p):
	'''
	 expr_72 :  expr_71 elementValue
		'''
	pass

def p_expr_73(p):
	'''
	 expr_73 :  COMMA
		'''
	pass

def p_expr_74(p):
	'''
	 expr_74 :  annotationTypeElementDeclaration
		'''
	pass

def p_expr_75(p):
	'''
	 expr_75 :  DEFAULT elementValue
		'''
	pass

def p_expr_76(p):
	'''
	 expr_76 :  blockStatement
		'''
	pass

def p_expr_77(p):
	'''
	 expr_77 :  COMMA variableDeclarator
		'''
	pass

def p_expr_78(p):
	'''
	 expr_78 :  ASSERT
		'''
	pass

def p_expr_79(p):
	'''
	 expr_79 :  COLON expression
		'''
	pass

def p_expr_80(p):
	'''
	 expr_80 :  COLON expression
		'''
	pass

def p_expr_81(p):
	'''
	 expr_81 :  ELSE statement
		'''
	pass

def p_expr_82(p):
	'''
	 expr_82 :  expression
		'''
	pass

def p_expr_83(p):
	'''
	 expr_83 :  IDENTIFIER
		'''
	pass

def p_expr_84(p):
	'''
	 expr_84 :  IDENTIFIER
		'''
	pass

def p_expr_85(p):
	'''
	 expr_85 :  switchBlockStatementGroup
		'''
	pass

def p_expr_86(p):
	'''
	 expr_86 :  blockStatement
		'''
	pass

def p_expr_87(p):
	'''
	 expr_87 :  catches FINALLY block 
	| catches 
	| FINALLY block
		'''
	pass

def p_expr_88(p):
	'''
	 expr_88 :  catchClause
		'''
	pass

def p_expr_89(p):
	'''
	 expr_89 :  FLPAREN FRPAREN
		'''
	pass

def p_expr_90(p):
	'''
	 expr_90 :  forInit
		'''
	pass

def p_expr_91(p):
	'''
	 expr_91 :  expression
		'''
	pass

def p_expr_92(p):
	'''
	 expr_92 :  expressionList
		'''
	pass

def p_expr_93(p):
	'''
	 expr_93 :  COMMA expression
		'''
	pass

def p_expr_94(p):
	'''
	 expr_94 :  assignmentOperator expression
		'''
	pass

def p_expr_95(p):
	'''
	 expr_95 :  QUES expression COLON conditionalExpression
		'''
	pass

def p_expr_96(p):
	'''
	 expr_96 :  OP_LOR conditionalAndExpression
		'''
	pass

def p_expr_97(p):
	'''
	 expr_97 :  OP_LAND inclusiveOrExpression
		'''
	pass

def p_expr_98(p):
	'''
	 expr_98 :  VERTICAL exclusiveOrExpression
		'''
	pass

def p_expr_99(p):
	'''
	 expr_99 :  CARET andExpression
		'''
	pass

def p_expr_100(p):
	'''
	 expr_100 :  AND equalityExpression
		'''
	pass

def p_expr_101(p):
	'''
	 expr_101 :  OP_EQ 
	| OP_NE
		'''
	pass

def p_expr_102(p):
	'''
	 expr_102 :  expr_101 instanceOfExpression
		'''
	pass

def p_expr_103(p):
	'''
	 expr_103 :  INSTANCEOF type
		'''
	pass

def p_expr_104(p):
	'''
	 expr_104 :  relationalOp shiftExpression
		'''
	pass

def p_expr_105(p):
	'''
	 expr_105 :  shiftOp additiveExpression
		'''
	pass

def p_expr_106(p):
	'''
	 expr_106 :  PLUS 
	| DASH
		'''
	pass

def p_expr_107(p):
	'''
	 expr_107 :  expr_106 multiplicativeExpression
		'''
	pass

def p_expr_108(p):
	'''
	 expr_108 :  MULT 
	| SLASH 
	| PERCENT
		'''
	pass

def p_expr_109(p):
	'''
	 expr_109 :  expr_108 unaryExpression
		'''
	pass

def p_expr_110(p):
	'''
	 expr_110 :  selector
		'''
	pass

def p_expr_111(p):
	'''
	 expr_111 :  OP_INC 
	| OP_DEC
		'''
	pass

def p_expr_112(p):
	'''
	 expr_112 :  DOT IDENTIFIER
		'''
	pass

def p_expr_113(p):
	'''
	 expr_113 :  identifierSuffix
		'''
	pass

def p_expr_114(p):
	'''
	 expr_114 :  DOT IDENTIFIER
		'''
	pass

def p_expr_115(p):
	'''
	 expr_115 :  identifierSuffix
		'''
	pass

def p_expr_116(p):
	'''
	 expr_116 :  FLPAREN FRPAREN
		'''
	pass

def p_expr_117(p):
	'''
	 expr_117 :  typeArguments
		'''
	pass

def p_expr_118(p):
	'''
	 expr_118 :  arguments
		'''
	pass

def p_expr_119(p):
	'''
	 expr_119 :  FLPAREN FRPAREN
		'''
	pass

def p_expr_120(p):
	'''
	 expr_120 :  FLPAREN expression FRPAREN
		'''
	pass

def p_expr_121(p):
	'''
	 expr_121 :  arguments
		'''
	pass

def p_expr_122(p):
	'''
	 expr_122 :  FLPAREN FRPAREN
		'''
	pass

def p_expr_123(p):
	'''
	 expr_123 :  FLPAREN expression FRPAREN
		'''
	pass

def p_expr_124(p):
	'''
	 expr_124 :  FLPAREN FRPAREN
		'''
	pass

def p_expr_125(p):
	'''
	 expr_125 :  COMMA variableInitializer
		'''
	pass

def p_expr_126(p):
	'''
	 expr_126 :  expr_125 variableInitializer
		'''
	pass

def p_expr_127(p):
	'''
	 expr_127 :  COMMA
		'''
	pass

def p_expr_128(p):
	'''
	 expr_128 :  nonWildcardTypeArguments
		'''
	pass

def p_expr_129(p):
	'''
	 expr_129 :  typeArguments
		'''
	pass

def p_expr_130(p):
	'''
	 expr_130 :  classBody
		'''
	pass

def p_expr_131(p):
	'''
	 expr_131 :  expressionList
		'''
	pass

def p_expr_132(p):
	'''
	 expr_132 :  ENUM 
	| IDENTIFIER
		'''
	pass

def p_expr_133(p):
	'''
	 expr_133 :  AT 
	| empty
		'''
	pass

def p_expr_134(p):
	'''
	 expr_134 :  expr_133 INTERFACE
		'''
	pass

def p_expr_135(p):
	'''
	 expr_135 :  CLASS 
	| ENUM 
	| expr_134
		'''
	pass

def p_expr_136(p):
	'''
	 expr_136 :  typeParameters 
	| empty
		'''
	pass

def p_expr_137(p):
	'''
	 expr_137 :  type 
	| VOID
		'''
	pass

def p_expr_138(p):
	'''
	 expr_138 :  FLPAREN FRPAREN
		'''
	pass

def p_expr_139(p):
	'''
	 expr_139 :  EQUALS 
	| COMMA 
	| SEMI
		'''
	pass

def p_expr_140(p):
	'''
	 expr_140 :  FLPAREN FRPAREN
		'''
	pass

def p_expr_141(p):
	'''
	 expr_141 :  EQUALS 
	| COMMA 
	| SEMI
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
	result = b.parse(lexer = l , debug=1)
	if b.error : return None
	
