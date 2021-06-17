#https://codeforces.com/problemset/problem/231/A

integer = int(input())
sols = [input() for i in range(integer)]
x = 0

for sol in sols:
  lists=[]
  lists[:0] = sol
  if lists.count('1') >= 2:
    x += 1
  elif lists.count('1') <2:
    x += 0

print(x)
