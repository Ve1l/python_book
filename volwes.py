vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}


for k  in word:
  if k in vowels:
    found.setdefault(k, 0)
    found[k] += 1
for k, v in sorted(found.items()):
  print(k, 'was found', v, 'time(s).')
