#https://codeforces.com/problemset/problem/677/A

k, v = input().split()
n = int(k)
h = int(v)

people = list(map(int, input().split()))
lists=[]
lists[:0] = people
lists = [x for x in lists if x != ' ']
lenlists = len(lists)

answer = 0

for j in range(0,lenlists):
  if int(lists[j]) > h:
    answer += 2
  elif int(lists[j]) <= h:
    answer += 1

print(answer)
