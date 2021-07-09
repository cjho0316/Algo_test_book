S = list(map(int, input()))
<<<<<<< HEAD
zero_cnt = 0
one_cnt = 0
pre = 999

for value in S:
  if value == 0 and pre != 0: 
    zero_cnt += 1

  if value == 1 and pre != 1:
    one_cnt += 1
    
  pre = value


print(min(zero_cnt, one_cnt))

# =======
# cnt = 0
# i = 0

# if S.count(1) < S.count(0):
#   K = 1
# else:
#   K = 0

# while True:
#   if i > len(S)-1:
#     break

#   if S[i] == K and S[i] != S[i+1]: 
#     cnt += 1

#   i+=1

# print(cnt)
# >>>>>>> aa431fb43484b6c3c979c00b760aa4b3e6483b54


# 0 과1주어져 있을 때 문자열 S의 모든 숫자를 전부 같게 만들기 

# 처음 linear search로 0 또는 1의 갯수세기
# 그중 적은 갯수를 가지고 있는 값을 피벗으로 하기

# 예를들어 (연속적인)1이 더 작을때 1->0인 경우만 카운팅하기 over
