import random


class Hangman:

    def __init__(self, old_list, tries):
        self.old_list = old_list
        self.tries = tries
        self.start_game()

    def start_game(self):
        word = random.choice(self.old_list)
        sliced_word = list(word)
        searched = ['-' for letter in sliced_word]
        print('''Game started!''')
        while True:
            if self.tries <= 0:
                print('You LOST!')
                self.tries = 8
                self.restart()
                break
            print(' '.join(searched))
            print(f'Tries - {str(self.tries)}')
            letter = input('Write a letter: ').strip(' ')
            len_of_letter = len(letter)
            if letter.isalpha():
                if letter.islower():
                    if len_of_letter == 1:
                        if letter in sliced_word:
                            for i, c in enumerate(sliced_word):
                                if letter in searched[i]:
                                    self.tries -= 1
                                    print('You\'ve already guessed this letter.')
                                    continue
                                if letter == c:
                                    searched[i] = letter
                                if '-' not in searched:
                                    print('YOU WORD: ' + ' '.join(searched))
                                    print('''Thanks for playing!  We'll see how well you did in the next stage''')

                                    self.restart()
                                    break
                        elif letter not in sliced_word:
                            self.tries -= 1
                            print('That letter doesn\'t appear in the word')
                            continue
                    else:
                        print('You should input a single letter.')
                else:
                    print('Please enter a lowercase English letter.')
            else:
                print('Please enter a lowercase English letter.')

    def restart(self):
        choose = str(input('Type "play" to play the game, "exit" to quit: '))
        if choose == 'play':
            self.start_game()
        elif choose == 'exit':
            print('Have a nice day :)')
        else:
            print('Pls, try again')
            self.restart()


Hangman(['python', 'java', 'javascript', 'php'], 8)