#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""
import sys


def generate_solutions(n):
    """Generate all valid solutions for the N-Queens problem."""
    solutions = [[]]
    for row in range(n):
        solutions = place_queen(row, n, solutions)
    return solutions


def place_queen(row, n, solutions):
    """Place a queen on the board and return all valid board configurations."""
    new_solutions = []
    for solution in solutions:
        for col in range(n):
            if is_safe(row, col, solution):
                new_solutions.append(solution + [col])
    return new_solutions


def is_safe(row, col, solution):
    """Check if a queen can be safely placed at the given row and column."""
    for r in range(row):
        if solution[r] == col or abs(solution[r] - col) == abs(r - row):
            return False
    return True


def get_board_size():
    """Parse the board size from command-line arguments and validate it."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def solve_n_queens():
    """Solve the N-Queens problem and print all solutions."""
    n = get_board_size()
    solutions = generate_solutions(n)
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])


if __name__ == '__main__':
    solve_n_queens()

