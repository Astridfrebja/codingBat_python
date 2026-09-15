def has23(nums):
  return 2 in nums or 3 in nums

assert has23([2, 5]) == True
assert has23([4, 3]) == True
assert has23([4, 5]) == False
assert has23([2, 2]) == True
assert has23([3, 2]) == True
assert has23([3, 3]) == True
assert has23([7, 7]) == False
assert has23([3, 9]) == True
assert has23([9, 5]) == False

print('Alle tester bestått')