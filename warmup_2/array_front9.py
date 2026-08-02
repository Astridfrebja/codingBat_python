def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
    
  for i in range(end):
    if nums[i] == 9:
      return True
  return False

assert array_front9([1, 2, 9, 3, 4]) == True
assert array_front9([1, 2, 3, 4, 9]) == False	
assert array_front9([1, 2, 3, 4, 5]) == False
assert array_front9([9, 2, 3]) == True
assert array_front9([1, 9, 9]) == True	
assert array_front9([1, 2, 3]) == False	
assert array_front9([1, 9]) == True	
assert array_front9([5, 5]) == False
assert array_front9([2]) == False	
assert array_front9([9]) == True
assert array_front9([]) == False
assert array_front9([3, 9, 2, 3, 3]) == True

print('Alle tester bestått')