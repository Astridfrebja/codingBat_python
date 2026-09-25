def cigar_party(cigars, is_weekend):
  if (40 <= cigars <= 60) and is_weekend == False:
    return True
  elif 40 <= cigars and is_weekend == True:
    return True
  else:
    return False

assert cigar_party(30, False) == False	
assert cigar_party(50, False) == True	
assert cigar_party(70, True) == True
assert cigar_party(30, True) == False	
assert cigar_party(50, True) == True
assert cigar_party(60, False) == True
assert cigar_party(61, False) == False	
assert cigar_party(40, False) == True
assert cigar_party(39, False) == False	
assert cigar_party(40, True) == True
assert cigar_party(39, True) == False

print('Alle tester bestått')