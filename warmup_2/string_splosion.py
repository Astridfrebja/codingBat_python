def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return result


string_splosion('Code') == 'CCoCodCode'
string_splosion('abc') == 'aababc'
string_splosion('ab') == 'aab'
string_splosion('x') == 'x'
string_splosion('fade') == 'ffafadfade'
string_splosion('There') == 'TThTheTherThere'
string_splosion('Kitten') == 'KKiKitKittKitteKitten'	
string_splosion('Bye') == 'BByBye'
string_splosion('Good') == 'GGoGooGood'
string_splosion('Bad') == 'BBaBad'

print('Alle tester bestått')