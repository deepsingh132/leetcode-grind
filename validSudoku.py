from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key = (r / 3, c / 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # if the cell is empty then continue
                    continue

                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]): # if there is a duplicate value in the row, column, or square then return false
                    return False

                cols[c].add(board[r][c]) # add the value to the column set
                rows[r].add(board[r][c]) # add the value to the row set
                squares[(r // 3, c // 3)].add(board[r][c]) # add the value to the square set

        return True

solution = Solution()
print(solution.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
