#https://codeforces.com/problemset/problem/977/A

x, y = input().split()
n = int(x)
k = int(y)


for i in range(1,k+1):
  if n%10==0:
    n = n/10
  elif n%10 != 0:
    n -= 1

print(int(n))
