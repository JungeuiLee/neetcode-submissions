class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for i in strs:
            ana = ''.join(sorted(i))

            if ana not in dic:
                dic[ana] = []
            dic[ana].append(i)

        return list(dic.values())