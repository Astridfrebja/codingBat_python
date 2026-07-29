def sleep_in(weekday, vacation):
  if (vacation == True) or (weekday == False):
    return True
  else:
    return False


assert sleep_in(False, False) == True
assert sleep_in(True, False) == False
assert sleep_in(False, True) == True
assert sleep_in(True, True) == True

print("Alle tester bestått")
