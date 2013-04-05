def p_TypeSpecifier( p ):
	''' 
	TypeSpecifier :  TypeName Dims 
	| TypeName 
	'''
	pass

def p_TypeName( p ):
	''' 
	TypeName :  QualifiedName 
	| PrimitiveType 
	'''
	pass

def p_ClassNameList( p ):
	''' 
	ClassNameList :  ClassNameList , QualifiedName 
	| QualifiedName 
	'''
	pass

def p_PrimitiveType( p ):
	''' 
	PrimitiveType :  VOID 
	| DOUBLE 
	| FLOAT 
	| LONG 
	| INT 
	| SHORT 
	| BYTE 
	| CHAR 
	| BOOLEAN 
	'''
	pass

def p_CompilationUnit( p ):
	''' 
	CompilationUnit :  ProgramFile 
	'''
	pass

def p_ProgramFile( p ):
	''' 
	ProgramFile :  TypeDeclarations 
	| ImportStatements 
	| PackageStatement 
	| ImportStatements TypeDeclarations 
	| PackageStatement TypeDeclarations 
	| PackageStatement ImportStatements 
	| PackageStatement ImportStatements TypeDeclarations 
	'''
	pass

def p_PackageStatement( p ):
	''' 
	PackageStatement :  PACKAGE QualifiedName ; 
	'''
	pass

def p_TypeDeclarations( p ):
	''' 
	TypeDeclarations :  TypeDeclarations TypeDeclaration 
	| TypeDeclaration 
	'''
	pass

def p_ImportStatements( p ):
	''' 
	ImportStatements :  ImportStatements ImportStatement 
	| ImportStatement 
	'''
	pass

def p_ImportStatement( p ):
	''' 
	ImportStatement :  IMPORT QualifiedName . * ; 
	| IMPORT QualifiedName ; 
	'''
	pass

def p_QualifiedName( p ):
	''' 
	QualifiedName :  QualifiedName . IDENTIFIER 
	| IDENTIFIER 
	'''
	pass

def p_TypeDeclaration( p ):
	''' 
	TypeDeclaration :  ClassHeader { } 
	| ClassHeader { FieldDeclarations } 
	'''
	pass

def p_ClassHeader( p ):
	''' 
	ClassHeader :  ClassWord IDENTIFIER 
	| ClassWord IDENTIFIER Interfaces 
	| ClassWord IDENTIFIER Extends 
	| Modifiers ClassWord IDENTIFIER 
	| ClassWord IDENTIFIER Extends Interfaces 
	| Modifiers ClassWord IDENTIFIER Interfaces 
	| Modifiers ClassWord IDENTIFIER Extends 
	| Modifiers ClassWord IDENTIFIER Extends Interfaces 
	'''
	pass

def p_Modifiers( p ):
	''' 
	Modifiers :  Modifiers Modifier 
	| Modifier 
	'''
	pass

def p_Modifier( p ):
	''' 
	Modifier :  SYNCHRONIZED 
	| NATIVE 
	| VOLATILE 
	| TRANSIENT 
	| STATIC 
	| PRIVATE 
	| PROTECTED 
	| PUBLIC 
	| FINAL 
	| ABSTRACT 
	'''
	pass

def p_ClassWord( p ):
	''' 
	ClassWord :  INTERFACE 
	| CLASS 
	'''
	pass

def p_Interfaces( p ):
	''' 
	Interfaces :  IMPLEMENTS ClassNameList 
	'''
	pass

def p_FieldDeclarations( p ):
	''' 
	FieldDeclarations :  FieldDeclarations FieldDeclaration 
	| FieldDeclaration 
	'''
	pass

def p_FieldDeclaration( p ):
	''' 
	FieldDeclaration :  TypeDeclaration 
	| NonStaticInitializer 
	| StaticInitializer 
	| ConstructorDeclaration 
	| MethodDeclaration 
	| FieldVariableDeclaration ; 
	'''
	pass

def p_FieldVariableDeclaration( p ):
	''' 
	FieldVariableDeclaration :  TypeSpecifier VariableDeclarators 
	| Modifiers TypeSpecifier VariableDeclarators 
	'''
	pass

def p_VariableDeclarators( p ):
	''' 
	VariableDeclarators :  VariableDeclarators , VariableDeclarator 
	| VariableDeclarator 
	'''
	pass

def p_VariableDeclarator( p ):
	''' 
	VariableDeclarator :  DeclaratorName = VariableInitializer 
	| DeclaratorName 
	'''
	pass

def p_VariableInitializer( p ):
	''' 
	VariableInitializer :  { ArrayInitializers } 
	| { } 
	| Expression 
	'''
	pass

