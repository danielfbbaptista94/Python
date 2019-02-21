import requests


count_letter = 0

response_web = requests.get('http://www.pythonhow.com/data/universe.txt')
txt = response_web.text.lower()

# count_letter = txt.count('a')

for char in txt:
    if char == 'a':
        count_letter += 1

print(count_letter)
