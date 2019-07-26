#A)Spl it a given Sentence into l ist of words.
#B) Sort that l ist according to the letters alphabetical ly.
#C) Sort that l ist alphabetically.

mystring = input("enter a string")
words = mystring.split( )
print(words)
print(sorted(words))

for word in words:
  print(sorted(word))
  b = sorted(word)
order = ''.join(b)
print(order)




