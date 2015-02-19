# let_language_for_Regex
This is a simple let language for the Regex construction

## let_language
Let-Language is a context-free language designed for Regex construction which simplifies 
the process as well lower the comprehension bar. For example, to build a Regex like this:
```
^( ( \d { 2 }  ) | [a-zA-Z]+ )
```
you may write a script using let-Language like this:
```
let _a be digit
let _b be repeat 2 _a
let _c be word
let _d be or _b _c
let _e be not _d
```

### syntax
The syntax of Let-Language is elaborated in BNF(Backus–Naur Form)
```
assign ::= LET NAME BE expr
expr ::= REPEAT NUMBER expr
	   | REPEAT ONEMORE expr
	   | REPEAT ZEROMORE expr
       | OR expr expr
       | NOT expr
       | CONCAT expr expr
       | expr END expr
       | expr HAS expr
       | expr BEGIN expr
       | term
term ::= DIGIT
       | WORD
       | CHAR
       | CONST
       | BLANK
       | LETTER
       | LOWCASE
       | UPCASE
       | NUMBER TO NUMBER
```

### Inplementation
Let-Language is build upon PLY(Python Lex-Yacc). 

### Demo

* To generate a normal regular expression (let/first.let)
```
let _a be digit
let _b be repeat 2 _a
let _c be word
let _d be or _b _c
let _e be char
let _f be one of 1-8
let _g be repeat zeromore _f
let _h be _d and _e
let _i be or _h _g
let _j be word end "er"
let _k be repeat zeromore lowcase
let _l be word has 3 one of "aeiou"
let _m be word begin "aaa"
let _n be or _j _l
let _o be _k and _m
let _p be repeat zeromore _o
let _q be _n and _p and _i
```
The regular expression generated(_q):
```
( ( \b[a-zA-Z]*er\b ) | ( \b[a-zA-Z]*[aeiou]{3}[a-zA-Z]*\b ) )[a-z]*( \baaa[a-zA-Z]*\b )*( ( \d { 2 }  | \b[a-zA-Z]+\b )\w | [1-8]* )
```

* To generate Protein Match (let/bio.let) for (FGFs) fgf(\s+|-)*\d+
```
let _part1 be "fgf"
let _part2 be repeat onemore blank 
let _part3 be or _part2 "-"
let _part4 be repeat zeromore _part3
let _part5 be repeat onemore digit
let _expression be _part1 and _part3 and _part5
```
The regular expression generated(_expression):
```
fgf( \s+ | - )\d+
```

* To generate DNA sequence (let/dna.let) to match nucleotide sequence
```
let _part1 be "AC"
let _part2 be one of "ATW"
let _part3 be "T"
let _part4 be one of "ACM"
let _part5 be "A"
let _part6 be one of "ACGTRYKMSWBDHVN"
let _expression be _part1 and _part2 and _part3 and _part4 and _part5 and _part6
```
The regular expression generated(_expression):
```
AC[ATW]T[ACM]A[ACGTRYKMSWBDHVN]
```
