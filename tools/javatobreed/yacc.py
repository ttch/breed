# *.* coding=utf-8 *.*

import ply.yacc as yacc
import lex
from collections import deque

tokens = lex.tokens
def p_compilationUnit(p):
	'''
	 compilationUnit :  annotations expr_2 
	| expr_3 expr_0 expr_1
	'''

	pass

def p_packageDeclaration(p):
	'''
	 packageDeclaration :  PACKAGE qualifiedName SEMI
	'''

	pass

def p_importDeclaration(p):
	'''
	 importDeclaration :  IMPORT expr_4 qualifiedName expr_5 SEMI
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
	 classOrInterfaceDeclaration :  classOrInterfaceModifiers expr_6
	'''

	pass

def p_classOrInterfaceModifiers(p):
	'''
	 classOrInterfaceModifiers :  expr_7
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
	 modifiers :  expr_8
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
	 normalClassDeclaration :  CLASS Identifier expr_9 expr_10 expr_11 classBody
	'''

	pass

def p_typeParameters(p):
	'''
	 typeParameters :  LESS typeParameter expr_12 MORE
	'''

	pass

def p_typeParameter(p):
	'''
	 typeParameter :  Identifier expr_13
	'''

	pass

def p_typeBound(p):
	'''
	 typeBound :  type expr_14
	'''

	pass

def p_enumDeclaration(p):
	'''
	 enumDeclaration :  ENUM Identifier expr_11 enumBody
	'''

	pass

def p_enumBody(p):
	'''
	 enumBody :  BLPAREN expr_15 expr_16 expr_17 BRPAREN
	'''

	pass

def p_enumConstants(p):
	'''
	 enumConstants :  enumConstant expr_18
	'''

	pass

def p_enumConstant(p):
	'''
	 enumConstant :  expr_19 Identifier expr_20 expr_21
	'''

	pass

def p_enumBodyDeclarations(p):
	'''
	 enumBodyDeclarations :  SEMI expr_22
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
	 normalInterfaceDeclaration :  INTERFACE Identifier expr_9 expr_23 interfaceBody
	'''

	pass

def p_typeList(p):
	'''
	 typeList :  type expr_24
	'''

	pass

def p_classBody(p):
	'''
	 classBody :  BLPAREN expr_22 BRPAREN
	'''

	pass

def p_interfaceBody(p):
	'''
	 interfaceBody :  BLPAREN expr_25 BRPAREN
	'''

	pass

def p_classBodyDeclaration(p):
	'''
	 classBodyDeclaration :  SEMI 
	| expr_4 block 
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
	 memberDeclaration :  type expr_26
	'''

	pass

def p_genericMethodOrConstructorDecl(p):
	'''
	 genericMethodOrConstructorDecl :  typeParameters genericMethodOrConstructorRest
	'''

	pass

def p_genericMethodOrConstructorRest(p):
	'''
	 genericMethodOrConstructorRest :  expr_27 Identifier methodDeclaratorRest 
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
	 methodDeclaratorRest :  formalParameters expr_28 expr_29 expr_30
	'''

	pass

def p_voidMethodDeclaratorRest(p):
	'''
	 voidMethodDeclaratorRest :  formalParameters expr_29 expr_30
	'''

	pass

def p_interfaceMethodDeclaratorRest(p):
	'''
	 interfaceMethodDeclaratorRest :  formalParameters expr_28 expr_29 SEMI
	'''

	pass

def p_interfaceGenericMethodDecl(p):
	'''
	 interfaceGenericMethodDecl :  typeParameters expr_27 Identifier interfaceMethodDeclaratorRest
	'''

	pass

def p_voidInterfaceMethodDeclaratorRest(p):
	'''
	 voidInterfaceMethodDeclaratorRest :  formalParameters expr_29 SEMI
	'''

	pass

def p_constructorDeclaratorRest(p):
	'''
	 constructorDeclaratorRest :  formalParameters expr_29 constructorBody
	'''

	pass

def p_constantDeclarator(p):
	'''
	 constantDeclarator :  Identifier constantDeclaratorRest
	'''

	pass

def p_variableDeclarators(p):
	'''
	 variableDeclarators :  variableDeclarator expr_31
	'''

	pass

