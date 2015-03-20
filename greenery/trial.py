import sys
from greenery.lego import parse

subregex = parse(sys.argv[1])
supregex = parse(sys.argv[2])

s = subregex&(supregex.everythingbut())
if s.empty():
  print("%s is a subset of %s"%(subregex,supregex))
else:
  print("%s is not a subset of %s, it also matches %s"%(subregex,supregex,s)