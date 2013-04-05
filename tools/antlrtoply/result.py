def p_type_specifier( p ):
	''' 
	type_specifier :  type_name dims 
	| type_name 
	'''
	pass

def p_type_name( p ):
	''' 
	type_name :  qualified_name 
	| primitive_type 
	'''
	pass

def p_class_name_list( p ):
	''' 
	class_name_list :  class_name_list COMMA qualified_name 
	| qualified_name 
	'''
	pass

def p_primitive_type( p ):
	''' 
	primitive_type :  VOID 
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

def p_compilation_unit( p ):
	''' 
	compilation_unit :  program_file 
	'''
	pass

def p_program_file( p ):
	''' 
	program_file :  type_declarations 
	| import_statements 
	| package_statement 
	| import_statements type_declarations 
	| package_statement type_declarations 
	| package_statement import_statements 
	| package_statement import_statements type_declarations 
	'''
	pass

def p_package_statement( p ):
	''' 
	package_statement :  PACKAGE qualified_name SEMI 
	'''
	pass

def p_type_declarations( p ):
	''' 
	type_declarations :  type_declarations type_declaration 
	| type_declaration 
	'''
	pass

def p_import_statements( p ):
	''' 
	import_statements :  import_statements import_statement 
	| import_statement 
	'''
	pass

def p_import_statement( p ):
	''' 
	import_statement :  IMPORT qualified_name DOT MULT SEMI 
	| IMPORT qualified_name SEMI 
	'''
	pass

def p_qualified_name( p ):
	''' 
	qualified_name :  qualified_name DOT IDENTIFIER 
	| IDENTIFIER 
	'''
	pass

def p_type_declaration( p ):
	''' 
	type_declaration :  class_header BLPAREN BRPAREN 
	| class_header BLPAREN field_declarations BRPAREN 
	'''
	pass

def p_class_header( p ):
	''' 
	class_header :  class_word IDENTIFIER 
	| class_word IDENTIFIER interfaces 
	| class_word IDENTIFIER extends 
	| modifiers class_word IDENTIFIER 
	| class_word IDENTIFIER extends interfaces 
	| modifiers class_word IDENTIFIER interfaces 
	| modifiers class_word IDENTIFIER extends 
	| modifiers class_word IDENTIFIER extends interfaces 
	'''
	pass

def p_modifiers( p ):
	''' 
	modifiers :  modifiers modifier 
	| modifier 
	'''
	pass

def p_modifier( p ):
	''' 
	modifier :  SYNCHRONIZED 
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

def p_class_word( p ):
	''' 
	class_word :  INTERFACE 
	| CLASS 
	'''
	pass

def p_interfaces( p ):
	''' 
	interfaces :  IMPLEMENTS class_name_list 
	'''
	pass

def p_field_declarations( p ):
	''' 
	field_declarations :  field_declarations field_declaration 
	| field_declaration 
	'''
	pass

def p_field_declaration( p ):
	''' 
	field_declaration :  type_declaration 
	| non_static_initializer 
	| static_initializer 
	| constructor_declaration 
	| method_declaration 
	| field_variable_declaration SEMI 
	'''
	pass

def p_field_variable_declaration( p ):
	''' 
	field_variable_declaration :  type_specifier variable_declarators 
	| modifiers type_specifier variable_declarators 
	'''
	pass

def p_variable_declarators( p ):
	''' 
	variable_declarators :  variable_declarators COMMA variable_declarator 
	| variable_declarator 
	'''
	pass

def p_variable_declarator( p ):
	''' 
	variable_declarator :  declarator_name EQUALS variable_initializer 
	| declarator_name 
	'''
	pass

def p_variable_initializer( p ):
	''' 
	variable_initializer :  BLPAREN array_initializers BRPAREN 
	| BLPAREN BRPAREN 
	| expression 
	'''
	pass

def p_array_initializers( p ):
	''' 
	array_initializers :  array_initializers COMMA 
	| array_initializers COMMA variable_initializer 
	| variable_initializer 
	'''
	pass

def p_method_declaration( p ):
	''' 
	method_declaration :  type_specifier method_declarator method_body 
	| type_specifier method_declarator throws method_body 
	| modifiers type_specifier method_declarator method_body 
	| modifiers type_specifier method_declarator throws method_body 
	'''
	pass

