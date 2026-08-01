def front3(str):
  front = str[:3]
  return front + front + front

assert front3('Java') == 'JavJavJav'
assert front3('Chocolate') == 'ChoChoCho'
assert front3('abc') == 'abcabcabc'
assert front3('abcXYZ') == 'abcabcabc'
assert front3('ab') == 'ababab'
assert front3('a') == 'aaa'
assert front3('') == ''

print('Alle tester bestått')