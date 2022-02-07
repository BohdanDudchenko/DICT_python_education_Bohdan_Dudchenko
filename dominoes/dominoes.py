import random


class Dominoes:
    def __init__(self, domino, player, cpu, start_piece, status, snake):
        self.domino = domino
        self.player = player
        self.cpu = cpu
        self.start_piece = start_piece
        self.status = status
        self.snake = snake
        # СТАНДАРТНЫЕ ДОМИНОШКИ
        self.hangout()
        # Раздача игроку
        self.player_pieces()
        # Раздача Комп
        self.cpu_pieces()
        # Выбор первой костяшки
        self.first_piece()
        # Выбор первого игрока
        self.first_player()
        # Информация по игре
        self.info()
        # Информация на каждом шагу
        self.step_info()
        while len(self.player) > 0 or len(self.cpu) > 0:
            self.draw()
            self.player_win()
            self.cpu_win()
            if self.status == 'draw':
                print('Status: The game is over. It\'s a draw!')
                break

            elif self.status == 'player_win':
                print('Status: The game is over. Player WIN')
                break

            elif self.status == 'cpu_win':
                print('Status: The game is over. CPU WIN')
                break
            else:
                if self.status == 'player':
                    self.step_player()
                else:
                    if self.status == 'cpu':
                        self.step_cpu()

    def hangout(self):
        self.domino = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
                       [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
                       [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
                       [3, 3], [3, 4], [3, 5], [3, 6],
                       [4, 4], [4, 5], [4, 6],
                       [5, 5], [5, 6],
                       [6, 6]]
        return self.domino

    def player_pieces(self):
        for i in range(7):
            drop = random.choice(self.domino)
            self.player.append(drop)
            for j, k in enumerate(self.domino):
                if k == drop:
                    self.domino.pop(j)
        return self.player

    def cpu_pieces(self):
        for i in range(7):  # CPU
            drop = random.choice(self.domino)
            self.cpu.append(drop)
            for j, k in enumerate(self.domino):
                if k == drop:
                    self.domino.pop(j)
        return self.cpu

    def first_piece(self):
        double = [[6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]
        for j in range(len(double)):
            if double[j] in self.player:
                self.start_piece = double[j]
                for i, c in enumerate(self.player):
                    if double[j] == c:
                        self.player.pop(i)
                        continue
                break
            elif double[j] in self.cpu:
                self.start_piece = double[j]
                for i, c in enumerate(self.cpu):
                    if double[j] == c:
                        self.cpu.pop(i)
                        continue
                break
        self.snake.append(self.start_piece)
        return self.start_piece

    def first_player(self):
        if len(self.player) < 7:
            self.status = 'cpu'
        elif len(self.cpu) < 7:
            self.status = 'player'

        return self.status

    def info(self):
        print(f'''
Stock pieces # {len(self.domino)} 
Computer pieces # {len(self.cpu)} 
Player pieces # {len(self.player)}
Domino snake # {self.start_piece} 
Status # {self.status}
        ''')
        return 0

    def player_win(self):
        if len(self.player) < 1:
            self.status = 'player_win'
            return self.status

    def cpu_win(self):
        if len(self.cpu) < 1:
            self.status = 'cpu_win'
            return self.status

    def draw(self):
        if len(self.domino) < 1:
            return 0
        elif self.snake[0][0] == self.snake[-1][-1]:
            score = 0
            for i in range(len(self.snake)):
                for j in self.snake[i]:
                    if j == self.snake[0][0]:
                        score += 1
            if score == 8:
                self.status = 'draw'
            return self.status

    def step_info(self):
        print('=' * 70)
        print(f'Stock size: {len(self.domino)}')
        print(f'Computer pieces: {len(self.cpu)}')
        if len(self.snake) > 6:
            print("\n{}{}{}...{}{}{}\n".format(*self.snake[:3], *self.snake[-3:]))
        else:
            print(f'{self.snake}')
        print('Your pieces:')
        for i, c in enumerate(self.player):
            print(f'{i + 1}: {c}')
        print(f'\n')

    def step_player(self):
        self.step_info()
        print(f'Status: It\'s your turn to make a move. Enter your command.')
        points = []
        count = 0
        for i in range(7):
            for j in self.snake:
                for n in range(len(j)):
                    if i == j[n]:
                        count += 1
            points.append(count)
            count -= count
        new_points = {i: points[i] for i in range(len(points))}
        print(new_points)
        new_dict = []
        take = []
        count = 0
        for i in range(len(take)):
            for j in range(len(take[i])):
                count += new_points[take[i][j]]
            new_dict.append(count)
            count -= count
            action = {new_dict[i]: i for i in range(len(take))}
            print(action)

        place = input('>>>')
        if place == '0':
            try:
                self.status = 'cpu'
                add = random.choice(self.domino)
                self.player.append(add)
                self.domino.remove(add)
                self.step_info()
                self.step_cpu()
            except IndexError:
                self.status = 'draw'
                return self.status

        else:
            try:
                place.split()

                if place[0] == '-':
                    side_of = '-'
                    domino_number = int(place[1:])
                else:
                    side_of = '+'
                    domino_number = int(place[:])
                if domino_number <= len(self.player):
                    drop = self.player[domino_number - 1]

                    if side_of == '+':
                        if self.snake[-1][1] == drop[0]:
                            self.snake.append(drop)
                            self.player.remove(drop)
                            self.step_info()
                        elif self.snake[-1][1] == drop[1]:
                            reverse = drop
                            reverse[0], reverse[1] = reverse[1], reverse[0]
                            self.snake.append(reverse)
                            self.player.remove(drop)
                            self.step_info()

                        else:
                            print('Try again!')
                            self.step_player()

                    elif side_of == '-':
                        if self.snake[0][0] == drop[1]:
                            self.snake.insert(0, drop)
                            self.player.remove(drop)
                            self.step_info()
                        elif self.snake[0][0] == drop[0]:
                            reverse = drop
                            reverse[0], reverse[1] = reverse[1], reverse[0]
                            self.snake.insert(0, reverse)
                            self.player.remove(drop)
                            self.step_info()
                        else:
                            print('Try again!')
                            self.step_player()

                else:
                    print('Invalid input. Please try again.')
                    self.step_player()

                if len(self.player) < 1:
                    self.status = 'player_win'
                else:
                    self.status = 'cpu'
                return self.status

            except ValueError:
                self.step_player()

    def step_cpu(self):
        self.step_info()
        print('Status: Computer is about to make a move. Press Enter to continue...')
        enter = input()
        for i, c in enumerate(self.cpu):
            if c[0] == self.snake[0][0] or c[1] == self.snake[0][0]:
                reverse = c
                if c[0] == self.snake[0][0]:
                    reverse[0], reverse[1] = reverse[1], reverse[0]
                    self.snake.insert(0, reverse)
                    self.cpu.remove(c)
                elif c[1] == self.snake[0][0]:
                    self.snake.insert(0, c)
                    self.cpu.remove(c)
                break
            elif c[0] == self.snake[-1][1] or c[1] == self.snake[-1][1]:
                reverse = c
                if c[1] == self.snake[-1][1]:
                    reverse[0], reverse[1] = reverse[1], reverse[0]
                    self.snake.append(reverse)
                    self.cpu.remove(c)
                elif c[0] == self.snake[-1][1]:
                    self.snake.append(c)
                    self.cpu.remove(c)
                break
            elif self.snake[0][0] != c[0] and self.snake[0][0] != c[1] and self.snake[-1][1] != c[0]\
                    and self.snake[-1][1] != c[1] and c == self.cpu[-1]:
                try:
                    add = random.choice(self.domino)
                    self.cpu.append(add)
                    self.domino.remove(add)
                    break
                except IndexError:
                    break
        if len(self.cpu) < 1:
            self.status = 'cpu_win'
            return self.status
        self.status = 'player'
        self.step_player()


Dominoes([], [], [], [], '', [])

