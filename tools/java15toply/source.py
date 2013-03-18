def p_compilationUnit(p):
	'''
	 compilationUnit :  A3 A2 A1
	
'''	pass

def p_packageDeclaration(p):
	'''
	 packageDeclaration :  'package' qualifiedName ';'
	
'''	pass

def p_importDeclaration(p):
	'''
	 importDeclaration :  A4 'import' IDENTIFIER '.' '*' ';' 
	| A5 'import' A7 A6 IDENTIFIER ';'
	
'''	pass

def p_qualifiedImportName(p):
	'''
	 qualifiedImportName :  A8 IDENTIFIER
	
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
	 modifiers :  A9
	
'''	pass

def p_variableModifiers(p):
	'''
	 variableModifiers :  A10
	
'''	pass

def p_classDeclaration(p):
	'''
	 classDeclaration :  normalClassDeclaration 
	| enumDeclaration
	
'''	pass

def p_normalClassDeclaration(p):
	'''
	 normalClassDeclaration :  modifiers 'class' A13 A12 A11 IDENTIFIER classBody
	
'''	pass

def p_typeParameters(p):
	'''
	 typeParameters :  '&lt;' A14 typeParameter '&gt;'
	
'''	pass

def p_typeParameter(p):
	'''
	 typeParameter :  A15 IDENTIFIER
	
'''	pass

def p_typeBound(p):
	'''
	 typeBound :  A16 type
	
'''	pass

def p_enumDeclaration(p):
	'''
	 enumDeclaration :  ( 'enum' ) modifiers A17 IDENTIFIER enumBody
	
'''	pass

def p_enumBody(p):
	'''
	 enumBody :  A18 '{' A19 ',' ? '}'
	
'''	pass

def p_enumConstants(p):
	'''
	 enumConstants :  A20 enumConstant
	
'''	pass

def p_enumConstant(p):
	'''
	 enumConstant :  A21 A23 A22 IDENTIFIER
	
'''	pass

def p_enumBodyDeclarations(p):
	'''
	 enumBodyDeclarations :  A24 ';'
	
'''	pass

def p_interfaceDeclaration(p):
	'''
	 interfaceDeclaration :  normalInterfaceDeclaration 
	| annotationTypeDeclaration
	
'''	pass

def p_normalInterfaceDeclaration(p):
	'''
	 normalInterfaceDeclaration :  modifiers 'interface' A26 A25 IDENTIFIER interfaceBody
	
'''	pass

def p_typeList(p):
	'''
	 typeList :  A27 type
	
'''	pass

def p_classBody(p):
	'''
	 classBody :  A28 '{' '}'
	
'''	pass

def p_interfaceBody(p):
	'''
	 interfaceBody :  A29 '{' '}'
	
'''	pass

def p_classBodyDeclaration(p):
	'''
	 classBodyDeclaration :  ';' 
	| A30 block 
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
	 methodDeclaration :  A31 modifiers IDENTIFIER A32 formalParameters A34 A33 '{' '}' 
	| A36 A35 modifiers IDENTIFIER A39 A38 A37 formalParameters
	
'''	pass

def p_fieldDeclaration(p):
	'''
	 fieldDeclaration :  modifiers type A40 variableDeclarator ';'
	
'''	pass

def p_variableDeclarator(p):
	'''
	 variableDeclarator :  A42 A41 IDENTIFIER
	
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
	 interfaceMethodDeclaration :  A44 A43 modifiers IDENTIFIER A46 A45 formalParameters ';'
	
'''	pass

def p_interfaceFieldDeclaration(p):
	'''
	 interfaceFieldDeclaration :  modifiers type A47 variableDeclarator ';'
	
'''	pass

def p_type(p):
	'''
	 type :  A48 classOrInterfaceType 
	| A49 primitiveType
	
'''	pass

def p_classOrInterfaceType(p):
	'''
	 classOrInterfaceType :  A52 A50 IDENTIFIER
	
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
	 typeArguments :  '&lt;' A53 typeArgument '&gt;'
	
'''	pass

def p_typeArgument(p):
	'''
	 typeArgument :  type 
	| A55 '?'
	
'''	pass

