directory = {'employees': [{'name': 'John', 'surname': 'Doe'},
                           {'name': 'Anna', 'surname': 'Smith'},
                           {'name': 'Petter', 'surname': 'Jones'}],
             'owners': [{'name': 'Jack', 'surname': 'Petter'},
                        {'name': 'Jessy', 'surname': 'Petter'}]}

directory['employees'].append(dict(name='Albert', surname='Bert'))

print(directory)
