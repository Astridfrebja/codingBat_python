def extra_end(str):
  end = str[-2:]
  return end*3

assert extra_end('Hello') == 'lololo'
assert extra_end('ab') == 'ababab'
assert extra_end('Hi') == 'HiHiHi'
assert extra_end('Candy') == 'dydydy'
assert extra_end('Code') == 'dedede'

print("Alle tester bestått")