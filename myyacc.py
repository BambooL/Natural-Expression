import yacc
import lexer # Import lexer information

tokens = lexer.tokens # Need token list
names = { }

def p_assign(p):
	'''assign : LET NAME BE expr'''
	names[p[2]] = p[4]

# def p_print(p):
# 	'show : PRINT expr'
# 	if (names[p[2]]):
# 		print names[p[2]]
# 	else:
# 		print "Sorry, no this value!"

def p_expr_repeat(p):
	'expr : REPEAT NUMBER expr'
	p[0] = '( ' + p[3] + " { " + p[2] + " } " + " )"

def p_expr_repeat_several(p):
	'expr : REPEAT SEVERAL expr'
	p[0] = '( ' + p[3] + "*" + " )"

def p_expr_repeat_range(p):
	'expr : REPEAT NUMBER TO NUMBER expr'
	p[0] = '( ' + p[5] + "{" + p[2] + "," + p[3] + "}" + " )"

def p_expr_and(p):
	'expr : expr AND expr'
	p[0] = p[1] + p[3] 

def p_expr_or(p):
	'expr : OR expr expr'
	p[0] = '( ' + p[2] + " | " + p[3] + " )"

def p_expr_concat(p):
	'expr : CONCAT expr expr'
	p[0] = p[2] + p[3]

def p_expr_not(p):
	'expr : NOT expr'
	p[0] = '( ' + '^' + p[2] + " )"

def p_expr_to(p):
	'expr : ONEOF NUMBER TO NUMBER'
	p[0] = '[' + p[2] + '-' + p[4] + ']'

def p_expr_term(p):
	'expr : term'
	p[0] = p[1] 

def p_expr_word_end(p):
	'expr : WORD END expr'
	if (p[3][0] == "\"" and p[3][-1] == "\""):
		p[3] = p[3][1:-1]
	p[0] = '( ' + '\\b[a-zA-Z]*' + p[3] + '\\b' + " )"

def p_expr_word_has(p):
	'expr : WORD HAS term'
	if (p[3][0] == "\"" and p[3][-1] == "\""):
		p[3] = p[3][1:-1]
	p[0] = '( ' + '\\b[a-zA-Z]*' + p[3] + '[a-zA-Z]*\\b' + " )"

def p_expr_word_has(p):
	'expr : WORD HAS NUMBER term'
	if (p[4][0] == "\"" and p[4][-1] == "\""):
		p[4] = p[4][1:-1]
	p[0] = '( ' + '\\b[a-zA-Z]*' + p[4] + '{' + p[3] + '}' + '[a-zA-Z]*\\b' + " )"

def p_expr_word_begin(p):
	'expr : WORD BEGIN expr'
	if (p[3][0] == "\"" and p[3][-1] == "\""):
		p[3] = p[3][1:-1]
	p[0] = '( ' + '\\b' + p[3] + '[a-zA-Z]*' + '\\b' + " )"


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

def p_term_letter(p):
	'term : LETTER'
	p[0] = '[a-zA-Z]'

def p_term_up_letter(p):
	'term : UPCASE'
	p[0] = '[A-Z]'

def p_term_low_letter(p):
	'term : LOWCASE'
	p[0] = '[a-z]'

def p_term_word(p):
	'term : WORD'
	p[0] = '\\b[a-zA-Z]+\\b'

def p_term_CONST(p):
	'term : CONST'
	p[1] = p[1][1:-1]
	p[0] = p[1]

def p_term_oneof(p):
	'term : ONEOF CONST'
	if (p[2][0] == "\"" and p[2][-1] == "\""):
		p[2] = p[2][1:-1]
	p[0] = '[' + p[2] + ']'

def p_error(p):
    print("Syntax error at '%s'" % p.value)




yacc.yacc() # Build the parser
