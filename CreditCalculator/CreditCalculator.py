import math


class CreditCalculator:

    def __init__(self):
        self.select()

    def option(self):
        choose = input(f'''
What do you want to calculate?
type "1" for number of monthly payments,
type "2" for annuity monthly payment amount,
type "3" for loan principal:
>>>''')
        if choose != choose.isnumeric():
            if choose == '1':
                self.number_of_monthly_payments()

            elif choose == '2':
                self.annuity_payment()

            elif choose == '3':
                self.loan_principal()
            else:
                print('Try Again!')
                self.option()
        else:
            print('Try Again!')
            self.option()

    def number_of_monthly_payments(self):
        principal = (input('Enter the loan principal:\n>>> '))
        per_month = int(input('Enter the monthly payment:\n>>> '))
        loan = int(input('Enter the loan interest:\n>>> '))
        if principal.isnumeric():
            interest = loan / (12 * 100)
            try:
                months = math.log((per_month / (per_month - (interest * int(principal)))), interest + 1)
                years = int(months / 12)
                month = math.ceil(months % 12)
                if years > 1 and month > 0:
                    print(f'It will take {years} years and {month} months to repay this loan!')
                    self.select()
                elif months < 12:
                    print(f'It will take {month} months to repay this loan!')
                    self.select()
                elif years > 0 and month == 0:
                    print(f'It will take {years} years to repay this loan!')
                    self.select()
            except ValueError:
                print('Try again!')
                self.option()

    def annuity_payment(self):
        try:
            principal = int(input('Enter the loan principal:\n>>> '))
            periods = int(input('Enter the number of periods:\n>>> '))
            loan = int(input('Enter the loan interest:\n>>> '))
            interest = loan / (12 * 100)
            monthly_payment = math.ceil((interest * pow(1 + interest, periods) / (pow(1 + interest, periods) - 1))
                                        * principal)
            print(f'Your monthly payment = {monthly_payment}!')
            self.select()
        except ValueError:
            print("Try again!")
            self.annuity_payment()

    def loan_principal(self):
        try:
            per_payment = float(input('Enter the annuity payment:\n>>> '))
            count_month = int(input('Enter the number of periods:\n>>> '))
            loan = float(input('Enter the loan interest:\n>>> '))
            interest = loan / (12 * 100)
            principal = int(per_payment /
                            ((pow(1 + interest, count_month) * interest) / (pow(1 + interest, count_month) - 1)))
            print(f'Your loan principal = {principal}!')
            self.select()
        except ValueError:
            print('Try Again!')
            self.loan_principal()

    def diff(self):
        try:
            principal = int(input("Enter the loan principal:"))
            periods = int(input("Enter the number of periods:"))
            interest = float(input("Enter the loan interest:"))
            interest = interest / (12 * 100)
            overpayment = 0
            for month in range(1, periods + 1):
                difference = math.ceil((principal / periods) + interest * (principal -
                                                                           ((principal * (month - 1)) / periods)))
                print(f"Month {month}: payment is {difference}")
                overpayment = overpayment + difference
                continue
            print(f"Overpayment = {overpayment - principal}")
            self.select()
        except ValueError:
            self.diff()

    def select(self):
        choose = input('Just calculate or DIff?? 1 - calculate || 2 - diff\n>>> ')
        if choose == '1':
            self.option()
        elif choose == '2':
            self.diff()
        else:
            print("Try Again!")
            self.select()


CreditCalculator()
