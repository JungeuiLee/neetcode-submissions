class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        # row
        for row in board:
            check = set()
            for num in row:
                if num == ".":
                    continue
                elif num in check:
                    return False
                elif num not in check:
                    check.add(num)
            

        # col
        for col in range(9):
            check = set()
            for row in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if num in check:
                    return False
                check.add(num)

        # 3x3
        for box_row in range(3):
            for box_col in range(3):
                check = set()
                for r in range(3):
                    for c in range(3):
                        num = board[box_row * 3 + r][box_col * 3 + c]
                        if num == ".":
                            continue
                        if num in check:
                            return False
                        check.add(num)
        
        return True