def p_qualifiedNameList(p):
	'''
	 qualifiedNameList :  A56 qualifiedName
	
'''	pass

def p_formalParameters(p):
	'''
	 formalParameters :  A57 '(' ')'
	
'''	pass

def p_formalParameterDecls(p):
	'''
	 formalParameterDecls :  ellipsisParameterDecl 
	| A58 normalParameterDecl 
	| A59 ellipsisParameterDecl
	
'''	pass

def p_normalParameterDecl(p):
	'''
	 normalParameterDecl :  variableModifiers type A60 IDENTIFIER
	
'''	pass

def p_ellipsisParameterDecl(p):
	'''
	 ellipsisParameterDecl :  variableModifiers type '...' IDENTIFIER
	
'''	pass

def p_explicitConstructorInvocation(p):
	'''
	 explicitConstructorInvocation :  A62 A61 arguments ';' 
	| primary A63 '.' 'super' arguments ';'
	
'''	pass

def p_qualifiedName(p):
	'''
	 qualifiedName :  A64 IDENTIFIER
	
'''	pass

def p_annotations(p):
	'''
	 annotations :  A65
	
'''	pass

def p_annotation(p):
	'''
	 annotation :  '@' A67 qualifiedName
	
'''	pass

def p_elementValuePairs(p):
	'''
	 elementValuePairs :  A68 elementValuePair
	
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
	 elementValueArrayInitializer :  A71 A70 '{' '}'
	
'''	pass

def p_annotationTypeDeclaration(p):
	'''
	 annotationTypeDeclaration :  modifiers '@' 'interface' IDENTIFIER annotationTypeBody
	
'''	pass

def p_annotationTypeBody(p):
	'''
	 annotationTypeBody :  A72 '{' '}'
	
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
	 annotationMethodDeclaration :  modifiers type IDENTIFIER '(' A73 ')' ';'
	
'''	pass

def p_block(p):
	'''
	 block :  A74 '{' '}'
	
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
	 localVariableDeclaration :  variableModifiers type A75 variableDeclarator
	
'''	pass

def p_statement(p):
	'''
	 statement :  block 
	| ( 'assert' ) A76 expression ';' 
	| 'assert' A77 expression ';' 
	| 'if' parExpression A78 statement 
	| forstatement 
	| 'while' parExpression statement 
	| 'do' statement 'while' parExpression ';' 
	| trystatement 
	| 'switch' parExpression '{' switchBlockStatementGroups '}' 
	| 'synchronized' parExpression block 
	| A79 'return' ';' 
	| 'throw' expression ';' 
	| A80 'break' ';' 
	| A81 'continue' ';' 
	| expression ';' 
	| IDENTIFIER ':' statement 
	| ';'
	
'''	pass

def p_switchBlockStatementGroups(p):
	'''
	 switchBlockStatementGroups :  A82
	
'''	pass

def p_switchBlockStatementGroup(p):
	'''
	 switchBlockStatementGroup :  A83 switchLabel
	
'''	pass

def p_switchLabel(p):
	'''
	 switchLabel :  'case' expression ':' 
	| 'default' ':'
	
'''	pass

def p_trystatement(p):
	'''
	 trystatement :  'try' A84 block
	
'''	pass

def p_catches(p):
	'''
	 catches :  A85 catchClause
	
'''	pass

def p_catchClause(p):
	'''
	 catchClause :  'catch' '(' formalParameter ')' block
	
'''	pass

def p_formalParameter(p):
	'''
	 formalParameter :  variableModifiers type A86 IDENTIFIER
	
'''	pass

def p_forstatement(p):
	'''
	 forstatement :  'for' '(' variableModifiers type IDENTIFIER ':' expression ')' statement 
	| 'for' A87 '(' A88 ';' A89 ';' ')' statement
	
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
	 expressionList :  A90 expression
	
'''	pass

def p_expression(p):
	'''
	 expression :  A91 conditionalExpression
	
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
	 conditionalExpression :  A92 conditionalOrExpression
	
'''	pass

def p_conditionalOrExpression(p):
	'''
	 conditionalOrExpression :  A93 conditionalAndExpression
	
'''	pass

