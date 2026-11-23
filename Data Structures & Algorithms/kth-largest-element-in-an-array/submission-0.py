import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-s for s in nums]
        heapq.heapify(nums)
        result = 0

        while k > 1:
            k -= 1
            heapq.heappop(nums)
        
        return heapq.heappop(nums) * -1