def p_compilationUnit(p):
	'''
	 compilationUnit :  expr_3 expr_2 expr_1
	
'''	pass

def p_packageDeclaration(p):
	'''
	 packageDeclaration :  'package' qualifiedName ';'
	
'''	pass

def p_importDeclaration(p):
	'''
	 importDeclaration :  expr_4 'import' IDENTIFIER '.' '*' ';' 
	| expr_5 'import' expr_7 expr_6 IDENTIFIER ';'
	
'''	pass

def p_qualifiedImportName(p):
	'''
	 qualifiedImportName :  expr_8 IDENTIFIER
	
'''	pass

def p_typeDeclaration(p):
	'''
	 typeDeclaration :  classOrInterfaceDeclaration 
	| ';'
	
'''	pass

def p_classOrInterfaceDeclaration(p):
	'''
	 classOrInterfaceDeclaration :  classDeclaration 
	| interfaceDeclaration
	
'''	pass

def p_modifiers(p):
	'''
	 modifiers :  expr_9
	
'''	pass

def p_variableModifiers(p):
	'''
	 variableModifiers :  expr_10
	
'''	pass

def p_classDeclaration(p):
	'''
	 classDeclaration :  normalClassDeclaration 
	| enumDeclaration
	
'''	pass

def p_normalClassDeclaration(p):
	'''
	 normalClassDeclaration :  modifiers 'class' expr_13 expr_12 expr_11 IDENTIFIER classBody
	
'''	pass

def p_typeParameters(p):
	'''
	 typeParameters :  '&lt;' expr_14 typeParameter '&gt;'
	
'''	pass

def p_typeParameter(p):
	'''
	 typeParameter :  expr_15 IDENTIFIER
	
'''	pass

def p_typeBound(p):
	'''
	 typeBound :  expr_16 type
	
'''	pass

def p_enumDeclaration(p):
	'''
	 enumDeclaration :  ( 'enum' ) modifiers expr_17 IDENTIFIER enumBody
	
'''	pass

def p_enumBody(p):
	'''
	 enumBody :  expr_18 '{' expr_19 ',' ? '}'
	
'''	pass

def p_enumConstants(p):
	'''
	 enumConstants :  expr_20 enumConstant
	
'''	pass

def p_enumConstant(p):
	'''
	 enumConstant :  expr_21 expr_23 expr_22 IDENTIFIER
	
'''	pass

def p_enumBodyDeclarations(p):
	'''
	 enumBodyDeclarations :  expr_24 ';'
	
'''	pass

def p_interfaceDeclaration(p):
	'''
	 interfaceDeclaration :  normalInterfaceDeclaration 
	| annotationTypeDeclaration
	
'''	pass

def p_normalInterfaceDeclaration(p):
	'''
	 normalInterfaceDeclaration :  modifiers 'interface' expr_26 expr_25 IDENTIFIER interfaceBody
	
'''	pass

def p_typeList(p):
	'''
	 typeList :  expr_27 type
	
'''	pass

def p_classBody(p):
	'''
	 classBody :  expr_28 '{' '}'
	
'''	pass

def p_interfaceBody(p):
	'''
	 interfaceBody :  expr_29 '{' '}'
	
'''	pass

def p_classBodyDeclaration(p):
	'''
	 classBodyDeclaration :  ';' 
	| expr_30 block 
	| memberDecl
	
'''	pass

def p_memberDecl(p):
	'''
	 memberDecl :  fieldDeclaration 
	| methodDeclaration 
	| classDeclaration 
	| interfaceDeclaration
	
'''	pass

def p_methodDeclaration(p):
	'''
	 methodDeclaration :  expr_31 modifiers IDENTIFIER expr_32 formalParameters expr_34 expr_33 '{' '}' 
	| expr_36 expr_35 modifiers IDENTIFIER expr_39 expr_38 expr_37 formalParameters
	
'''	pass

def p_fieldDeclaration(p):
	'''
	 fieldDeclaration :  modifiers type expr_40 variableDeclarator ';'
	
'''	pass

def p_variableDeclarator(p):
	'''
	 variableDeclarator :  expr_42 expr_41 IDENTIFIER
	
'''	pass

def p_interfaceBodyDeclaration(p):
	'''
	 interfaceBodyDeclaration :  interfaceFieldDeclaration 
	| interfaceMethodDeclaration 
	| interfaceDeclaration 
	| classDeclaration 
	| ';'
	
'''	pass

