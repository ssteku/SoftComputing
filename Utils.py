from letters import *
from brail import *
from random import randint
class Utils:
	def addRandomNosie(self, percentOfNoise, data):
	    numberOfNoise = len(data)*0.01*percentOfNoise
	    newData = []
	    newData = data[:]
	    for i in range(int(numberOfNoise)):
	        randNr = randint(0, len(data)-1)
	        newData[randNr] = 1 if data[randNr] == -1 else -1
	    return newData
	def getInputData(self):
	    inputData = dict()
	    for letter in lettersDict:
	        inputData[letter] =  [(x*2)-1 for x in lettersDict[letter]]
	    return inputData
	
