def last2(str):
  if len(str) < 2:
    return 0
  
  last2 = str[len(str)-2:]
  count = 0
  
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count

assert last2('hixxhi') == 1
assert last2('xaxxaxaxx') == 1
assert last2('axxxaaxx') == 2
assert last2('xxaxxaxxaxx') == 3
assert last2('xaxaxaxx') == 0	
assert last2('xxxx') == 2		
assert last2('13121312') == 1	
assert last2('11212') == 1	
assert last2('13121311') == 0	
assert last2('1717171') == 2	
assert last2('hi') == 0	
assert last2('h') == 0	
assert last2('') == 0

print('Alle tester bestått')