def p_variableDeclarator(p):
	'''
	 variableDeclarator :  variableDeclaratorId expr_32
	'''

	pass

def p_constantDeclaratorsRest(p):
	'''
	 constantDeclaratorsRest :  constantDeclaratorRest expr_33
	'''

	pass

def p_constantDeclaratorRest(p):
	'''
	 constantDeclaratorRest :  expr_28 EQUALS variableInitializer
	'''

	pass

def p_variableDeclaratorId(p):
	'''
	 variableDeclaratorId :  Identifier expr_28
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
	 arrayInitializer :  BLPAREN expr_36 BRPAREN
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
	 type :  classOrInterfaceType expr_28 
	| primitiveType expr_28
	'''

	pass

def p_classOrInterfaceType(p):
	'''
	 classOrInterfaceType :  Identifier expr_37 expr_38
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
	 typeArguments :  LESS typeArgument expr_39 MORE
	'''

	pass

def p_typeArgument(p):
	'''
	 typeArgument :  type 
	| QUES expr_41
	'''

	pass

def p_qualifiedNameList(p):
	'''
	 qualifiedNameList :  qualifiedName expr_42
	'''

	pass

def p_formalParameters(p):
	'''
	 formalParameters :  LPAREN expr_43 RPAREN
	'''

	pass

def p_formalParameterDecls(p):
	'''
	 formalParameterDecls :  variableModifiers type formalParameterDeclsRest
	'''

	pass

def p_formalParameterDeclsRest(p):
	'''
	 formalParameterDeclsRest :  variableDeclaratorId expr_44 
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
	 constructorBody :  BLPAREN expr_45 expr_46 BRPAREN
	'''

	pass

def p_explicitConstructorInvocation(p):
	'''
	 explicitConstructorInvocation :  expr_47 expr_48 arguments SEMI 
	| primary DOT expr_47 SUPER arguments SEMI
	'''

	pass

def p_qualifiedName(p):
	'''
	 qualifiedName :  Identifier expr_49
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
	 annotations :  expr_50
	'''

	pass

def p_annotation(p):
	'''
	 annotation :  AT annotationName expr_52
	'''

	pass

def p_annotationName(p):
	'''
	 annotationName :  Identifier expr_49
	'''

	pass

def p_elementValuePairs(p):
	'''
	 elementValuePairs :  elementValuePair expr_53
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
	 elementValueArrayInitializer :  BLPAREN expr_55 expr_35 BRPAREN
	'''

	pass

def p_annotationTypeDeclaration(p):
	'''
	 annotationTypeDeclaration :  AT INTERFACE Identifier annotationTypeBody
	'''

	pass

def p_annotationTypeBody(p):
	'''
	 annotationTypeBody :  BLPAREN expr_56 BRPAREN
	'''

	pass

def p_annotationTypeElementDeclaration(p):
	'''
	 annotationTypeElementDeclaration :  modifiers annotationTypeElementRest
	'''

	pass

def p_annotationTypeElementRest(p):
	'''
	 annotationTypeElementRest :  type annotationMethodOrConstantRest SEMI 
	| normalClassDeclaration expr_57 
	| normalInterfaceDeclaration expr_57 
	| enumDeclaration expr_57 
	| annotationTypeDeclaration expr_57
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
	 annotationMethodRest :  Identifier LPAREN RPAREN expr_58
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
	 block :  BLPAREN expr_46 BRPAREN
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
	 localVariableDeclaration :  variableModifiers type variableDeclarators
	'''

	pass

def p_variableModifiers(p):
	'''
	 variableModifiers :  expr_59
	'''

	pass

def p_statement(p):
	'''
	 statement :  block 
	| ASSERT expression expr_60 SEMI 
	| IF parExpression statement expr_61 
	| FOR LPAREN forControl RPAREN statement 
	| WHILE parExpression statement 
	| DO statement WHILE parExpression SEMI 
	| TRY block expr_62 
	| SWITCH parExpression BLPAREN switchBlockStatementGroups BRPAREN 
	| SYNCHRONIZED parExpression block 
	| RETURN expr_63 SEMI 
	| THROW expression SEMI 
	| BREAK expr_64 SEMI 
	| CONTINUE expr_64 SEMI 
	| SEMI 
	| statementExpression SEMI 
	| Identifier COLON statement
	'''

	pass

