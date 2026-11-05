class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        output = []

        for i in nums:
            if i not in dic:
                dic[i] = 0

            if i in dic:
                dic[i] += 1

        size = len(nums) + 1

        bucket = []

        for index in range(size):
            empty_list = []
            bucket.append(empty_list)

        for pair in dic.items():
            num = pair[0]
            freq = pair[1]

            target_list = bucket[freq]

            target_list.append(num)

        result = []

        for freq in range(len(bucket) -1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result
                    