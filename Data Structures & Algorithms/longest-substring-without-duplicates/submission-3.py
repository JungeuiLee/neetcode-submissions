class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        if not s:
            return 0

        for i in range(len(s)):
            char_set = set()
            for j in range(i,len(s)):

                if s[j] in char_set:
                    break
                else:
                    char_set.add(s[j])
                count = max(count, j - i + 1)
                
        return count
