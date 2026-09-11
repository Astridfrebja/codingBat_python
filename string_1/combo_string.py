def combo_string(a, b):
  if (len(a) > len(b)):
    return b + a + b
  else:
    return a + b + a

assert combo_string('Hello', 'hi') == 'hiHellohi'
assert combo_string('hi', 'Hello') == 'hiHellohi'
assert combo_string('aaa', 'b') == 'baaab'
assert combo_string('b', 'aaa') == 'baaab'
assert combo_string('aaa', '') == 'aaa'	
assert combo_string('', 'bb') == 'bb'
assert combo_string('aaa', '1234') == 'aaa1234aaa'
assert combo_string('aaa', 'bb') == 'bbaaabb'
assert combo_string('a', 'bb') == 'abba'
assert combo_string('bb', 'a') == 'abba'	
assert combo_string('xyz', 'ab') == 'abxyzab'	

print('Alle tester bestått')