from letters import *
from brail import *
from random import randint, choice, shuffle
import math
class Utils:
    def __getBlackPixelsIndexesList(self, data):
        pixelIndexesList = list()
        for i in range(len(data)):
            if(data[i] == 1):
                pixelIndexesList.append(i)
        return pixelIndexesList 

    def addRandomNosie(self, percentOfNoise, data):
        numberOfNoise = len(data)*0.01*percentOfNoise
        newData = []
        newData = data[:]
        for i in range(int(numberOfNoise)):
            randNr = randint(0, len(data)-1)
            newData[randNr] = 1 if data[randNr] == -1 else -1
        return newData
    def removeLineVerticaly(self, lineNumber, data):
        sizeSqrt = math.sqrt(len(data))
        newData = []
        newData = data[:]
        for i in range(len(data)):
            if(i%sizeSqrt == lineNumber):
                newData[i] = -1;
        return newData
    def removeLineHorizontal(self, lineNumber, data):
        sizeSqrt = math.sqrt(len(data))        
        newData = []
        newData = data[:]        
        for i in range(len(data)):
            currentLineNumber = math.floor(i/sizeSqrt)
            if(currentLineNumber == lineNumber):
                newData[i] = -1;
        return newData
    def removeRandomHorizontalLines(self, numberOfLines, data):
        sizeSqrt = math.sqrt(len(data))     
        newData = data[:]
        if numberOfLines > sizeSqrt:
            numberOfLines = sizeSqrt
        lineNumbers = range(int(sizeSqrt))
        shuffle(lineNumbers)
        for i in range(numberOfLines):
            newData = self.removeLineHorizontal(lineNumbers[i], newData)
        return newData;
    def removeRandomVerticalLines(self, numberOfLines, data):
        sizeSqrt = math.sqrt(len(data))     
        newData = data[:]
        if numberOfLines > sizeSqrt:
            numberOfLines = sizeSqrt
        lineNumbers = range(int(sizeSqrt))
        shuffle(lineNumbers)
        for i in range(numberOfLines):
            newData = self.removeLineVerticaly(lineNumbers[i], newData)
        return newData;
    def removeRandomSquare(self, size, data):
        sizeSqrt = math.sqrt(len(data))     
        randomX = randint(0, sizeSqrt-1)
        randomY = randint(0, sizeSqrt-1)
        endX = randomX+size-1
        endY = randomY+size-1
        newData = data[:]
        for i in range(len(data)):
            currentColumn = i%sizeSqrt
            currentLineNumber = math.floor(i/sizeSqrt)
            if(currentColumn>= randomY and currentColumn <= endY):
                if(currentLineNumber >= randomX and currentLineNumber <= endX):
                    newData[i] = -1;
        return newData

    def addRandomAdjecentPixels(self, numberOfPixels, data):
        pixelIndexesList = self.__getBlackPixelsIndexesList(data)
        shuffle(pixelIndexesList)
        newData = data[:]
        sizeSqrt = math.sqrt(len(data)) 
        p = 0    
        factor = 1
        maxLoopsWithoutChange = 1000
        loopsWithoutChange = 0
        while(p < numberOfPixels):            
            pixelIndex = pixelIndexesList[p%len(pixelIndexesList)]
            randShiftX = randint(-1*factor,  1*factor)
            randShiftY = randint(-1*factor,  1*factor)

            changedColumn = pixelIndex%sizeSqrt+randShiftX
            changedLine = math.floor(pixelIndex/sizeSqrt)+randShiftY
            if(changedColumn>0 and changedColumn<sizeSqrt and changedLine>0 and changedLine<sizeSqrt):
                if(newData[int(changedLine*sizeSqrt+changedColumn)] != 1):
                    newData[int(changedLine*sizeSqrt+changedColumn)] = 1
                    loopsWithoutChange = 0
                    p = p +1
                else:
                    loopsWithoutChange = loopsWithoutChange +1 
            else:
                loopsWithoutChange = loopsWithoutChange +1

            if(loopsWithoutChange > maxLoopsWithoutChange*factor):
                loopsWithoutChange = 0
                factor = factor +1  
        
        return newData
    
    def getInputData(self):
        inputData = dict()
        for letter in lettersDict:
            inputData[letter] =  [(x*2)-1 for x in lettersDict[letter]]
        return inputData
    
