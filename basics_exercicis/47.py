import glob

letters = []

file_list = glob.iglob("letters45e/*.txt")
check_word = 'python'

for filename in file_list:
    with open(filename, 'r') as file:
        letter = file.read().strip('\n')
        if letter in check_word:
            letters.append(letter)

print(letters)
