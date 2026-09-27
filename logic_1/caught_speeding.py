def caught_speeding(speed, is_birthday):
    limit = 65 if is_birthday else 60

    if speed <= limit:
        return 0
    elif speed <= limit + 20:
        return 1
    else:
        return 2

assert caught_speeding(60, False) == 0
assert caught_speeding(65, False) == 1	
assert caught_speeding(65, True) == 0
assert caught_speeding(80, False) == 1	
assert caught_speeding(85, False) == 2
assert caught_speeding(85, True) == 1
assert caught_speeding(70, False) == 1	
assert caught_speeding(75, False) == 1
assert caught_speeding(75, True) == 1
assert caught_speeding(40, False) == 0
assert caught_speeding(40, True) == 0	
assert caught_speeding(90, False) == 2

print('Alle tester bestått')