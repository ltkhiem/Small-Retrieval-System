import build_inverted_index
from collections import defaultdict
import in2pos
import os

documentDir = "../docs/";
dictionaryDir = "../dictionary/"
myDictionary = defaultdict(list)
allDocs = []

#Create the inverted index
def Initialize():
	build_inverted_index.LoadDictionary(myDictionary)
	build_inverted_index.BuildInvertedIndex(myDictionary)
	global allDocs 
	allDocs = os.listdir(documentDir)

#Calculate the AND operator
def CalcAnd(op1, op2):
	newop = []
	for token in op1:
		if token in op2:
			newop.append(token)
	return newop

#Calculate the OR operator
def CalcOr(op1, op2):
	newop = op1
	for token in op2:
		if token not in op1:
			newop.append(token)
	return newop

#Calculate the NOT operator
def CalcNot(op):
	newop = []
	for item in allDocs:
		if item not in op:
			newop.append(item)
	return newop

#Process the input query
def Search(query):
	stack = []
	#Get the posfix notation of the query:
	tokens = in2pos.ParseQuery(query)
	#Compute for result
	for token in tokens:
		if token in ["AND","OR"]:
			operand1 = stack.pop()
			operand2 = stack.pop()
			if token in "AND":
				stack.append(CalcAnd(operand1,operand2))
			else:
				stack.append(CalcOr(operand1,operand2))
		elif token in "NOT":
			operand = stack.pop()
			stack.append(CalcNot(operand))
		else:
			stack.append(myDictionary[token])
	return stack.pop()

Initialize()


