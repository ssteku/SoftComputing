from testLetters import *
from letters import *
from brail import *
from Utils import Utils
import string
import math 
from ChartDrawer import ChartDrawer

class TestPlan:
    def __init__(self):
        self.util = Utils()

    def test(self, trained, inputData, tester):     
        chartDrawer = ChartDrawer(inputData.keys())  
        chartDrawer.addChart("All")
        chartDrawer.addChart("Removed_lines")  
        chartDrawer.addChart("RandNoise")  
        chartDrawer.addChart("VerLine")  
        chartDrawer.addChart("HorLine")  
        chartDrawer.addChart("LinesHor")  
        chartDrawer.addChart("LinesVer")  
        chartDrawer.addChart("Squares")  
        chartDrawer.addChart("Adjecent")  
        avarageSum = 0
        resultList = list()
        print "------------>> Test with random noise Begin <<---------------"
        for letter in inputData.keys():
            result = tester.testWithGivenModificationFunction(trained, inputData, letter, 50, self.util.addRandomNosie)
            resultList.append(result)
            avarageSum = avarageSum + result
            print "Letter: "+letter+" fail with percent err: "+str(result)+"%"
        print "Avarage error : " + str(avarageSum/len(inputData))
        print "------------>> Test with random noise End <<---------------"
        chartDrawer.addResults("Maximum negated random pixels without error",resultList, ["All", "RandNoise"])  

        avarageSum = 0
        resultList = list()
        print "------------>> Test with removed 1 line Begin <<---------------"
        for letter in inputData.keys():
            result = tester.testWithRemovedVerticalLine(trained, inputData, letter)
            resultList.append(result)
            avarageSum = avarageSum + result
            print "Letter: "+letter+" error in : "+str(result)+"% cases" 
        print "Avarage error : " + str(avarageSum/len(inputData))
        print "------------>> Test with removed 1 line End <<---------------"
        chartDrawer.addResults("Succes rate of removal 1 vertical line",resultList, ["Removed_lines", "VerLine"])  

        avarageSum = 0
        resultList = list()
        print "------------>> Test with removed 1 horizontal line Begin <<---------------"
        for letter in inputData.keys():
            result = tester.testWithRemovedHorizontalLine(trained, inputData, letter)
            resultList.append(result)
            avarageSum = avarageSum + result
            print "Letter: "+letter+" error in : "+str(result)+"% cases" 
        print "Avarage error : " + str(avarageSum/len(inputData))
        print "------------>> Test with removed 1 horizontal line End <<---------------"
        chartDrawer.addResults("Succes rate of removal 1 horizontal line",resultList, ["Removed_lines", "HorLine"])  

        avarageSum = 0
        resultList = list()
        print "------------>> Test with removed number of horizontal lines Begin <<---------------"
        for letter in inputData.keys():
            sizeSqrt = math.sqrt(len(inputData[letter]))
            result = tester.testWithGivenModificationFunction(trained, inputData, letter, sizeSqrt, tester.util.removeRandomHorizontalLines)
            resultList.append(result)
            avarageSum = avarageSum + result

            print "Letter: "+letter+" avarage error with removed : "+str(result)+" lines" 
        print "Avarage error : " + str(avarageSum/len(inputData))
        print "------------>> Test with number of horizontal lines End <<---------------"
        chartDrawer.addResults("Removed number of horizontal lines",resultList, ["All", "LinesHor"])  

        avarageSum = 0
        resultList = list()
        print "------------>> Test with removed number of Vertical lines Begin <<---------------"
        for letter in inputData.keys():
            sizeSqrt = math.sqrt(len(inputData[letter]))
            result = tester.testWithGivenModificationFunction(trained, inputData, letter, sizeSqrt, tester.util.removeRandomVerticalLines)
            resultList.append(result)
            avarageSum = avarageSum + result

            print "Letter: "+letter+" avarage error with removed : "+str(result)+" lines" 
        print "Avarage error : " + str(avarageSum/len(inputData))
        print "------------>> Test with number of Vertical lines End <<---------------"
        chartDrawer.addResults("Removed number of vertical lines",resultList, ["All", "LinesVer"])  


        avarageSum = 0
        resultList = list()
        print "------------>> Test with removed square Begin <<---------------"
        for letter in inputData.keys():
            sizeSqrt = math.sqrt(len(inputData[letter]))
            result = tester.testWithGivenModificationFunction(trained, inputData, letter, sizeSqrt, tester.util.removeRandomSquare)
            resultList.append(result)
            avarageSum = avarageSum + result

            print "Letter: "+letter+" avarage error with removed square of size: "+str(result) 
        print "Avarage error : " + str(avarageSum/len(inputData))
        print "------------>> Test with removed square End <<---------------"
        chartDrawer.addResults('Removed squares of size',resultList, ["All", "Squares"])  

        
        avarageSum = 0
        resultList = list()
        print "------------>> Test with random adjecent pixels Begin <<---------------"
        for letter in inputData.keys():
            sizeSqrt = math.sqrt(len(inputData[letter]))
            result = tester.testWithGivenModificationFunction(trained, inputData, letter, 100, tester.util.addRandomAdjecentPixels)
            resultList.append(result)
            avarageSum = avarageSum + result
            print "Letter: "+letter+" avarage error with added number of pixels: "+str(result)
        print "Avarage error : " + str(avarageSum/len(inputData))
        print "------------>> Test with random adjecent pixels End <<---------------"
        chartDrawer.addResults('Adjecent pixels number',resultList, ["All", "Adjecent"])  
        chartDrawer.saveChartToFile("TestPlanResultsChart_"+tester.__class__.__name__)
