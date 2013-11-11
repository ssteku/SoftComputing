from pybrain.datasets import SupervisedDataSet
from letters import *
from brail import *
from testLetters import *
from Utils import Utils
import math
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
            if result[i] > 0.5:
                result[i] = 1
            else:
                result[i] = 0
            if result[i] != correctAnswer[i]:
                return False
        return True

    def testWithGivenModificationFunction(self, trained, inputData, letter, removalRange, removalFunction):
        testRange = 100
        avarageSum = 0
        wasFailed = False
        for d in range(testRange):
            for i in range(int(removalRange)):
                if not self.checkIfCorrect(trained.activate(removalFunction(i, inputData[letter])), brailDict[letter]):
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
            if not self.checkIfCorrect(trained.activate(self.util.removeLineVerticaly(i, inputData[letter])), brailDict[letter]):
                avarageSum = avarageSum + 1                
        return 100*avarageSum/sizeSqrt
        
    def testWithRemovedHorizontalLine(self, trained, inputData, letter):
        sizeSqrt = math.sqrt(len(inputData[letter]))
        avarageSum = 0
        for i in range(int(sizeSqrt)):
            if not self.checkIfCorrect(trained.activate(self.util.removeLineHorizontal(i, inputData[letter])), brailDict[letter]):
                avarageSum = avarageSum + 1
        return 100*avarageSum/sizeSqrt 