def p_method_declarator( p ):
	''' 
	method_declarator :  method_declarator OP_DIM 
	| declarator_name LPAREN RPAREN 
	| declarator_name LPAREN parameter_list RPAREN 
	'''
	pass

def p_parameter_list( p ):
	''' 
	parameter_list :  parameter_list COMMA parameter 
	| parameter 
	'''
	pass

def p_parameter( p ):
	''' 
	parameter :  type_specifier declarator_name 
	'''
	pass

def p_declarator_name( p ):
	''' 
	declarator_name :  declarator_name OP_DIM 
	| IDENTIFIER 
	'''
	pass

def p_throws( p ):
	''' 
	throws :  THROWS class_name_list 
	'''
	pass

def p_method_body( p ):
	''' 
	method_body :  SEMI 
	| block 
	'''
	pass

def p_constructor_declaration( p ):
	''' 
	constructor_declaration :  constructor_declarator block 
	| constructor_declarator throws block 
	| modifiers constructor_declarator block 
	| modifiers constructor_declarator throws block 
	'''
	pass

def p_constructor_declarator( p ):
	''' 
	constructor_declarator :  IDENTIFIER LPAREN RPAREN 
	| IDENTIFIER LPAREN parameter_list RPAREN 
	'''
	pass

def p_static_initializer( p ):
	''' 
	static_initializer :  STATIC block 
	'''
	pass

def p_non_static_initializer( p ):
	''' 
	non_static_initializer :  block 
	'''
	pass

def p_extends( p ):
	''' 
	extends :  extends COMMA type_name 
	| EXTENDS type_name 
	'''
	pass

def p_block( p ):
	''' 
	block :  BLPAREN BRPAREN 
	| BLPAREN local_variable_declarations_and_statements BRPAREN 
	'''
	pass

def p_local_variable_declarations_and_statements( p ):
	''' 
	local_variable_declarations_and_statements :  local_variable_declarations_and_statements local_variable_declaration_or_statement 
	| local_variable_declaration_or_statement 
	'''
	pass

def p_local_variable_declaration_or_statement( p ):
	''' 
	local_variable_declaration_or_statement :  statement 
	| local_variable_declaration_statement 
	'''
	pass

def p_local_variable_declaration_statement( p ):
	''' 
	local_variable_declaration_statement :  type_specifier variable_declarators SEMI 
	'''
	pass

def p_statement( p ):
	''' 
	statement :  block 
	| guarding_statement 
	| jump_statement 
	| iteration_statement 
	| selection_statement 
	| expression_statement SEMI 
	| labeled_statement 
	| empty_statement 
	'''
	pass

def p_empty_statement( p ):
	''' 
	empty_statement :  SEMI 
	'''
	pass

def p_labeled_statement( p ):
	''' 
	labeled_statement :  DEFAULT COLON local_variable_declaration_or_statement 
	| CASE constant_expression COLON local_variable_declaration_or_statement 
	| IDENTIFIER COLON local_variable_declaration_or_statement 
	'''
	pass

def p_expression_statement( p ):
	''' 
	expression_statement :  expression 
	'''
	pass

def p_selection_statement( p ):
	''' 
	selection_statement :  SWITCH LPAREN expression RPAREN block 
	| IF LPAREN expression RPAREN statement ELSE statement 
	| IF LPAREN expression RPAREN statement 
	'''
	pass

def p_iteration_statement( p ):
	''' 
	iteration_statement :  FOR LPAREN for_init for_expr RPAREN statement 
	| FOR LPAREN for_init for_expr for_incr RPAREN statement 
	| DO statement WHILE LPAREN expression RPAREN SEMI 
	| WHILE LPAREN expression RPAREN statement 
	'''
	pass

def p_for_init( p ):
	''' 
	for_init :  SEMI 
	| local_variable_declaration_statement 
	| expression_statements SEMI 
	'''
	pass

def p_for_expr( p ):
	''' 
	for_expr :  SEMI 
	| expression SEMI 
	'''
	pass

def p_for_incr( p ):
	''' 
	for_incr :  expression_statements 
	'''
	pass

