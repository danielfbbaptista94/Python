import json

directory = {'employees': [{'name': 'John', 'surname': 'Doe'},
                           {'name': 'Anna', 'surname': 'Smith'},
                           {'name': 'Petter', 'surname': 'Jones'}],
             'owners': [{'name': 'Jack', 'surname': 'Petter'},
                        {'name': 'Jessy', 'surname': 'Petter'}]}

with open('company_employees.json', 'w') as file:
    json.dump(directory, file, indent=4)
