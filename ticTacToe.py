import random
import os
import platform


class TicTacToe:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.done = ""

    def printBoard(self):
        print("")
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("-----------")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("-----------")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])

    def reset(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.done = ""

    def checkWinOrDraw(self):
        dict_win = {}

        for i in ["X", "O"]:
            # HORIZONTAIS
            dict_win[i] = (self.board[0][0] == i and self.board[0][1] == i and self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == i and self.board[1][1] == i and self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == i and self.board[2][1] == i and self.board[2][2] == i) or dict_win[i]

            # VERTICAIS
            dict_win[i] = (self.board[0][0] == i and self.board[1][0] == i and self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (self.board[0][1] == i and self.board[1][1] == i and self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == i and self.board[1][2] == i and self.board[2][2] == i) or dict_win[i]

            # Diagonais
            dict_win[i] = (self.board[0][0] == i and self.board[1][1] == i and self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == i and self.board[1][1] == i and self.board[0][2] == i) or dict_win[i]

        if dict_win["X"]:
            self.done = "X"
            print('X Venceu!')
            return
        elif dict_win["O"]:
            self.done = "O"
            print('O Venceu!')
            return

        c = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != " ":
                    c += 1
                    break

        if c == 0:
            self.done = "d"
            print('Draw!')

    def getPlayerMove(self):
        invalid_move = True
        while invalid_move:
            try:
                print('Digite a linha do seu próximo lance:')
                x = int(input())

                print('Digite a coluna do seu préximo lance:')
                y = int(input())

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print('Coordenadas inválidas!')
                if self.board[x][y] != " ":
                    print('Posição já preenchida.')
                    continue
            except Exception as e:
                print(e)
                continue

            invalid_move = False
        self.board[x][y] = "X"

    def makeMove(self):
        list_move = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    list_move.append((i, j))

        if len(list_move) > 0:
            x, y = random.choice(list_move)
            self.board[x][y] = "O"


tic_tac_toe = TicTacToe()
tic_tac_toe.printBoard()
next_move = 0


def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


while next_move == 0:
    clear_screen()
    tic_tac_toe.printBoard()
    while tic_tac_toe.done == "":
        tic_tac_toe.getPlayerMove()
        tic_tac_toe.makeMove()
        clear_screen()
        tic_tac_toe.printBoard()
        tic_tac_toe.checkWinOrDraw()

    print('Digite 1 para sair do jogo ou qualquer outro número para jogar novamente!')

    next_move = int(input())
    if next_move == 1:
        break
    else:
        tic_tac_toe.reset()
        next_move = 0

