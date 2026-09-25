def squirrel_play(temp, is_summer):
  if (60 <= temp <= 90) and (is_summer == False): 
    return True
  elif (60 <= temp <= 100) and (is_summer == True):
    return True
  else:
    return False


assert squirrel_play(70, False) == True
assert squirrel_play(95, False) == False
assert squirrel_play(95, True) == True	
assert squirrel_play(90, False) == True
assert squirrel_play(90, True) == True	
assert squirrel_play(50, False) == False
assert squirrel_play(50, True) == False
assert squirrel_play(100, False) == False
assert squirrel_play(100, True) == True	
assert squirrel_play(105, True) == False
assert squirrel_play(59, False) == False
assert squirrel_play(59, True) == False
assert squirrel_play(60, False) == True

print('Alle tester bestått')