class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = set(s)
        b = set(t)

        print(a, b)