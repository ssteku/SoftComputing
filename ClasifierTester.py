from testLetters import *
from letters import *
from brail import *
from Utils import Utils
import string
from pybrain.datasets import ClassificationDataSet
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
    def testUntilWrong(self, trained, inputData, letter):
        testRange = 100
        avarageSum = 0
        for d in range(testRange):
            for i in range(30):
                if not self.checkIfCorrect(trained.activate(self.util.addRandomNosie(i, inputData[letter])), letter):
                    avarageSum = avarageSum + i
                    # print "Error: "+letter+" , i: "+str(i)
                    break
        return avarageSum/testRange
    def testWithChangedLetter(self, trained, key, letter):
        inputData = dict()
        inputData[key] =  [(x*2)-1 for x in testLetters[key]]
        if not self.checkIfCorrect(trained.activate(inputData[key]), letter):
            print "FAIL: "+key
        else:
            print "SUCCESS: "+key
    def testWithChangedLetters(self, trained):
        self.testWithChangedLetter(trained, "C1bold", "C")
        self.testWithChangedLetter(trained, "Cbold", "C")
        self.testWithChangedLetter(trained, "Cnoise", "C")

    def testUntilWrongWithAllLetters(self, trained, inputData): 
        avarageSum = 0
        for letter in inputData.keys():
            result = self.testUntilWrong(trained, inputData, letter)
            avarageSum = avarageSum + result
            print "Letter: "+letter+" fail with percent err: "+str(result)+"%"
        print "Avarage error : " + str(avarageSum/len(inputData))
