#https://codeforces.com/problemset/problem/236/A

inputs = input()
a_list = []
a_list[:0] = inputs

a_set = set(a_list)
length = len(a_set)

if length%2==0:
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")
