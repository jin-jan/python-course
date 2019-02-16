import shutil

def get_stty_size():
    cols, rows = shutil.get_terminal_size()
    if rows%2 == 0:
        rows = rows - 1
    if cols%2 == 0:
        cols = cols - 1
    if rows != cols:
        cols = rows
    return rows, cols

def play_board(rows, cols):
    try:
        if rows%2 == 0 and cols%2 == 0:
            return False
        if type(rows) != int:
            return False
        if type(cols) != int:
            return False
        if rows != cols:
            return False
        for row in range(rows):
            if row%2 == 0:
                for col in range(1, cols+1):
                    if col%2 == 0:
                        print("|", end=" ")
                    else:
                        if col != cols:
                            print(" ", end=" ")
                        else:
                            print(" ")
            else:
                print("-"*(rows+rows))
        return True
    except TypeError as e:
        return False

play_board(3,3)
print("\n")
play_board(5,5)
print("\n")
play_board(5,6)
print("\n")
play_board(8,8)
print("\n")
play_board(9,9)
print("\n")
rows, cols = get_stty_size()
play_board(rows, cols)
print("\n")
