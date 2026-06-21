class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pnt = set()
        for num in nums:
            if num in pnt:
                return True
            pnt.add(num)
        return False