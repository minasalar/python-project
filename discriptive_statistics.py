# This program prints Hello, world!
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import statistics

class DiscriptiveStatistics:

    def __init__(self, dataPath):
        self.df = pd.read_csv(dataPath)
     
    def printCrimeData(self):
        print(self.df)

    def printHead(self):
        data = self.df.head()
        with open('discriptive_result/head_data_file.txt', 'w') as f:
            f.write(str(data))
        print(data)

    def printColumnName(self):
        print(self.df.dtypes)
    
    def printDataDescription(self):
        print(self.df.describe())
    
    def printCorr(self, firstColumn, secondColumn):
        data = self.df[[firstColumn,secondColumn]].corr()
        with open('discriptive_result/corr_data_file_{0}_{1}.txt'.format(firstColumn,secondColumn), 'w') as f:
            f.write(str(data))
        print(data)

    def countUniqueValue(self, column):
        print(self.df[column].value_counts)
    
    def percentageValue(self, column):
        print(self.df[column].value_counts(normalize=True))
    
   

  
   
