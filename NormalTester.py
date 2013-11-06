from pybrain.datasets import SupervisedDataSet
from letters import *
from brail import *
from testLetters import *
from Utils import Utils
class NormalTester:
    def __init__(self):
        self.util = Utils()
    def createDataset(self, inputData):
        data = SupervisedDataSet(100,6)
        for i in range(300):
            for letter in inputData.keys():
                data.addSample(inputData[letter], brailDict[letter])       
        return data

    def checkIfCorrect(self, result, correctAnswer):
        for i in range(len(result)):
            # print "Result i = "+str(i)+" , result: "+str(result[i])+" , correct: "+str(correctAnswer[i])
            if result[i] > 0.5:
                result[i] = 1
            else:
                result[i] = 0
            if result[i] != correctAnswer[i]:
                return False
        return True
    def testUntilWrong(self, trained, inputData, letter):
        testRange = 100
        avarageSum = 0
        for d in range(testRange):
            for i in range(30):
                if not self.checkIfCorrect(trained.activate(self.util.addRandomNosie(i, inputData[letter])), brailDict[letter]):
                    avarageSum = avarageSum + i
                    # print "Error: "+letter+" , i: "+str(i)
                    break
        return avarageSum/testRange

    def testWithChangedLetter(self, trained, key, letter):
        inputData = dict()
        inputData[key] =  [(x*2)-1 for x in testLetters[key]]
        if not self.checkIfCorrect(trained.activate(inputData[key]), brailDict[letter]):
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