def p_interfaceMethodDeclaration(p):
	'''
	 interfaceMethodDeclaration :  expr_44 expr_43 modifiers IDENTIFIER expr_46 expr_45 formalParameters ';'
	
'''	pass

def p_interfaceFieldDeclaration(p):
	'''
	 interfaceFieldDeclaration :  modifiers type expr_47 variableDeclarator ';'
	
'''	pass

def p_type(p):
	'''
	 type :  expr_48 classOrInterfaceType 
	| expr_49 primitiveType
	
'''	pass

def p_classOrInterfaceType(p):
	'''
	 classOrInterfaceType :  expr_52 expr_50 IDENTIFIER
	
'''	pass

def p_primitiveType(p):
	'''
	 primitiveType :  'boolean' 
	| 'char' 
	| 'byte' 
	| 'short' 
	| 'int' 
	| 'long' 
	| 'float' 
	| 'double'
	
'''	pass

def p_typeArguments(p):
	'''
	 typeArguments :  '&lt;' expr_53 typeArgument '&gt;'
	
'''	pass

def p_typeArgument(p):
	'''
	 typeArgument :  type 
	| expr_55 '?'
	
'''	pass

def p_qualifiedNameList(p):
	'''
	 qualifiedNameList :  expr_56 qualifiedName
	
'''	pass

def p_formalParameters(p):
	'''
	 formalParameters :  expr_57 '(' ')'
	
'''	pass

def p_formalParameterDecls(p):
	'''
	 formalParameterDecls :  ellipsisParameterDecl 
	| expr_58 normalParameterDecl 
	| expr_59 ellipsisParameterDecl
	
'''	pass

def p_normalParameterDecl(p):
	'''
	 normalParameterDecl :  variableModifiers type expr_60 IDENTIFIER
	
'''	pass

def p_ellipsisParameterDecl(p):
	'''
	 ellipsisParameterDecl :  variableModifiers type '...' IDENTIFIER
	
'''	pass

def p_explicitConstructorInvocation(p):
	'''
	 explicitConstructorInvocation :  expr_62 expr_61 arguments ';' 
	| primary expr_63 '.' 'super' arguments ';'
	
'''	pass

def p_qualifiedName(p):
	'''
	 qualifiedName :  expr_64 IDENTIFIER
	
'''	pass

def p_annotations(p):
	'''
	 annotations :  expr_65
	
'''	pass

def p_annotation(p):
	'''
	 annotation :  '@' expr_67 qualifiedName
	
'''	pass

def p_elementValuePairs(p):
	'''
	 elementValuePairs :  expr_68 elementValuePair
	
'''	pass

def p_elementValuePair(p):
	'''
	 elementValuePair :  IDENTIFIER '=' elementValue
	
'''	pass

def p_elementValue(p):
	'''
	 elementValue :  conditionalExpression 
	| annotation 
	| elementValueArrayInitializer
	
'''	pass

def p_elementValueArrayInitializer(p):
	'''
	 elementValueArrayInitializer :  expr_71 expr_70 '{' '}'
	
'''	pass

def p_annotationTypeDeclaration(p):
	'''
	 annotationTypeDeclaration :  modifiers '@' 'interface' IDENTIFIER annotationTypeBody
	
'''	pass

def p_annotationTypeBody(p):
	'''
	 annotationTypeBody :  expr_72 '{' '}'
	
'''	pass

def p_annotationTypeElementDeclaration(p):
	'''
	 annotationTypeElementDeclaration :  annotationMethodDeclaration 
	| interfaceFieldDeclaration 
	| normalClassDeclaration 
	| normalInterfaceDeclaration 
	| enumDeclaration 
	| annotationTypeDeclaration 
	| ';'
	
'''	pass

def p_annotationMethodDeclaration(p):
	'''
	 annotationMethodDeclaration :  modifiers type IDENTIFIER '(' expr_73 ')' ';'
	
'''	pass

def p_block(p):
	'''
	 block :  expr_74 '{' '}'
	
'''	pass

def p_blockStatement(p):
	'''
	 blockStatement :  localVariableDeclarationStatement 
	| classOrInterfaceDeclaration 
	| statement
	
'''	pass

def p_localVariableDeclarationStatement(p):
	'''
	 localVariableDeclarationStatement :  localVariableDeclaration ';'
	
'''	pass

