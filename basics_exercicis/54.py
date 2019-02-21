directory = {'employees': [{'name': 'John', 'surname': 'Doe'},
                           {'name': 'Anna', 'surname': 'Smith'},
                           {'name': 'Petter', 'surname': 'Jones'}],
             'owners': [{'name': 'Jack', 'surname': 'Petter'},
                        {'name': 'Jessy', 'surname': 'Petter'}]}

directory['employees'][1]['surname'] = 'Smooth'

print(directory['employees'][1]['surname'])
