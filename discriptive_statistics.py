import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

class DiscriptiveStatistics:
    # initialized DiscriptiveStatistics with data path
    def __init__(self, dataPath):
        self.df = pd.read_csv(dataPath)

    # print whole data file 
    def ç(self):
        print(self.df)

    # print first 5 data file and create a .txt file 
    def printHead(self):
        data = self.df.head()
        with open('discriptive_result/head_data_file.txt', 'w') as f:
            f.write(str(data))
        print(data)

    # print data types
    def printColumnName(self):
        print(self.df.dtypes)
    
    # print Descriptive statistics data
    def printDataDescriptive(self):
        print(self.df.describe())
    
    # print and create a file for compute pairwise correlation of columns
    def printCorr(self, firstColumn, secondColumn):
        data = self.df[[firstColumn,secondColumn]].corr()
        with open('discriptive_result/corr_data_file_{0}_{1}.txt'.format(firstColumn,secondColumn), 'w') as f:
            f.write(str(data))
        print(data)
    
    # print and create a file for compute pairwise correlation of crime with all other variable
    def printAllCorr(self, firstColumn):
        columnList = ['TotPop',  'AgeYoun' ,   'Bdegree',  'BelowPoverty'  ,'Unemplo'  ,'PerIncome' , 'Region']
        for column in columnList:
            self.printCorr(firstColumn, column)
       
    # Return a counts of unique values.
    def countUniqueValue(self, column):
        print(self.df[column].value_counts)

    # Percentage of Region categories.
    def percentageValue(self, column):
        print(self.df[column].value_counts(normalize=True))
    
    # Mean Serious Crime in Region category
    def meanCrimeInRegion(self):
        for (i) in range(4):
            print(self.df[self.df['Region'] == i + 1]['SeriCrim'].mean())
     

   

  
   
