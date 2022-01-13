# Check words in spanish
# Function for number of tries (max 5)

import random
from spellchecker import SpellChecker
spell = SpellChecker(language='es')

letters_playing = {'in_word': [], 'not_in_word': []}
counter = 0


def play(counter):
    #print('Counter = ' + str(counter))
    if counter < 5:
        userWord = input('Ingresa una palabra de 5 letras: ')
        word_exists(userWord, counter)
    elif counter == 5:
        print('💔 You loose 👎 Try again!')


def choose_word():
    random_word = ''
    while len(random_word) != 5:
        random_word = random.choice([word for word in spell])
        if len(random_word) == 5:
            print(random_word)
            return random_word


game_word = choose_word()


def word_exists(userWord, counter):
    word = userWord.lower()
    check = spell.known([word])
    if word in check and len(word) == 5:
        print('🔹 ' + word.title() + ' is playing.')
        results(word, game_word, counter)
    else:
        print('⚠️  ' + word.title() + ' is not a valid word')
        print('')
        play(counter)


def results(word, game_word, counter):
    if word == game_word:
        print('YOU WON! ✨')
    else:
        result_word = ''
        in_word = ''
        not_in_word = ''

        for i in range(len(word)):
            if word[i] == game_word[i]:
                result_word = result_word + game_word[i].upper() + ' '
            elif word[i] in game_word:
                result_word += "_"+' '
                if word[i] not in letters_playing['in_word']:
                    letters_playing['in_word'].append(word[i])
            elif word[i] not in game_word:
                result_word += "_"+' '
                if word[i] not in letters_playing['not_in_word']:
                    letters_playing['not_in_word'].append(word[i])

        print(result_word)
        for value in letters_playing['in_word']:
            in_word += value
        in_word = ', '.join(sorted(in_word))
        for i in letters_playing['not_in_word']:
            not_in_word += i
        not_in_word = ', '.join(sorted(not_in_word))

        print('Letters in word: ' + in_word)
        print('Letters not in word: ' + not_in_word)
        print(' ')
        counter += 1
        play(counter)


play(counter)