def p_localVariableDeclaration(p):
	'''
	 localVariableDeclaration :  variableModifiers type expr_75 variableDeclarator
	
'''	pass

def p_statement(p):
	'''
	 statement :  block 
	| ( 'assert' ) expr_76 expression ';' 
	| 'assert' expr_77 expression ';' 
	| 'if' parExpression expr_78 statement 
	| forstatement 
	| 'while' parExpression statement 
	| 'do' statement 'while' parExpression ';' 
	| trystatement 
	| 'switch' parExpression '{' switchBlockStatementGroups '}' 
	| 'synchronized' parExpression block 
	| expr_79 'return' ';' 
	| 'throw' expression ';' 
	| expr_80 'break' ';' 
	| expr_81 'continue' ';' 
	| expression ';' 
	| IDENTIFIER ':' statement 
	| ';'
	
'''	pass

def p_switchBlockStatementGroups(p):
	'''
	 switchBlockStatementGroups :  expr_82
	
'''	pass

def p_switchBlockStatementGroup(p):
	'''
	 switchBlockStatementGroup :  expr_83 switchLabel
	
'''	pass

def p_switchLabel(p):
	'''
	 switchLabel :  'case' expression ':' 
	| 'default' ':'
	
'''	pass

def p_trystatement(p):
	'''
	 trystatement :  'try' expr_84 block
	
'''	pass

def p_catches(p):
	'''
	 catches :  expr_85 catchClause
	
'''	pass

def p_catchClause(p):
	'''
	 catchClause :  'catch' '(' formalParameter ')' block
	
'''	pass

def p_formalParameter(p):
	'''
	 formalParameter :  variableModifiers type expr_86 IDENTIFIER
	
'''	pass

def p_forstatement(p):
	'''
	 forstatement :  'for' '(' variableModifiers type IDENTIFIER ':' expression ')' statement 
	| 'for' expr_87 '(' expr_88 ';' expr_89 ';' ')' statement
	
'''	pass

def p_forInit(p):
	'''
	 forInit :  localVariableDeclaration 
	| expressionList
	
'''	pass

def p_parExpression(p):
	'''
	 parExpression :  '(' expression ')'
	
'''	pass

def p_expressionList(p):
	'''
	 expressionList :  expr_90 expression
	
'''	pass

def p_expression(p):
	'''
	 expression :  expr_91 conditionalExpression
	
'''	pass

def p_assignmentOperator(p):
	'''
	 assignmentOperator :  '=' 
	| '+=' 
	| '-=' 
	| '*=' 
	| '/=' 
	| '&amp;=' 
	| '|=' 
	| '^=' 
	| '%=' 
	| '&lt;' '&lt;' '=' 
	| '&gt;' '&gt;' '&gt;' '=' 
	| '&gt;' '&gt;' '='
	
'''	pass

def p_conditionalExpression(p):
	'''
	 conditionalExpression :  expr_92 conditionalOrExpression
	
'''	pass

def p_conditionalOrExpression(p):
	'''
	 conditionalOrExpression :  expr_93 conditionalAndExpression
	
'''	pass

def p_conditionalAndExpression(p):
	'''
	 conditionalAndExpression :  expr_94 inclusiveOrExpression
	
'''	pass

def p_inclusiveOrExpression(p):
	'''
	 inclusiveOrExpression :  expr_95 exclusiveOrExpression
	
'''	pass

def p_exclusiveOrExpression(p):
	'''
	 exclusiveOrExpression :  expr_96 andExpression
	
'''	pass

def p_andExpression(p):
	'''
	 andExpression :  expr_97 equalityExpression
	
'''	pass

def p_equalityExpression(p):
	'''
	 equalityExpression :  expr_99 instanceOfExpression
	
'''	pass

def p_instanceOfExpression(p):
	'''
	 instanceOfExpression :  expr_100 relationalExpression
	
'''	pass

def p_relationalExpression(p):
	'''
	 relationalExpression :  expr_101 shiftExpression
	
'''	pass

def p_relationalOp(p):
	'''
	 relationalOp :  '&lt;' '=' 
	| '&gt;' '=' 
	| '&lt;' 
	| '&gt;'
	
'''	pass

def p_shiftExpression(p):
	'''
	 shiftExpression :  expr_102 additiveExpression
	
'''	pass

def p_shiftOp(p):
	'''
	 shiftOp :  '&lt;' '&lt;' 
	| '&gt;' '&gt;' '&gt;' 
	| '&gt;' '&gt;'
	
'''	pass

