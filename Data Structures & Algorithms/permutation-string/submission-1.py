class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 나중에 시간 지나고 꼭 윈도우 방식으로 풀어볼것
        # 아래 방식은 brute force
        sorted_s1 = sorted(s1)
        
        for i in range(0, len(s2) - len(s1) + 1):
            if sorted(s2[i:i+len(s1)]) == sorted_s1:
                return True
        return False            #42ms

        # i = 0
        # for r in range(len(s2)):
        #     if s2[r]

        #     if (r - 1) == len(s2):
        #         i += 1