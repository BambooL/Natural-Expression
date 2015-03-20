import sys
from greenery.lego import parse

def verify(subregex, supregex):
	# supregex : "\d" 
	# subregex : "\d{3}"

	p_subregex = parse(".*" + subregex + ".*")
	p_supregex = parse(".*" + supregex + ".*")

	s = p_subregex&(p_supregex.everythingbut())

	if s.empty():
		print("Verified" + "------    "+subregex + " " + supregex)
	else:
		print("Not pass!" + "------    "+ subregex + " " + supregex)

