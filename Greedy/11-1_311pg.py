N = int(input())
K = list(map(int, input().split()))
cnt = 0
i = 0
result = 0

K.sort()    #정렬

for i in K:
  cnt += 1
  if cnt >= i:
    result += 1
    cnt = 0


print(result)
# =======
# K.sort()    #정렬
# K.reverse()

# while True:
#   if i >= N+1:
#     break

#   if K[i] == 1:
#     i += 1
    
#   else:
#     i += K[i]
#     if i >= N+1:
#       break

#   cnt += 1

# print(cnt)
# >>>>>>> aa431fb43484b6c3c979c00b760aa4b3e6483b54

# 공포도 X인 모험가 -> 반드시 X명 이상으로 구성한 모험가 그룹 참여
# : 최댓값을 찾아서 그 그룹에다 때려박아야 하는일..

# 그룹 수의 최댓값 -> 공포도가 최소(1) 부터 그룹핑 해주고.. 
# 순차적으로 그룹핑하기