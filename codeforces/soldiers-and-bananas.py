#https://codeforces.com/problemset/problem/546/A

k, n, w = input().split()
myarr = []
x = 0
for i in range(1,int(w)+1):
  x += int(i)*int(k)

subtract = int(x) - int(n)
if subtract > 0:
  print(int(x)-int(n))
if subtract <= 0:
  print(0)

