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

        for box_row in range(3):
            for box_col in range(3):
                seen3 = set()
                for r in range(3):
                    for c in range(3):
                        # 3x3 박스 안의 실제 좌표 계산
                        curr_r = box_row * 3 + r
                        curr_c = box_col * 3 + c
                        val = board[curr_r][curr_c]

                        if val != ".":
                            if val in seen3:
                                return False
                            seen3.add(val)
        return True