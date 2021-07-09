def solution(food_times, k):
  i = 0

  while True:
    if i > len(food_times)-1:
      i = 0
    
    if k == 0:
      break

    if food_times[i] < 1: 
      i += 1

    food_times[i] -= 1
    
    i += 1
    k -= 1

  answer = i+1

  return answer

N, k = map(int, input().split())
S = list(map(int, input().split(',')))

x = solution(S, k)
print(x)


# 1~N 회전판이고 번호 증가하는 순서대로 가져다 놓음 (N -> 1)
# N개의 배열이 주어지고, 각 속성은 1초에 하나씩 감소(한번 갈때마다 -1) 
# 네트워크 장애 때는 해당하는 속성값을 빼지않고 그다음으로 넘어간다.
# 그다음으로 넘어가는 음식이 몇번인지 return하기 38:30