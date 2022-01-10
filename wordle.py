from spellchecker import SpellChecker
spell = SpellChecker(language='es')


def word_exists(word):
    check = spell.known([word])
    if word in check:
        print(word + ' is true')
    else:
        print(word + ' is false')


userWord = input('Ingresa una palabra de 5 letras: ')
word_exists(userWord)

# we need to pick a random word from pyspellchecker
# Codecademy final proyect CS.101
# making tests
