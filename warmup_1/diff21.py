def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2

assert diff21(19) == 2
assert diff21(10) == 11	
assert diff21(21) == 0	
assert diff21(22) == 2	
assert diff21(25) == 8	
assert diff21(30) == 18	
assert diff21(0) == 21	
assert diff21(1) == 20	
assert diff21(2) == 19	
assert diff21(-1) == 22	
assert diff21(-2) == 23	
assert diff21(50) == 58

print('Alle tester bestått')