def p_catches(p):
	'''
	 catches :  catchClause expr_65
	'''

	pass

def p_catchClause(p):
	'''
	 catchClause :  CATCH LPAREN formalParameter RPAREN block
	'''

	pass

def p_formalParameter(p):
	'''
	 formalParameter :  variableModifiers type variableDeclaratorId
	'''

	pass

def p_switchBlockStatementGroups(p):
	'''
	 switchBlockStatementGroups :  expr_66
	'''

	pass

def p_switchBlockStatementGroup(p):
	'''
	 switchBlockStatementGroup :  expr_67 expr_46
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
	 forControl :  enhancedForControl 
	| expr_68 SEMI expr_69 SEMI expr_70
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
	 expressionList :  expression expr_71
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
	 expression :  conditionalExpression expr_72
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
	 conditionalExpression :  conditionalOrExpression expr_73
	'''

	pass

def p_conditionalOrExpression(p):
	'''
	 conditionalOrExpression :  conditionalAndExpression expr_74
	'''

	pass

def p_conditionalAndExpression(p):
	'''
	 conditionalAndExpression :  inclusiveOrExpression expr_75
	'''

	pass

def p_inclusiveOrExpression(p):
	'''
	 inclusiveOrExpression :  exclusiveOrExpression expr_76
	'''

	pass

def p_exclusiveOrExpression(p):
	'''
	 exclusiveOrExpression :  andExpression expr_77
	'''

	pass

def p_andExpression(p):
	'''
	 andExpression :  equalityExpression expr_78
	'''

	pass

def p_equalityExpression(p):
	'''
	 equalityExpression :  instanceOfExpression expr_80
	'''

	pass

def p_instanceOfExpression(p):
	'''
	 instanceOfExpression :  relationalExpression expr_81
	'''

	pass

def p_relationalExpression(p):
	'''
	 relationalExpression :  shiftExpression expr_82
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
	 shiftExpression :  additiveExpression expr_83
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
	 additiveExpression :  multiplicativeExpression expr_85
	'''

	pass

def p_multiplicativeExpression(p):
	'''
	 multiplicativeExpression :  unaryExpression expr_87
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
	| primary expr_88 expr_89
	'''

	pass

def p_castExpression(p):
	'''
	 castExpression :  LPAREN primitiveType RPAREN unaryExpression 
	| LPAREN expr_90 RPAREN unaryExpressionNotPlusMinus
	'''

	pass

def p_primary(p):
	'''
	 primary :  parExpression 
	| THIS expr_49 expr_91 
	| SUPER superSuffix 
	| literal 
	| NEW creator 
	| Identifier expr_49 expr_91 
	| primitiveType expr_28 DOT CLASS 
	| VOID DOT CLASS
	'''

	pass

def p_identifierSuffix(p):
	'''
	 identifierSuffix :  expr_28 DOT CLASS 
	| expr_92 
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
	| createdName expr_93
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
	 innerCreator :  expr_47 Identifier classCreatorRest
	'''

	pass

def p_arrayCreatorRest(p):
	'''
	 arrayCreatorRest :  FLPAREN expr_94
	'''

	pass

def p_classCreatorRest(p):
	'''
	 classCreatorRest :  arguments expr_21
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
	 selector :  DOT Identifier expr_20 
	| DOT THIS 
	| DOT SUPER superSuffix 
	| DOT NEW innerCreator 
	| FLPAREN expression FRPAREN
	'''

	pass

def p_superSuffix(p):
	'''
	 superSuffix :  arguments 
	| DOT Identifier expr_20
	'''

	pass

def p_arguments(p):
	'''
	 arguments :  LPAREN expr_95 RPAREN
	'''

	pass

def p_expr_0(p):
	'''
	 expr_0 :  importDeclaration 
	| expr_0 importDeclaration 
	| empty
		'''
	pass

def p_expr_1(p):
	'''
	 expr_1 :  typeDeclaration 
	| expr_1 typeDeclaration 
	| empty
		'''
	pass

def p_expr_2(p):
	'''
	 expr_2 :  packageDeclaration expr_0 expr_1 
	| classOrInterfaceDeclaration expr_1
		'''
	pass

