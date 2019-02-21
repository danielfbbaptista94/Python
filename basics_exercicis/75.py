import pandas
import matplotlib.pylab as p


data = pandas.read_csv('http://www.pythonhow.com/data/sampledata.txt')
data.plot(x='x', y='y', kind='scatter')
p.show()
