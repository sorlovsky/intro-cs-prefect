test =    [ [5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9] ]

test1 =    [ [3,5,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9] ]

testRow = [3,4,5,2,8,6,1,7,9]


'''
Helper function that returns whether row data is unique. Takes list (row)
'''
def isUnique(row):
    for i in range(len(row)):
        currentCount = 0
        currentNumber = row[i]
        for j in range(len(row)):
            if row[j] == currentNumber:
                currentCount += 1
        if currentCount > 1:
            return False
    return True

'''
Takes in a board and returns its columns as an array of lists
'''
def getCols(board):
    columns = [[],[],[],[],[],[],[],[],[]]
    column = []

    for i in range(len(board)):
        for j in range(len(board)):
            columns[i].append(board[j][i])

    return columns

'''
Takes a board and returns list of subboards
'''
def splitBoard(board):
    miniBoard = [[],[],[]]
    for i in range(len(board)):
        for j in range(len(board)):



def isValid(board):
    # Sanitize User Data
    if len(board) != 9:
        return "Invalid number of rows"

    for i in range(len(board)):
        if len(board[i]) != 9:
            return "Invalid number of columns"


    # Loop through rows to make sure each row is unique
    for i in range(len(board)):
        if not isUnique(board[i]):
            return "Row {} is not unique".format(i+1)

    # Loop through columns to make each is column is unique
    columns = getCols(board)
    for i in range(len(columns)):
        if not isUnique(columns[i]):
            return "Column {} is not unique".format(i+1)

    return "Valid board"



def main():
    print(isValid(test1))

main()
