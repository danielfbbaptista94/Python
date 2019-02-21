import pandas


data = pandas.read_csv('http://www.pythonhow.com/data/sampledata.txt')
data_2 = data*2
data_2.to_csv('73e.txt', index=None)
