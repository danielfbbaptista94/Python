import string
import os

if not os.path.exists("letters45e"):
    os.makedirs("letters45e")

for letter in string.ascii_lowercase:
    with open("letters45e/" + letter + ".txt", "w") as file:
        file.write(letter + "\n")
