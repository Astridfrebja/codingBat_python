def in1to10(n, outside_mode):
    if outside_mode == False:
        return 1 <= n <= 10
    else:
        return n <= 1 or n >= 10


assert in1to10(5, False) == True
assert in1to10(11, False) == False
assert in1to10(11, True) == True
assert in1to10(10, False) == True
assert in1to10(10, True) == True
assert in1to10(9, False) == True
assert in1to10(9, True) == False
assert in1to10(1, False) == True
assert in1to10(1, True) == True	
assert in1to10(0, False) == False
assert in1to10(0, True) == True
assert in1to10(-1, False) == False
assert in1to10(-1, True) == True	
assert in1to10(99, False) == False	
assert in1to10(-99, True) == True

print('Alle tester bestått')