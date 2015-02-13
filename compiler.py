import myyacc
import sys

# filename = raw_input('--> ')

filename = "first.let"
fo = open(filename, "rw+")

lines = fo.readlines()

for line in lines:
	line = (line[-1] == "\n") and line[0:-1] or line
	myyacc.yacc.parse(line)

key = raw_input("The final you want:")

print myyacc.names[key]





