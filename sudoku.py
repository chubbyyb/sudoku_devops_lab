def solve_sudoku(board):
    if not is_valid_board(board):
        return None
        
    def find_empty(board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(board, num, pos):
        # Check row
        for j in range(len(board[0])):
            if board[pos[0]][j] == num and pos[1] != j:
                return False
                
        # Check column
        for i in range(len(board)):
            if board[i][pos[1]] == num and pos[0] != i:
                return False
                
        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num and (i,j) != pos:
                    return False
        return True

    def solve(board):
        empty = find_empty(board)
        if not empty:
            return True
            
        row, col = empty
        for num in range(1,10):
            if is_valid(board, num, (row,col)):
                board[row][col] = num
                if solve(board):
                    return True
                board[row][col] = 0
        return False

    # Create a copy of the board
    board_copy = [row[:] for row in board]
    if solve(board_copy):
        return board_copy
    return None

def is_valid_board(board):
    if len(board) != 9 or any(len(row) != 9 for row in board):
        return False
    return True