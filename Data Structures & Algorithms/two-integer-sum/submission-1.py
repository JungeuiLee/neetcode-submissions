class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pnt = 0
        
        for i in range(pnt +1, len(nums)):

            if nums[pnt] + nums[i] == target:
                return [pnt, i]
        pnt += 1