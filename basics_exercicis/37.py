def file_count_words(filepath):
    with open(filepath, 'r') as file:
        phrase = file.read()
        phrase = phrase.replace(",", " ")
        phrase_list = phrase.split(" ")
        return len(phrase_list)


print(file_count_words('/home/daniel/Documents/Python/basics_exercicis/37e'))
