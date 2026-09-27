def alarm_clock(day, vacation):
  if (1 <= day <= 5) and (vacation == False):
    return '7:00'
  elif ((day == 0) or (day == 6)) and (vacation == True):
    return 'off'
  else:
    return '10:00'

assert alarm_clock(1, False) == '7:00'
assert alarm_clock(5, False) == '7:00'
assert alarm_clock(0, False) == '10:00'	
assert alarm_clock(6, False) == '10:00'
assert alarm_clock(0, True) == 'off'	
assert alarm_clock(6, True) == 'off'
assert alarm_clock(1, True) == '10:00'	
assert alarm_clock(3, True) == '10:00'
assert alarm_clock(5, True) == '10:00'

print('Alle tester bestått')