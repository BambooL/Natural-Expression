gPats = [

# Not
  [r'(.*) does not (contain|have|contains|has) (.*) (\"|\')(.*)(\"|\')(.*)',
  ['LET _%1 BE NOT "%5"'], ["Okay, %1 does not contain '%5'!"]],

  [r'(.*) (contain|contains|have|has) only (.*) (\"|\')(.*)(\"|\')(.*)',
  ['LET _%1 BE "%5"'], ["Okay, %1 only contains '%5'!"]],

  [r'(.*) only (contain|contains|have|has) (.*) (\"|\')(.*)(\"|\')(.*)',
  ['LET _%1 BE "%5"'], ["Okay, %1 only contains '%5'!"]],

  [r'(.*) (use|using|has|contains|have|contain) words ending in (\"|\')(.*)(\"|\')(.*)',
  ['LET _%1 BE WORD END "%4"'], ["Okay, %1 uses words ending in '%4'!"]],

  [r'(.*) (contain|contains|have|has) only lowercase (characters|letters|letter|character|alphabet|alphabets)(.*)',
  ['LET _%1 BE REPEAT SEVERAL LOWCASE'], ["Okay, %1 contains only lowercase letters!"]],

  [r'(.*) (use|using|has|contains|have|contain) the word (\"|\')(.*)(\"|\')(.*)',
  ['LET _%1 BE WORD "%4"'], ["Okay, %1 is word '%4'!"]],

  [r'(.*) (use|using|has|contains|have|contain) word (\"|\')(.*)(\"|\')(.*)',
  ['LET _%1 BE WORD "%4"'], ["Okay, %1 is word '%4'!"]],

  [r'(.*) (use|using|has|contains|have|contain) words that (use|using|has|contains|have|contain) (\d*) (vowels|vowel)(.*)',
  ['LET _%1 BE WORD HAS %4 ONE OF "aeiou"'],["Okay, %1 is word has %4 vowels!"]],

  [r'(.*) (use|using|has|contains|have|contain) words (use|using|has|contains|have|contain) (\d*) (vowels|vowel)(.*)',
  ['LET _%1 BE WORD HAS %4 ONE OF "aeiou"'],["Okay, %1 is word has %4 vowels!"]],

  [r'(.*) (use|using|has|contains|have|contain) (\"|\')(.*)(\"|\')(.*)',
  ['LET _%1 BE "%3"'],["Okay, %1 has %3"]]









#repeat
  # A{m,n}


#   [r'(.*)Let (.*) be (\W*) repeat (\d*) to (\d*) time(.*)',
#   ["%2: %3{%4,%5}"],["Okay, Let's make %2 an expression of repeating %3 %4 to %5 times!"]],

#   # A{m}
#   [r'(.*)Let (.*) be (\W*) repeat (\d*) time(.*)',
#   ["%2:%3{%4}"],["Okay, Let's make %2 an expression of repeating %3 %4 times!"]],

#   [r'(.*)Let (.*) be (\w*) repeat (\d*) time(.*)',
#   ["%2:%3{%4}"],["Okay, Let's make %2 an expression of repeating %3 %4 times!"]],

#   [r'repeat (\W*) (\d*) time(.*)',
#   ["%1{%2}"],["Okay, Let's repeat %1 for %2 times!"]],

#   [r'repeat (\w*) (\d*) time(.*)',
#   ["%1{%2}"],["Okay, Let's repeat %1 for %2 times!"]],

#   # A*
#   [r'(.*)repeat (\w*) sevral time(.*)',
#   ["%2*"],["Okay, Let's repeat %2 several times!"]],

#   [r'(.*)repeat (\W*) sevral time(.*)',
#   ["%2*"],["Okay, Let's repeat %2 several times!"]],

#   [r'(.*)',
#   ["%2*"],["Okay, Let's repeat %2 several times!"]],

#   [r'(.*)Let (\W*) repeat several time(.*)',
#   ["%2*"],["Okay, Let's repeat %2 several times!"]],

#   # A?
#   [r'(.*)Let (.*) be (\W*) (one|zero) or (one|zero) time(.*)',
#   ["%2:%3?"],["Okay, Let's make %2 an expression of %3 occur zero or one time!"]],  

#   [r'(.*)Let (.*) be (\w*) (one|zero) or (one|zero) time(.*)',
#   ["%2:%3?"],["Okay, Let's make %2 an expression of %3 occur zero or one time!"]],  

#   [r'(.*)Let (\W*) occur (one|zero) or (one|zero) time in (\w*)(.*)',
#   ["%5:%2?"],["Okay, Let's make %3 an expression of %3 occur zero or one time!"]],

#   [r'(.*)Let (\w*) occur (one|zero) or (one|zero) time in (\w*)(.*)',
#   ["%5:%2?"],["Okay, Let's make %3 an expression of %3 occur zero or one time!"]],
  
#   # A+
#   [r'(.*)let (\W*) repeat at least one time in (\w*)(.*)',
#   ["%3:%2+"],["Okay, Let's repeat %2 at least one time in %3!"]],

#   [r'(.*)let (\w*) repeat at least one time in (\w*)(.*)',
#   ["%3:%2+"],["Okay, Let's repeat %2 at least one time in %3!"]],

#   [r'(.*)Let (.*) be (\w*) repeat at least one time(.*)',
#   ["%2:%3+"],["Okay, Let's %2 be %3 repeat at least one time!"]],

#   [r'(.*)Let (.*) be (\W*) repeat at least one time(.*)',
#   ["%2:%3+"],["Okay, Let's %2 be %3 repeat at least one time!"]],

#   [r'(.*)Let (\w*) be (\W*) repeat at least one time(.*)',
#   ["%2:%3+"],["Okay, Let's %2 be %3 repeat at least one time!"]],

#   [r'(.*)Let (\w*) be (\w*) repeat at least one time(.*)',
#   ["%2:%3+"],["Okay, Let's %2 be %3 repeat at least one time!"]],
# # 

# # local varialble

#   [r'(.*)Let (.*)=(\W*) in(.*)',
#   ["%2:%3"],["Okay, Let %2 = %3!"]],

#   [r'(.*)Let (.*)=(\w*) in(.*)',
#   ["%2:%3"],["Okay, Let %2 = %3!"]],

#   [r'(.*)Let (.*) equals (\W*) in(.*)',
#   ["%2:%3"],["Okay, Let %2 = %3!"]],

#   [r'(.*)Let (.*) equals (\w*) in(.*)',
#   ["%2:%3"],["Okay, Let %2 = %3!"]],

  
# #follow
#   [r'(.*)Let (.*) be (.*) and (.*) and (.*) and (.*)',
#   ["%2:%3%4%5%6"],["Okay, Let's make %2 be %3 %4 %5 %6!"]],

#   [r'(.*)Let (.*) be (.*) and (.*) and (.*)',
#   ["%2:%3%4%5"],["Okay, Let's make %2 be %3 %4 %5!"]],

#   [r'(.*)Let (.*) start with (\w*) and then follow with (\w*)(.*)',
#   ["%2:%3%4"],["Okay, Let's make %2 start with %3 and follow with %4!"]],

#   [r'(.*)Let (.*) start with (\w*) and then follow with (\W*)(.*)',
#   ["%2:%3%4"],["Okay, Let's make %2 start with %3 and follow with %4!"]],

#   [r'(.*)Let (.*) start with (\W*) and then follow with (\w*)(.*)',
#   ["%2:%3%4"],["Okay, Let's make %2 start with %3 and follow with %4!"]],

#   [r'(.*)Let (.*) start with (\W*) and then follow with (\W*)(.*)',
#   ["%2:%3 %4"],["Okay, Let's make %2 start with %3 and follow with %4!"]],

#   [r'(.*)Let (.*) start with a  (.*) followed with (.*)',
#   ["%2:\d%4"],["Okay, Let's make %2 start with a number and followed with %4!"]],
  
#   [r'(.*)Let (.*) be (.*) followed by (.*)',
#   ["%2:%3%4"],["Okay, Let's make %2 an expression that starts with %3 and follows with %4!"]],

# #definition  
#   [r'(.*)Let (.*) be a digit(.*)',
#   ["%2:\d"],["Okay, Let %2 be a digit!"]],

#   [r'(.*)Let (.*) be several digits(.*)',
#   ["%2:\d*"],["Okay, Let %2 be a digit!"]],

#   # or
#   #[A-B C-D]
#   [r'(.*)Let (.*) be one of ((\w|\d)*) to ((\w|\d)*) or ((\w|\d)*) to ((\w|\d)*)(.*)',
#   ["%2:[%3-%5 %7-%9]"],["Okay, Let's make %2 one of %3 to %5 or %7 to %9!"]],
 
#   [r'(.*)Let (.*) be ((\w|\d)*) to ((\w|\d)*) or ((\w|\d)*) to ((\w|\d)*)(.*)',
#   ["%2:[%3-%5 %7-%9]"],["Okay, Let's make %2 one of %3 to %5 or %7 to %9!"]],

#   #[AB]

#   [r'(.*)Let (.*) be a (\w*) or (\w*) or (\w*) or (\w*) or (\w*)(.*)',
#   ["%2:[%3%4%5%6%7]"],["Okay, Let's make %2 %3 or %4 or %5 or %6 or %7!"]],

#   [r'(.*)Let (.*) be a (\w*) or (\w*) or (\w*) or (\w*) or (\w*)(.*)',
#   ["%2:[%3%4%5%6%7]"],["Okay, Let's make %2 %3 or %4 or %5 or %6 or %7!"]],

#   [r'(.*)Let (.*) be a (\w*) or (\w*) or (\w*) or (\w*)',
#   ["%2:[%3%4%5%6]"],["Okay, Let's make %2 %3 or %4 or %5 or %6!"]],

#   [r'(.*)Let (.*) be a (\w*) or (\w*) or (\w*) or (\w*)',
#   ["%2:[%3%4%5%6]"],["Okay, Let's make %2 %3 or %4 or %5 or %6!"]],

#   [r'(.*)Let (.*) be a (\w*) or (\w*) or (\w*)',
#   ["%2:[%3%4%5]"],["Okay, Let's make %2 %3 or %4 or %5!"]],

#   [r'(.*)Let (.*) be a (.*) or (.*)',
#   ["%2:[%3%4]"],["Okay, Let's make %2 be %3 or %4!"]],
  
#   [r'(.*)Let (.*) be (.*) or (.*)',
#   ["%2:(%3|%4)"],["Okay, Let's make %2 %3 or %4!"]],

#   [r'Let (.*) be (.*) character set include (.*)',
#   ["%1:[%3]"],["Okay, Let's make %1 a character set include %3!"]],

#   [r'Let (.*) be (.*) character set exclude (.*)',
#   ["%1:[^%3]"],["Okay, Let's make %1 a character set exclude %3!"]],
  
#   [r'(.*)Let (.*) be (.*) to (.*)',
#   ["%2:[%3-%4]"],["Okay, Let's make '%2' range from %3 to %4!"]],
  
#   [r'(.*)Let (.*) be a character(.*)',
#   ["%2:[A-Za-z]"],["Okay, Let %2 be a character!"]],
  
#   [r'(.*)Let (.*) be several character(.*)',
#   ["%2:[A-Za-z]*"],["Okay, Let %2 be several characters!"]],

#   [r'(.*)a word boundary(.*)',
#   ["\\b"],["Okay, Let's make here a word boundary!"]],

#   [r'(.*)a nonword boundary(.*)',
#   ["\B"],["Okay, Let's make here a nonword boundary!"]],

#   [r'(.*)a digit(.*)',
#   ["\d"],["Okay, Let's put a digit here!"]],

#   [r'(.*)a non digit',
#   ["\D"],["Okay, Let's put a non digit here!"]],

#   [r'(.*)another page(.*)',
#   ["\\f"],["Okay, Let's start a new page here!"]],

#   [r'(.*)another line(.*)',
#   ["\\n"],["Okay, Let's start a new line here!"]],

#   [r'(.*)Let (\w*) equals (\w*)',
#   ["%2:%3"],["Okay, Let's make %2 equals to %3!"]],

#   [r'(.*)Let (.*)=(.*)',
#   ["%2:%3"],["Okay, Let's make %2 equals to %3!"]],

#   [r'(.*)Let (.*) be a string(.*)',
#   ["%2:^string$"],["Okay, Let's make %2 a string!"]],





]


gReflections = {
  "or":"|",
  "one":"1",
  "two":"2",
  "three":"3",
  "four":"4",
  "five":"5",
  "six":"6",
  "seven":"7",
  "eight":"8",
  "nine":"9",
  "zero":"0",
  "not a":"non ",
  "become":"be",
  "integer" : "int",
  "character" : "char",
  "am"   : "are",
  "was"  : "were",
  "i"    : "you",
  "i'd"  : "you would",
  "i've"  : "you have",
  "i'll"  : "you will",
  "my"  : "your",
  "are"  : "am",
  "you've": "I have",
  "you'll": "I will",
  "your"  : "my",
  "yours"  : "mine",
  "you"  : "me",
  "me"  : "you",
  "east":"0",
  "south":"270",
  "west":"180",
  "north":"90",
  "first":"1",
  "second":"2",
  "third":"3"
}