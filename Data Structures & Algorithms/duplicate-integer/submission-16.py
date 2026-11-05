class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = 0
        for i in range(len(nums)):
            if nums[a] == nums[i]:
                return true
            else:
                return false