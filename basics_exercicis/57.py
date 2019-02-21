import json
from pprint import pprint

with open('company_employees.json', 'r') as file:
    directory = json.loads(file.read())

pprint(directory)
