class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(nums)

        seen = {}

        for i in sorted_nums:
            if i not in seen:
                seen[i] = 0

            else:
                seen[i] += 1
        
        sorted_seen = sorted(seen.items())

        lst = []
        for j in range(k):
            lst.append(sorted_seen[-k])
        
        return lst