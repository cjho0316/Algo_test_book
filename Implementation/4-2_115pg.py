S = list(map(str, input()))

X = int(ord(S[0])-96)
Y = int(S[1])

dx = [2,2,-1,1,-2,-2,1,-1]
dy = [1,-1,-2,-2,1,-1,2,2]

cnt = 0

for i in range (len(dx)):
  nx = 0
  ny = 0

  nx = X + dx[i]
  ny = Y + dy[i]

  if nx <1 or nx >8 or ny <1 or ny >8:
    continue
  else:
    cnt += 1

print(cnt)

# 나이트 이동-> 수직2 + 수평1 or 수평2 + 수직1
# 최소1 최대6 만큼 이동가능..

# 위치정보 전달 -> 가능한 범위에 있는지 조사 x축(a~h) y축(1~8) 내부에 있는지.. ->가능한 경우의수 출력

#참고
#steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
#for step in steps:
#nX = X + step[0], nY = Y + step[1] 로도 표현이 가능하다. 22:37ㄿ