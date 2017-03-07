import os;
import system_io;
from collections import defaultdict
import gather_dictionaries

documentDir = "../training/documents/";
dictionaryDir = "../training/"
myDictionary = defaultdict(list)

def LoadDictionary(dictionary):
	if "dictionary.txt" not in os.listdir(dictionaryDir):
		gather_dictionaries.CreateDictionary()
	f = open(dictionaryDir+"dictionary.txt", "r");
	dictionary = f.read().split();

def BuildInvertedIndex(dictionary):
	docsList = os.listdir(documentDir);
	for doc in docsList:
		words = system_io.ReadWordsFromFile(documentDir+doc);
		for word in words:
			dictionary[word].append(doc);

def Test():
	LoadDictionary(myDictionary)
	BuildInvertedIndex(myDictionary)
	print("The inverted list: ")
	for word in myDictionary:
		print(word + ": " , end='')
		print(myDictionary[word])

#Call for Test() to test the building inverted index process
Test()
