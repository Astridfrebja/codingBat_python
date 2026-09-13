def sum2(nums):
  if len(nums) >= 2:
    return nums[0] + nums[1]
  elif len(nums) == 1:
    return nums[0]
  else:
    return 0

assert sum2([1, 2, 3]) == 3	
assert sum2([1, 1]) == 2	
assert sum2([1, 1, 1, 1]) == 2
assert sum2([1, 2]) == 3	
assert sum2([1]) == 1	
assert sum2([]) == 0
assert sum2([4, 5, 6]) == 9
assert sum2([4]) == 4

print('Alle tester bestått')