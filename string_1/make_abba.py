def make_abba(a, b):
  return a + b + b + a

assert make_abba('Hi', 'Bye') == 'HiByeByeHi'	
assert make_abba('Yo', 'Alice') == 'YoAliceAliceYo'
assert make_abba('What', 'Up') == 'WhatUpUpWhat'
assert make_abba('aaa', 'bbb') == 'aaabbbbbbaaa'
assert make_abba('x', 'y') == 'xyyx'
assert make_abba('x', '') == 'xx'
assert make_abba('', 'y') == 'yy'
assert make_abba('Bo', 'Ya') == 'BoYaYaBo'
assert make_abba('Ya', 'Ya') == 'YaYaYaYa'

print('Alle tester bestått')