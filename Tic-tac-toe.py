class Player:

    def __init__(self, name):
        self.name = name

    def choose(self, num):
        game.label()
        cell = int(input('Выберите ячейку: '))
        while True:
            if game.matrix[cell - 1] == 'x' or game.matrix[cell - 1] == 'o':
                print('Данная ячейка уже занята!')
                cell = int(input('Выберите ячейку: '))
            else:
                break
        if num == 1:
            game.matrix[cell - 1] = 'x'
        else:
            game.matrix[cell - 1] = 'o'
        return game.matrix


class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def label(self):
        print(f'╔═══╦═══╦═══╗\n║ {game.matrix[0]} ║ {self.matrix[1]} ║ {self.matrix[2]} ║\n║ {self.matrix[3]} ║'
              f' {self.matrix[4]} ║ {self.matrix[5]} ║\n║ {self.matrix[6]} ║ {self.matrix[7]} ║'
              f' {self.matrix[8]} ║\n╚═══╩═══╩═══╝')

    def get_winner(self):
        if self.matrix[:3].count('x') == 3 or self.matrix[:3].count('o') == 3:
            return True
        elif self.matrix[3:6].count('x') == 3 or self.matrix[3:6].count('o') == 3:
            return True
        elif self.matrix[6:].count('x') == 3 or self.matrix[6:].count('o') == 3:
            return True
        elif self.matrix[::3].count('x') == 3 or self.matrix[::3].count('o') == 3:
            return True
        elif self.matrix[1::3].count('x') == 3 or self.matrix[1::3].count('o') == 3:
            return True
        elif self.matrix[2::3].count('x') == 3 or self.matrix[2::3].count('o') == 3:
            return True
        elif self.matrix[::4].count('x') == 3 or self.matrix[::4].count('o') == 3:
            return True
        else:
            return False

    def play(self):
        print(f'╔{'═' * 36}╗', '║ Игра в крестики-нолики начинается! ║', f'╚{'═' * 36}╝', sep='\n')
        while True:
            print(f'Ход игрока: {self.player_1.name}!')
            self.player_1.choose(1)
            if self.get_winner():
                self.label()
                print(f'Игрок по имени: {self.player_1.name} - победитель кубка 2024 года!!!')
                break
            print(f'Ход игрока: {self.player_2.name}!')
            self.player_2.choose(2)
            if self.get_winner():
                self.label()
                print(f'Игрок по имени: {self.player_2.name} - победитель кубка 2024 года!!!')
                break
            if 9 not in game.matrix and 1 not in game.matrix and 2 not in game.matrix and 3 not in game.matrix and 4 \
                    not in game.matrix and 5 \
                    not in game.matrix and 6 not in game.matrix and 7 not in game.matrix and 8 not in game.matrix:
                self.label()
                print('Объявлена ничья! Победителя обнаружить не удалось... =(')
                break


player_1 = Player(input('Введите имя первого игрока: '))
player_2 = Player(input('Введите имя второго игрока: '))
game = Game(player_1, player_2)
game.play()
