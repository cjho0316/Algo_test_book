N, M = map(int, input().split())
S = list(map(int, input().split()))
cnt = 0

S.sort()

for i in range(len(S)-1):
  for j in range(i+1, len(S)):
   if S[i] != S[j]:
     cnt += 1

print(cnt)


# 5. 서로다른 볼링공의 조합을 구하는 일이므로
# sort -> 같은것 넘어가고 서로 다른 볼링공이 나올때 값 추가(이중포문) 17:41
# 1 2 2 3 3
# 1.2
# 1.2
# 1.3
# 1.3
# 2.3
# 2.3
# 2.3
# 2.3
