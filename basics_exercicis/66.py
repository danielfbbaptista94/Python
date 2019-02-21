dict = {'weather': 'clima', 'earth': 'terra', 'rain': 'chuva'}


def translator(word):
    return dict[word]


word = input("Enter word: ")
print(translator(word))
