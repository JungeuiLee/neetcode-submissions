class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        jihee = 0

        while left < right:
            current_vol = 0
            left_top = left
            
            if height[left] > height[right]:
                left_top = left

                right -= 1
            else:
                right_top = right
            
            current_vol = (right - left) * (min(left_top, right_top))

            jihee = max(jihee, current_vol)

            left += 1
            right -= 1
        return jihee