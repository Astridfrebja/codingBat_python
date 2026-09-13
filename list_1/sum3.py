def sum3(nums):
  return nums[0] + nums[1] + nums[2]

assert sum3([1, 2, 3]) == 6
assert sum3([5, 11, 2]) == 18
assert sum3([7, 0, 0]) == 7	
assert sum3([1, 2, 1]) == 4
assert sum3([1, 1, 1]) == 3	
assert sum3([2, 7, 2]) == 11

print('Alle tester bestått')