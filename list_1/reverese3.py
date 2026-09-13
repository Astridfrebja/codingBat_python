def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

assert reverse3([1, 2, 3]) == [3, 2, 1]	
assert reverse3([5, 11, 9]) == [9, 11, 5]		
assert reverse3([7, 0, 0]) == [0, 0, 7]	
assert reverse3([2, 1, 2]) == [2, 1, 2]	
assert reverse3([1, 2, 1]) == [1, 2, 1]		
assert reverse3([2, 11, 3]) == [3, 11, 2]
assert reverse3([0, 6, 5]) == [5, 6, 0]	
assert reverse3([7, 2, 3]) == [3, 2, 7]	

print('Alle tester bestått')