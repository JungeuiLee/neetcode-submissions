class Solution:
    def isPalindrome(self, s: str) -> bool:
        line = "".join([c.lower() for c in s if c.isalnum()])

        return line == line[::-1]