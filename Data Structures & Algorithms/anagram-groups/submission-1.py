class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        for str in strs:
            str = ''.join(sorted(str))