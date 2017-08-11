# Natural Expressions
**Natural Expressions** is a new regular expression language designed to produce readable, context-free, and reusable code.

It significantly simplifies the process of creating powerful regular expressions, and makes it possible for even laymen to understand. For example, to build a Regex like this:
```
^( ( \d { 2 }  ) | + )
```
you may write a script using Natural Expressions like this:
```
let _a be digit
let _b be repeat 2 _a
let _c be word
let _d be or _b _c
let _e be not _d
```

### Syntax

The syntax of Let-Language is denoted in BNF(Backus–Naur Form). Upper-case Tokens are tokens in the lexer. 

```
assign        ::= LET NAME BE quantifier expr 
quantifier    ::= EXACT
               |  EXIST
expr          ::= REPEAT NUMBER expr 
               |  REPEAT ONEMORE expr 
               |  REPEAT ZEROMORE expr 
               |  REPEAT NUMBER TO NUMBER expr 
               |  expr OR expr 
               |  NOT expr 
               |  expr AND expr 
               |  ONEZERO expr 
               |  term
term          ::= DIGIT | CHAR | LETTER | WORD 
               |  WORD END expr | WORD HAS expr 
               |  WORD BEGIN expr | CHAR | CONST 
               |  BLANK | LETTER  | LOWCASE 
               |  UPCASE | ONEOF NUMBER TO NUMBER 
               |  NUMBER TO NUMBER 
```


### Implementation

Let-Language utilizes PLY(Python Lex-Yacc) to create a compiler for the language. 

To compile a `.let` script, just use `compiler.py`.

    python compiler.py let/torrent.let

### Example Scripts

* To generate a normal regular expression (let/first.let)
```
let _a be digit
let _b be repeat 2 _a
let _c be word
let _d be _b or _c
let _e be char
let _f be one of 1-8
let _g be repeat zeromore _f
let _h be _d and _e
let _i be _h or _g
let _j be word end "er"
let _k be repeat zeromore lowcase
let _l be word has 3 one of "aeiou"
let _m be word begin "aaa"
let _n be _j or _l
let _o be _k and _m
let _p be repeat zeromore _o
let _q be _n and _p and _i
```
The regular expression generated(_q):
```
( ( \b* )
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
AC
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
https?://regex\.com/r/( (  | \d ){1,6} )
```

* distorted_email
```
let _character be "-" or letter or digit or "\."
let _Username be repeat onemore _character
let _option1 be repeat onemore blanks and "at" and repeat onemore blanks
let _option2 be repeat zeromore blanks and "@" and repeat zeromore blanks
let _option3 be repeat zeromore blanks and repeat 3 one of "\@" and repeat zeromore blanks
let _part2 be _option1 or _option2 or _option3
let _domain be repeat onemore _character
let _blanks be repeat zeromore blanks
let _each be one of "\dot\."
let _option be repeat 3 TO 5 _each
let _part5 be "dot" or "\." or _option
let _TLD be repeat onemore char
let _email be _Username and _part2 and _domain and _blanks and _part5 and _blanks and _TLD
```
The regular expression generated(_email):
```
( - | ( {3,5} ) ) )\s*\w+
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
let _year be onezero one of "("
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
( - | \w )+(   | . )?( - | \w )+(   | . )?*( ( ( ^\d(   | . )?+ )season(   | . )??\d\d?e\d\d?( -e\d\d? | x\d\d? )? | .?264 ) ) ) ) ) ) ) ) ) ) ) ) ) )
```

## Verification
* In our design, there are basically three unit operations: ``AND`` ``OR`` ``REPEAT`` 
corresponding to the ``Concatenation`` ``Option`` and ``Kleen Star`` in the traditional
regex. In each of the three unit operations, we use inclusion to verify the correctness
of the regex generation. The idea comes from the construction of regex, e.g.,
```
.*\d{3}.* is subset of .*\d.*
```
or
```
.*abcd.* is subset of .*ab.*
.*a.* is subset of .*(a|b).*
```
Here the relationship of super- and sub-set means that, all the strings can be match 
with super-set can be matched with sub-set.

* Check Syntax Error along the way

### Generate examples for validation
* let _header be 'http" and ONEZERO "s" and "://"
* **u'https://' 'http://'**
* let _domainname be "regex.com"
* **u'regex.com'**
* let _next be "/r/"
* **u'/r/'**
* let _validcharacter be letter or digit 
* **u'L' '1'**
* let _id be REPEAT 1 TO 6 _validcharacter 
* **u'820n1Y' 'u'**
* let _url be _header and _domainname and _next and _id
* **u'http://regex.com/r/k' 'http://regex.com/r/kRf356'**


## Applications of regular expression
* Regular Expressions for IPS



