def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

assert string_bits('Hello') == 'Hlo'
assert string_bits('Hi') == 'H'
assert string_bits('Heeololeo') == 'Hello'
assert string_bits('HiHiHi') == 'HHH'
assert string_bits('') == ''
assert string_bits('Greetings') == 'Getns'
assert string_bits('Chocoate') == 'Coot'
assert string_bits('pi') == 'p'
assert string_bits('Hello Kitten') == 'HloKte'
assert string_bits('hxaxpxpxy') == 'happy'

print('Alle tester bestått')