class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        for str in strs:
            sort_str = ''.join(sorted(str))
            lst.append(sort_str)