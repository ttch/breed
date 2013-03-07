# *.* coding = utf-8 *.*
import ply.yacc as yacc
import breed_lex

from collections import deque
import function_

tokens = breed_lex.tokens

precedence = (
)

component = {}
importlist = []
function_list = {}
stack = deque()

#--------------------------main statment---------------------------
def p_statment( p ):
	""" statment : component_statment import_statements at_statments
	"""
	pass


#-----------------------component statment-------------------------
def p_component_statment(p):
	'component_statment : COMPONENT ID'
	component[p[2]] = ""
	pass

#--------------------------import statment-------------------------
def p_import_statements( p ):
	"""import_statements : import_statement
	| import_statements import_statement
	"""
	pass

def p_import_statement(p):
	'import_statement : IMPORT qualified_name SEMI'
	importlist.append(deque(stack))
	stack.clear()
	pass


#--------------------------@ statment---------------------------

def p_at_statments(p):
	""" at_statments : at_statment
		| at_statments at_statment
	"""
	pass


def p_at_statment(p):
	''' at_statment : AT at_operater_statment at_end_statment
	'''
	pass

def p_at_operater_statment( p ):
	''' at_operater_statment : FUNCTION function_statments
		| FUNCTION
		| DEFINE define_statments
		| DEFINE
	'''
	pass

def p_at_end_statment( p ):
	' at_end_statment : AT END'
	pass
#--------------------------define statment-----------------------

def p_define_statments( p ):
	''' define_statments : interface_statments
	'''
	print "interface_statments ",p[1]
	pass

def p_interface_statments( p ):
	''' interface_statments : interface_statment
							| interface_statments interface_statment
	'''
	pass

def p_interface_statment( p ):
	'''
		interface_statment : INTERFACE ID LPAREN RPAREN BLPAREN interface_declare_statments BRPAREN
							| INTERFACE ID LPAREN RPAREN BLPAREN BRPAREN
	'''
	print "interface ID is " , p[2]
	pass

def p_interface_declare_statments( p ):
	'''
		interface_declare_statments : field_declare
									| interface_declare_statments field_declare
									| function_declare
									| interface_declare_statments function_declare
	'''
	pass

def p_field_declare( p ):
	'''
		field_declare : type_specifier declarator_name SEMI
	'''

def p_function_declare ( p ):
	'''
		function_declare : FUNC ID ID SEMI
	'''

#--------------------------function statment---------------------

def p_function_statments( p ):
	""" function_statments : function_statment
	| function_statments function_statment """
	pass

def p_function_statment( p ):
	'''
		function_statment : FUNC function_declarator BLPAREN BRPAREN
	'''
	print '====================='
	pass

def p_function_declarator(p):
	"""
		function_declarator : ID LPAREN function_paras RPAREN
	"""
	print 'function name is ' , p[1]
	pass

def p_function_paras(p):
	'''
		function_paras : function_para
						| function_paras function_para
	'''
	pass

def p_function_para( p ):
	'''
		function_para : FLPAREN function_para_action FRPAREN type_specifier declarator_name
						| function_para COMMA function_para
	'''
	pass

def p_function_para_action( p ):
	'''
		function_para_action : IN
		| OUT
		| RETURN
		| IN_OUT
	'''
	print p[1]
	pass

#--------------------type and declare qualified name (common) statment--------------------
def p_type_specifier(p):
	'type_specifier : qualified_name '
	print "type is:", deque(stack)
	stack.clear()
	pass

def p_declarator_name(p):
	'declarator_name : ID '
	print "declarator name is " , p[1]
	pass

def p_qualified_name(p):
	"""qualified_name : ID
	| qualified_name DOT ID
	"""
	if len(p) == 2:
		stack.append(p[1])
	if len(p)== 4:
		stack.append(p[3])
	pass



#### Empty
   
def p_empty(p):
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
	print component
	print importlist
	if b.error : return None
