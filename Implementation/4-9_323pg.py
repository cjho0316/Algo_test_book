# 시간초과
def solution(s):
  for i in range(len(s)):
    m.append(s[i:i+target])
    

    answer = len(m)
    return answer

target = 1
m = []
s = list(str(input()))
k = solution(s)

print(k)