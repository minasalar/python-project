# This program prints Hello, world!
from cProfile import label
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import statistics

class VisualizeData:

    def __init__(self, dataPath):
        self.df = pd.read_csv(dataPath)  
    
    # plot a histogram
    def plotColumnHistogram(self, column):
        self.df[[column]].hist()
        plt.savefig('plots/{0}_column_histogram.pdf'.format(column))
        # plt.show()
    
    # shows presence of a lot of outliers/extreme values
    def plotBoxData(self, forColumn, byColumn):
        self.df.boxplot(column=forColumn,by=byColumn)
        plt.savefig('plots/box_data_for_{0}_by_{1}.pdf'.format(forColumn,byColumn))
        # plt.show()
    
    def plotScatter(self, firstColumn, secondColumn):
        plt.scatter(self.df[firstColumn], self.df[secondColumn], label = 'star', color = 'm', marker = '*')
        plt.xlabel('Observation Value')
        plt.ylabel('Time Period')
        plt.savefig('plots/scatter_data_for_{0}_by_{1}.pdf'.format(firstColumn, secondColumn))
        plt.show()

   
