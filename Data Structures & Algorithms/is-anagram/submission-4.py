class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = set(s)
        b = set(t)

        if a == b:
            return True
        else:
            return False