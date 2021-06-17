#https://codeforces.com/problemset/problem/339/A
#TODO: clean up this code because it's pretty redundant and you could do better

inputs = input()

myarr0 = []
myarr0[:0] = inputs

number_list = [x for x in myarr0 if x != '+']
number_list = [int(i) for i in number_list]

list_size = len(number_list)

for j in range(list_size):
  smallest_index = j
  smallest = number_list[j]
  for i in range(j+1,list_size):
    if smallest > number_list[i]:
      smallest = number_list[i]
      smallest_index = i
  if smallest_index != j:
    temp = number_list[j]
    number_list[j] = smallest 
    number_list[smallest_index] = temp 

myarr = []
for i in number_list:
  myarr.append(str(i))

string = '+'.join(myarr)

print(string)

