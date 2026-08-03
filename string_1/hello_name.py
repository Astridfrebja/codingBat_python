def hello_name(name):
  return('Hello ' + name + '!')


assert hello_name('Bob') == 'Hello Bob!'
assert hello_name('Alice') == 'Hello Alice!'
assert hello_name('X') == 'Hello X!'
assert hello_name('Dolly') == 'Hello Dolly!'
assert hello_name('Alpha') == 'Hello Alpha!'
assert hello_name('Omega') == 'Hello Omega!'
assert hello_name('Goodbye') == 'Hello Goodbye!'
assert hello_name('ho ho ho') == 'Hello ho ho ho!'	
assert hello_name('xyz!') == 'Hello xyz!!'
assert hello_name('Hello') == 'Hello Hello!'

print('Alle tester bestått')