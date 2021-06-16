#https://codeforces.com/problemset/problem/71/A

integer = int(input())
lines = [input() for i in range(integer)]

for word in lines:
  lockers_list=[]
  lockers_list[:0] = word
  myarr = []
  if len(lockers_list) > 10:
    first = lockers_list[0]
    last = lockers_list[-1]
    lockers_list.pop(0)
    lockers_list.pop(-1)
    length = len(lockers_list)
    myarr.append(first)
    myarr.append(str(length))
    myarr.append(last)
    x = ' '.join(myarr)
    print(x.replace(" ", ""))
  elif len(lockers_list) <= 10:
    print(word)



