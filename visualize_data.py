from cProfile import label
from matplotlib import pyplot as plt
import pandas as pd


class VisualizeData:
    
    # initialized VisualizeData with data path
    def __init__(self, dataPath):
        self.df = pd.read_csv(dataPath)  
    
    # Histogram plot base of column
    def plotColumnHistogram(self, column):
        self.df[[column]].hist()
        plt.savefig('plots/{0}_column_histogram.pdf'.format(column))
        # plt.show()
    
    # Shows presence of a lot of outliers/extreme values
    def plotBoxData(self, forColumn, byColumn):
        self.df.boxplot(column=forColumn,by=byColumn)
        plt.savefig('plots/box_data_for_{0}_by_{1}.pdf'.format(forColumn,byColumn))
        plt.show()
    
    # Plotting points as a scatter plot
    def plotScatter(self, firstColumn, secondColumn):
        plt.scatter(self.df[firstColumn], self.df[secondColumn], label = 'star', color = 'm', marker = '*')
        plt.xlabel(firstColumn)
        plt.ylabel(secondColumn)
        plt.savefig('plots/scatter_data_for_{0}_by_{1}.pdf'.format(firstColumn, secondColumn))
        plt.show()


   
