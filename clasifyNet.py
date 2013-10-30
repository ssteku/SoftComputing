from pybrain.datasets import ClassificationDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised import BackpropTrainer
from pybrain.tools.xml.networkwriter import NetworkWriter
from letters import *
from brail import *
import time
from random import randint
from pybrain.structure.modules   import LinearLayer,StateDependentLayer,GaussianLayer,SoftmaxLayer, SigmoidLayer,LSTMLayer, TanhLayer
import string


def addRandomNosie(percentOfNoise, data):
    numberOfNoise = len(data)*0.01*percentOfNoise
    newData = []
    newData = data
    for i in range(int(numberOfNoise)):
        randNr = randint(0, len(data)-1)
        newData[randNr] = 1 if data[randNr] == -1 else -1
    return newData
def getInputData():
    inputData = dict()
    for letter in lettersDict:
        inputData[letter] =  [(x*2)-1 for x in lettersDict[letter]]
    return inputData

def createClassificationDataset(inputData):
    data = ClassificationDataSet(100,nb_classes=len(inputData.keys()), class_labels=inputData.keys())
    allTheLetters = string.uppercase
    for i in range(100):
        for letter in inputData.keys():
            data.addSample(inputData[letter], allTheLetters.index(letter)) 
    
    data._convertToOneOfMany([0,1])
    print data.calculateStatistics()

    return data

def createDataset(inputData):
    data = SupervisedDataSet(100,6)
    for i in range(10):
        for letter in inputData.keys():
            data.addSample(inputData[letter], brailDict[letter])       
    return data


def training(d):
    net = buildNetwork(d.indim, 25,25,25,  d.outdim, bias=True,recurrent=True, hiddenclass =SigmoidLayer , outclass = SigmoidLayer)
    t = BackpropTrainer(net, d,learningrate = 0.01,momentum=0.8, verbose = True)
    t.trainUntilConvergence(continueEpochs=1200, maxEpochs=1100)
    NetworkWriter.writeToFile(net, 'myNetwork'+str(time.time())+'.xml')
    return t

def testWithClassTrainingData(trained, inputData, noisePercentRate = 0):
    print "TEST--------------> Noise: "+str(noisePercentRate)+"%"
    allTheLetters = string.uppercase
    testdata =  ClassificationDataSet(100, nb_classes=len(inputData.keys()), class_labels=inputData.keys())   
    for letter in inputData.keys():
        testdata.addSample(addRandomNosie(noisePercentRate, inputData[letter]), allTheLetters.index(letter))
    testdata._convertToOneOfMany([0,1])
    trained.testOnData(testdata, verbose= True)

def testWithTrainingData(trained, inputData, noisePercentRate = 0):
    print "TEST--------------> Noise: "+str(noisePercentRate)+"%"
    testdata =  SupervisedDataSet(100, 6)   
    for letter in inputData.keys():
            testdata.addSample(addRandomNosie(noisePercentRate, inputData[letter]), brailDict[letter])
    trained.testOnData(testdata, verbose= True)


def testWithChangedChars(trained, inputData):
    print "TEST--------------> Changed C"
    testdata =  SupervisedDataSet(100, 6)    
    testdata.addSample(testDict["Cbold"], brailDict["C"])
    testdata.addSample(testDict["C1bold"], brailDict["C"])
    testdata.addSample(testDict["Cnoise"], brailDict["C"])
    trained.testOnData(testdata, verbose= True)


inputData = getInputData()
trainingdata = createDataset(inputData)
trained = training(trainingdata)
testWithChangedChars(trained, inputData)
testWithTrainingData(trained, inputData, 0)
testWithTrainingData(trained, inputData, 2)
testWithTrainingData(trained, inputData, 4)
# testWithTrainingData(trained, inputData, 8)
# testWithTrainingData(trained, inputData, 16)
# testWithTrainingData(trained, inputData, 32)
