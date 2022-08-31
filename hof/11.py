class Solution:
    def __init__(self,nums):
        self.nums = nums

    def removeDuplicates(self):
        num = list(set(self.nums))
        return num

    def count_of_num(self):
        num = self.removeDuplicates()
        return len(num)    


num_1 = Solution([1,1,2])

print(num_1.removeDuplicates())
print(num_1.count_of_num())