import re;

def ReadWordsFromFile(dir):
	f = open(dir,"r");
	words = set();
	words.update(re.split("\s|\~|\@|\#|\$|\%|\^|\&|\*|\(|\)|\-|\+|\=|\_|\[|\{|\]|\}|\/|\:|[\x92]|[\x93]|[\x94]|\\|\?|\<|\>|\,|\.| |", f.read()));
	return words;

def WriteToFile(dir, list):
	f = open(dir,"w");
	for item in list:
		f.write(item + "\n");