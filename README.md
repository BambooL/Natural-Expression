# let_language_for_Regex
This is a simple let language for the Regex construction

## let_language
Let-Language is a context-free language designed for Regex construction which simplifies 
the process as well lower the comprehension bar. For example, to build a Regex like this:
'''^( ( \d { 2 }  ) | [a-zA-Z]+ )'''
you may write a script using let-Language like this:
'''
let _a be digit
let _b be repeat 2 _a
let _c be word
let _d be or _b _c
let _e be not _d
'''

### syntax
The syntax of Let-Language is elaborated in BNF(Backus–Naur Form)
```
assign ::= LET NAME BE expr
expr ::= REPEAT NUMBER expr
       | OR expr expr
       | NOT expr
       | CONCAT expr expr
       | term
term ::= DIGIT
       | WORD
       | CHAR
       | CONST
```

### Inplementation
Let-Language is build upon PLY(Python Lex-Yacc). 
