# specimen of sudoku
sudokuBoard = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
# a method to print the sudoku
def print_board(sd):
    # separate every 3 rows
    for i in range(0,len(sd)):
        if i % 3 == 0:
            print("- - - - - - - - - - - - - ")
            # separate every 3 columns
        for j in range(0,len(sd)):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(sd[i][j])
            else:
                print(str(sd[i][j]) + " ", end="")

# print sudoku
print_board(sudokuBoard)

def find_empty(sd):
    for i in range(len(sd)):
        for j in range(len(sd)):
            if sd[i][j] == 0:
                return (i, j)



def solve(sd):
    find = find_empty(sd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(sd, i, (row, col)):
            sd[row][col] = i

            if solve(sd):
                return True

            sd[row][col] = 0

    return False


def valid(sd, num, pos):
    # Check row
    for i in range(len(sd[0])):
        if sd[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(sd)):
        if sd[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if sd[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(sd):
    for i in range(len(sd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(sd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(sd[i][j])
            else:
                print(str(sd[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

solve(sudokuBoard)

print("************************************************************")

print_board(sudokuBoard)
