def kiemtra(board, row, col, number):
    #kiểm tra xem numberber đặt vào có hợp lệ hay không
    for i in range(9):
        if board[row][i] == number or board[i][col] == number:
            return False
    #kiểm tra 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == number:
                return False
    return True
def sudoku(board):
    #Hàm để giải sudoku bằng thuật toán quay lui
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for number in range(1, 10):
                    if kiemtra(board, row, col, number):
                        board[row][col] = number
                        if sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True
def xuat(board):
    for row in board:
        print(" ".join(map(str, row)))
def main():
    #Ví dụ bảng sudoku:
    bang_sudoku = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    print("Bảng ban đầu là:")
    xuat(bang_sudoku)
    if sudoku(bang_sudoku):
        print("\nBảng sudoku đã giải là:")
        xuat(bang_sudoku)
    else:
        print("\nKhông có cách giải!")

if __name__ == "__main__":
    main()