def p_additiveExpression(p):
	'''
	 additiveExpression :  expr_104 multiplicativeExpression
	
'''	pass

def p_multiplicativeExpression(p):
	'''
	 multiplicativeExpression :  expr_106 unaryExpression
	
'''	pass

def p_unaryExpression(p):
	'''
	 unaryExpression :  '+' unaryExpression 
	| '-' unaryExpression 
	| '++' unaryExpression 
	| '--' unaryExpression 
	| unaryExpressionNotPlusMinus
	
'''	pass

def p_unaryExpressionNotPlusMinus(p):
	'''
	 unaryExpressionNotPlusMinus :  '~' unaryExpression 
	| '!' unaryExpression 
	| castExpression 
	| expr_108 expr_107 primary
	
'''	pass

def p_castExpression(p):
	'''
	 castExpression :  '(' primitiveType ')' unaryExpression 
	| '(' type ')' unaryExpressionNotPlusMinus
	
'''	pass

def p_primary(p):
	'''
	 primary :  parExpression 
	| expr_110 expr_109 'this' 
	| expr_112 expr_111 IDENTIFIER 
	| 'super' superSuffix 
	| literal 
	| creator 
	| expr_113 primitiveType '.' 'class' 
	| 'void' '.' 'class'
	
'''	pass

def p_superSuffix(p):
	'''
	 superSuffix :  arguments 
	| expr_114 '.' expr_115 IDENTIFIER
	
'''	pass

def p_identifierSuffix(p):
	'''
	 identifierSuffix :  expr_116 '.' 'class' 
	| expr_117 
	| arguments 
	| '.' 'class' 
	| '.' nonWildcardTypeArguments IDENTIFIER arguments 
	| '.' 'this' 
	| '.' 'super' arguments 
	| innerCreator
	
'''	pass

def p_selector(p):
	'''
	 selector :  '.' expr_118 IDENTIFIER 
	| '.' 'this' 
	| '.' 'super' superSuffix 
	| innerCreator 
	| '[' expression ']'
	
'''	pass

def p_creator(p):
	'''
	 creator :  'new' nonWildcardTypeArguments classOrInterfaceType classCreatorRest 
	| 'new' classOrInterfaceType classCreatorRest 
	| arrayCreator
	
'''	pass

def p_arrayCreator(p):
	'''
	 arrayCreator :  'new' createdName '[' expr_119 ']' arrayInitializer 
	| 'new' createdName '[' expression expr_121 expr_120 ']'
	
'''	pass

def p_variableInitializer(p):
	'''
	 variableInitializer :  arrayInitializer 
	| expression
	
'''	pass

def p_arrayInitializer(p):
	'''
	 arrayInitializer :  expr_124 expr_123 '{' '}'
	
'''	pass

def p_createdName(p):
	'''
	 createdName :  classOrInterfaceType 
	| primitiveType
	
'''	pass

def p_innerCreator(p):
	'''
	 innerCreator :  '.' expr_125 'new' expr_126 IDENTIFIER classCreatorRest
	
'''	pass

def p_classCreatorRest(p):
	'''
	 classCreatorRest :  expr_127 arguments
	
'''	pass

def p_nonWildcardTypeArguments(p):
	'''
	 nonWildcardTypeArguments :  '&lt;' typeList '&gt;'
	
'''	pass

def p_arguments(p):
	'''
	 arguments :  expr_128 '(' ')'
	
'''	pass

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
	
'''	pass

def p_classHeader(p):
	'''
	 classHeader :  modifiers 'class' IDENTIFIER
	
'''	pass

def p_enumHeader(p):
	'''
	 enumHeader :  expr_129 modifiers IDENTIFIER
	
'''	pass

def p_interfaceHeader(p):
	'''
	 interfaceHeader :  modifiers 'interface' IDENTIFIER
	
'''	pass

def p_annotationHeader(p):
	'''
	 annotationHeader :  modifiers '@' 'interface' IDENTIFIER
	
'''	pass

def p_typeHeader(p):
	'''
	 typeHeader :  expr_130 modifiers IDENTIFIER
	
'''	pass

def p_methodHeader(p):
	'''
	 methodHeader :  modifiers expr_131 typeParameters ? IDENTIFIER '('
	
'''	pass

def p_fieldHeader(p):
	'''
	 fieldHeader :  modifiers type expr_133 expr_132 IDENTIFIER
	