def p_ArrayInitializers( p ):
	''' 
	ArrayInitializers :  ArrayInitializers , 
	| ArrayInitializers , VariableInitializer 
	| VariableInitializer 
	'''
	pass

def p_MethodDeclaration( p ):
	''' 
	MethodDeclaration :  TypeSpecifier MethodDeclarator MethodBody 
	| TypeSpecifier MethodDeclarator Throws MethodBody 
	| Modifiers TypeSpecifier MethodDeclarator MethodBody 
	| Modifiers TypeSpecifier MethodDeclarator Throws MethodBody 
	'''
	pass

def p_MethodDeclarator( p ):
	''' 
	MethodDeclarator :  MethodDeclarator OP_DIM 
	| DeclaratorName ( ) 
	| DeclaratorName ( ParameterList ) 
	'''
	pass

def p_ParameterList( p ):
	''' 
	ParameterList :  ParameterList , Parameter 
	| Parameter 
	'''
	pass

def p_Parameter( p ):
	''' 
	Parameter :  TypeSpecifier DeclaratorName 
	'''
	pass

def p_DeclaratorName( p ):
	''' 
	DeclaratorName :  DeclaratorName OP_DIM 
	| IDENTIFIER 
	'''
	pass

def p_Throws( p ):
	''' 
	Throws :  THROWS ClassNameList 
	'''
	pass

def p_MethodBody( p ):
	''' 
	MethodBody :  ; 
	| Block 
	'''
	pass

def p_ConstructorDeclaration( p ):
	''' 
	ConstructorDeclaration :  ConstructorDeclarator Block 
	| ConstructorDeclarator Throws Block 
	| Modifiers ConstructorDeclarator Block 
	| Modifiers ConstructorDeclarator Throws Block 
	'''
	pass

def p_ConstructorDeclarator( p ):
	''' 
	ConstructorDeclarator :  IDENTIFIER ( ) 
	| IDENTIFIER ( ParameterList ) 
	'''
	pass

def p_StaticInitializer( p ):
	''' 
	StaticInitializer :  STATIC Block 
	'''
	pass

def p_NonStaticInitializer( p ):
	''' 
	NonStaticInitializer :  Block 
	'''
	pass

def p_Extends( p ):
	''' 
	Extends :  Extends , TypeName 
	| EXTENDS TypeName 
	'''
	pass

def p_Block( p ):
	''' 
	Block :  { } 
	| { LocalVariableDeclarationsAndStatements } 
	'''
	pass

def p_LocalVariableDeclarationsAndStatements( p ):
	''' 
	LocalVariableDeclarationsAndStatements :  LocalVariableDeclarationsAndStatements LocalVariableDeclarationOrStatement 
	| LocalVariableDeclarationOrStatement 
	'''
	pass

def p_LocalVariableDeclarationOrStatement( p ):
	''' 
	LocalVariableDeclarationOrStatement :  Statement 
	| LocalVariableDeclarationStatement 
	'''
	pass

def p_LocalVariableDeclarationStatement( p ):
	''' 
	LocalVariableDeclarationStatement :  TypeSpecifier VariableDeclarators ; 
	'''
	pass

def p_Statement( p ):
	''' 
	Statement :  Block 
	| GuardingStatement 
	| JumpStatement 
	| IterationStatement 
	| SelectionStatement 
	| ExpressionStatement ; 
	| LabeledStatement 
	| EmptyStatement 
	'''
	pass

def p_EmptyStatement( p ):
	''' 
	EmptyStatement :  ; 
	'''
	pass

def p_LabeledStatement( p ):
	''' 
	LabeledStatement :  DEFAULT : LocalVariableDeclarationOrStatement 
	| CASE ConstantExpression : LocalVariableDeclarationOrStatement 
	| IDENTIFIER : LocalVariableDeclarationOrStatement 
	'''
	pass

def p_ExpressionStatement( p ):
	''' 
	ExpressionStatement :  Expression 
	'''
	pass

def p_SelectionStatement( p ):
	''' 
	SelectionStatement :  SWITCH ( Expression ) Block 
	| IF ( Expression ) Statement ELSE Statement 
	| IF ( Expression ) Statement 
	'''
	pass

def p_IterationStatement( p ):
	''' 
	IterationStatement :  FOR ( ForInit ForExpr ) Statement 
	| FOR ( ForInit ForExpr ForIncr ) Statement 
	| DO Statement WHILE ( Expression ) ; 
	| WHILE ( Expression ) Statement 
	'''
	pass

def p_ForInit( p ):
	''' 
	ForInit :  ; 
	| LocalVariableDeclarationStatement 
	| ExpressionStatements ; 
	'''
	pass

def p_ForExpr( p ):
	''' 
	ForExpr :  ; 
	| Expression ; 
	'''
	pass

