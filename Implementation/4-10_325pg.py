#시간초과, 아이디어 부족
def rotation(Key):

def moving(Key):

def solution(key, lock):
    
    
    answer = True
    return answer

M, N = map(int, input().split())

Lock = [[0]*M for _ in range(M)]
Key = [[0]*N for _ in range(N)]

for i in range(len(Lock)):
  Lock[i] = list(map(int, input().split()))

for j in range(len(Key)):
  Key[j] = list(map(int, input().split()))


solution(Key, Lock)