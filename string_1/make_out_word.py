def make_out_word(out, word):
  return (out[:2] + word + out[2:])

assert make_out_word('<<>>', 'Yay') == '<<Yay>>'
assert make_out_word('<<>>', 'WooHoo') == '<<WooHoo>>'
assert make_out_word('[[]]', 'word') == '[[word]]'		
assert make_out_word('HHoo', 'Hello') == 'HHHellooo'
assert make_out_word('abyz', 'YAY') == 'abYAYyz'

print("Alle tester bestått")