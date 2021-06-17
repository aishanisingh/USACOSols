#https://codeforces.com/problemset/problem/50/A

l, w = input().split()
area = int(l)*int(w)
x = area/2
if x%1 == 0:
  print(int(x))
else:
  answer = x - 0.5
  print(int(answer))
