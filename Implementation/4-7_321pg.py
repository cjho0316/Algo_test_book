N = list(map(int, input()))

half = int(len(N/2))
first = 0
last = 0

for i in range(len(N)):
  if i < half:
    first += N[i]
  else:
    last += N[i]

if first == last:
  print("LUCKY")
else:
  print("READY")

# 점수 N 주어지면 -> 왼 / 오 반갈후 오, 왼의 자릿수 합 각각 동일할때
# input N -> 리스트에 저장

# lenN 절반의 int값을 변수에 저장하기
# (짝수만 들어오니깐 0<<lenN/2 , lenN < <lenN으로 저장)

# (0부터 lenN /2)합 구하기
# (lenN /2부터 lenN까지) 합 구하기 

# 서로비교하여 같으면 LUCKY출력 , 다르면 READY 21:04