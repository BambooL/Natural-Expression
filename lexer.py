import lex 



tokens = [ 'LET', 'BE', 'NAME', 'REPEAT', 'OR', 'NOT', 'CONCAT', 'DIGIT', 'CHAR', 'WORD', 'CONST', 'NUMBER', 'PRINT', 'SEVERAL', 'TO', 'ONEOF' ]

t_ignore = r' \t'
t_LET = r'[l|L][e|E][t|T]'
t_BE = r'[b|B][e|E]'
t_REPEAT = r'[r|R][e|E][p|P][e|E][a|A][t|T]'
t_OR = r'[o|O][r|R]'
t_NOT = r'[n|N][o|O][t|T]'
t_CONCAT = r'[c|C][o|O][n|N][c|C][a|A][t|T]'
t_ONEOF = r'[o|O][n|N][e|E][\s|][o|O][f|F]'
t_PRINT = r'[p|P][r|R][i|I][n|N][t|T]'
t_SEVERAL = r'[s|S][e|E][v|V][e|E][r|R][a|A][l|L]'
t_TO = r'([t|T][o|O])|\-'
t_DIGIT = r'[d|D][i|I][g|G][i|I][t|T]'
t_CHAR = r'[c|C][h|H][a|A][r|R]'
t_WORD = r'[w|W][o|O][r|R][d|D]'
t_NAME = r'[_][a-zA-Z0-9_]*'
t_CONST = r'(\".*\")'
t_NUMBER = r'\d+'


lex.lex() # Build the lexer


