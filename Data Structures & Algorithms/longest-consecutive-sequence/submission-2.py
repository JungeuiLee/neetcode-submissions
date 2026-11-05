class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0 

        for num in nums_set:
            if (num - 1) not in nums_set:
                current_num = num
                current_steak = 1

                while (current_num + 1) in nums_set:
                    current_num += 1
                    current_steak += 1
                result = max(result, current_steak)
        
        return result