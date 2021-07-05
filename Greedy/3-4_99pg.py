N, K = map(int, input().split())
cnt = 0

while True:

  if N % K == 0:
    N /= K
  else:
    N -= 1
  
  cnt+=1

  if N == 1: break

print(cnt)

# N -> 1 될때까지
# 1. N에서 1빼기
# 2. N을 K로 나누기 두가지 방법
# 최대한 K로 나누려고 시도하기...나누기를 위해 뺄셈을 존재시킴 9:26