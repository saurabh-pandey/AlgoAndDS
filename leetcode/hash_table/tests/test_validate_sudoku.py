import pytest

import hash_table.validate_sudoku as prob

class TestValidateSudoku:
    def test_example1(self):
        board = [["5","3",".",".","7",".",".",".","."],
                 ["6",".",".","1","9","5",".",".","."],
                 [".","9","8",".",".",".",".","6","."],
                 ["8",".",".",".","6",".",".",".","3"],
                 ["4",".",".","8",".","3",".",".","1"],
                 ["7",".",".",".","2",".",".",".","6"],
                 [".","6",".",".",".",".","2","8","."],
                 [".",".",".","4","1","9",".",".","5"],
                 [".",".",".",".","8",".",".","7","9"]]
        res = True
        assert prob.isValidSudoku(board) == res
    
    def test_example2(self):
        board = [["8","3",".",".","7",".",".",".","."],
                 ["6",".",".","1","9","5",".",".","."],
                 [".","9","8",".",".",".",".","6","."],
                 ["8",".",".",".","6",".",".",".","3"],
                 ["4",".",".","8",".","3",".",".","1"],
                 ["7",".",".",".","2",".",".",".","6"],
                 [".","6",".",".",".",".","2","8","."],
                 [".",".",".","4","1","9",".",".","5"],
                 [".",".",".",".","8",".",".","7","9"]]
        res = False
        assert prob.isValidSudoku(board) == res
    
    def test_my1(self):
        board = [["5","3",".",".","7",".",".",".","."],
                 ["6",".",".","1","9","5",".",".","."],
                 [".","9","8",".",".",".",".","6","."],
                 ["8",".",".",".","6",".",".",".","3"],
                 ["4",".",".","8",".","3",".",".","1"],
                 ["7",".",".",".","2",".",".",".","6"],
                 [".","6",".",".",".",".","2","8","."],
                 [".",".",".","4","1","9",".",".","8"],
                 [".",".",".",".","8",".",".","7","9"]]
        res = False
        assert prob.isValidSudoku(board) == res
    
    def test_my2(self):
        board = [["5","3",".",".","7",".",".",".","."],
                 ["6",".",".","1","9","5",".",".","."],
                 [".","9","8",".",".",".",".","6","."],
                 ["8",".",".",".","6",".",".",".","3"],
                 ["4",".",".","8",".","3",".",".","1"],
                 ["7",".",".",".","2",".",".",".","6"],
                 [".","9",".",".",".",".","2","8","."],
                 [".",".",".","4","1","9",".",".","5"],
                 [".",".",".",".","8",".",".","7","9"]]
        res = False
        assert prob.isValidSudoku(board) == res
    
    def test_my3(self):
        board = [["5","3",".",".","7",".",".",".","."],
                 ["6",".",".","1","9","5",".",".","."],
                 [".","9","8",".",".",".",".","6","."],
                 ["8",".",".",".","6",".",".",".","3"],
                 ["4",".",".","8",".","3",".",".","1"],
                 ["7",".",".",".","2",".",".",".","6"],
                 [".","6",".",".",".",".","2","8","."],
                 ["9",".",".","4","1","9",".",".","5"],
                 [".",".",".",".","8",".",".","7","9"]]
        res = False
        assert prob.isValidSudoku(board) == res