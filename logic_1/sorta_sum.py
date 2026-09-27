def sorta_sum(a, b):
  if (a + b <= 9):
    return a + b
  elif (10 <= a + b <= 19):
    return 20
  else:
    return a + b

assert sorta_sum(3, 4) == 7
assert sorta_sum(9, 4) == 20
assert sorta_sum(10, 11) == 21
assert sorta_sum(12, -3) == 9
assert sorta_sum(-3, 12) == 9
assert sorta_sum(4, 5) == 9	
assert sorta_sum(4, 6) == 20	
assert sorta_sum(14, 7) == 21
assert sorta_sum(14, 6) == 20

print('Alle tester bestått')