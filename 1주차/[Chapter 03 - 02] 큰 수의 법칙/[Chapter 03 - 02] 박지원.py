# N, M, K 받아오기
# input() > 입력된 값을 문자열로 받아옴 
# split() > 구분자를 기준으로 구분하여 나눠줌. 기본형 사용시 구분자 띄어쓰기
# input().split() > 입력된 값을 띄어쓰기로 나누어 가져옴 > 여기서 문제 : 문자형으로 받아옴 
# 해결책 : 리스트에 int함수를 적용하여 int로 변경 
# map(int, input().split())
N, M, K = map(int, input().split())
# N개의 자연수 list로 받아오기 
data = list(map(int, input().split()))

#정렬
data.sort(reverse = True) 
# 기본값이 false(오름차순)이라서 내림차순 원할때는 True로 지정해야함
# print(data) 확인용
first_value = data[0]
second_value = data[1]
ans = 0 # 답

# 방법 1
# 가장 큰 값 k번 더하고 두번째로 큰 값 한번 더하는 횟수(K+1)로 나누고 몫만큼 곱함
# 그리고 나머지 만큼 가장 큰 값 더해줌 
ans = (first_value * K + second_value) * (M // (K+1)) + first_value * (M % (K+1))



# 방법 2
#                           # M번 반복되고, 최대 K번 반복 가능하다. 
# while True:
#     for i in range(K):    # K번 반복
#         if M == 0:
#             break
#         ans += first_value
#         M -= 1
#     if M == 0:
#         break
#     ans += second_value   # K번 중복 후 그 다음값 1번 
#     M -= 1

print(ans)


