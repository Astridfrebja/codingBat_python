def left2(str):
  end = str[:2]
  start = str[2:]
  return start + end

assert left2('Hello') == 'lloHe'
assert left2('java') == 'vaja'
assert left2('Hi') == 'Hi'
assert left2('code') == 'deco'
assert left2('cat') == 'tca'
assert left2('12345') == '34512'	
assert left2('Chocolate') == 'ocolateCh'	
assert left2('bricks') == 'icksbr'

print('Alle tester bestått')