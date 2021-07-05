N, M, K = map(int, input().split())
gd = list(map(int, input().split()))
gd.sort()
gd.reverse()

first = gd[0]
second = gd[1]

cnt = 0

while True:
  for i in range (K):
    if M == 0: break    # 반복문의 처음에 조건문 배치
    cnt += first
    M -= 1
    
  if M == 0: break
  else:
    cnt += second
    M -= 1
    if M == 0: break

print(cnt)

