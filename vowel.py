char=raw_input('Enter the char:')
cha=char[0]
if len(cha)>0 and original.isalpha():
  if cha in 'aeiou':
    print("vowel")
else:
  print("constant")