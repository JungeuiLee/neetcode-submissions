class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(1, len(nums)):
            pnt = 0
            if nums[pnt] + nums[i] == target:
                return [pnt, i]
            print(pnt, i)
            pnt += 1