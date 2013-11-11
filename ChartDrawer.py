import pygal                                                       # First import pygal

class ChartDrawer:
    def __init__(self, labels):
        self.bar_chart = pygal.StackedBar()  
        self.bar_chart.x_labels = labels    
    def addResults(self, name, results):                                  # Then create a bar graph object
        self.bar_chart.add(name,results)  # Add some values

    def saveChartToFile(self, filename):
        self.bar_chart.render_to_file(filename)     
        
