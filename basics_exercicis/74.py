import pandas



data1 = pandas.read_csv('http://www.pythonhow.com/data/sampledata.txt')
data2 = pandas.read_csv('http://pythonhow.com/data/sampledata_x_2.txt')

result = pandas.concat([data1, data2])
result.to_csv('74e.txt', index=None)