def p_expression_statements( p ):
	''' 
	expression_statements :  expression_statements COMMA expression_statement 
	| expression_statement 
	'''
	pass

def p_jump_statement( p ):
	''' 
	jump_statement :  THROW expression SEMI 
	| RETURN SEMI 
	| RETURN expression SEMI 
	| CONTINUE SEMI 
	| CONTINUE IDENTIFIER SEMI 
	| BREAK SEMI 
	| BREAK IDENTIFIER SEMI 
	'''
	pass

def p_guarding_statement( p ):
	''' 
	guarding_statement :  TRY block catches finally 
	| TRY block catches 
	| TRY block finally 
	| SYNCHRONIZED LPAREN expression RPAREN statement 
	'''
	pass

def p_catches( p ):
	''' 
	catches :  catches catch 
	| catch 
	'''
	pass

def p_catch( p ):
	''' 
	catch :  catch_header block 
	'''
	pass

def p_catch_header( p ):
	''' 
	catch_header :  CATCH LPAREN type_specifier RPAREN 
	| CATCH LPAREN type_specifier IDENTIFIER RPAREN 
	'''
	pass

def p_finally( p ):
	''' 
	finally :  FINALLY block 
	'''
	pass

def p_primary_expression( p ):
	''' 
	primary_expression :  not_just_name 
	| qualified_name 
	'''
	pass

def p_not_just_name( p ):
	''' 
	not_just_name :  complex_primary 
	| new_allocation_expression 
	| special_name 
	'''
	pass

def p_complex_primary( p ):
	''' 
	complex_primary :  complex_primary_no_parenthesis 
	| LPAREN expression RPAREN 
	'''
	pass

def p_complex_primary_no_parenthesis( p ):
	''' 
	complex_primary_no_parenthesis :  method_call 
	| field_access 
	| array_access 
	| BOOLLIT 
	| LITERAL 
	'''
	pass

def p_array_access( p ):
	''' 
	array_access :  complex_primary FLPAREN expression FRPAREN 
	| qualified_name FLPAREN expression FRPAREN 
	'''
	pass

def p_field_access( p ):
	''' 
	field_access :  real_postfix_expression DOT IDENTIFIER 
	| not_just_name DOT IDENTIFIER 
	'''
	pass

def p_method_call( p ):
	''' 
	method_call :  method_access LPAREN RPAREN 
	| method_access LPAREN argument_list RPAREN 
	'''
	pass

def p_method_access( p ):
	''' 
	method_access :  qualified_name 
	| special_name 
	| complex_primary_no_parenthesis 
	'''
	pass

def p_special_name( p ):
	''' 
	special_name :  JNULL 
	| SUPER 
	| THIS 
	'''
	pass

def p_argument_list( p ):
	''' 
	argument_list :  argument_list COMMA expression 
	| expression 
	'''
	pass

def p_new_allocation_expression( p ):
	''' 
	new_allocation_expression :  class_allocation_expression BLPAREN field_declarations BRPAREN 
	| array_allocation_expression BLPAREN array_initializers BRPAREN 
	| class_allocation_expression BLPAREN BRPAREN 
	| array_allocation_expression BLPAREN BRPAREN 
	| class_allocation_expression 
	| array_allocation_expression 
	'''
	pass

def p_class_allocation_expression( p ):
	''' 
	class_allocation_expression :  NEW type_name LPAREN RPAREN 
	| NEW type_name LPAREN argument_list RPAREN 
	'''
	pass

def p_array_allocation_expression( p ):
	''' 
	array_allocation_expression :  NEW type_name dims 
	| NEW type_name dim_exprs 
	| NEW type_name dim_exprs dims 
	'''
	pass

def p_dim_exprs( p ):
	''' 
	dim_exprs :  dim_exprs dim_expr 
	| dim_expr 
	'''
	pass

def p_dim_expr( p ):
	''' 
	dim_expr :  FLPAREN expression FRPAREN 
	'''
	pass

def p_dims( p ):
	''' 
	dims :  dims OP_DIM 
	| OP_DIM 
	'''
	pass

def p_postfix_expression( p ):
	''' 
	postfix_expression :  real_postfix_expression 
	| primary_expression 
	'''
	pass

