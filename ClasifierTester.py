from testLetters import *
from letters import *
from brail import *
from Utils import Utils
import string
from pybrain.datasets import ClassificationDataSet
import math 
class ClasifierTester:
    def __init__(self):
        self.util = Utils()
    def createDataset(self, inputData):
        data = ClassificationDataSet(100,nb_classes=len(inputData.keys()), class_labels=inputData.keys())
        allTheLetters = string.uppercase
        for i in range(300):
            for letter in inputData.keys():
                data.addSample(inputData[letter], allTheLetters.index(letter)) 
        
        data._convertToOneOfMany([0,1])
        return data
    def checkIfCorrect(self, result, correctAnswer):
        maximum = result[0]
        maximumIndex = 0
        allTheLetters = string.uppercase
        for i in range(len(result)):
            if result[i] > maximum:
                maximum = result[i]
                maximumIndex = i
        return allTheLetters.index(correctAnswer) == maximumIndex

    def testWithGivenModificationFunction(self, trained, inputData, letter, removalRange, removalFunction):
        testRange = 100
        avarageSum = 0
        wasFailed = False
        for d in range(testRange):
            for i in range(int(removalRange)):
                if not self.checkIfCorrect(trained.activate(removalFunction(i, inputData[letter])), letter):
                    # print "Fail with value i: "+str(i)
                    avarageSum = avarageSum + i
                    wasFailed = True
                    break
        if wasFailed:        
            return avarageSum/testRange    
        else:
            return 100

    def testWithRemovedVerticalLine(self, trained, inputData, letter):
        sizeSqrt = math.sqrt(len(inputData[letter]))
        avarageSum = 0        
        for i in range(int(sizeSqrt)):
            if not self.checkIfCorrect(trained.activate(self.util.removeLineVerticaly(i, inputData[letter])), letter):
                avarageSum = avarageSum + 1                
        return 100*avarageSum/sizeSqrt
    
    def testWithRemovedHorizontalLine(self, trained, inputData, letter):
        sizeSqrt = math.sqrt(len(inputData[letter]))
        avarageSum = 0        
        for i in range(int(sizeSqrt)):
            if not self.checkIfCorrect(trained.activate(self.util.removeLineHorizontal(i, inputData[letter])), letter):
                avarageSum = avarageSum + 1
                
        return 100*avarageSum/sizeSqrt       

