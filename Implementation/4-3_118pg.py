def turn_left():                #왼쪽으로 회전
  global direction
  direction -= 1
  if direction == -1:
    direction = 3


N, M = map(int, input().split())
A, B, direction = map(int, input().split()) #캐릭터 위치 init

S = [[0 for _ in range(M)] for _ in range(N)] # 방문위치 init
# [[0]*m for _ in range(N)]으로도 2차원 리스트 초기화 가능하다
S[A][B] = 1                               #현재 좌표 방문 처리

array = []
for i in range(N):                        # 전체 맵 정보 입력받기
  array.append(list(map(int, input().split())))

dx = [-1,0,1,0]                           #사분위 방향 정의
dy = [0,1,0,-1]

cnt = 1
turn_time = 0                             # 4번생기면 종료위해 변수선언

while True:
  turn_left()
  nx = A + dx[direction]
  ny = B + dy[direction]

  if S[nx][ny] ==0 and array[nx][ny] == 0:# 방문x, 육지일때 
    S[nx][ny] = 1                         # 현재 좌표 방문처리
    x = nx
    y = ny
    cnt += 1
    turn_time = 0
    continue
    
  else:
    turn_time += 1

  if turn_time == 4:
    nx = x-dx[direction]
    ny = y-dy[direction]
    if array[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    
    turn_time = 0

print(cnt)
