#https://codeforces.com/problemset/problem/282/A

integer = int(input())
operations = [input() for i in range(integer)]
x = 0

for operation in operations:
  lists=[]
  lists[:0] = operation
  if lists[1] == '+':
    x += 1
  elif lists[1] == '-':
    x -= 1

print(x)