def p_expr_3(p):
	'''
	 expr_3 :  packageDeclaration 
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
	 expr_5 :  DOT MULT 
	| empty
		'''
	pass

def p_expr_6(p):
	'''
	 expr_6 :  classDeclaration 
	| interfaceDeclaration
		'''
	pass

def p_expr_7(p):
	'''
	 expr_7 :  classOrInterfaceModifier 
	| expr_7 classOrInterfaceModifier 
	| empty
		'''
	pass

def p_expr_8(p):
	'''
	 expr_8 :  modifier 
	| expr_8 modifier 
	| empty
		'''
	pass

def p_expr_9(p):
	'''
	 expr_9 :  typeParameters 
	| empty
		'''
	pass

def p_expr_10(p):
	'''
	 expr_10 :  EXTENDS type 
	| empty
		'''
	pass

def p_expr_11(p):
	'''
	 expr_11 :  IMPLEMENTS typeList 
	| empty
		'''
	pass

def p_expr_12(p):
	'''
	 expr_12 :  COMMA typeParameter 
	| expr_12 COMMA typeParameter 
	| empty
		'''
	pass

def p_expr_13(p):
	'''
	 expr_13 :  EXTENDS typeBound 
	| empty
		'''
	pass

def p_expr_14(p):
	'''
	 expr_14 :  AND type 
	| expr_14 AND type 
	| empty
		'''
	pass

def p_expr_15(p):
	'''
	 expr_15 :  enumConstants 
	| empty
		'''
	pass

def p_expr_16(p):
	'''
	 expr_16 :  COMMA 
	| empty
		'''
	pass

def p_expr_17(p):
	'''
	 expr_17 :  enumBodyDeclarations 
	| empty
		'''
	pass

def p_expr_18(p):
	'''
	 expr_18 :  COMMA enumConstant 
	| expr_18 COMMA enumConstant 
	| empty
		'''
	pass

def p_expr_19(p):
	'''
	 expr_19 :  annotations 
	| empty
		'''
	pass

def p_expr_20(p):
	'''
	 expr_20 :  arguments 
	| empty
		'''
	pass

def p_expr_21(p):
	'''
	 expr_21 :  classBody 
	| empty
		'''
	pass

def p_expr_22(p):
	'''
	 expr_22 :  classBodyDeclaration 
	| expr_22 classBodyDeclaration 
	| empty
		'''
	pass

def p_expr_23(p):
	'''
	 expr_23 :  EXTENDS typeList 
	| empty
		'''
	pass

def p_expr_24(p):
	'''
	 expr_24 :  COMMA type 
	| expr_24 COMMA type 
	| empty
		'''
	pass

def p_expr_25(p):
	'''
	 expr_25 :  interfaceBodyDeclaration 
	| expr_25 interfaceBodyDeclaration 
	| empty
		'''
	pass

def p_expr_26(p):
	'''
	 expr_26 :  methodDeclaration 
	| fieldDeclaration
		'''
	pass

def p_expr_27(p):
	'''
	 expr_27 :  type 
	| VOID
		'''
	pass

def p_expr_28(p):
	'''
	 expr_28 :  FLPAREN FRPAREN 
	| expr_28 FLPAREN FRPAREN 
	| empty
		'''
	pass

def p_expr_29(p):
	'''
	 expr_29 :  THROWS qualifiedNameList 
	| empty
		'''
	pass

def p_expr_30(p):
	'''
	 expr_30 :  methodBody 
	| SEMI
		'''
	pass

def p_expr_31(p):
	'''
	 expr_31 :  COMMA variableDeclarator 
	| expr_31 COMMA variableDeclarator 
	| empty
		'''
	pass

def p_expr_32(p):
	'''
	 expr_32 :  EQUALS variableInitializer 
	| empty
		'''
	pass

def p_expr_33(p):
	'''
	 expr_33 :  COMMA constantDeclarator 
	| expr_33 COMMA constantDeclarator 
	| empty
		'''
	pass

def p_expr_34(p):
	'''
	 expr_34 :  COMMA variableInitializer 
	| expr_34 COMMA variableInitializer 
	| empty
		'''
	pass

def p_expr_35(p):
	'''
	 expr_35 :  COMMA 
	| empty
		'''
	pass

