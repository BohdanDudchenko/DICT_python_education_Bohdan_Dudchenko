import os
import random


class CoffeeMachine:
    def __init__(self):
        self.water = 0
        self.milk = 0
        self.beans = 0
        self.clean_cup = 0
        self.money = 0

        self.save()

    def option(self):
        choose = str(input(f'Write action (buy, fill, take, remaining, exit)\n>>> '))
        if choose == 'buy':
            self.buy_func()
        elif choose == 'fill':
            self.fill()
        elif choose == 'take':
            self.take()
        elif choose == 'remaining':
            self.remaining()
        elif choose == 'exit':
            file = open('save.txt', 'w')
            file.write(str(self.water) + f'\n')
            file.write(str(self.milk) + f'\n')
            file.write(str(self.beans) + f'\n')
            file.write(str(self.clean_cup) + f'\n')
            file.write(str(self.money) + f'\n')
            file.close()
            print('GoodBye!')
        else:
            print('Try Again!')

    def buy_func(self):
        choose = int(input(f'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino ||  0 - Main Menu\n>>> '))
        if choose == 1:
            water_per_cup = 250
            milk_per_cup = 16
            beans_per_cup = 0
            price = 4
            self.machine(water_per_cup, milk_per_cup, beans_per_cup, price)
        elif choose == 2:
            water_per_cup = 350
            milk_per_cup = 75
            beans_per_cup = 20
            price = 7
            self.machine(water_per_cup, milk_per_cup, beans_per_cup, price)
        elif choose == 3:
            water_per_cup = 200
            milk_per_cup = 100
            beans_per_cup = 12
            price = 6
            self.machine(water_per_cup, milk_per_cup, beans_per_cup, price)
        elif choose == 0:
            self.option()
        else:
            print('Try Again!')
            self.buy_func()

    def machine(self, water_per_cup, milk_per_cup, beans_per_cup, price):
        print(f'You will be given a first clean glass for each coffee.')
        ingredients = list([self.water, self.milk, self.beans])
        ingredients2 = list([self.water, self.milk])
        minimum = min(ingredients)
        minimum2 = min(ingredients2)
        cup = int(input(f'Write how many cups of coffee you will need:\n>>> '))
        if water_per_cup * cup > self.water:
            print('Sorry, not enough water')
            choose = int(input(f'Do u wanna fill?  1 - Yes  ||  2 - Choose another quantity\n>>> '))
            if choose == 1:
                self.fill()
            elif choose == 2:
                self.buy_func()
        elif milk_per_cup * cup > self.milk:
            print('Sorry, not enough milk')
            choose = int(input(f'Do u wanna fill?  1 - Yes  ||  2 - Choose another quantity\n>>> '))
            if choose == 1:
                self.fill()
            elif choose == 2:
                self.buy_func()
        elif beans_per_cup * cup > self.beans:
            print('Sorry, not enough beans')
            choose = int(input(f'Do u wanna fill?  1 - Yes  ||  2 - Choose another quantity\n>>> '))
            if choose == 1:
                self.fill()
            elif choose == 2:
                self.buy_func()
        elif cup > self.clean_cup:
            print('Sorry, not enough disposable cups')
            choose = int(input(f'Do u wanna fill?  1 - Yes  ||  2 - Choose another quantity\n>>> '))
            if choose == 1:
                self.fill()
            elif choose == 2:
                self.buy_func()

        else:
            print('I have enough resources, making you a coffee!')
            all_portion = 0
            if minimum == ingredients[0]:
                all_portion = int(self.water / water_per_cup)
            elif minimum == ingredients[1]:
                all_portion = int(self.milk / milk_per_cup)
            elif beans_per_cup <= 0 and minimum == ingredients[2]:
                if minimum2 == ingredients2[0]:
                    all_portion = int(self.water / water_per_cup)
                if minimum2 == ingredients2[1]:
                    all_portion = int(self.milk / milk_per_cup)
            elif beans_per_cup > 0 and minimum == ingredients[2]:
                all_portion = int(self.beans / beans_per_cup)
            can_cup = all_portion - cup

            choose = int(input(f'''
    Yes, I can make that amount of coffee (and even {can_cup} more than that.)
    Are you sure you want {cup} servings?
    ---------It cost {price * cup}!---------
    1 - Yes  ||  2 - Choose amount\n>>> '''))
            if choose == 1:
                get_money = int(input(f'Contribute money\n>>> '))
                cost_portion = price * cup
                money_back = get_money - cost_portion
                if get_money >= cost_portion:
                    self.money = self.money + get_money - money_back
                    print(f'''
    Starting to make a coffee
    Grinding coffee beans
    Boiling water
    Mixing boiled water with crushed coffee beans
    Pouring coffee into the cup
    Pouring some milk into the cup
    Coffee is ready!               
    Your surrender is {get_money - cost_portion} UAH!
    ''')
                    self.water = self.water - int(cup * water_per_cup)
                    self.milk = self.milk - int(cup * milk_per_cup)
                    if beans_per_cup > 0:
                        self.beans = self.beans - int(cup * beans_per_cup)
                    self.clean_cup = self.clean_cup - cup
                    self.option()
                elif get_money < cost_portion:
                    question = int(input(f'''
    Money not enough! Money back ({get_money})
    Do u wanna try again?  1 - Yes  ||  2 - Main Menu\n>>> '''))
                    if question == 1:
                        self.buy_func()
                    elif question == 2:
                        self.option()
            elif choose == 2:
                self.buy_func()

    def fill(self):
        print(f'''{self.water} of water  |  {self.milk} of milk  |  {self.beans} of coffee beans  |\
{self.clean_cup} of disposable cups''')
        choose = int(input(f'Do u wanna add ingredients?  1 - Add | 2 - Main Menu\n>>> '))
        if choose == 1:
            water_add = int(input(f'Write how many ml of water do you want to add:\n>>> '))
            self.water = water_add + self.water
            milk_add = int(input(f'Write how many ml of milk do you want to add:\n>>> '))
            self.milk = milk_add + self.milk
            beans_add = int(input(f'Write how many grams of coffee beans do you want to add:\n>>> '))
            self.beans = beans_add + self.beans
            add_clean_cup = int(input(f'Write how many disposable cups of coffee do you want to add:\n>>> '))
            self.clean_cup = add_clean_cup + self.clean_cup
            add_money = int(input(f'Write how many of money do you want to add:\n>>> '))
            self.money = add_money + self.money
            print(f'''{self.water} of water  |  {self.milk} of milk  |  {self.beans} of coffee beans  |\
{self.clean_cup} of disposable cups''')
            choose = int(input(f'Do u wanna add more ingredients?  1 - Yes  | 2 - Main Menu\n>>> '))
            if choose == 1:
                self.fill()
            if choose == 2:
                self.option()
        if choose == 2:
            self.option()

    def take(self):
        print(f'Money in bank: {self.money}')
        choose = int(input(f'Do u wanna take money?  1 - Yes  ||  2 - Main Menu\n>>> '))
        if choose == 1:
            if self.money == 0:
                print('no money')
                self.take()
            elif self.money > 0:
                self.money = self.money - self.money + 1000
                print('Money received successfully')
                self.take()
        elif choose == 2:
            self.option()

    def remaining(self):
        print(f'''The coffee machine has:
    {self.water} of water  |  {self.milk} of milk  |  {self.beans} of coffee beans  |  {self.clean_cup} \
    of disposable cups  |  {self.money} of money
    ''')
        choose = int(input(f'Do u wanna add ingredients?  1 - Add ingredients  | 2 - Main Menu\n>>> '))
        if choose == 1:
            self.fill()
        if choose == 2:
            self.option()

    def save(self):
        file = open('save.txt', 'r')
        lines = file.readlines()
        try:
            if os.stat("save.txt").st_size == 0:
                file.close()
                self.water = random.randint(25000, 50000)
                self.milk = random.randint(10000, 25000)
                self.beans = random.randint(2500, 6000)
                self.clean_cup = random.randint(60, 120)
                self.money = random.randint(3000, 7000)
                file = open('save.txt', 'w')
                file.write(str(self.water) + f'\n')
                file.write(str(self.milk) + f'\n')
                file.write(str(self.beans) + f'\n')
                file.write(str(self.clean_cup) + f'\n')
                file.write(str(self.money) + f'\n')
                file.close()
            else:
                file = open('save.txt')
                self.water = int(lines[0])
                self.milk = int(lines[1])
                self.beans = int(lines[2])
                self.clean_cup = int(lines[3])
                self.money = int(lines[4])
                file.close()

        finally:
            self.option()


CoffeeMachine()
