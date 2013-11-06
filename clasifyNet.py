from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader

import time
from pybrain.structure.modules   import LinearLayer,StateDependentLayer,GaussianLayer,SoftmaxLayer, SigmoidLayer,LSTMLayer, TanhLayer
import string

from Utils import Utils
from NormalTester import NormalTester
from ClasifierTester import ClasifierTester
import pickle

def training(inputData, hiddenNodesArg = 55, learningRateArg = 0.004,
        momentumArg=0.99, biasArg=True, recurrentArg=True,
        hiddenclassArg = SoftmaxLayer, outclassArg = SoftmaxLayer,
        epochs = 22):

    net = buildNetwork(inputData.indim, hiddenNodesArg, inputData.outdim, bias = biasArg ,recurrent = recurrentArg , hiddenclass = hiddenclassArg , outclass = outclassArg)
    t = BackpropTrainer(net, inputData,learningrate = learningRateArg, momentum = momentumArg, verbose = False)
    t.trainUntilConvergence(continueEpochs=1200, maxEpochs = epochs)
    NetworkWriter.writeToFile(net, 'myNetwork'+str(time.time())+'.xml')
    return t, net 

def doCalsificationTestWithHiddenNodes():
    print "----------------> Clasifier: Hidden nodes test BEGIN<------------------"
    tester = ClasifierTester()
    trainingdata = tester.createDataset(inputData)
    for i in range(1):
        print "Testing with i = "+str(i)+" , hiddenNodesArg = "+str((i+1)*5)
        trained, net = training(trainingdata, hiddenNodesArg=55)
        tester.testUntilWrongWithAllLetters(net, inputData)
    print "----------------> Clasifier: Hidden nodes test END<------------------"

def doTranslationTestWithHiddenNodes():
    print "----------------> Translator: Hidden nodes test BEGIN<------------------"
    tester = NormalTester()
    trainingdata = tester.createDataset(inputData)
    for i in range(20):
        print "Testing with i = "+str(i)+" , hiddenNodesArg = "+str((i+1)*5)
        trained, net = training(trainingdata,hiddenNodesArg=(i+1)*5, hiddenclassArg = SigmoidLayer, outclassArg = SigmoidLayer)
        tester.testUntilWrongWithAllLetters(net, inputData)
    print "----------------> Translator: Hidden nodes test END<------------------"

def doCalsificationTestWithMomentum():
    print "----------------> Clasifier: Momentum test BEGIN<------------------"
    tester = ClasifierTester()
    trainingdata = tester.createDataset(inputData)
    for i in range(20):
        print "Testing with i = "+str(i)+" , momentumArg = "+str((i+1)*0.05)
        trained, net = training(trainingdata, momentumArg=(i+1)*0.05)
        tester.testUntilWrongWithAllLetters(net, inputData)
    print "----------------> Clasifier: Momentum test END<------------------"

def doTranslationTestWithMomentum():
    print "----------------> Translator: Momentum test BEGIN<------------------"
    tester = NormalTester()
    trainingdata = tester.createDataset(inputData)
    for i in range(20):
        print "Testing with i = "+str(i)+" , momentumArg = "+str((i+1)*0.05)
        trained, net = training(trainingdata,momentumArg=(i+1)*0.05, hiddenclassArg = SigmoidLayer, outclassArg = SigmoidLayer)
        tester.testUntilWrongWithAllLetters(net, inputData)
    print "----------------> Translator: Momentum test END<------------------"

def doCalsificationTestWithLearningRate():
    print "----------------> Clasifier: learningRate test BEGIN<------------------"
    tester = ClasifierTester()
    trainingdata = tester.createDataset(inputData)
    for i in range(20):
        print "Testing with i = "+str(i)+" , learningRateArg = "+str((i+1)*0.001)
        trained, net = training(trainingdata, learningRateArg=(i+1)*0.001)
        tester.testUntilWrongWithAllLetters(net, inputData)
    print "----------------> Clasifier: learningRate test END<------------------"

def doTranslationTestWithLearningRate():
    print "----------------> Translator: learningRate test BEGIN<------------------"
    tester = NormalTester()
    trainingdata = tester.createDataset(inputData)
    for i in range(20):
        print "Testing with i = "+str(i)+" , learningRateArg = "+str((i+1)*0.001)
        trained, net = training(trainingdata,learningRateArg=(i+1)*0.001, hiddenclassArg = SigmoidLayer, outclassArg = SigmoidLayer)
        tester.testUntilWrongWithAllLetters(net, inputData)
    print "----------------> Translator: learningRate test END<------------------"

def doCalsificationTestWithLongTraining():
    print "----------------> Clasifier: Long training 1000 epochs test BEGIN<------------------"
    tester = ClasifierTester()
    trainingdata = tester.createDataset(inputData)
    print "Testing Long training 1000 epochsArg = "
    trained, net = training(trainingdata,epochs = 1000, learningRateArg=0.02)
    tester.testUntilWrongWithAllLetters(net, inputData)
    print "----------------> Clasifier: Long training 1000 epochs test END<------------------"

def doTranslationTestWithLongTraining():
    print "----------------> Translator: Long training 1000 epochs test BEGIN<------------------"
    tester = NormalTester()
    trainingdata = tester.createDataset(inputData)
    print "Testing Long training 1000 epochsArg = "
    trained, net = training(trainingdata,epochs = 1000, learningRateArg=0.016, hiddenclassArg = SigmoidLayer, outclassArg = SigmoidLayer)
    tester.testUntilWrongWithAllLetters(net, inputData)
    print "----------------> Translator: Long training 1000 epochs test END<------------------"
def doTranslationTestFromLoadedNN(filename):

    print "----------------> Translator: Loaded NN test BEGIN<------------------"
    tester = NormalTester()
    trainingdata = tester.createDataset(inputData)
    net = NetworkReader.readFrom(filename)
    tester.testUntilWrongWithAllLetters(net, inputData)
    print "----------------> Translator: Loaded NN test END<------------------"
def doCalsificationTestFromLoadedNN(filename):
    print "----------------> Clasifier: Loaded NN test BEGIN<------------------"
    tester = ClasifierTester()
    trainingdata = tester.createDataset(inputData)
    net = NetworkReader.readFrom(filename)
    tester.testUntilWrongWithAllLetters(net, inputData)
    print "----------------> Clasifier: Loaded NN test END<------------------"


util = Utils()
inputData = util.getInputData()
doCalsificationTestWithHiddenNodes()
# doTranslationTestWithHiddenNodes()
# doCalsificationTestWithMomentum()
# doTranslationTestWithMomentum()
# doCalsificationTestWithLearningRate()
# doTranslationTestWithLearningRate()
# doCalsificationTestWithLongTraining()
# doCalsificationTestWithLongTraining()
doTranslationTestFromLoadedNN('automatic_translation_trained_2013-101-03-17-17.xml')
doTranslationTestFromLoadedNN('sigma_sigma_trained.xml.xml')
doCalsificationTestFromLoadedNN('myNetwork.xml')

