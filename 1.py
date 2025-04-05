import numpy as np

def is_safe(board, row, col):
    """Check if a queen can be placed at board[row][col] without being attacked."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n=8):
    """Find a valid placement of 8 queens on an 8x8 board using numpy."""
    board = np.full(n, -1)
    rows = np.arange(n)
    np.random.shuffle(rows)  # Randomize row order
    
    def place_queens(row):
        if row == n:
            return True
        cols = np.arange(n)
        np.random.shuffle(cols)  # Randomize column order
        for col in cols:
            if is_safe(board, row, col):
                board[row] = col
                if place_queens(row + 1):
                    return True
        return False
    
    while not place_queens(0):
        np.random.shuffle(rows)  # Reshuffle if a valid placement isn't found
    
    return board

def print_board(board):
    """Print the board with queens placed."""
    n = len(board)
    for row in range(n):
        line = np.array(["Q" if board[row] == col else "." for col in range(n)])
        print(" ".join(line))

def main():
    board = solve_n_queens()
    print("Randomly placed valid solution for 8-Queens problem:")
    print_board(board)

if __name__ == "__main__":
    main()
