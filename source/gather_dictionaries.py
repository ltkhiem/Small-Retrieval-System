import os;
import system_io;

documentDir = "../training/documents/";
dictionaryDir = "../training/"
myDictionary = set();

#Get data from documents and build dictionary
def CreateDictionary():
	global myDictionary
	docsList = os.listdir(documentDir);
	for doc in docsList:
		words = system_io.ReadWordsFromFile(documentDir+doc);
		myDictionary.update(words)
		while '' in myDictionary:
			myDictionary.remove('')

	myDictionary = sorted(myDictionary)
	system_io.WriteToFile(dictionaryDir+"dictionary.txt", myDictionary);

#Call CreateDictionary() to test for creating new dictionary from documents at "source code/training/documents/"
#The result is stored at "source code/training/"

#CreateDictionary()