'''	pass

def p_localVariableHeader(p):
	'''
	 localVariableHeader :  variableModifiers type expr_135 expr_134 IDENTIFIER
	
'''	pass

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
	 expr_4 :  'static' 
	| empty
		'''
	pass

def p_expr_5(p):
	'''
	 expr_5 :  'static' 
	| empty
		'''
	pass

def p_expr_6(p):
	'''
	 expr_6 :  '.' IDENTIFIER 
	| expr_6 '.' IDENTIFIER
		'''
	pass

def p_expr_7(p):
	'''
	 expr_7 :  '.' '*' 
	| empty
		'''
	pass

def p_expr_8(p):
	'''
	 expr_8 :  '.' IDENTIFIER 
	| expr_8 '.' IDENTIFIER 
	| empty
		'''
	pass

def p_expr_9(p):
	'''
	 expr_9 :  annotation 
	| 'public' 
	| 'protected' 
	| 'private' 
	| 'static' 
	| 'abstract' 
	| 'final' 
	| 'native' 
	| 'synchronized' 
	| 'transient' 
	| 'volatile' 
	| 'strictfp'
		'''
	pass

def p_expr_10(p):
	'''
	 expr_10 :  'final' 
	| annotation
		'''
	pass

def p_expr_11(p):
	'''
	 expr_11 :  typeParameters 
	| empty
		'''
	pass

def p_expr_12(p):
	'''
	 expr_12 :  'extends' type 
	| empty
		'''
	pass

def p_expr_13(p):
	'''
	 expr_13 :  'implements' typeList 
	| empty
		'''
	pass

def p_expr_14(p):
	'''
	 expr_14 :  ',' typeParameter 
	| expr_14 ',' typeParameter 
	| empty
		'''
	pass

def p_expr_15(p):
	'''
	 expr_15 :  'extends' typeBound 
	| empty
		'''
	pass

def p_expr_16(p):
	'''
	 expr_16 :  '&amp;' type 
	| expr_16 '&amp;' type 
	| empty
		'''
	pass

def p_expr_17(p):
	'''
	 expr_17 :  'implements' typeList 
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
	 expr_19 :  enumBodyDeclarations 
	| empty
		'''
	pass

def p_expr_20(p):
	'''
	 expr_20 :  ',' enumConstant 
	| expr_20 ',' enumConstant 
	| empty
		'''
	pass

def p_expr_21(p):
	'''
	 expr_21 :  annotations 
	| empty
		'''
	pass

def p_expr_22(p):
	'''
	 expr_22 :  arguments 
	| empty
		'''
	pass

def p_expr_23(p):
	'''
	 expr_23 :  classBody 
	| empty
		'''
	pass

def p_expr_24(p):
	'''
	 expr_24 :  classBodyDeclaration 
	| expr_24 classBodyDeclaration 
	| empty
		'''
	pass

def p_expr_25(p):
	'''
	 expr_25 :  typeParameters 
	| empty
		'''
	pass

def p_expr_26(p):
	'''
	 expr_26 :  'extends' typeList 
	| empty
		'''
	pass

def p_expr_27(p):
	'''
	 expr_27 :  ',' type 
	| expr_27 ',' type 
	| empty
		'''
	pass

def p_expr_28(p):
	'''
	 expr_28 :  classBodyDeclaration 
	| expr_28 classBodyDeclaration 
	| empty
		'''
	pass

def p_expr_29(p):
	'''
	 expr_29 :  interfaceBodyDeclaration 
	| expr_29 interfaceBodyDeclaration 
	| empty
		'''
	pass

def p_expr_30(p):
	'''
	 expr_30 :  'static' 
	| empty
		'''
	pass

def p_expr_31(p):
	'''
	 expr_31 :  typeParameters 
	| empty
		'''
	pass

def p_expr_32(p):
	'''
	 expr_32 :  'throws' qualifiedNameList 
	| empty
		'''
	pass

def p_expr_33(p):
	'''
	 expr_33 :  explicitConstructorInvocation 
	| empty
		'''
	pass

def p_expr_34(p):
	'''
	 expr_34 :  blockStatement 
	| expr_34 blockStatement 
	| empty
		'''
	pass

def p_expr_35(p):
	'''
	 expr_35 :  typeParameters 
	| empty
		'''
	pass

def p_expr_36(p):
	'''
	 expr_36 :  type 
	|
		'''
	pass

