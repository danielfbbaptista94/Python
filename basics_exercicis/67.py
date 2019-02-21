dict = {'weather': 'clima', 'earth': 'terra', 'rain': 'chuva'}


def translator(word):
    try:
        return dict[word]
    except KeyError:
        return "That word does not exist!"


word = input("Enter word: ")
print(translator(word))
