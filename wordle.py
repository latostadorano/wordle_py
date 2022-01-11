import random
from spellchecker import SpellChecker
spell = SpellChecker(language='es')


def choose_word():
    random_word = ''
    while len(random_word) != 5:
        random_word = random.choice([word for word in spell])
        if len(random_word) == 5:
            print(random_word)
            return random_word


game_word = choose_word()


def word_exists(userWord):
    word = userWord.lower()
    check = spell.known([word])
    if word in check and len(word) == 5:
        print(word.upper() + ' is playing')
        play(word, game_word)
    else:
        print(word.upper() + ' is not a valid word')


def play(word, game_word):
    if word == game_word:
        print('You won!')
    else:
        result_word = ''
        letters_in_word = ''
        letters_not_in_word = ''
        for i in range(len(word)):
            if word[i] == game_word[i]:
                result_word = result_word + game_word[i].upper()
            elif word[i] in game_word:
                result_word += "_"
                letters_in_word += word[i]
            elif word[i] not in game_word:
                result_word += "_"
                letters_not_in_word += word[i]
        print(result_word)
        print('Letters in word: ' + letters_in_word)
        print('Letters not in word: ' + letters_not_in_word)
        print(' ')


userWord = input('Ingresa una palabra de 5 letras: ')
word_exists(userWord)
