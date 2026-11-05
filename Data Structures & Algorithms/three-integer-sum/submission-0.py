class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        fpoint = 0
        sorted_nums = nums.sort()
        print(sorted_nums)
        lst = []

        a = 0
        b = a + 1
        for i in range(len(nums)):
            if fpoint == a:
                a += 1
                continue
            if fpoint == b:
                break
            
            if nums[a]+ nums[b] + nums[fpoint] == 0:
                lst.append(nums[a], nums[b], fpoint)
            
            fpoint += 1

        
        return lst
