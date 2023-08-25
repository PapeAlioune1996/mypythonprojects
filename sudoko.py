import random

def create_sudoku_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    return board

def is_valid_move(board, row, col, num):
    # Vérifier la validité de la valeur dans la ligne
    if num in board[row]:
        return False

    # Vérifier la validité de la valeur dans la colonne
    if num in [board[i][col] for i in range(9)]:
        return False

    # Vérifier la validité de la valeur dans le carré 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def fill_board(board):
    # Liste des chiffres possibles pour remplir les cellules vides
    digits = list(range(1, 10))

    # Remplir la grille en utilisant un algorithme de remplissage aléatoire récursif
    def fill_cell(row, col):
        if row == 9:
            return True

        next_row, next_col = row, col + 1
        if next_col == 9:
            next_row, next_col = row + 1, 0

        if board[row][col] != 0:
            return fill_cell(next_row, next_col)

        random.shuffle(digits)
        for num in digits:
            if is_valid_move(board, row, col, num):
                board[row][col] = num
                if fill_cell(next_row, next_col):
                    return True
                board[row][col] = 0

        return False

    fill_cell(0, 0)

def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

def main():
    sudoku_board = create_sudoku_board()
    fill_board(sudoku_board)
    print("Grille de Sudoku partiellement remplie :")
    print_board(sudoku_board)

if __name__ == "__main__":
    main()
