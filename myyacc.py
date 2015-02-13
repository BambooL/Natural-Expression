import yacc
import lexer # Import lexer information

tokens = lexer.tokens # Need token list
names = { }

def p_assign(p):
	'''assign : LET NAME BE expr'''
	names[p[2]] = p[4]

def p_print(p):
	'show : PRINT expr'
	if (names[p[2]]):
		print names[p[2]]
	else:
		print "Sorry, no this value!"


# def p_expr(p):
# 	'''expr : REPEAT NUMBER expr
# 	| OR expr expr
# 	| CONCAT expr expr
# 	| term'''

def p_expr_repeat(p):
	'expr : REPEAT NUMBER expr'
	p[0] = '( ' + p[3] + " { " + p[2] + " } " + " )"

def p_expr_or(p):
	'expr : OR expr expr'
	p[0] = '( ' + p[2] + " | " + p[3] + " )"

def p_expr_concat(p):
	'expr : CONCAT expr expr'
	p[0] = '( ' + p[2] + p[3] + " )"

def p_expr_not(p):
	'expr : NOT expr'
	p[0] = '^' + p[2]

def p_expr_term(p):
	'expr : term'
	p[0] = p[1]

# def p_term(p):
# 	'''term : DIGIT
# 	| CHAR
# 	| WORD
# 	| CONST'''
# 	if (p[1] == 'digit'):
# 		p[0] = '\\d'
# 	elif (p[1] == 'char'):
# 		p[0] = '\w'
# 	elif (p[1] == 'word'):
# 		p[0] = '[a-zA-Z]+'
# 	else:
# 		p[0] = p[1]
def p_term_name(p):
	'term : NAME'
	if (names[p[1]]):
		p[0] = names[p[1]]
	else:
		p[0] = p[1] 

def p_term_digit(p):
	'term : DIGIT'
	p[0] = '\\d'

def p_term_char(p):
	'term : CHAR'
	p[0] = '\w'

def p_term_word(p):
	'term : WORD'
	p[0] = '[a-zA-Z]+'

def p_term_CONST(p):
	'term : CONST'
	p[0] = p[1]

def p_error(p):
    print("Syntax error at '%s'" % p.value)




yacc.yacc() # Build the parser