def p_real_postfix_expression( p ):
	''' 
	real_postfix_expression :  postfix_expression OP_DEC 
	| postfix_expression OP_INC 
	'''
	pass

def p_unary_expression( p ):
	''' 
	unary_expression :  logical_unary_expression 
	| arithmetic_unary_operator cast_expression 
	| OP_DEC unary_expression 
	| OP_INC unary_expression 
	'''
	pass

def p_logical_unary_expression( p ):
	''' 
	logical_unary_expression :  logical_unary_operator unary_expression 
	| postfix_expression 
	'''
	pass

def p_logical_unary_operator( p ):
	''' 
	logical_unary_operator :  EXCLAMATION 
	| TILDE 
	'''
	pass

def p_arithmetic_unary_operator( p ):
	''' 
	arithmetic_unary_operator :  DASH 
	| PLUS 
	'''
	pass

def p_cast_expression( p ):
	''' 
	cast_expression :  LPAREN expression RPAREN logical_unary_expression 
	| LPAREN class_type_expression RPAREN cast_expression 
	| LPAREN primitive_type_expression RPAREN cast_expression 
	| unary_expression 
	'''
	pass

def p_primitive_type_expression( p ):
	''' 
	primitive_type_expression :  primitive_type dims 
	| primitive_type 
	'''
	pass

def p_class_type_expression( p ):
	''' 
	class_type_expression :  qualified_name dims 
	'''
	pass

def p_multiplicative_expression( p ):
	''' 
	multiplicative_expression :  multiplicative_expression PERCENT cast_expression 
	| multiplicative_expression SLASH cast_expression 
	| multiplicative_expression MULT cast_expression 
	| cast_expression 
	'''
	pass

def p_additive_expression( p ):
	''' 
	additive_expression :  additive_expression DASH multiplicative_expression 
	| additive_expression PLUS multiplicative_expression 
	| multiplicative_expression 
	'''
	pass

def p_shift_expression( p ):
	''' 
	shift_expression :  shift_expression OP_SHRR additive_expression 
	| shift_expression OP_SHR additive_expression 
	| shift_expression OP_SHL additive_expression 
	| additive_expression 
	'''
	pass

def p_relational_expression( p ):
	''' 
	relational_expression :  relational_expression INSTANCEOF type_specifier 
	| relational_expression OP_GE shift_expression 
	| relational_expression OP_LE shift_expression 
	| relational_expression MORE shift_expression 
	| relational_expression LESS shift_expression 
	| shift_expression 
	'''
	pass

def p_equality_expression( p ):
	''' 
	equality_expression :  equality_expression OP_NE relational_expression 
	| equality_expression OP_EQ relational_expression 
	| relational_expression 
	'''
	pass

def p_and_expression( p ):
	''' 
	and_expression :  and_expression AND equality_expression 
	| equality_expression 
	'''
	pass

def p_exclusive_or_expression( p ):
	''' 
	exclusive_or_expression :  exclusive_or_expression CARET and_expression 
	| and_expression 
	'''
	pass

def p_inclusive_or_expression( p ):
	''' 
	inclusive_or_expression :  inclusive_or_expression VERTICAL exclusive_or_expression 
	| exclusive_or_expression 
	'''
	pass

def p_conditional_and_expression( p ):
	''' 
	conditional_and_expression :  conditional_and_expression OP_LAND inclusive_or_expression 
	| inclusive_or_expression 
	'''
	pass

def p_conditional_or_expression( p ):
	''' 
	conditional_or_expression :  conditional_or_expression OP_LOR conditional_and_expression 
	| conditional_and_expression 
	'''
	pass

def p_conditional_expression( p ):
	''' 
	conditional_expression :  conditional_or_expression QUES expression COLON conditional_expression 
	| conditional_or_expression 
	'''
	pass

def p_assignment_expression( p ):
	''' 
	assignment_expression :  unary_expression assignment_operator assignment_expression 
	| conditional_expression 
	'''
	pass

def p_assignment_operator( p ):
	''' 
	assignment_operator :  ASS_OR 
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
	| EQUALS 
	'''
	pass

def p_expression( p ):
	''' 
	expression :  assignment_expression 
	'''
	pass

def p_constant_expression( p ):
	''' 
	constant_expression :  conditional_expression 
	'''
	pass

