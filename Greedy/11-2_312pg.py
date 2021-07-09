S = list(map(int, input())) # 입력값을 split없이 list 사용하면 독방행
result = 0
i = 0 

<<<<<<< HEAD
for value in S:
  if value < 2 or result == 0:   # 0또는 1일때 더하기
    result += value

  else:
    result *= value

=======
while True:
  if i >= (len(S)-1):
    break

  if S[i] == 0:
    result += S[i+1]
    i += 2

  elif result == 0:
    result += S[i]
    i += 1
  
  else:
    result *= S[i]
    i += 1
>>>>>>> aa431fb43484b6c3c979c00b760aa4b3e6483b54

print(result)

# x or + 연산자를 사용해서 가장 큰 수를 만들기
# 0이 있는경우를 제외하고 모든 자연수 곱하기 
# 처음 나오는 자연수는 더해주기 23:10