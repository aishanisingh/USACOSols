#https://cses.fi/problemset/task/1068

n = int(input())

myarr = [str(n)]

while n!=1:
  if n%2==0:
    n = n/2
    myarr.append(str(int(n)))
  else:
    n = n*3 + 1
    myarr.append(str(int(n)))


print(' '.join(myarr))
