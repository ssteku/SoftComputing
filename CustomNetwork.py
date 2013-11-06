from pybrain.datasets import ClassificationDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import FullConnection
from letters import *
from brail import *
import time
from random import randint
from pybrain.structure.modules   import LinearLayer,StateDependentLayer,GaussianLayer,SoftmaxLayer, SigmoidLayer,LSTMLayer, TanhLayer
import string


def addRandomNosie(percentOfNoise, data):
    numberOfNoise = len(data)*0.01*percentOfNoise
    for i in range(int(numberOfNoise)):
        randNr = randint(0, len(data)-1)
        data[randNr] = 1 if data[randNr] == 0 else 0
    return data
def createDataset():
    data = ClassificationDataSet(100,nb_classes=len(lettersDict.keys()), class_labels=lettersDict.keys())
    allTheLetters = string.uppercase
    for letter in lettersDict.keys():
        data.addSample(lettersDict[letter], allTheLetters.index(letter)) 
    
    data._convertToOneOfMany(bounds=[0, 1])
    print data.calculateStatistics()

    return data

def training(d):
    # net = buildNetwork(d.indim, 55, d.outdim, bias=True,recurrent=False, hiddenclass =SigmoidLayer , outclass = SoftmaxLayer)
    net = FeedForwardNetwork()
    inLayer = SigmoidLayer(d.indim)
    hiddenLayer1 = SigmoidLayer(d.outdim)
    hiddenLayer2 = SigmoidLayer(d.outdim)
    outLayer = SigmoidLayer(d.outdim)

    net.addInputModule(inLayer)
    net.addModule(hiddenLayer1)
    net.addModule(hiddenLayer2)
    net.addOutputModule(outLayer)

    in_to_hidden = FullConnection(inLayer, hiddenLayer1)
    hidden_to_hidden = FullConnection(hiddenLayer1, hiddenLayer2)
    hidden_to_out = FullConnection(hiddenLayer2, outLayer)

    net.addConnection(in_to_hidden)
    net.addConnection(hidden_to_hidden)
    net.addConnection(hidden_to_out)

    net.sortModules()
    print net

    t = BackpropTrainer(net, d, learningrate = 0.9,momentum=0.9, weightdecay=0.01, verbose = True)
    t.trainUntilConvergence(continueEpochs=1200, maxEpochs=1000)
    NetworkWriter.writeToFile(net, 'myNetwork'+str(time.time())+'.xml')
    return t

def test(trained):

    allTheLetters = string.uppercase
    testdata = data = ClassificationDataSet(100,nb_classes=len(lettersDict.keys()), class_labels=lettersDict.keys())
    for letter in lettersDict.keys():        
        testdata.appendLinked(addRandomNosie(0, lettersDict[letter]), allTheLetters.index(letter))

    # testdata.addSample(testDict["Cbold"], allTheLetters.index("C"))
    # testdata.addSample(testDict["C1bold"], allTheLetters.index("C"))
    # testdata.addSample(testDict["Cnoise"], allTheLetters.index("C"))

    # testdata.addSample(testDict["Cbold"], allTheLetters.index("C"))
    # testdata.addSample(testDict["C1bold"], allTheLetters.index("C"))
    # testdata.addSample(testDict["Cnoise"], allTheLetters.index("C"))
    testdata._convertToOneOfMany(bounds=[0, 1])
    trained.testOnData(testdata, verbose= True)

trainingdata = createDataset()
trained = training(trainingdata)
test(trained)
