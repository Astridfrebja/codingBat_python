def first_half(str):
  return str[:len(str)//2]

assert first_half('WooHoo') == 'Woo'
assert first_half('HelloThere') == 'Hello'	
assert first_half('abcdef') == 'abc'
assert first_half('ab') == 'a'
assert first_half('') == ''	
assert first_half('0123456789') == '01234'
assert first_half('kitten') == 'kit'

print('Alle tester bestått')