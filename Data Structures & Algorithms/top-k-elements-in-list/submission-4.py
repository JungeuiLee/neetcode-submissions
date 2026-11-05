class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(nums)

        seen = {}

        for i in sorted_nums:
            if i not in seen:
                seen[i] = 1

            else:
                seen[i] += 1
        
        # sorted_seen = sorted(seen.items())

        lst = []
        for key, val in seen.items():
            lst.append((val, key))

        sorted_seen = sorted(lst)

        # print(seen)
        # print(sorted_seen)

        output = []
        for j in range(k):
            output.append(sorted_seen[-1 - j][1])
        
        return output