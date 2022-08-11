
from discriptive_statistics import DiscriptiveStatistics
from visualize_data import VisualizeData
 
dataPath = "/Users/user/Desktop/project/Data.CDI.csv"
crimeDiscriptiveData = DiscriptiveStatistics(dataPath)
crimeVisualizeData = VisualizeData(dataPath)


# crimeDiscriptiveData.printCrimeData()
# crimeDiscriptiveData.printHead()
# crimeDiscriptiveData.printColumnName()
# crimeDiscriptiveData.printDataDescription()
# crimeDiscriptiveData.printCorr('TotPop','SeriCrim')
# crimeDiscriptiveData.countUniqueValue('Region')
#crimeDiscriptiveData.percentageValue('Region')


# PLOT
# crimeVisualizeData.plotColumnHistogram('TotPop')
# crimeVisualizeData.plotBoxData('SeriCrim', 'Region')
# crimeVisualizeData.plotScatter('SeriCrim', 'Region')


