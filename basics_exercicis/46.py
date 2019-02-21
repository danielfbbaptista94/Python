import string

letters = []

for letter in string.ascii_lowercase:
    with open("letters45e/" + letter + ".txt", "r") as file:
        letters.append(file.read().strip("\n"))

print(letters)
