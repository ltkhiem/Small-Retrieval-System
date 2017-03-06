#Split the query into tokens
def GenerateToken(s):
	res = ""
	for i in s:
		if i in ['(',')']:
			res += " " + i + " "
		else: 
			res += i
	return res.split()

#Return the precedence of each token
def Precedence(token):
	if token is "(":
		return 0;
	elif token in ["AND", "OR"]:
		return 1;
	elif token in "NOT":
		return 2;
	else:
		return 100;

#Transform the query into the postfix notation
def ParseQuery(s):
	postfix = []
	stack = []
	tokens = GenerateToken(s);
	for token in tokens:
		if token in ["AND", "OR", "NOT"]:
			pre = Precedence(token)
			while len(stack)>0 and pre<=Precedence(stack[-1]) :
				postfix.append(stack.pop())
			stack.append(token)
		elif token is "(":
			stack.append(token)
		elif token is ")":
			op = stack.pop()
			while op is not "(":
				postfix.append(op)
				op = stack.pop()
		else: 
			postfix.append(token[1:-1])

	while len(stack)>0:
		postfix.append(stack.pop())

	return postfix




