def array_count9(nums):
  count = 0
  
  for num in nums:
    if num == 9:
      count = count + 1
      
  return count

assert array_count9([1, 2, 9]) == 1	
assert array_count9([1, 9, 9]) == 2	
assert array_count9([1, 9, 9, 3, 9]) == 3	
assert array_count9([1, 2, 3]) == 0	
assert array_count9([]) == 0
assert array_count9([4, 2, 4, 3, 1]) == 0
assert array_count9([9, 2, 4, 3, 1]) == 1

print('Alle tester bestått')