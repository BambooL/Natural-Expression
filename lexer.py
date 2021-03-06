import lex 



tokens = [ 'LSCOPE', 'RSCOPE', 'RETURN', 'IN', 'LET', 'BE', 'NAME', 'REPEAT', 'OR', 'NOT', 'CONCAT', 'DIGIT', 'CHAR', 'LETTER', 'WORD', 'CONST', 'NUMBER', 'BLANK', 'LOWCASE', 'UPCASE', 'PRINT', 'ONEMORE','ONEZERO', 'ZEROMORE', 'TO', 'ONEOF', 'AND', 'END', 'BEGIN', 'HAS', 'EXIST', 'EXACT' ]

t_ignore = r' \t'
t_RETURN = r'(\n\r|\n|\r)'
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
t_EXIST = r'[e|E][x|X][i|I][s|S][t|T]'
t_EXACT = r'[e|E][x|X][a|A][c|C][t|T]'
t_LOWCASE = r'[l|L][o|O][w|W][c|C][a|A][s|S][e|E]'
t_UPCASE = r'[u|U][p|P][c|C][a|A][s|S][e|E]'
t_BLANK = r'[b|B][l|L][a|A][n|N][k|K][s|S|\s]'
t_ONEMORE = r'[o|O][n|N][e|E][m|M][o|O][r|R][e|E]'
t_ZEROMORE = r'[z|Z][e|E][r|R][o|O][m|M][o|O][r|R][e|E]'
t_ONEZERO = r'[o|O][n|N][e|E][z|Z][e|E][r|R][o|O]'
t_TO = r'[t|T][o|O]'
t_DIGIT = r'[d|D][i|I][g|G][i|I][t|T]'
t_CHAR = r'[c|C][h|H][a|A][r|R]'
t_LETTER = r'[l|L][e|E][t|T][t|T][e|E][r|R]'
t_WORD = r'[w|W][o|O][r|R][d|D]'
t_NAME = r'[_][a-zA-Z0-9_]*'
t_CONST = r'[\"\'][^\"\']*[\"\']'
t_NUMBER = r'\d+'
# t_IN = r'[i|I][n|N]'
# t_LSCOPE = r'[\[\{]'
# t_RSCOPE = r'[\]\}]'





lex.lex() # Build the lexer


