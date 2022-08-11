
from discriptive_statistics import DiscriptiveStatistics
from visualize_data import VisualizeData
 
dataPath = "/Users/user/Desktop/project/Data.CDI.csv"
crimeDiscriptiveData = DiscriptiveStatistics(dataPath)
crimeVisualizeData = VisualizeData(dataPath)

crimeDiscriptiveData.printData()
crimeDiscriptiveData.printHead()
crimeDiscriptiveData.printColumnName()
crimeDiscriptiveData.printDataDescriptive()
crimeDiscriptiveData.printCorr('TotPop','SeriCrim')
crimeDiscriptiveData.printAllCorr('SeriCrim')
crimeDiscriptiveData.countUniqueValue('Region')
crimeDiscriptiveData.percentageValue('Region')
crimeDiscriptiveData.meanCrimeInRegion()


# PLOT
crimeVisualizeData.plotColumnHistogram('SeriCrim')
crimeVisualizeData.plotBoxData('SeriCrim', 'Region')
crimeVisualizeData.plotScatter('SeriCrim', 'BelowPoverty')
crimeVisualizeData.plotScatter('SeriCrim', 'PerIncome')


