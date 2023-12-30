N, M = map(int, input().split())
ans = 0

# # 방법 1: 하나씩 빼는 방법
# # 큰 숫자일수록 효율이 떨어짐
# while True:
#     if N == 1:
#         break
#     elif N % M == 0:    # elif를 사용했으므로 N이 1이 아니고, M으로 나누어 떨어지는경우 
#         N = N // M      # 나눔
#     else : 
#         N -= 1          # N이 1이 아니고, M으로 나누어 떨어지지 않는 경우 
#     ans += 1


# 방법 2: 
while True:
    tmp = (N // M) * M  # 몫 * M
    ans += N - tmp      # 나머지를 한번에 빼준다고 생각 
    N = tmp             # 나머지만큼 빼고 M의 배수인 상태 
    if N < M :          # N이 M보다 작아서 나눌수 없는 경우 
        break           # 반복문 종료
    else :              # N이 M보다 크거나 같은 경우
        N //= M         # 나눔
        ans += 1

ans += (N - 1)          # N이 M보다 작아서 while문을 종료 한 경우, 1이 될 때까지 빼줌 

print(ans)
