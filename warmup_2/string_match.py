def string_match(a, b):
  shorter = min(len(a), len(b))
  count = 0
  
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1
  return count 

assert string_match('xxcaazz', 'xxbaaz') == 3
assert string_match('abc', 'abc') == 2
assert string_match('abc', 'axc') == 0
assert string_match('hello', 'he') == 1
assert string_match('he', 'hello') == 1
assert string_match('h', 'hello') == 0
assert string_match('', 'hello') == 0
assert string_match('aabbccdd', 'abbbxxd') == 1	
assert string_match('aaxxaaxx', 'iaxxai') == 3
assert string_match('iaxxai', 'aaxxaaxx') == 3

print('Alle tester bestått')