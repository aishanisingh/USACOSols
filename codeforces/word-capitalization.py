#i made this so complex and for what
#anyways
#https://codeforces.com/problemset/problem/281/A

word = input()
myarr = []
myarr[:0] = word

first = myarr[0]
myarr2 = []

if first.isupper() == False:
  capfirst = first.upper()
  myarr.pop(0)
  myarr2.append(capfirst)
  myarr2.append(' '.join(myarr))
  myarr3 = ' '.join(myarr2)
  print(myarr3.replace(" ", ""))
if first.isupper() == True:
  print(word)
