import sys
from greenery.lego import parse

def verify(subregex, supregex):
	# supregex : "\d" 
	# subregex : "\d{3}"

	p_subregex = parse(subregex)
	p_supregex = parse(supregex)

	s1 = p_subregex&(p_supregex.everythingbut())
	s2 = p_supregex&(p_subregex.everythingbut())

	if s1.empty() and s2.empty():
		print("Verified" + "  ------    "+subregex + " " + supregex)
	else:
		print("Not pass!" + "  ------    "+ subregex + " " + supregex)


verify("(.*)\d{6,10}(.*)", "(.*)[0-9]{6,10}(.*)")

# Contain
# verify properties one by one

# There are three digits before the characters

# 