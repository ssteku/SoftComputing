import pygal                                                       # First import pygal

class ChartDrawer:
    def __init__(self, labels):          
        self.chartDict = dict()
        self.x_labels = labels  
    def addChart(self, label, title = "Avarage point of first wrong recognition occurence", y_label="", legendFontSize=8):
        chart = pygal.StackedBar(
            fill=True,
            interpolate='cubic',
            x_label_rotation=30,
            legend_at_bottom=True,
            legend_font_size=legendFontSize,
            truncate_legend=100,
            x_title='Characters',
            y_title=y_label)
        self.chartDict[label] = chart
        self.chartDict[label].x_labels = self.x_labels
        self.chartDict[label].title = title

    def addResults(self, name, results, labels=list()):                                  
        if len(labels) == 0:
            for label in self.chartDict:
                self.chartDict[label].add(name,results)  
        else:
            for label in labels:
                self.chartDict[label].add(name,results) 

    def saveChartToFile(self, filename):
        for label in self.chartDict:
            self.chartDict[label].render_to_file("Charts/"+label+filename)     
        
