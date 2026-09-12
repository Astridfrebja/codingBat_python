def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[-1]

assert same_first_last([1, 2, 3]) == False
assert same_first_last([1, 2, 3, 1]) == True
assert same_first_last([1, 2, 1]) == True
assert same_first_last([7]) == True
assert same_first_last([]) == False
assert same_first_last([1, 2, 3, 4, 5, 1]) == True
assert same_first_last([1, 2, 3, 4, 5, 13]) == False
assert same_first_last([13, 2, 3, 4, 5, 13]) == True	
assert same_first_last([7, 7]) == True

print('Alle tester bestått')