#URL: https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1126/
#Description
"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to 
the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true


Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since 
there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""
def getBoxId(row, col):
    if row <= 2:
        if col <= 2:
            return 0
        elif 3 <= col <= 5:
            return 1
        else:
            return 2
    elif 3 <= row <= 5:
        if col <= 2:
            return 3
        elif 3 <= col <= 5:
            return 4
        else:
            return 5
    else:
        if col <= 2:
            return 6
        elif 3 <= col <= 5:
            return 7
        else:
            return 8

def isValidSudoku(board):
    val_dict = {}
    for i in range(9):
        for j in range(9):
            board_str = board[i][j]
            if board_str != "." and board_str.isnumeric():
                board_val = int(board_str)
                if board_val > 9 or board_val < 1:
                    return False
                else:
                    if board_val in val_dict:
                        for row, col in val_dict[board_val]:
                            if row == i or col == j:
                                return False
                        box_id = getBoxId(i, j)
                        for row, col in val_dict[board_val]:
                            if getBoxId(row, col) == box_id:
                                return False
                        val_dict[board_val].append((i, j))
                    else:
                        val_dict[board_val] = [(i, j)]
    return True
