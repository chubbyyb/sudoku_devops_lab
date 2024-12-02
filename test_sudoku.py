import unittest
from sudoku import solve_sudoku

class TestSudoku(unittest.TestCase):
    def test_valid_puzzle(self):
        board = [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        solution = solve_sudoku(board)
        self.assertIsNotNone(solution)
        self.assertNotEqual(solution, board)

    def test_invalid_board_size(self):
        board = [[1,2,3], [4,5,6], [7,8,9]]
        self.assertIsNone(solve_sudoku(board))

    def test_empty_board(self):
        board = [[0]*9 for _ in range(9)]
        solution = solve_sudoku(board)
        self.assertIsNotNone(solution)

    def test_already_solved(self):
        board = [
            [5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]
        ]
        solution = solve_sudoku(board)
        self.assertEqual(solution, board)

    def test_unsolvable(self):
        board = [
            [5,5,0,0,7,0,0,0,0],  # Two 5s in first row makes it unsolvable
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        self.assertIsNone(solve_sudoku(board))

    def test_invalid_characters(self):
        board = [
            [5,'x',0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        self.assertIsNone(solve_sudoku(board))

if __name__ == '__main__':
    unittest.main()