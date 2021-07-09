N = int(input())
S = list(map(int, input().split()))
S.sort()

target = 1
for x in S:
  if x > target:
    break
  target += x

print(target)