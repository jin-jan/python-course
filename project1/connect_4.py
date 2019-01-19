#!/usr/local/bin/python3
from termcolor import colored, cprint
"""
Connect 4
|x|x|x|x|x|x|x|
---------------
|x|x|x|x|x|x|x|
---------------
|x|x|x|x|x|x|x|
---------------
|x|x|x|x|x|x|x|
---------------
|x|x|x|x|x|x|x|
---------------
|x|x|x|x|x|x|x|
---------------

"""
ROWS = 12
COLUMNS = 15

game = [[" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "]]

print_x = lambda x : cprint(x, 'red', 'on_white', attrs=['bold'], end="")
print_o = lambda x : cprint(x, 'blue', 'on_white', attrs=['bold'], end="")
ellipse = u'\u2B2E'


def print_board(game):
    for row in range(ROWS):
        new_row = int(row/2)
        if row % 2 == 0:
            for col in range(COLUMNS):
                new_col = int(col/2)
                if col % 2 == 0:
                    if col != COLUMNS-1:
                        cprint("|", 'green', 'on_cyan', end="")
                    else:
                        cprint("|", 'green', 'on_cyan')
                else:
                    if game[new_col][new_row] == 'X':
                        print_x(ellipse)
                    elif game[new_col][new_row] == 'O':
                        print_o(ellipse)
                    else:
                        print_o(game[new_col][new_row])
        else:
            cprint("-" * COLUMNS, 'green', 'on_cyan')
    return True


def check_winner(column, game):
    depth = 3
    num_check = 4
    row_elem = 5
    for check in range(depth):
        check_ver_list = game[column][check:check + num_check]
        win_ver_x = [i == "X" for i in check_ver_list]
        win_ver_o = [i == "O" for i in check_ver_list]
        if all(win_ver_x) or all(win_ver_o):
            return True

    for check in range(num_check):
        hor_list = game[check:check + num_check]
        for row_hor in range(row_elem, -1, -1):
            check_hor_list = [hor_list[i][row_hor] for i in range(num_check)]
            win_hor_x = [i == "X" for i in check_hor_list]
            win_hor_o = [i == "O" for i in check_hor_list]
            if all(win_hor_x) or all(win_hor_o):
                return True

    col = [i for i in range(len(game))]
    row_right = [i for i in range(row_elem, -1, -1)]
    row_left = [i for i in range(len(game[column]))]
    dia_right = []
    dia_left = []

    for i in range(num_check):
        for j in range(depth):
            for k in range(num_check):
                dia_right += [game[col[k+i]][row_right[k+j]]]
                dia_left += [game[col[k+i]][row_left[k+j]]]
            win_dia_right_x = [i == "X" for i in dia_right]
            win_dia_right_o = [i == "O" for i in dia_right]
            win_dia_left_x = [i == "X" for i in dia_left]
            win_dia_left_o = [i == "O" for i in dia_left]
            if all(win_dia_right_x) or all(win_dia_right_o):
                return True
            if all(win_dia_left_x) or all(win_dia_left_o):
                return True
            dia_right = []
            dia_left = []


def main():
    player = 1
    winner = False
    player_x = colored('Where do you want to put your piece?: ', 'red', attrs=['bold', 'reverse'])
    player_o = colored('Where do you want to put your piece?: ', 'blue', attrs=['bold', 'reverse'])
    while not winner:
        if player == 1:
            try:
                column = int(input(player_x)) - 1
                if column < 0 or column >= len(game):
                    print("Wrong column, try again")
                else:
                    for row in range(len(game[column]), 0, -1):
                        row_limit = row - 1
                        if game[column][row_limit] == " ":
                            game[column][row_limit] = "X"
                            if check_winner(column, game):
                                print("Winner")
                                winner = True
                            print_board(game)
                            player = 2
                            break
            except ValueError:
                print("Wrong value, try again")

        else:
            try:
                column = int(input(player_o)) - 1
                if column < 0 or column >= len(game):
                    print("Wrong column, try again")
                else:
                    for row in range(len(game[column]), 0, -1):
                        row_limit = row - 1
                        if game[column][row_limit] == " ":
                            game[column][row_limit] = "O"
                            if check_winner(column, game):
                                print("Winner")
                                winner = True
                            print_board(game)
                            player = 1
                            break
            except ValueError:
                print("Wrong value, try again")


main()
