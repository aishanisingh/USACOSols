#https://codeforces.com/problemset/problem/41/A
#TODO: check array from the back to reduce memory

straight = input()
backwards = input()
straightarr = []
backwardsarr = []
straightarr[:0] = straight
backwardsarr[:0] = backwards
straightarr.reverse()

straightlen = len(straightarr)
backwardslen = len(backwardsarr)

for i in range(0,len(backwardsarr)):
  if straightarr[i] == backwardsarr[i]:
    answer = "YES"
  else:
    answer = "NO"
    break

print(answer)
