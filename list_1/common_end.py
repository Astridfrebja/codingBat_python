def common_end(a, b):
  return a[:1] == b[:1] or a[-1:] == b[-1:]

assert common_end([1, 2, 3], [7, 3]) == True	
assert common_end([1, 2, 3], [7, 3, 2]) == False
assert common_end([1, 2, 3], [1, 3]) == True
assert common_end([1, 2, 3], [1]) == True
assert common_end([1, 2, 3], [2]) == False

print('Alle tester bestått')