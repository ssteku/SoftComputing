from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer
from letters import *
from brail import *
import string

def createDataset():
    allTheLetters = string.uppercase
    data = SupervisedDataSet(100,6)
    for letter in allTheLetters:
        data.addSample(lettersDict[letter], brailDict[letter])   
    return data

def training(d):

    n = buildNetwork(d.indim, 8, d.outdim,recurrent=True)
    t = BackpropTrainer(n, d, learningrate = 0.01, momentum = 0.70, verbose = True)
    for epoch in range(0,10000):
        t.train()
    return t

def test(trained):

    testdata = SupervisedDataSet(100,6)
    allTheLetters = string.uppercase
    for letter in allTheLetters:
        testdata.addSample(lettersDict[letter], brailDict[letter])

    trained.testOnData(testdata, verbose= True)



trainingdata = make_dataset()
trained = training(trainingdata)
test(trained)
