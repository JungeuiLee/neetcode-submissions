class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            num = target - nums[i]

            if num not in seen:
                seen[nums[i]] = i
            else:
                return [dic[nums], i]