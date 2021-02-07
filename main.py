# Initialize puzzle
puzzle = [
    [5, 8, 6, 4, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 8, 0, 0, 0, 4],
    [0, 0, 0, 9, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 9, 7, 2, 0],
    [0, 4, 0, 0, 5, 0, 0, 0, 1],
    [7, 0, 0, 0, 0, 0, 0, 6, 0],
    [0, 5, 0, 0, 3, 2, 0, 0, 0],
    [2, 0, 0, 0, 6, 0, 0, 0, 0]
]


# Define printGrid(puzzle) to print out the puzzle to the console in a more visible way
def printGrid(puzzle):

    # adds lines after the 3rd and 6th row.
    for i in range(9):
        if i == 3 or i == 6:
            print("------+------+------")

        # adds vertical lines after 3rd and 6th column
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(puzzle[i][j])
            else:
                print(str(puzzle[i][j]) + " ", end="")


# Define findEmpty(puzzle) to find the first empty cell in the puzzle row by row, where 0 = empty cell
def findEmpty(puzzle):

    # Loop through the puzzle row by row and find empty cells
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return None, None


# Define numberIsValid() to check if a given number will be valid according to sudoku rules in each cell.
# x, y will passed on from findEmpty() for the empty position
def numberIsValid(puzzle, x, y, num):
    # check if number is already found in the row
    row = puzzle[x]
    if num in row:
        return False

    # check if number is already found in the column
    col = []
    for i in range(9):
        col.append(puzzle[i][y])
        if num in col:
            return False

    # check if number is already found in each 3X3 square
    square_x = (x // 3) * 3
    square_y = (y // 3) * 3

    for i in range(square_x, square_x + 3):
        for j in range(square_y, square_y + 3):
            if puzzle[i][j] == num:
                return False
    return True


# Define solveGrid() to use the helper methods findEmpty() numberIsValid() to fill in all the empty slots by using
# backtracking.

def solveGrid(puzzle):
    x, y = findEmpty(puzzle)    # sets x and y to the position of the empty cells

    if x is None and y is None:     # if no cell is empty, returns true. Puzzle solved.
        return True

    # Try inputting numbers from 1-9 in the empty cell and check for validation.
    for i in range(1, 10):
        if numberIsValid(puzzle, x, y, i):  # If the number is valid, place it in that empty cell.
            puzzle[x][y] = i

            if solveGrid(puzzle):   # Calls the same solveGrid() function again to check for
                return True

        puzzle[x][y] = 0
    return False


print("---------------")
print("Original Puzzle")
print("---------------")
printGrid(puzzle)
solveGrid(puzzle)
print("")
print("")
print("---------------")
print("Solved Puzzle")
print("---------------")
printGrid(puzzle)
