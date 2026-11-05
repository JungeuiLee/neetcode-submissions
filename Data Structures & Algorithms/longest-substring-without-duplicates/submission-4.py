class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            # 중복 문자가 존재하면 중복이 사라질 때까지 왼쪽 포인터(l)를 오른쪽으로 이동
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            # 현재 문자 추가 및 최대 길이 갱신
            char_set.add(s[r])
            res = max(res, r - l + 1)
            
        return res