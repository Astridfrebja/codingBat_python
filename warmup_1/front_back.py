def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]
  
  return str[len(str)-1] + mid + str[0]

assert front_back('code') == 'eodc'	
assert front_back('a') == 'a'
assert front_back('ab') == 'ba'	
assert front_back('abc') == 'cba'
assert front_back('') == ''	
assert front_back('Chocolate') == 'ehocolatC'
assert front_back('aavJ') == 'Java'
assert front_back('hello') == 'oellh'

print('Alle tester bestått')