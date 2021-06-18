inp = input()
arr = []
arr[:0] = inp

number = arr.count('4') + arr.count('7')

if number == 4 or number == 7:
  print("YES")
else:
  print("NO")
