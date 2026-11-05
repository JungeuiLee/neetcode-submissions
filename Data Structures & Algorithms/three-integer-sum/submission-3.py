class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sorted_nums = sorted(nums)
        lst = []

        for i in range(len(nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            a = i + 1
            b = n - 1

            while a < b and sorted_nums[i] == sorted_nums[i-1]:
                if sorted_nums[a]+ sorted_nums[b] + sorted_nums[i] < 0:
                    a += 1
                elif sorted_nums[a]+ sorted_nums[b] + sorted_nums[i] > 0:
                    b -= 1
                else:
                    lst.append([sorted_nums[a], sorted_nums[b], sorted_nums[i]])
                    a += 1
                    b -= 1

        
        return lst
