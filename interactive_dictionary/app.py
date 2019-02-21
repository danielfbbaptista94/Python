import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yes_or_no = input('Did you mean %s ? \n Enter yes or no...' % get_close_matches(word, data.keys())[0])
        yes_or_no = yes_or_no.lower()
        if yes_or_no == 'yes' or yes_or_no == 'YES' or yes_or_no == 'Y' or yes_or_no == 'y':
            return meaning(get_close_matches(word, data.keys())[0])
        elif yes_or_no == 'no' or yes_or_no == 'NO' or yes_or_no == 'N' or yes_or_no == 'n':
            return 'Word does not exist'
        else:
            return 'Please resend the word!'
    else:
        return 'Word does not exist'


word = input('Enter a word: ')

output = meaning(word)

if type(output) is list:
    for item in output:
        print(item)
else:
    print(output)
