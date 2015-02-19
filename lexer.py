import lex 



tokens = [ 'LET', 'BE', 'NAME', 'REPEAT', 'OR', 'NOT', 'CONCAT', 'DIGIT', 'CHAR', 'LETTER', 'WORD', 'CONST', 'NUMBER', 'LOWCASE', 'UPCASE', 'PRINT', 'SEVERAL', 'TO', 'ONEOF', 'AND', 'END', 'BEGIN', 'HAS' ]

t_ignore = r' \t'
t_LET = r'[l|L][e|E][t|T]'
t_BE = r'[b|B][e|E]'
t_REPEAT = r'[r|R][e|E][p|P][e|E][a|A][t|T]'
t_OR = r'[o|O][r|R]'
t_NOT = r'[n|N][o|O][t|T]'
t_CONCAT = r'[c|C][o|O][n|N][c|C][a|A][t|T]'
t_AND = r'[a|A][n|N][d|D]'
t_ONEOF = r'[o|O][n|N][e|E][\s|][o|O][f|F]'
t_PRINT = r'[p|P][r|R][i|I][n|N][t|T]'
t_END = r'[e|E][n|N][d|D]'
t_BEGIN = r'[b|B][e|E][G|g][i|I][n|N]'
t_HAS = r'[h|H][a|A][s|S]'
t_LOWCASE = r'[l|L][o|O][w|W][c|C][a|A][s|S][e|E]'
t_UPCASE = r'[u|U][p|P][c|C][a|A][s|S][e|E]'
t_SEVERAL = r'[s|S][e|E][v|V][e|E][r|R][a|A][l|L]'
t_TO = r'([t|T][o|O])|\-'
t_DIGIT = r'[d|D][i|I][g|G][i|I][t|T]'
t_CHAR = r'[c|C][h|H][a|A][r|R]'
t_LETTER = r'[l|L][e|E][t|T][t|T][e|E][r|R]'
t_WORD = r'[w|W][o|O][r|R][d|D]'
t_NAME = r'[_][a-zA-Z0-9_]*'
t_CONST = r'(\".*\")'
t_NUMBER = r'\d+'



lex.lex() # Build the lexer


