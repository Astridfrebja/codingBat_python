def string_times(str, n):
  return str * n

assert string_times('Hi', 2) == 'HiHi'
assert string_times('Hi', 3) == 'HiHiHi'
assert string_times('Hi', 1) == 'Hi'
assert string_times('Hi', 0) == ''
assert string_times('Hi', 5) == 'HiHiHiHiHi'
assert string_times('Oh Boy!', 2) == 'Oh Boy!Oh Boy!'
assert string_times('x', 4) == 'xxxx'
assert string_times('', 4) == ''
assert string_times('code', 2) == 'codecode'
assert string_times('code', 3) == 'codecodecode'

print('Alle tester bestått')