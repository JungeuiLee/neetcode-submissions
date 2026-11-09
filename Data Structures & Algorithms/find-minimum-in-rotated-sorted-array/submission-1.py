class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[0]

        while left <= right:
            middle = (left + right) // 2
            
            # 왼쪽이 정렬되어 있는 경우
            if nums[left] <= nums[middle]:
                res = min(res, nums[left])
                left = middle + 1

            # 오른쪽이 정렬되어 있는 경우
            else:
                right = middle - 1
                res = min(res, nums[middle])
        return res