class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left+right)//2

            if nums[middle] == target:
                return middle

            # 왼쪽 구간이 정렬이 되어 있는 경우의 수
            if nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
                
            # 오른쪽 구간이 정렬이 되어 있는 경우의 수
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle+1
                else:
                    right=middle-1
        return -1