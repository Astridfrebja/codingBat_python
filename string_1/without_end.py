def without_end(str):
  return str[1:-1]

assert without_end('Hello') == 'ell'
assert without_end('java') == 'av'
assert without_end('coding') == 'odin'	
assert without_end('code') == 'od'
assert without_end('ab') == ''
assert without_end('Chocolate!') == 'hocolate'
assert without_end('kitten') == 'itte'
assert without_end('woohoo') == 'ooho'

print('Alle tester bestått')