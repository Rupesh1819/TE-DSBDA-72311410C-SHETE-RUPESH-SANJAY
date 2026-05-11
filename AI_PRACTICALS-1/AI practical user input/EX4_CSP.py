# N-Queens Problem using Backtracking with User Input

"""
Time Complexity

Worst Case:
O(N!)

Because many possible arrangements are checked.

Space Complexity
O(N²)

Due to chessboard storage.
"""

# ---------------- USER INPUT ---------------- #

N = int(input("Enter value of N: "))

# Create empty chessboard
board = [[0] * N for _ in range(N)]


# ---------------- CHECK SAFE POSITION ---------------- #

def is_safe(row, col):

    # Check left side
    for i in range(col):

        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i, j = row, col

    while i >= 0 and j >= 0:

        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Check lower diagonal
    i, j = row, col

    while i < N and j >= 0:

        if board[i][j] == 1:
            return False

        i += 1
        j -= 1

    return True


# ---------------- BACKTRACKING FUNCTION ---------------- #

def solve(col):

    # All queens placed
    if col >= N:
        return True

    # Try every row
    for row in range(N):

        # Check safe position
        if is_safe(row, col):

            # Place queen
            board[row][col] = 1

            # Recursive call
            if solve(col + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# ---------------- DISPLAY BOARD ---------------- #

def print_board():

    print("\nSolution Found:\n")

    for row in board:

        for cell in row:

            if cell == 1:
                print("Q", end=" ")

            else:
                print(".", end=" ")

        print()


# ---------------- MAIN PROGRAM ---------------- #

if solve(0):

    print_board()

else:

    print("\nNo Solution Exists")