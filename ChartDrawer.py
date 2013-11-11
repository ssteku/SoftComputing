import pygal                                                       # First import pygal

class ChartDrawer:
    def __init__(self, labels):          
        self.chartDict = dict()
        self.x_labels = labels  
    def addChart(self, label):
        chart = pygal.StackedBar()
        self.chartDict[label] = chart
        self.chartDict[label].x_labels = self.x_labels

    def addResults(self, name, results, labels=list()):                                  
        if len(labels) == 0:
            for label in self.chartDict:
                self.chartDict[label].add(name,results)  
        else:
            for label in labels:
                self.chartDict[label].add(name,results) 

    def saveChartToFile(self, filename):
        for label in self.chartDict:
            self.chartDict[label].render_to_file(label+filename)     
        
