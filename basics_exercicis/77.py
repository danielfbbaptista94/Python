from datetime import datetime

age = int(input('Enter your age: '))
print('We think you were born back in %s' % str(datetime.now().year - age))
