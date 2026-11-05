class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pnt = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[pnt]:
                return True
            pnt += 1
        return False