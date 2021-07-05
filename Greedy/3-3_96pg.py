N, M = map(int, input().split())
K = [[0 for _ in range(M)] for _ in range(N)] # 2차원배열 생성
min = 0

for i in range(N):
  K[i] = list(map(int, input().split()))
  K[i].sort()
  if min == 0 or min < K[i][0]:
    min = K[i][0]

print(min)


# 리스트 받아오고 -> 제일작은것 선택
# 열(N)만큼 반복...
# 가장 큰 값을 출력하기

# 열마다 이중반복문, min()함수 불러도 됨 -25:44