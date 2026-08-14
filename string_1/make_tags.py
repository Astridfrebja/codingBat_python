def make_tags(tag, word):
  return ("<" + tag + ">"+ word + "</" + tag + ">")

assert make_tags('i', 'Yay') == '<i>Yay</i>'
assert make_tags('i', 'Hello') == '<i>Hello</i>'
assert make_tags('cite', 'Yay') == '<cite>Yay</cite>'
assert make_tags('address', 'here') == '<address>here</address>'	
assert make_tags('body', 'Heart') == '<body>Heart</body>'
assert make_tags('i', 'i') == '<i>i</i>'	
assert make_tags('i', '') == '<i></i>'	

print("Alle tester bestått")