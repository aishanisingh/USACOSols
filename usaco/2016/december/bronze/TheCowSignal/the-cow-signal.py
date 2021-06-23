m,n,k = input().split()
lines = [input() for i in range(int(m))]


for line in lines:
  for j in range(int(n)):
    string = ""
    for c in line:
      for l in range(int(k)):     
        string = string + c
  for q in range(int(k)):
    print(string)



