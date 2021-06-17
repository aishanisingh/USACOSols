integer = int(input())
lines = [input() for i in range(integer)]

for word in lines:
  lists=[]
  lists[:0] = word
  myarr = []
  if len(lists) > 10:
    first = lists[0]
    last = lists[-1]
    lists.pop(0)
    lists.pop(-1)
    length = len(lists)
    myarr.append(first)
    myarr.append(str(length))
    myarr.append(last)
    x = ' '.join(myarr)
    print(x.replace(" ", ""))
  elif len(lists) <= 10:
    print(word)



