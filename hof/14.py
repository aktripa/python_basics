nums = [2,7,11,15]
target = 9
l = len(nums)
for i in range(l):
    for j in range(1,l):
        if nums[i] + nums[j] == target and nums.index(nums[i]) != nums.index(nums[j]):
            op = [nums.index(nums[i]),nums.index(nums[j])]
  
print(op)