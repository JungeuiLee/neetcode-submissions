class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorta = ''.join(sorted(s))
        sortb = ''.join(sorted(t))

        if sorta == sortb:
            return True
        else:
            return False