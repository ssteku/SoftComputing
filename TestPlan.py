from testLetters import *
from letters import *
from brail import *
from Utils import Utils
import string
import math 

class TestPlan:
    def __init__(self):
        self.util = Utils()
    def test(self, trained, inputData, tester):         
        avarageSum = 0
        print "------------>> Test with random noise Begin <<---------------"
        for letter in inputData.keys():
            result = tester.testWithGivenModificationFunction(trained, inputData, letter, 50, self.util.addRandomNosie)
            avarageSum = avarageSum + result
            print "Letter: "+letter+" fail with percent err: "+str(result)+"%"
        print "Avarage error : " + str(avarageSum/len(inputData))
        print "------------>> Test with random noise End <<---------------"

        avarageSum = 0
        print "------------>> Test with removed 1 line Begin <<---------------"
        for letter in inputData.keys():
            result = tester.testWithRemovedVerticalLine(trained, inputData, letter)
            avarageSum = avarageSum + result
            print "Letter: "+letter+" error in : "+str(result)+"% cases" 
        print "Avarage error : " + str(avarageSum/len(inputData))
        print "------------>> Test with removed 1 line End <<---------------"

        avarageSum = 0
        print "------------>> Test with removed 1 horizontal line Begin <<---------------"
        for letter in inputData.keys():
            result = tester.testWithRemovedHorizontalLine(trained, inputData, letter)
            avarageSum = avarageSum + result
            print "Letter: "+letter+" error in : "+str(result)+"% cases" 
        print "Avarage error : " + str(avarageSum/len(inputData))
        print "------------>> Test with removed 1 horizontal line End <<---------------"

        avarageSum = 0
        print "------------>> Test with removed number of horizontal lines Begin <<---------------"
        for letter in inputData.keys():
            sizeSqrt = math.sqrt(len(inputData[letter]))
            result = tester.testWithGivenModificationFunction(trained, inputData, letter, sizeSqrt, tester.util.removeRandomHorizontalLines)
            avarageSum = avarageSum + result

            print "Letter: "+letter+" avarage error with removed : "+str(result)+" lines" 
        print "Avarage error : " + str(avarageSum/len(inputData))
        print "------------>> Test with number of horizontal lines End <<---------------"

        avarageSum = 0
        print "------------>> Test with removed number of Vertical lines Begin <<---------------"
        for letter in inputData.keys():
            sizeSqrt = math.sqrt(len(inputData[letter]))
            result = tester.testWithGivenModificationFunction(trained, inputData, letter, sizeSqrt, tester.util.removeRandomVerticalLines)
            avarageSum = avarageSum + result

            print "Letter: "+letter+" avarage error with removed : "+str(result)+" lines" 
        print "Avarage error : " + str(avarageSum/len(inputData))
        print "------------>> Test with number of Vertical lines End <<---------------"

        avarageSum = 0
        print "------------>> Test with removed square Begin <<---------------"
        for letter in inputData.keys():
            sizeSqrt = math.sqrt(len(inputData[letter]))
            result = tester.testWithGivenModificationFunction(trained, inputData, letter, sizeSqrt, tester.util.removeRandomSquare)
            avarageSum = avarageSum + result

            print "Letter: "+letter+" avarage error with removed square of size: "+str(result) 
        print "Avarage error : " + str(avarageSum/len(inputData))
        print "------------>> Test with removed square End <<---------------"

        avarageSum = 0
        print "------------>> Test with random adjecent pixels Begin <<---------------"
        for letter in inputData.keys():
            sizeSqrt = math.sqrt(len(inputData[letter]))
            result = tester.testWithGivenModificationFunction(trained, inputData, letter, 100, tester.util.addRandomAdjecentPixels)
            avarageSum = avarageSum + result

            print "Letter: "+letter+" avarage error with added number of pixels: "+str(result)
        print "Avarage error : " + str(avarageSum/len(inputData))
        print "------------>> Test with random adjecent pixels End <<---------------"