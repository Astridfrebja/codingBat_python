def non_start(a, b):
  return a[1:] + b[1:]

assert non_start('Hello', 'There') == 'ellohere'
assert non_start('java', 'code') == 'avaode'	
assert non_start('shotl', 'java') == 'hotlava'
assert non_start('ab', 'xy') == 'by'
assert non_start('ab', 'x') == 'b'	
assert non_start('x', 'ac') == 'c'
assert non_start('a', 'x') == ''
assert non_start('kit', 'kat') == 'itat'	
assert non_start('mart', 'dart') == 'artart'

print('Alle tester bestått')