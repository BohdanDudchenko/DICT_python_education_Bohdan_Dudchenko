import random


class DinnerParty:
    def __init__(self, users):
        self.users = users
        self.start()

    def start(self):
        choose = int(input("Start?  1 - Yes ||  2 - No\n>>> "))
        try:
            if choose == 1:
                self.invite()
            elif choose == 2:
                print('Goodbye!')
            else:
                print('Goodbye!')
        except ValueError:
            print('TryAgain!')
            self.start()

    # Выбираем кого хотели бы видить на празднике
    def invite(self):
        amount = int(input('Enter the number of friends joining (including you):\n>>> '))
        try:
            if amount <= 0:
                print('No one is joining for the party')
            else:
                print('Enter the name of every friend (including you), each on a new line:')
                print(f'Name 1 - Me')
                for i in range(1, amount):
                    user = input(f'Name {i + 1} - ')
                    self.users[user] = user
                for key, value in self.users.items():
                    self.users[key] = 0
                self.total(amount)
        except ValueError:
            print('TryAgain!')
            self.invite()

    # Подсчитываем сколько каждый должен заплатить
    def total(self, amount):
        try:
            bank = float(input("Enter the total amount"))
            bank = float(bank)
            total_lucky = float(bank)
            bank = round(float(bank / amount), 2)
            for key, value in self.users.items():
                self.users[key] = bank
            self.lucky(amount, total_lucky)
        except ValueError:
            print('TryAgain!')
            self.total(amount)

    # Функция выбора счасливчика, который не платит за праздник
    def lucky(self, amount, total_lucky):

        print(self.users)
        choose = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n>>> ')
        if choose == 'Yes':
            bank = round(float(total_lucky / (amount - 1)), 2)
            keys = []
            for key, value in self.users.items():
                keys.append(key)
            luck = random.choice(keys)
            print(f'{luck} is the lucky one!')
            for key, value in self.users.items():
                self.users[key] = bank
            self.users[luck] = 0
            print(self.users)


DinnerParty({'Me': 0})