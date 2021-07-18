board = [
    [0,4,0,0,0,0,0,2,9],
    [0,0,0,0,2,6,3,0,4],
    [0,2,1,4,3,0,0,0,0],
    [0,0,0,0,0,0,8,0,0],
    [0,0,0,9,8,7,4,3,1],
    [7,0,8,0,0,0,9,0,0],
    [0,7,0,5,0,8,2,4,0],
    [0,0,9,0,4,1,0,0,8],
    [0,8,0,0,6,0,0,0,0],
]


def print_board(brd):
#prints out a 9x9 sudoku board, brd is a 2d list input
    for i in range(len(brd)):
        if i == 3 or i == 6:
            print("---------------------")

        for j in range(len(brd)):
            if j == 3 or j == 6:
                print('| ',end='')

            if j == 8:
                print(brd[i][j])
                #end = '\n' since we are at the end of the row and need to print the next line
            else:
                print(brd[i][j],end=' ')



def empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd)):
            if brd[i][j] == 0:
                return (i, j)
                #row, col indices

    else:
        return None



def isValid(brd,i,j,num):

    #row check
    for x in range(len(brd)):
        if num == brd[i][x] and j != x:
            return False

    #column check
    for x in range(len(brd)):
        if num == brd[x][j] and i != x:
            return False

    #sub-grid check
    #i = 2, j = 4
    sub_row = i // 3 #=0
    sub_col = j // 3 #=1

    for x in range(sub_row*3, sub_row*3+3):
        for y in range(sub_col*3,sub_col*3+3):
            if brd[x][y] == num and (x,y) != (i,j):
                return False

    return True


def solve(brd):
    nxt = empty(brd)
    #base case when board has been filled up
    if nxt == None:
        return True
    else:
        i, j = nxt

    for val in range(1,10):
        if isValid(brd, i, j, val):
            brd[i][j] = val

            #recursively run solve again with the new value inputted
            if solve(brd) == True:
                #runs if board is full
                return True

            else:
                brd[i][j] = 0

    return False



print_board(board)
solve(board)
print('\n')
print_board(board)

