class Solution:
    def __init__(self,nums: list[int]) -> int:
        self.nums = nums

    def expectedNums(self):
        nums = list(set(self.nums))
        return nums
    
    def removeDuplicates(self):
        nums = self.expectedNums()
        return len(nums)


obj_1 = Solution([1,1,2])
print(obj_1.expectedNums())
print(obj_1.removeDuplicates())