#
# # --------------------ДЗ Крестики нолики------------------------------------------
# # Напишите класс TicTacToeBoard для игры в крестики-нолики, который должен иметь следующие методы:
# # new_game() – для создания новой игры;
# # get_field() – для получения поля (список списков);
# # check_field() – для проверки, есть ли победитель, который возвращает X,
# # если победил первый игрок, 0, если второй, D, если ничья и None, если можно продолжать игру;
#
# # make_move(row, col) – который устанавливает значение текущего хода в ячейку поля с координатами row, col,
# # если это возможно, «переключает» ход игрока, а также возвращает сообщение «Победил игрок X» при победе крестиков,
# # «Победил игрок 0» при победе ноликов, «Ничья» в случае ничьей и «Продолжаем играть», если победитель после
# # данного хода неопределён.
# # Кроме того, метод make_move должен возвращать сообщение «Клетка <row>, <col> уже занята», если в клетке уже
# # стоит крестик или нолик, и «Игра уже завершена», если в текущей игре уже выявлен победитель или закончились
# # ячейки для ходов.
# # При создании объекта класса должна создаваться новая игра.
# # Аргументы row и col метода make_move могут принимать значения от 1 до 3.
#
#        if self.field[row - 1][col - 1] != '-':
#             return f'Клетка {row}, {col} уже занята'
#        else:

class TicTacToeBoard:
    def __init__(self):
        self.bool_player = True
        self.player = 'X'
        self.field = [['-', '_', '-'], ['-', '_', '-'], ['-', '_', '-']]
        self.field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def new_game(self):
        self.field = [['-', '_', '-'], ['-', '_', '-'], ['-', '_', '-']]
        self.field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def get_field(self):
        return self.field


    def check_field(self):
        if ((self.field[0][0] and self.field[1][0] and self.field[2][0])
            or (self.field[0][1] and self.field[1][1] and self.field[2][1])
            or (self.field[0][2] and self.field[1][2] and self.field[2][2])
            or (self.field[0][0] and self.field[1][1] and self.field[2][2])
            or (self.field[0][2] and self.field[1][1] and self.field[2][0])) == self.player:
            print(f'Winner {self.player}')
            print(*self.get_field(), sep="\n")
            self.new_game()
        elif '-' not in (self.field[0] and self.field[1] and self.field[2]):
            print('Ничья')
            print(*self.get_field(), sep="\n")
            self.new_game()


    def make_move(self, row, col):
        if self.bool_player:
            if self.field[row - 1][col - 1] != '-':
                return f'Клетка {row}, {col} уже занята'
            else:
                print('Продолжаем играть')
                self.field[row - 1][col - 1] = self.player
                self.player = 'O'
                self.bool_player = False
        else:
            if self.field[row - 1][col - 1] != '-':
                return f'Клетка {row}, {col} уже занята'
            else:
                print('Продолжаем играть')
                self.field[row - 1][col - 1] = self.player
                self.player = 'X'
                self.bool_player = True
        self.check_field()


board = TicTacToeBoard()

print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")

