import json
import random
import re
import sys
import requests
from bs4 import BeautifulSoup


class Test:
    def __init__(self):
        self.data = {}
        self.name = ''
        self.lvl_easy = 0
        self.lvl_hard = 0
        self.lvl_logic = 0
        self.count_good = 0
        self.difficult = ''
        self.auth()

    def auth(self):
        self.name = input(f'Hello, enter your name, pls!\n>>> ')
        with open('save.json', 'r') as data:
            self.data = json.load(data)
            if self.name in self.data:
                self.lvl_easy = self.data[self.name]["lvl_easy"]
                self.lvl_hard = self.data[self.name]["lvl_hard"]
                self.lvl_logic = self.data[self.name]["lvl_logic"]
                self.count_good = self.data[self.name]["count_good"]
            else:
                pass

        self.select()

    def select(self):
        difficult = input("Select difficulty! 1 -- Simple || 2 -- Hard || 3 -- LOGIC QUEST || 0 -- Exit\n>>> ")
        self.count_good = 0
        if difficult == '1':
            print('-------------Simple operations with numbers 2-9--------------')
            self.simple(5)
            self.lvl_easy += 1
        elif difficult == '2':
            print('------------------Integral squares of 11-29-------------------')
            self.hard(5)
            self.lvl_hard += 1
        elif difficult == '3':
            print('------------------------LOGIC QUEST----------------------------')
            self.logic_quest()
            self.lvl_logic += 1
            print(f'LOGIC TEST COMPLETED!')
            self.save()
        elif difficult == '0':
            print('GoodBye!')
            sys.exit()
        else:
            print('Try again!')
            Test()
        print(f'Your mark is {self.count_good}/5.')
        self.save()

    def simple(self, num):
        num = num
        for i in range(num):
            first_num = random.randint(2, 10)
            second_num = random.randint(2, 10)
            func = random.choice(['-', '+', '*'])
            question = f'{first_num} {func} {second_num}'
            correct_answer = eval(question)
            print(question + ' = ?')
            try:
                answer_player = int(input(f'>>> '))
                num -= 1
            except ValueError:
                print('Incorrect format!')
                return self.simple(num)
            if correct_answer == answer_player:
                print('Right!')
                self.count_good += 1
            else:
                print('Wrong!')

    def hard(self, num):
        num = num
        for i in range(num):
            number = random.randint(11, 30)
            correct_answer = number * number
            print(f'Number - {number}')
            try:
                answer_player = int(input(f'>>> '))
                num -= 1
            except ValueError:
                print('Incorrect format!')
                return self.hard(num)
            if correct_answer == answer_player:
                print('Right!')
                self.count_good += 1
            else:
                print('Wrong!')

    def logic_quest(self):
        url = 'https://mat-zadachi.ru/4-class/zadachi-s-ovetami.php'
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        questions = soup.find_all('div', class_='border')
        questions = str(random.choice(questions))
        quest = re.search('<p>(.+?):', questions).groups()[0]
        answers = re.search('<ul>(.+?)</ul>', questions.replace('\n', '')).groups()[0]
        answers = answers.replace('<li>', '')
        answers = answers.replace('</li>', '')
        answers = answers.split(';')
        try:
            correct_answer = re.search('Ответ:(.+?)\)', questions.replace('\n', '')).groups()[0][-1]
        except AttributeError:
            correct_answer = re.search('Решение:(.+?)\)', questions.replace('\n', '')).groups()[0][-1]
        if correct_answer == '6':
            correct_answer = 'б'
        print(correct_answer)
        print(f'{quest}')
        for i in answers:
            print(i)
        while True:
            answer = input('Enter your answer or "stop"\n>>> ')
            if answer == correct_answer:
                print('Right!')
                break
            elif answer == 'stop':
                self.select()

    def save(self):
        combination = ['yes', 'y']
        select = input(f'''Do you wanna save result? y\\n\n>>> ''')
        if select.lower() in combination:
            self.data[self.name] = {
                "lvl_easy": self.lvl_easy,
                "lvl_hard": self.lvl_hard,
                "lvl_logic": self.lvl_logic,
                "count_good": self.count_good}
            with open('save.json', 'w') as save:
                json.dump(self.data, save, sort_keys=True, indent=4)
            print('Statistic Saved!')

        select = input(f'''Do you wanna play again? y\\n\n>>> ''')
        if select.lower() in combination:
            self.select()
        else:
            print('GoodBye')
            sys.exit()


Test()
