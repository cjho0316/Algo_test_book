S = list(map(str, input()))
S.sort()
zero_nine = ['0','1','2','3','4','5','6','7','8','9']
K = []
result = 0


for i in S:
  if i in zero_nine:
    result += int(i)
    del i

  else:
    K.append(i)

K.append(str(result))
X = "".join(K)      # "식별자".join 함수는 문자열로 변환시켜준다


print(X)

#linear search를 하는데 속성값이 0~9 range 안에 있으면 변수에 저장하고 삭제
#for문 -> if S[i] in range(0,9) -> result += S[i] -> del S[i] 33:07