import requests


response_web = requests.get('http://www.pythonhow.com/data/universe.txt')
print(response_web.text)