def p_ForIncr( p ):
	''' 
	ForIncr :  ExpressionStatements 
	'''
	pass

def p_ExpressionStatements( p ):
	''' 
	ExpressionStatements :  ExpressionStatements , ExpressionStatement 
	| ExpressionStatement 
	'''
	pass

def p_JumpStatement( p ):
	''' 
	JumpStatement :  THROW Expression ; 
	| RETURN ; 
	| RETURN Expression ; 
	| CONTINUE ; 
	| CONTINUE IDENTIFIER ; 
	| BREAK ; 
	| BREAK IDENTIFIER ; 
	'''
	pass

def p_GuardingStatement( p ):
	''' 
	GuardingStatement :  TRY Block Catches Finally 
	| TRY Block Catches 
	| TRY Block Finally 
	| SYNCHRONIZED ( Expression ) Statement 
	'''
	pass

def p_Catches( p ):
	''' 
	Catches :  Catches Catch 
	| Catch 
	'''
	pass

def p_Catch( p ):
	''' 
	Catch :  CatchHeader Block 
	'''
	pass

def p_CatchHeader( p ):
	''' 
	CatchHeader :  CATCH ( TypeSpecifier ) 
	| CATCH ( TypeSpecifier IDENTIFIER ) 
	'''
	pass

def p_Finally( p ):
	''' 
	Finally :  FINALLY Block 
	'''
	pass

def p_PrimaryExpression( p ):
	''' 
	PrimaryExpression :  NotJustName 
	| QualifiedName 
	'''
	pass

def p_NotJustName( p ):
	''' 
	NotJustName :  ComplexPrimary 
	| NewAllocationExpression 
	| SpecialName 
	'''
	pass

def p_ComplexPrimary( p ):
	''' 
	ComplexPrimary :  ComplexPrimaryNoParenthesis 
	| ( Expression ) 
	'''
	pass

def p_ComplexPrimaryNoParenthesis( p ):
	''' 
	ComplexPrimaryNoParenthesis :  MethodCall 
	| FieldAccess 
	| ArrayAccess 
	| BOOLLIT 
	| LITERAL 
	'''
	pass

def p_ArrayAccess( p ):
	''' 
	ArrayAccess :  ComplexPrimary [ Expression ] 
	| QualifiedName [ Expression ] 
	'''
	pass

def p_FieldAccess( p ):
	''' 
	FieldAccess :  RealPostfixExpression . IDENTIFIER 
	| NotJustName . IDENTIFIER 
	'''
	pass

def p_MethodCall( p ):
	''' 
	MethodCall :  MethodAccess ( ) 
	| MethodAccess ( ArgumentList ) 
	'''
	pass

def p_MethodAccess( p ):
	''' 
	MethodAccess :  QualifiedName 
	| SpecialName 
	| ComplexPrimaryNoParenthesis 
	'''
	pass

def p_SpecialName( p ):
	''' 
	SpecialName :  JNULL 
	| SUPER 
	| THIS 
	'''
	pass

def p_ArgumentList( p ):
	''' 
	ArgumentList :  ArgumentList , Expression 
	| Expression 
	'''
	pass

def p_NewAllocationExpression( p ):
	''' 
	NewAllocationExpression :  ClassAllocationExpression { FieldDeclarations } 
	| ArrayAllocationExpression { ArrayInitializers } 
	| ClassAllocationExpression { } 
	| ArrayAllocationExpression { } 
	| ClassAllocationExpression 
	| ArrayAllocationExpression 
	'''
	pass

def p_ClassAllocationExpression( p ):
	''' 
	ClassAllocationExpression :  NEW TypeName ( ) 
	| NEW TypeName ( ArgumentList ) 
	'''
	pass

def p_ArrayAllocationExpression( p ):
	''' 
	ArrayAllocationExpression :  NEW TypeName Dims 
	| NEW TypeName DimExprs 
	| NEW TypeName DimExprs Dims 
	'''
	pass

def p_DimExprs( p ):
	''' 
	DimExprs :  DimExprs DimExpr 
	| DimExpr 
	'''
	pass

def p_DimExpr( p ):
	''' 
	DimExpr :  [ Expression ] 
	'''
	pass

def p_Dims( p ):
	''' 
	Dims :  Dims OP_DIM 
	| OP_DIM 
	'''
	pass

def p_PostfixExpression( p ):
	''' 
	PostfixExpression :  RealPostfixExpression 
	| PrimaryExpression 
	'''
	pass

def p_RealPostfixExpression( p ):
	''' 
	RealPostfixExpression :  PostfixExpression OP_DEC 
	| PostfixExpression OP_INC 
	'''
	pass

