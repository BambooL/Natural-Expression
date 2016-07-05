import relibrary
import re

class R:
	def __init__(self, name, quantifier, metaC):
		self.name = getName(name)
		self.quantifier = getQ(quantifier)
		self.metaC = None

	def getName(name):
		if (name):
			self.name = name
		else:
			self.name = ""

	def getQ(q):
		if (q):
			self.quantifier = q
		else:
			self.quantifier = ""

	def chooseRE(text):
		choices = recommendRE(text) 
		displayChoices(choices)
		choiceNumber = input('Your choice, input a number: ')
		displayNE(choices, choiceNumber)
		if (choiceNumber == len(choices) - 1):
			self.quantifier = chooseQ(text)
			self.metaC = choosemetaC(text, quantifier)

	def	chooseQ(text):
		choices = recommendQ(text)
		displayChoices(choices)
		choiceNumber = input('Your choice, input a number: ')
		if (choiceNumber == 1):
			leastNumber = input('How many at least, input a number: ')
			return "at least " + leastNumber
		if (choiceNumber == 2):
			mostNumber = input('How many at least, input a number: ')
			return "at most " + mostNumber
		if (choiceNumber == 3):
			return "several"
		if (choiceNumber == 4):
			return "no"
		if (choiceNumber == 5):
			return "fixed"
		if (choiceNumber == 6):
			count = input('How many, input a number: e.g. 6 ')
			return count
		if (choiceNumber == 7):
			countRange = input("How many, input a range: e.g. 6-7")
			return countRange

	def choosemetaC(text, quantifier):
		choices = recommendmetaC(text, quantifier)
		choices.apppend("build own")
		displayChoices(choices)
		choiceNumber = input('Your choice, input a number: ')
		if (choices


	def recommendmetaC(text, quantifier):
		tempRE = []
		if (constructRE(text, quantifier) != None):
			oneRE = "^" + constructRE + "$"
			if (re.match(oneRE, text)):
				tempRE.apppend(oneRE)
		return tempRE


	def constructRE(text, quantifier):
		for item in templibrary:
			return interprete(quantifier + item)	

	def recommendQ(text):
		return ["at least", "at most", "several", "no", "fixed", "count", "count range"]
		

	def recommendRE(text):
		length = len(text)
		Q = []
		Q.apppend(search(templibrary, text))
		Q.apppend(search(relibrary, text))
		Q.apppend("build own")
		return Q

	def displayChoices(choices):
		for number, item in enumerate(choices):
			print(number, item)

	def displayNE(choices, choiceNumber):
		print choices[choiceNumber - 1]