def p_expr_37(p):
	'''
	 expr_37 :  '[' ']' 
	| expr_37 '[' ']' 
	| empty
		'''
	pass

def p_expr_38(p):
	'''
	 expr_38 :  'throws' qualifiedNameList 
	| empty
		'''
	pass

def p_expr_39(p):
	'''
	 expr_39 :  block 
	|
		'''
	pass

def p_expr_40(p):
	'''
	 expr_40 :  ',' variableDeclarator 
	| expr_40 ',' variableDeclarator 
	| empty
		'''
	pass

def p_expr_41(p):
	'''
	 expr_41 :  '[' ']' 
	| expr_41 '[' ']' 
	| empty
		'''
	pass

def p_expr_42(p):
	'''
	 expr_42 :  '=' variableInitializer 
	| empty
		'''
	pass

def p_expr_43(p):
	'''
	 expr_43 :  typeParameters 
	| empty
		'''
	pass

def p_expr_44(p):
	'''
	 expr_44 :  type 
	|
		'''
	pass

def p_expr_45(p):
	'''
	 expr_45 :  '[' ']' 
	| expr_45 '[' ']' 
	| empty
		'''
	pass

def p_expr_46(p):
	'''
	 expr_46 :  'throws' qualifiedNameList 
	| empty
		'''
	pass

def p_expr_47(p):
	'''
	 expr_47 :  ',' variableDeclarator 
	| expr_47 ',' variableDeclarator 
	| empty
		'''
	pass

def p_expr_48(p):
	'''
	 expr_48 :  '[' ']' 
	| expr_48 '[' ']' 
	| empty
		'''
	pass

def p_expr_49(p):
	'''
	 expr_49 :  '[' ']' 
	| expr_49 '[' ']' 
	| empty
		'''
	pass

def p_expr_50(p):
	'''
	 expr_50 :  typeArguments 
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
	 expr_52 :  '.' expr_51 IDENTIFIER 
	| expr_52 '.' expr_51 IDENTIFIER 
	| empty
		'''
	pass

def p_expr_53(p):
	'''
	 expr_53 :  ',' typeArgument 
	| expr_53 ',' typeArgument 
	| empty
		'''
	pass

def p_expr_54(p):
	'''
	 expr_54 :  'extends' 
	|
		'''
	pass

def p_expr_55(p):
	'''
	 expr_55 :  expr_54 type 
	| empty
		'''
	pass

def p_expr_56(p):
	'''
	 expr_56 :  ',' qualifiedName 
	| expr_56 ',' qualifiedName 
	| empty
		'''
	pass

def p_expr_57(p):
	'''
	 expr_57 :  formalParameterDecls 
	| empty
		'''
	pass

def p_expr_58(p):
	'''
	 expr_58 :  ',' normalParameterDecl 
	| expr_58 ',' normalParameterDecl 
	| empty
		'''
	pass

def p_expr_59(p):
	'''
	 expr_59 :  normalParameterDecl ',' 
	| expr_59 normalParameterDecl ','
		'''
	pass

def p_expr_60(p):
	'''
	 expr_60 :  '[' ']' 
	| expr_60 '[' ']' 
	| empty
		'''
	pass

def p_expr_61(p):
	'''
	 expr_61 :  nonWildcardTypeArguments 
	| empty
		'''
	pass

def p_expr_62(p):
	'''
	 expr_62 :  'this' 
	|
		'''
	pass

def p_expr_63(p):
	'''
	 expr_63 :  nonWildcardTypeArguments 
	| empty
		'''
	pass

def p_expr_64(p):
	'''
	 expr_64 :  '.' IDENTIFIER 
	| expr_64 '.' IDENTIFIER 
	| empty
		'''
	pass

def p_expr_65(p):
	'''
	 expr_65 :  annotation 
	| expr_65 annotation
		'''
	pass

def p_expr_66(p):
	'''
	 expr_66 :  elementValuePairs 
	| elementValue
		'''
	pass

def p_expr_67(p):
	'''
	 expr_67 :  expr_66 '(' ')' 
	| empty
		'''
	pass

def p_expr_68(p):
	'''
	 expr_68 :  ',' elementValuePair 
	| expr_68 ',' elementValuePair 
	| empty
		'''
	pass

def p_expr_69(p):
	'''
	 expr_69 :  ',' elementValue 
	| expr_69 ',' elementValue 
	| empty
		'''
	pass

