def front_times(str, n):
  front = str[:3]
  return front * n

assert front_times('Chocolate', 2) == 'ChoCho'
assert front_times('Chocolate', 3) == 'ChoChoCho'
assert front_times('Abc', 3) == 'AbcAbcAbc'
assert front_times('Ab', 4) == 'AbAbAbAb'
assert front_times('A', 4) == 'AAAA'
assert front_times('', 4) == ''
assert front_times('Abc', 0) == ''

print('Alle tester bestått')