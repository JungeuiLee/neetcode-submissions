class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_vol = 0

        while left < right:
            ji = right - left
            hee = min(heights[left], heights[right])

            current_vol = ji * hee

            max_vol = max(max_vol, current_vol)

            if heights[left] < heights[right]:
                left += 1
            
            else:
                right -= 1
            
        return max_vol