def p_expr_70(p):
	'''
	 expr_70 :  expr_69 elementValue 
	| empty
		'''
	pass

def p_expr_71(p):
	'''
	 expr_71 :  ',' 
	| empty
		'''
	pass

def p_expr_72(p):
	'''
	 expr_72 :  annotationTypeElementDeclaration 
	| expr_72 annotationTypeElementDeclaration 
	| empty
		'''
	pass

def p_expr_73(p):
	'''
	 expr_73 :  'default' elementValue 
	| empty
		'''
	pass

def p_expr_74(p):
	'''
	 expr_74 :  blockStatement 
	| expr_74 blockStatement 
	| empty
		'''
	pass

def p_expr_75(p):
	'''
	 expr_75 :  ',' variableDeclarator 
	| expr_75 ',' variableDeclarator 
	| empty
		'''
	pass

def p_expr_76(p):
	'''
	 expr_76 :  ':' expression 
	| empty
		'''
	pass

def p_expr_77(p):
	'''
	 expr_77 :  ':' expression 
	| empty
		'''
	pass

def p_expr_78(p):
	'''
	 expr_78 :  'else' statement 
	| empty
		'''
	pass

def p_expr_79(p):
	'''
	 expr_79 :  expression 
	| empty
		'''
	pass

def p_expr_80(p):
	'''
	 expr_80 :  IDENTIFIER 
	| empty
		'''
	pass

def p_expr_81(p):
	'''
	 expr_81 :  IDENTIFIER 
	| empty
		'''
	pass

def p_expr_82(p):
	'''
	 expr_82 :  switchBlockStatementGroup 
	| expr_82 switchBlockStatementGroup 
	| empty
		'''
	pass

def p_expr_83(p):
	'''
	 expr_83 :  blockStatement 
	| expr_83 blockStatement 
	| empty
		'''
	pass

def p_expr_84(p):
	'''
	 expr_84 :  catches 'finally' block 
	| catches 
	| 'finally'
		'''
	pass

def p_expr_85(p):
	'''
	 expr_85 :  catchClause 
	| expr_85 catchClause 
	| empty
		'''
	pass

def p_expr_86(p):
	'''
	 expr_86 :  '[' ']' 
	| expr_86 '[' ']' 
	| empty
		'''
	pass

def p_expr_87(p):
	'''
	 expr_87 :  forInit 
	| empty
		'''
	pass

def p_expr_88(p):
	'''
	 expr_88 :  expression 
	| empty
		'''
	pass

def p_expr_89(p):
	'''
	 expr_89 :  expressionList 
	| empty
		'''
	pass

def p_expr_90(p):
	'''
	 expr_90 :  ',' expression 
	| expr_90 ',' expression 
	| empty
		'''
	pass

def p_expr_91(p):
	'''
	 expr_91 :  assignmentOperator expression 
	| empty
		'''
	pass

def p_expr_92(p):
	'''
	 expr_92 :  '?' expression ':' conditionalExpression 
	| empty
		'''
	pass

def p_expr_93(p):
	'''
	 expr_93 :  '||' conditionalAndExpression 
	| expr_93 '||' conditionalAndExpression 
	| empty
		'''
	pass

def p_expr_94(p):
	'''
	 expr_94 :  '&amp;&amp;' inclusiveOrExpression 
	| expr_94 '&amp;&amp;' inclusiveOrExpression 
	| empty
		'''
	pass

def p_expr_95(p):
	'''
	 expr_95 :  '|' exclusiveOrExpression 
	| expr_95 '|' exclusiveOrExpression 
	| empty
		'''
	pass

def p_expr_96(p):
	'''
	 expr_96 :  '^' andExpression 
	| expr_96 '^' andExpression 
	| empty
		'''
	pass

def p_expr_97(p):
	'''
	 expr_97 :  '&amp;' equalityExpression 
	| expr_97 '&amp;' equalityExpression 
	| empty
		'''
	pass

def p_expr_98(p):
	'''
	 expr_98 :  '==' 
	|
		'''
	pass

def p_expr_99(p):
	'''
	 expr_99 :  expr_98 instanceOfExpression 
	| expr_99 expr_98 instanceOfExpression 
	| empty
		'''
	pass

def p_expr_100(p):
	'''
	 expr_100 :  'instanceof' type 
	| empty
		'''
	pass

def p_expr_101(p):
	'''
	 expr_101 :  relationalOp shiftExpression 
	| expr_101 relationalOp shiftExpression 
	| empty
		'''
	pass

