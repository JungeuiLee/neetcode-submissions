class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for w in strs:
            sort_str = ''.join(sorted(w))

            if sort_str not in seen:
                seen[sort_str] = []
            seen[sort_str].append(w)

        return list(seen.values())