def p_expr_36(p):
	'''
	 expr_36 :  variableInitializer expr_34 expr_35 
	| empty
		'''
	pass

def p_expr_37(p):
	'''
	 expr_37 :  typeArguments 
	| empty
		'''
	pass

def p_expr_38(p):
	'''
	 expr_38 :  DOT Identifier expr_37 
	| expr_38 DOT Identifier expr_37 
	| empty
		'''
	pass

def p_expr_39(p):
	'''
	 expr_39 :  COMMA typeArgument 
	| expr_39 COMMA typeArgument 
	| empty
		'''
	pass

def p_expr_40(p):
	'''
	 expr_40 :  EXTENDS 
	| SUPER
		'''
	pass

def p_expr_41(p):
	'''
	 expr_41 :  expr_40 type 
	| empty
		'''
	pass

def p_expr_42(p):
	'''
	 expr_42 :  COMMA qualifiedName 
	| expr_42 COMMA qualifiedName 
	| empty
		'''
	pass

def p_expr_43(p):
	'''
	 expr_43 :  formalParameterDecls 
	| empty
		'''
	pass

def p_expr_44(p):
	'''
	 expr_44 :  COMMA formalParameterDecls 
	| empty
		'''
	pass

def p_expr_45(p):
	'''
	 expr_45 :  explicitConstructorInvocation 
	| empty
		'''
	pass

def p_expr_46(p):
	'''
	 expr_46 :  blockStatement 
	| expr_46 blockStatement 
	| empty
		'''
	pass

def p_expr_47(p):
	'''
	 expr_47 :  nonWildcardTypeArguments 
	| empty
		'''
	pass

def p_expr_48(p):
	'''
	 expr_48 :  THIS 
	| SUPER
		'''
	pass

def p_expr_49(p):
	'''
	 expr_49 :  DOT Identifier 
	| expr_49 DOT Identifier 
	| empty
		'''
	pass

def p_expr_50(p):
	'''
	 expr_50 :  annotation 
	| expr_50 annotation
		'''
	pass

def p_expr_51(p):
	'''
	 expr_51 :  elementValuePairs 
	| elementValue
		'''
	pass

def p_expr_52(p):
	'''
	 expr_52 :  LPAREN expr_51 RPAREN 
	| empty
		'''
	pass

def p_expr_53(p):
	'''
	 expr_53 :  COMMA elementValuePair 
	| expr_53 COMMA elementValuePair 
	| empty
		'''
	pass

def p_expr_54(p):
	'''
	 expr_54 :  COMMA elementValue 
	| expr_54 COMMA elementValue 
	| empty
		'''
	pass

def p_expr_55(p):
	'''
	 expr_55 :  elementValue expr_54 
	| empty
		'''
	pass

def p_expr_56(p):
	'''
	 expr_56 :  annotationTypeElementDeclaration 
	| expr_56 annotationTypeElementDeclaration 
	| empty
		'''
	pass

def p_expr_57(p):
	'''
	 expr_57 :  SEMI 
	| empty
		'''
	pass

def p_expr_58(p):
	'''
	 expr_58 :  defaultValue 
	| empty
		'''
	pass

def p_expr_59(p):
	'''
	 expr_59 :  variableModifier 
	| expr_59 variableModifier 
	| empty
		'''
	pass

def p_expr_60(p):
	'''
	 expr_60 :  COLON expression 
	| empty
		'''
	pass

def p_expr_61(p):
	'''
	 expr_61 :  ELSE statement 
	| empty
		'''
	pass

def p_expr_62(p):
	'''
	 expr_62 :  catches FINALLY block 
	| catches 
	| FINALLY block
		'''
	pass

def p_expr_63(p):
	'''
	 expr_63 :  expression 
	| empty
		'''
	pass

def p_expr_64(p):
	'''
	 expr_64 :  Identifier 
	| empty
		'''
	pass

def p_expr_65(p):
	'''
	 expr_65 :  catchClause 
	| expr_65 catchClause 
	| empty
		'''
	pass

def p_expr_66(p):
	'''
	 expr_66 :  switchBlockStatementGroup 
	| expr_66 switchBlockStatementGroup 
	| empty
		'''
	pass

