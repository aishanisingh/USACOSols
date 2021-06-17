#https://codeforces.com/problemset/problem/59/A

inp = input()
words = []
words[:0] = inp

upper = 0
lower = 0

for word in words:
  if word.isupper() == True:
    upper += 1
  if word.isupper() == False:
    lower += 1

if upper > lower:
  answer = inp.upper()

if lower > upper:
  answer = inp.lower()

if lower == upper:
  answer = inp.lower()

print(answer)