def p_UnaryExpression( p ):
	''' 
	UnaryExpression :  LogicalUnaryExpression 
	| ArithmeticUnaryOperator CastExpression 
	| OP_DEC UnaryExpression 
	| OP_INC UnaryExpression 
	'''
	pass

def p_LogicalUnaryExpression( p ):
	''' 
	LogicalUnaryExpression :  LogicalUnaryOperator UnaryExpression 
	| PostfixExpression 
	'''
	pass

def p_LogicalUnaryOperator( p ):
	''' 
	LogicalUnaryOperator :  ! 
	| ~ 
	'''
	pass

def p_ArithmeticUnaryOperator( p ):
	''' 
	ArithmeticUnaryOperator :  - 
	| + 
	'''
	pass

def p_CastExpression( p ):
	''' 
	CastExpression :  ( Expression ) LogicalUnaryExpression 
	| ( ClassTypeExpression ) CastExpression 
	| ( PrimitiveTypeExpression ) CastExpression 
	| UnaryExpression 
	'''
	pass

def p_PrimitiveTypeExpression( p ):
	''' 
	PrimitiveTypeExpression :  PrimitiveType Dims 
	| PrimitiveType 
	'''
	pass

def p_ClassTypeExpression( p ):
	''' 
	ClassTypeExpression :  QualifiedName Dims 
	'''
	pass

def p_MultiplicativeExpression( p ):
	''' 
	MultiplicativeExpression :  MultiplicativeExpression % CastExpression 
	| MultiplicativeExpression / CastExpression 
	| MultiplicativeExpression * CastExpression 
	| CastExpression 
	'''
	pass

def p_AdditiveExpression( p ):
	''' 
	AdditiveExpression :  AdditiveExpression - MultiplicativeExpression 
	| AdditiveExpression + MultiplicativeExpression 
	| MultiplicativeExpression 
	'''
	pass

def p_ShiftExpression( p ):
	''' 
	ShiftExpression :  ShiftExpression OP_SHRR AdditiveExpression 
	| ShiftExpression OP_SHR AdditiveExpression 
	| ShiftExpression OP_SHL AdditiveExpression 
	| AdditiveExpression 
	'''
	pass

def p_RelationalExpression( p ):
	''' 
	RelationalExpression :  RelationalExpression INSTANCEOF TypeSpecifier 
	| RelationalExpression OP_GE ShiftExpression 
	| RelationalExpression OP_LE ShiftExpression 
	| RelationalExpression > ShiftExpression 
	| RelationalExpression < ShiftExpression 
	| ShiftExpression 
	'''
	pass

def p_EqualityExpression( p ):
	''' 
	EqualityExpression :  EqualityExpression OP_NE RelationalExpression 
	| EqualityExpression OP_EQ RelationalExpression 
	| RelationalExpression 
	'''
	pass

def p_AndExpression( p ):
	''' 
	AndExpression :  AndExpression & EqualityExpression 
	| EqualityExpression 
	'''
	pass

def p_ExclusiveOrExpression( p ):
	''' 
	ExclusiveOrExpression :  ExclusiveOrExpression ^ AndExpression 
	| AndExpression 
	'''
	pass

def p_InclusiveOrExpression( p ):
	''' 
	InclusiveOrExpression :  InclusiveOrExpression | ExclusiveOrExpression 
	| ExclusiveOrExpression 
	'''
	pass

def p_ConditionalAndExpression( p ):
	''' 
	ConditionalAndExpression :  ConditionalAndExpression OP_LAND InclusiveOrExpression 
	| InclusiveOrExpression 
	'''
	pass

def p_ConditionalOrExpression( p ):
	''' 
	ConditionalOrExpression :  ConditionalOrExpression OP_LOR ConditionalAndExpression 
	| ConditionalAndExpression 
	'''
	pass

def p_ConditionalExpression( p ):
	''' 
	ConditionalExpression :  ConditionalOrExpression ? Expression : ConditionalExpression 
	| ConditionalOrExpression 
	'''
	pass

def p_AssignmentExpression( p ):
	''' 
	AssignmentExpression :  UnaryExpression AssignmentOperator AssignmentExpression 
	| ConditionalExpression 
	'''
	pass

def p_AssignmentOperator( p ):
	''' 
	AssignmentOperator :  ASS_OR 
	| ASS_XOR 
	| ASS_AND 
	| ASS_SHRR 
	| ASS_SHR 
	| ASS_SHL 
	| ASS_SUB 
	| ASS_ADD 
	| ASS_MOD 
	| ASS_DIV 
	| ASS_MUL 
	| = 
	'''
	pass

def p_Expression( p ):
	''' 
	Expression :  AssignmentExpression 
	'''
	pass

def p_ConstantExpression( p ):
	''' 
	ConstantExpression :  ConditionalExpression 
	'''
	pass

