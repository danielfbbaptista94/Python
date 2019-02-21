dict = {'weather': 'clima', 'earth': 'terra', 'rain': 'chuva'}


def translator(word):
    dir()
    try:
        return dict[word]
    except KeyError:
        return "We couldn't find that word!"


word = input("Enter word: ").lower()
print(translator(word))