# =================================Решение с семинара================================================
# class TicTacToeBoard:
#
#     def __init__(self):
#         self.field = []
#         for row in range(3):
#             r = []
#             for col in range(3):
#                 r.append('-')
#             self.field.append(r)
#         self.move_x = True
#         self.end_of_game = False
#         self.winner = None
#         self.win = ''
#         self.first_move = True
#
#     def new_game(self):
#         self.field = []
#         for row in range(3):
#             r = []
#             for col in range(3):
#                 r.append('-')
#             self.field.append(r)
#             self.move_x = True
#             self.end_of_game = False
#             self.winner = None
#             self.win = ''
#             self.first_move = True
#
#     def get_field(self):
#         return self.field
#
#     def check_field(self):
#         if self.win == 'X':
#             return 'X'
#         elif self.win == 'O':
#             return 'O'
#         elif self.win == 'ничья':
#             return 'D'
#         else:
#             return None
#
#     def make_move(self, row, col):
#         if self.end_of_game and not self.first_move:
#             return 'Игра уже завершена'
#         else:
#             if self.field[row - 1][col - 1] != '-':
#                 return f'Клетка {row}, {col} уже занята'
#             else:
#                 if self.move_x:
#                     self.field[row - 1][col - 1] = 'X'
#                     self.move_x = False
#                     self.first_move = False
#                 else:
#                     self.field[row - 1][col - 1] = 'O'
#                     self.move_x = True
#                     self.first_move = False
#             if self.field[0].count(self.field[0][0]) == 3 and self.field[0][0] != '-':
#                 self.end_of_game = True
#                 self.win = self.field[0][0]
#                 return f'Победил игрок {self.field[0][0]}'
#             elif self.field[1].count(self.field[1][0]) == 3 and self.field[1][0] != '-':
#                 self.end_of_game = True
#                 self.win = self.field[1][0]
#                 return f'Победил игрок {self.field[1][0]}'
#             elif self.field[2].count(self.field[2][0]) == 3 and self.field[2][0] != '-':
#                 self.end_of_game = True
#                 self.win = self.field[2][0]
#                 return f'Победил игрок {self.field[2][0]}'
#             elif self.field[0][0] == self.field[1][0] == self.field[2][0] and self.field[0][0] != '-':
#                 self.end_of_game = True
#                 self.win = self.field[0][0]
#                 return f'Победил игрок {self.field[0][0]}'
#             elif self.field[0][1] == self.field[1][1] == self.field[2][1] and self.field[0][1] != '-':
#                 self.end_of_game = True
#                 self.win = self.field[0][1]
#                 return f'Победил игрок {self.field[0][1]}'
#             elif self.field[0][2] == self.field[1][2] == self.field[2][2] and self.field[0][2] != '-':
#                 self.end_of_game = True
#                 self.win = self.field[0][2]
#                 return f'Победил игрок {self.field[0][2]}'
#             elif self.field[0][0] == self.field[1][1] == self.field[2][2] and self.field[0][0] != '-':
#                 self.end_of_game = True
#                 self.win = self.field[0][0]
#                 return f'Победил игрок {self.field[0][0]}'
#             elif self.field[2][0] == self.field[1][1] == self.field[0][2] and self.field[2][0] != '-':
#                 self.end_of_game = True
#                 self.win = self.field[2][0]
#                 return f'Победил игрок {self.field[2][0]}'
#             elif self.field[0].count('-') == 3 and self.field[1].count('-') == 3 and self.field[2].count('-'):
#                 self.end_of_game = True
#                 self.win = 'ничья'
#                 return 'Ничья'
#             else:
#                 return 'Продолжаем играть'
#
#
# board = TicTacToeBoard()
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(board.make_move(1, 2))
# print(*board.get_field(), sep="\n")
# print(board.make_move(2, 1))
# print(board.make_move(2, 2))
# print(board.make_move(3, 1))
# print(board.make_move(2, 2))
# print(*board.get_field(), sep="\n")
# ===========================================================


# class SeaMap():
#
#     def __init__(self):
#         self.map = []
#         for row in range(10):
#             r = []
#             for col in range(10):
#                 r.append('-')
#             self.map.append(r)
#         print(*self.map, sep="\n")
#
# def cell(self):
#     return self.map
#
# def died(self, row, col):
#     if row - 1 != 0 and row != 10 and col - 1 != 0 and col != 10:
#         if self.map[row - 2][col - 1] == 'x':
#             self.died(row - 2, col - 1)
#         if self.map[row][col - 1] == 'x':
#             self.died(row, col - 1)
#         if self.map[row - 1][col - 2] == 'x':
#             self.died(row - 1, col - 2)
#         if self.map[row - 1][col] == 'x':
#             self.died(row - 1, col)

# if self.map[row - 2][col - 1] == '-' or '*':
#     self.map[row - 2][col] = '*'
#     self.map[row - 2][col + 1] = '*'
#     self.map[row - 2][col - 1] = '*'
#
# if self.map[row][col - 1] == '-' or '*':
#     self.map[row][col] = '*'
#     self.map[row][col + 1] = '*'
#     self.map[row][col - 1] = '*'
#
# if self.map[row - 1][col - 2] == '-' or '*':
#     self.map[row - 1][col - 2] = '*'
#     self.map[row][col - 2] = '*'
#     self.map[row + 1][col - 2] = '*'
#
# if self.map[row - 1][col] == '-' or '*':
#     self.map[row - 1][col] = '*'
#     self.map[row][col] = '*'
#     self.map[row + 1][col] = '*'
# else:
#     pass
#
# def shoot(self, row, col, result):
#     if result == 'miss':
#         self.map[row - 1][col - 1] = '*'
#     if result == 'hit':
#         self.map[row - 1][col - 1] = 'x'
#     if result == 'sink':
#         self.map[row - 1][col - 1] = 'x'
#         self.died(row, col)
#
#
# sm = SeaMap()
# sm.shoot(5, 6, 'hit')
# sm.shoot(5, 4, 'hit')
# sm.shoot(5, 5, 'sink')
# for row in range(10):
#     for col in range(10):
#         print(sm.cell(row, col), end=" ")
#     print()
# print(*sm.cell(), sep='\n')
#
