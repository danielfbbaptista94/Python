import json

with open('company_employees.json', 'r+') as file:
    directory = json.loads(file.read())
    directory['employees'].append(dict(name='Tomas', surname='White'))
    file.seek(0)
    json.dump(directory, file, indent=4, sort_keys=True)
    file.truncate()