def p_expr_102(p):
	'''
	 expr_102 :  shiftOp additiveExpression 
	| expr_102 shiftOp additiveExpression 
	| empty
		'''
	pass

def p_expr_103(p):
	'''
	 expr_103 :  '+' 
	|
		'''
	pass

def p_expr_104(p):
	'''
	 expr_104 :  expr_103 multiplicativeExpression 
	| expr_104 expr_103 multiplicativeExpression 
	| empty
		'''
	pass

def p_expr_105(p):
	'''
	 expr_105 :  '*' 
	| '/' 
	|
		'''
	pass

def p_expr_106(p):
	'''
	 expr_106 :  expr_105 unaryExpression 
	| expr_106 expr_105 unaryExpression 
	| empty
		'''
	pass

def p_expr_107(p):
	'''
	 expr_107 :  selector 
	| expr_107 selector 
	| empty
		'''
	pass

def p_expr_108(p):
	'''
	 expr_108 :  '++' 
	| '--'
		'''
	pass

def p_expr_109(p):
	'''
	 expr_109 :  '.' IDENTIFIER 
	| expr_109 '.' IDENTIFIER 
	| empty
		'''
	pass

def p_expr_110(p):
	'''
	 expr_110 :  identifierSuffix 
	| empty
		'''
	pass

def p_expr_111(p):
	'''
	 expr_111 :  '.' IDENTIFIER 
	| expr_111 '.' IDENTIFIER 
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
	 expr_113 :  '[' ']' 
	| expr_113 '[' ']' 
	| empty
		'''
	pass

def p_expr_114(p):
	'''
	 expr_114 :  typeArguments 
	| empty
		'''
	pass

def p_expr_115(p):
	'''
	 expr_115 :  arguments 
	| empty
		'''
	pass

def p_expr_116(p):
	'''
	 expr_116 :  '[' ']' 
	| expr_116 '[' ']'
		'''
	pass

def p_expr_117(p):
	'''
	 expr_117 :  '[' expression ']' 
	| expr_117 '[' expression ']'
		'''
	pass

def p_expr_118(p):
	'''
	 expr_118 :  arguments 
	| empty
		'''
	pass

def p_expr_119(p):
	'''
	 expr_119 :  '[' ']' 
	| expr_119 '[' ']' 
	| empty
		'''
	pass

def p_expr_120(p):
	'''
	 expr_120 :  '[' expression ']' 
	| expr_120 '[' expression ']' 
	| empty
		'''
	pass

def p_expr_121(p):
	'''
	 expr_121 :  '[' ']' 
	| expr_121 '[' ']' 
	| empty
		'''
	pass

def p_expr_122(p):
	'''
	 expr_122 :  ',' variableInitializer 
	| expr_122 ',' variableInitializer 
	| empty
		'''
	pass

def p_expr_123(p):
	'''
	 expr_123 :  expr_122 variableInitializer 
	| empty
		'''
	pass

def p_expr_124(p):
	'''
	 expr_124 :  ',' 
	| empty
		'''
	pass

def p_expr_125(p):
	'''
	 expr_125 :  nonWildcardTypeArguments 
	| empty
		'''
	pass

def p_expr_126(p):
	'''
	 expr_126 :  typeArguments 
	| empty
		'''
	pass

def p_expr_127(p):
	'''
	 expr_127 :  classBody 
	| empty
		'''
	pass

def p_expr_128(p):
	'''
	 expr_128 :  expressionList 
	| empty
		'''
	pass

def p_expr_129(p):
	'''
	 expr_129 :  'enum' 
	|
		'''
	pass

def p_expr_130(p):
	'''
	 expr_130 :  'class' 
	| 'enum' 
	| ( '@' ? 'interface'
		'''
	pass

def p_expr_131(p):
	'''
	 expr_131 :  type 
	| 'void'
		'''
	pass

def p_expr_132(p):
	'''
	 expr_132 :  '[' ']' 
	| expr_132 '[' ']' 
	| empty
		'''
	pass

def p_expr_133(p):
	'''
	 expr_133 :  '=' 
	| ',' 
	|
		'''
	pass

def p_expr_134(p):
	'''
	 expr_134 :  '[' ']' 
	| expr_134 '[' ']' 
	| empty
		'''
	pass

def p_expr_135(p):
	'''
	 expr_135 :  '=' 
	| ',' 
	|
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
	