class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for w in strs:
            sort_str = ''.join(sorted(w))
            lst.append(sort_str)

            if sort_str not in seen:
                seen[sort_str] = []
            seen[word_str].append(w)

        return list(seen.values())
