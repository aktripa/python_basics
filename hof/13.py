class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1
        
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l  

obj_1 = Solution()

print(obj_1.removeDuplicates([1,1,2]))
