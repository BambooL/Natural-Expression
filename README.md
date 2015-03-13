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
let _expression be _part1 and _part4 and _part5
```
The regular expression generated(_expression):
```
fgf( \s+ | - )*\d+
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

## Testcases from regex101
* url
```
let _header be 'http" and ONEZERO "s" and "://"
let _domainname be "regex.com"
let _next be "/r/"
let _validcharacter be letter or digit 
let _id be REPEAT 1 TO 6 _validcharacter 
let _url be _header and _domainname and _next and _id

```
The regular expression generated(_url):
```
https?://regex.com/r/( ( [a-zA-Z] | \d ){1,6} )
```

* distorted_email
```
let _character be "-" or letter or digit or "\."
let _Username be repeat onemore _character
let _option1 be repeat onemore blanks and "at" and repeat onemore blanks
let _option2 be repeat zeromore blanks and "@" and repeat zeromore blanks
let _option3 be repeat zeromore blanks and repeat 3 one of "\[\]@" and repeat zeromore blanks
let _part2 be _option1 or _option2 or _option3
let _domain be repeat onemore _character
let _blanks be repeat zeromore blanks
let _each be one of "\[\]dot\."
let _option be repeat 3 TO 5 _each
let _part5 be "dot" or "\." or _option
let _TLD be repeat onemore char
let _email be _Username and _part2 and _domain and _blanks and _part5 and _blanks and _TLD
```
The regular expression generated(_email):
```
( - | ( [a-zA-Z] | ( \d | \. ) ) )+( \sat\s++ | ( \s@\s** | \s[\[\]@]\s* { 3 } * ) )( - | ( [a-zA-Z] | ( \d | \. ) ) )+\s*( dot | ( \. | ( [\[\]dot\.]{3,5} ) ) )\s*\w+
```

* torrent
```
let _each be "-" or char
let _separator be " " or "."
let _unit1 be repeat onemore _each
let _unit2 be onezero _separator
let _unit be  _unit1 and _unit2 
let _title be _unit and repeat zeromore _unit
let _part1 be not repeat onemore digit and onezero _separator
let _part2 be "season" and onezero _separator
let _season be digit and onezero digit
let _part4 be "e" and digit and onezero digit
let _part5 be "-e" and digit and onezero digit
let _part6 be "x" and digit and onezero digit
let _lastofoption1 be _part4 and _part5 or _part6
let _insideoption1 be _part1 and onezero _part2 and _season and onezero _lastofoption1
let _year be onezero one of "([" and repeat 4 digit and onezero one of ")]"
let _option1 be _insideoption1 or _year 
let _fulloption1 be _option1 and _separator
let _HD be "HD" and "TV" or "DVD"
let _RIP be "DVD" or "BD" or "BR" or "WEB" and "RIP"
let _dp be repeat onemore digit and "p"
let _hx be one of "hx" and onezero "." and "264"
let _option2 be "BOXSET" or "XVID" or "DIVX" or "LIMITED" or "UNRATED" or "PROPER" or "DTS" or "AC3" or "AAC" or "BLURAY" or _HD or _RIP or _dp or _hx
let _torrent be _title and _option1 or _option2
```
The regular expression generated(_torrent):
```
( - | \w )+(   | . )?( - | \w )+(   | . )?*( ( ( ^\d(   | . )?+ )season(   | . )??\d\d?e\d\d?( -e\d\d? | x\d\d? )? | [([]?\d[)]]? { 4 }  ) | ( BOXSET | ( XVID | ( DIVX | ( LIMITED | ( UNRATED | ( PROPER | ( DTS | ( AC3 | ( AAC | ( BLURAY | ( HD( TV | DVD ) | ( ( DVD | ( BD | ( BR | WEBRIP ) ) ) | ( \dp+ | [hx].?264 ) ) ) ) ) ) ) ) ) ) ) ) ) )
```



## Applications of regular expression
* Regular Expressions for IPS



