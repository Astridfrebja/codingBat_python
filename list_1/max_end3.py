def max_end3(nums):
  if nums[0] > nums[2]:
    return [nums[0], nums[0], nums[0]]
  else:
    return [nums[2], nums[2], nums[2]]

assert max_end3([1, 2, 3]) == [3, 3, 3]
assert max_end3([11, 5, 9]) == [11, 11, 11]		
assert max_end3([2, 11, 3]) == [3, 3, 3]	
assert max_end3([11, 3, 3]) == [11, 11, 11]	
assert max_end3([3, 11, 11]) == [11, 11, 11]	
assert max_end3([2, 2, 2]) == [2, 2, 2]	
assert max_end3([2, 11, 2]) == [2, 2, 2]	
assert max_end3([0, 0, 1]) == [1, 1, 1]

print('Alle tester bestått')