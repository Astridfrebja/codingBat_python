def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile:
    return True
  else:
    return False

assert monkey_trouble(True, True) == True
assert monkey_trouble(False, False) == True	
assert monkey_trouble(True, False) == False	
assert monkey_trouble(False, True) == False

print("Alle tester bestått")