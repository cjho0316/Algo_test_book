S = list(map(int, input())) # 입력값을 split없이 list 사용하면 독방행
result = 0
i = 0 

for value in S:
  if value < 2 or result == 0:   # 0또는 1일때 더하기
    result += value

  else:
    result *= value


print(result)

# x or + 연산자를 사용해서 가장 큰 수를 만들기
# 0이 있는경우를 제외하고 모든 자연수 곱하기 
# 처음 나오는 자연수는 더해주기 23:10