import random
from spellchecker import SpellChecker
spell = SpellChecker(language='es')

print(random.choice([word for word in spell]))


def word_exists(userWord):
    word = userWord.lower()
    check = spell.known([word])
    if word in check and len(word) == 5:
        print(word.upper() + ' is true')
    else:
        print(word.upper() + ' is not a valid word')


userWord = input('Ingresa una palabra de 5 letras: ')
word_exists(userWord)