def p_expr_67(p):
	'''
	 expr_67 :  switchLabel 
	| expr_67 switchLabel
		'''
	pass

def p_expr_68(p):
	'''
	 expr_68 :  forInit 
	| empty
		'''
	pass

def p_expr_69(p):
	'''
	 expr_69 :  expression 
	| empty
		'''
	pass

def p_expr_70(p):
	'''
	 expr_70 :  forUpdate 
	| empty
		'''
	pass

def p_expr_71(p):
	'''
	 expr_71 :  COMMA expression 
	| expr_71 COMMA expression 
	| empty
		'''
	pass

def p_expr_72(p):
	'''
	 expr_72 :  assignmentOperator expression 
	| empty
		'''
	pass

def p_expr_73(p):
	'''
	 expr_73 :  QUES expression COLON expression 
	| empty
		'''
	pass

def p_expr_74(p):
	'''
	 expr_74 :  OP_LOR conditionalAndExpression 
	| expr_74 OP_LOR conditionalAndExpression 
	| empty
		'''
	pass

def p_expr_75(p):
	'''
	 expr_75 :  OP_LAND inclusiveOrExpression 
	| expr_75 OP_LAND inclusiveOrExpression 
	| empty
		'''
	pass

def p_expr_76(p):
	'''
	 expr_76 :  VERTICAL exclusiveOrExpression 
	| expr_76 VERTICAL exclusiveOrExpression 
	| empty
		'''
	pass

def p_expr_77(p):
	'''
	 expr_77 :  CARET andExpression 
	| expr_77 CARET andExpression 
	| empty
		'''
	pass

def p_expr_78(p):
	'''
	 expr_78 :  AND equalityExpression 
	| expr_78 AND equalityExpression 
	| empty
		'''
	pass

def p_expr_79(p):
	'''
	 expr_79 :  OP_EQ 
	| OP_NE
		'''
	pass

def p_expr_80(p):
	'''
	 expr_80 :  expr_79 instanceOfExpression 
	| expr_80 expr_79 instanceOfExpression 
	| empty
		'''
	pass

def p_expr_81(p):
	'''
	 expr_81 :  INSTANCEOF type 
	| empty
		'''
	pass

def p_expr_82(p):
	'''
	 expr_82 :  relationalOp shiftExpression 
	| expr_82 relationalOp shiftExpression 
	| empty
		'''
	pass

def p_expr_83(p):
	'''
	 expr_83 :  shiftOp additiveExpression 
	| expr_83 shiftOp additiveExpression 
	| empty
		'''
	pass

def p_expr_84(p):
	'''
	 expr_84 :  PLUS 
	| DASH
		'''
	pass

def p_expr_85(p):
	'''
	 expr_85 :  expr_84 multiplicativeExpression 
	| expr_85 expr_84 multiplicativeExpression 
	| empty
		'''
	pass

def p_expr_86(p):
	'''
	 expr_86 :  MULT 
	| SLASH 
	| PERCENT
		'''
	pass

def p_expr_87(p):
	'''
	 expr_87 :  expr_86 unaryExpression 
	| expr_87 expr_86 unaryExpression 
	| empty
		'''
	pass

def p_expr_88(p):
	'''
	 expr_88 :  selector 
	| expr_88 selector 
	| empty
		'''
	pass

def p_expr_89(p):
	'''
	 expr_89 :  OP_INC 
	| OP_DEC
		'''
	pass

def p_expr_90(p):
	'''
	 expr_90 :  type 
	| expression
		'''
	pass

def p_expr_91(p):
	'''
	 expr_91 :  identifierSuffix 
	| empty
		'''
	pass

def p_expr_92(p):
	'''
	 expr_92 :  FLPAREN expression FRPAREN 
	| expr_92 FLPAREN expression FRPAREN
		'''
	pass

def p_expr_93(p):
	'''
	 expr_93 :  arrayCreatorRest 
	| classCreatorRest
		'''
	pass

def p_expr_94(p):
	'''
	 expr_94 :  FRPAREN expr_28 arrayInitializer 
	| expression FRPAREN expr_92 expr_28
		'''
	pass

def p_expr_95(p):
	'''
	 expr_95 :  expressionList 
	| empty
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
	result = b.parse(lexer = l , debug=1)
	if b.error : return None
	