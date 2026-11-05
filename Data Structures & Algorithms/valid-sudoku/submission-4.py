class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # row
        for row in board:
            seen = set()
            for i in row:
                if i != ".":
                    if i in seen:
                        return False
                    seen.add(i)

        # col
        for col in range(9):
            seen2 = set()
            for j in range(9):
                val = board[j][col]
                if val != ".":
                    if val in seen2:
                        return False
                    seen2.add(val)
        return True