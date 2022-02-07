class ChatBot:

    def __init__(self, age):
        self.age = age

        self.get_info()
        self.question()

    def get_info(self):
        bot_name = "Stepan"
        birth = "2021"
        print(f"Hello! My name is {bot_name}")
        print(f"I was created in {birth}")

        name = str(input(f"Please, remind me your name.\n>>> "))
        print(f"What a great name you have, {name}!")

        print("""
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
        """)
        remainder3 = int(input('>'))
        remainder5 = int(input('>'))
        remainder7 = int(input('>'))
        self.age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
        return self.age

    def question(self):
        if self.age == 0:
            self.get_info()
        else:
            print(f"Your age is {self.age}; that's a good time to start programming!")
            print("Now I will prove to you that I can count to any number you want.")
            num = int(input('>>> '))
            for i in range(num + 1):
                print(i, end="! \n")
            print("Completed, have a nice day!")

            print("Let's test your programming knowledge.")
            print("""
How many bytes are there in a kilobyte?
1. 256
2. 1024
3. 128
4. 825
""")
            self.answers()

    def answers(self):
        answer = int(input('>>> '))
        if answer == 2:
            print("Congratulations, have a nice day!")
        else:
            print("Please, try again.")
            self.answers()


ChatBot('')