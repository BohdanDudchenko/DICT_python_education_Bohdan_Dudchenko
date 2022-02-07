import random


class RockPaperScissors:

    def __init__(self, score, status):
        self.status = status
        self.score = score
        self.guns = []
        self.cpu = 0
        self.player = 0
        take = []
        self.default = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper',
                        'air', 'water', 'dragon', 'devil', 'lightning', 'gun']
        name = str(input("Hello, enter your name:\n>>> "))
        self.save(name)
        self.gun()
        while True:
            if self.status == '!exit':
                self.save(name)
                print('GoodBye!')
                break
            elif self.status == '!rating':
                print(f'Your score: {self.score}')
                self.gun()
            else:
                self.human()
                if self.status == '!exit':
                    self.save(name)
                    break
                self.bot()
                self.game(take)
                print(self.status)

    def gun(self):
        choose = str(input('fire,scissors,snake,human,tree,wolf,sponge,paper,air,water,dragon,devil,lightning,gun,\
rock\n>>>'))

        take = []
        if choose == '!exit':
            self.status = '!exit'
            return self.status
        elif choose == '!rating':
            self.status = '!rating'
            return self.status
        else:
            take.append(choose)
            take.append(take[0].replace(',', ' '))
            take.pop(0)
            take.append(take[0].split())
            for i, name in enumerate(take[1]):
                if name in self.default:
                    self.guns.append(name)
            return self.guns

    def human(self):
        print('What you want to pick?')
        count = 0
        for i, name in enumerate(self.guns):
            print(f'{i} -> {name}')
            count += 1
        choose = input('Enter your answer!\n>>> ')
        if choose == '!exit':
            self.status = '!exit'
            return self.status
        elif choose == '!rating':
            print(f'Your score {self.score}!')
            self.human()
        else:
            try:
                self.player = int(choose)
            except ValueError:
                print('TryAgain!')
                self.human()

    def bot(self):
        self.cpu = random.choice(list(self.guns))
        return self.cpu

    def game(self, take):
        add = 0
        id_gun = self.default.index([self.guns[self.player]][0])
        if self.default.index(self.default[-1]) - id_gun <= 7:
            for i in range(len(self.default)):
                if id_gun == 14 or self.player == 0:
                    take = self.default[0:8]
                elif i == id_gun:
                    take = self.default[i + 1:] + self.default[0: 7 - len(self.default[i + 1:])]
        else:
            take = self.default[id_gun + 1: id_gun + 8]
        print(f'YOU ---> {self.guns[self.player]}\n')
        print(f'CPU ---> {self.cpu}!')
        if self.default[id_gun] == self.cpu:
            self.status = 'DRAW'
            add = 50
        elif self.cpu in take:
            self.status = 'WIN'
            add = 100
        else:
            self.status = 'LOSE'
        self.score += add
        return self.status, add, take

    def save(self, name):
        if self.status == '!exit':
            with open("ratings.txt", "a") as file:
                file.write(f'{name} {self.score}\n')
                file.close()
            return 0
        elif self.status == '':
            with open("ratings.txt", "r") as file:
                lines = file.readlines()
                file.close()
                for i in range(0, len(lines)):
                    line = lines[i].split()
                    key = line[0]
                    value = line[1]
                    if key == name:
                        self.score = int(value)
            with open("ratings.txt", "w") as file:
                for line in lines:
                    if line != f'{name} {self.score}\n':
                        file.write(line)
                file.close()
            print(f'Hello {name}, your score {self.score}!')
            print('OK, Let\'s start!')
            return 0


RockPaperScissors(0, '')
