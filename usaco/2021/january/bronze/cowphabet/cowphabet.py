alphabet = input()
s = input()

reverse = {}

for i in range(len(alphabet)):
  reverse[alphabet[i]] = i

print(reverse)

curr = -1
count = 1

for c in s:
  print(c)
  if reverse[c] <= curr:
    count+=1
  curr = reverse[c]

print(count)
