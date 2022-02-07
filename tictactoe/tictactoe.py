def info(game):
    print(f'''
-------
| {"".join(map(str, game))[0:3]} |\n| {"".join(map(str, game))[3:6]} |\n| \
{"".join(map(str, game))[6:9]} |
-------
''')


class TicTacToe:
    def __init__(self):
        game = list(['_', '_', '_', '_', '_', '_', '_', '_', '_'])
        choose = list()
        print(f'''TicTacToe''')
        info(game)
        x_player = 'X'
        o_player = 'O'
        winner = 0
        buf = x_player
        self.play(x_player, o_player, winner, buf, choose)

    def restart(self, choose, x_player, o_player, winner, buf):
        restart = str(input('Do you wanna play again?  1 -- Restart  ||  2 -- Exit\n>>> '))

        if restart.isnumeric():
            restart = int(restart)
            if restart == 1:
                choose.clear()
                self.play(x_player, o_player, winner, buf, choose)
            elif restart == 2:
                print('GoodBye')
            else:
                print('Try Again')
                self.restart(choose, x_player, o_player, winner, buf)
        else:
            print('Try again!')
            self.restart(choose, x_player, o_player, winner, buf)

    def play(self, x_player, o_player, winner, buf, choose):
        game = list(['_', '_', '_', '_', '_', '_', '_', '_', '_'])
        while True:
            word = "".join(map(str, game))
            if game[0] == 'X' and game[1] == 'X' and game[2] == 'X' or \
                    game[0] == 'X' and game[3] == 'X' and game[6] == 'X' or\
                    game[0] == 'X' and game[4] == 'X' and game[8] == 'X' or\
                    game[2] == 'X' and game[5] == 'X' and game[8] == 'X' or\
                    game[2] == 'X' and game[4] == 'X' and game[6] == 'X' or\
                    game[6] == 'X' and game[7] == 'X' and game[8] == 'X' or\
                    game[1] == 'X' and game[4] == 'X' and game[7] == 'X' or\
                    game[3] == 'X' and game[4] == 'X' and game[5] == 'X':
                print('X WIN')
                winner = 1
                break
            elif game[0] == 'O' and game[1] == 'O' and game[2] == 'O' or\
                    game[0] == 'O' and game[3] == 'O' and game[6] == 'O' or\
                    game[0] == 'O' and game[4] == 'O' and game[8] == 'O' or\
                    game[2] == 'O' and game[5] == 'O' and game[8] == 'O' or\
                    game[2] == 'O' and game[4] == 'O' and game[6] == 'O' or\
                    game[6] == 'O' and game[7] == 'O' and game[8] == 'O' or\
                    game[1] == 'O' and game[4] == 'O' and game[7] == 'O' or\
                    game[3] == 'O' and game[4] == 'O' and game[5] == 'O':
                print('O WIN')
                winner = 1
                break
            elif '_' not in game and winner == 0:
                print('Draw')
                break
            print(f'Enter cells: {word}')
            player = str(input(f'Enter {buf}\nCoordinates:>>> '))
            split_player = ''.join(player.split())
            coordinates = {'1 1': 0, '1 2': 1, '1 3': 2, '2 1': 3, '2 2': 4, '2 3': 5, '3 1': 6, '3 2': 7, '3 3': 8}
            numbers = ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']
            if player.isnumeric():
                print('Unknown, pls enter coordinates!!!')
                info(game)
                continue
            elif str(player) not in str(numbers) and player != player.isnumeric():
                print('Coordinates should be from 1 to 3!')
                info(game)
                continue
            elif split_player.isnumeric():
                pop = coordinates[player]
            else:
                print('You should enter numbers!')
                info(game)
                continue
            if pop < 0 or pop > 8:
                print('Unknown')
                continue
            elif pop in choose:
                print('This cell is occupied! Choose another one!')
                info(game)
                continue
            else:
                choose.append(pop)
                game.pop(pop)
                game.insert(pop, buf)
                info(game)
                if buf == x_player:
                    buf = o_player
                elif buf == o_player:
                    buf = x_player
        winner = 0
        self.restart(choose, x_player, o_player, winner, buf)


TicTacToe()
