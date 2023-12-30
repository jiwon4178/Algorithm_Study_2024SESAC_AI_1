# N이랑 M 입력받기 
N, M = map(int, input().split())

ans = 0 

## 행마다 가장 작은 수를 찾고, 최소값들을 비교하여 그중 최대값을 찾는다 


# 행마다 반복 
for i in range(N):
    tmp = list(map(int, input().split())) # 한 행 입력받기
    min_value = min(tmp)            # 최소값 찾기 
    ans = max(ans, min_value)       # 기존 최대 값과 비교하여 더 큰값을 저장하기 
  
print(ans)

# # 방법2 2중 for문 
# for i in range(N):
#     tmp = list(map(int, input().split()))
#     min_value = 10001                       # N의 범위가 1이상 10000이하 > 10001은 N에 어떤 수가 와도 가장 큰 수가 됨
#     for a in tmp:                           # 이건 한 행을 다 비교하는거라 효율성이 첫번째 방법보다는 떨어짐 
#         min_value = min(min_value, a)
#     ans = max(ans, min_value)
    
# print(ans)