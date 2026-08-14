def first_two(str):
  start = str[:2]
  return start

assert first_two('Hello') == 'He'
assert first_two('abcdefg') == 'ab'
assert first_two('ab') == 'ab'
assert first_two('a') == 'a'
assert first_two('') == ''
assert first_two('Kitten') == 'Ki'
assert first_two('hi') == 'hi'
assert first_two('hiya') == 'hi'	

print("Alle tester bestått")