def p_conditionalAndExpression(p):
	'''
	 conditionalAndExpression :  A94 inclusiveOrExpression
	
'''	pass

def p_inclusiveOrExpression(p):
	'''
	 inclusiveOrExpression :  A95 exclusiveOrExpression
	
'''	pass

def p_exclusiveOrExpression(p):
	'''
	 exclusiveOrExpression :  A96 andExpression
	
'''	pass

def p_andExpression(p):
	'''
	 andExpression :  A97 equalityExpression
	
'''	pass

def p_equalityExpression(p):
	'''
	 equalityExpression :  A99 instanceOfExpression
	
'''	pass

def p_instanceOfExpression(p):
	'''
	 instanceOfExpression :  A100 relationalExpression
	
'''	pass

def p_relationalExpression(p):
	'''
	 relationalExpression :  A101 shiftExpression
	
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
	 shiftExpression :  A102 additiveExpression
	
'''	pass

def p_shiftOp(p):
	'''
	 shiftOp :  '&lt;' '&lt;' 
	| '&gt;' '&gt;' '&gt;' 
	| '&gt;' '&gt;'
	
'''	pass

def p_additiveExpression(p):
	'''
	 additiveExpression :  A104 multiplicativeExpression
	
'''	pass

def p_multiplicativeExpression(p):
	'''
	 multiplicativeExpression :  A106 unaryExpression
	
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
	| A108 A107 primary
	
'''	pass

def p_castExpression(p):
	'''
	 castExpression :  '(' primitiveType ')' unaryExpression 
	| '(' type ')' unaryExpressionNotPlusMinus
	
'''	pass

def p_primary(p):
	'''
	 primary :  parExpression 
	| A110 A109 'this' 
	| A112 A111 IDENTIFIER 
	| 'super' superSuffix 
	| literal 
	| creator 
	| A113 primitiveType '.' 'class' 
	| 'void' '.' 'class'
	
'''	pass

def p_superSuffix(p):
	'''
	 superSuffix :  arguments 
	| A114 '.' A115 IDENTIFIER
	
'''	pass

def p_identifierSuffix(p):
	'''
	 identifierSuffix :  A116 '.' 'class' 
	| A117 
	| arguments 
	| '.' 'class' 
	| '.' nonWildcardTypeArguments IDENTIFIER arguments 
	| '.' 'this' 
	| '.' 'super' arguments 
	| innerCreator
	
'''	pass

def p_selector(p):
	'''
	 selector :  '.' A118 IDENTIFIER 
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
	 arrayCreator :  'new' createdName '[' A119 ']' arrayInitializer 
	| 'new' createdName '[' expression A121 A120 ']'
	
'''	pass

def p_variableInitializer(p):
	'''
	 variableInitializer :  arrayInitializer 
	| expression
	
'''	pass

def p_arrayInitializer(p):
	'''
	 arrayInitializer :  A124 A123 '{' '}'
	
'''	pass

def p_createdName(p):
	'''
	 createdName :  classOrInterfaceType 
	| primitiveType
	
'''	pass

def p_innerCreator(p):
	'''
	 innerCreator :  '.' A125 'new' A126 IDENTIFIER classCreatorRest
	
'''	pass

def p_classCreatorRest(p):
	'''
	 classCreatorRest :  A127 arguments
	
'''	pass

def p_nonWildcardTypeArguments(p):
	'''
	 nonWildcardTypeArguments :  '&lt;' typeList '&gt;'
	
'''	pass

def p_arguments(p):
	'''
	 arguments :  A128 '(' ')'
	
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
	 enumHeader :  A129 modifiers IDENTIFIER
	
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
	 typeHeader :  A130 modifiers IDENTIFIER
	
'''	pass

def p_methodHeader(p):
	'''
	 methodHeader :  modifiers A131 typeParameters ? IDENTIFIER '('
	
'''	pass

def p_fieldHeader(p):
	'''
	 fieldHeader :  modifiers type A133 A132 IDENTIFIER
	
'''	pass

def p_localVariableHeader(p):
	'''
	 localVariableHeader :  variableModifiers type A135 A134 IDENTIFIER
	
'''	pass

