def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8

assert near_ten(12) == True	
assert near_ten(17) == False
assert near_ten(19) == True
assert near_ten(31) == True
assert near_ten(6) == False
assert near_ten(10) == True
assert near_ten(11) == True
assert near_ten(21) == True
assert near_ten(22) == True	
assert near_ten(23) == False
assert near_ten(54) == False
assert near_ten(155) == False
assert near_ten(158) == True
assert near_ten(3) == False	
assert near_ten(1) == True

print('Alle tester bestått')