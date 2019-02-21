import string


with open('41e', 'w') as file:
    for letter in string.ascii_lowercase:
        file.write(letter + ' ')
