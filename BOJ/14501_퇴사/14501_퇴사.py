# import sys
# sys.stdin = open("input.txt")

N = int(input())
Ti = [0] * (N + 1)
Pi = [0] * (N + 1)

for i in range(1, N + 1):
    Ti[i], Pi[i] = map(int, input().split())

# print(Ti)   # [0, 3, 5, 1, 1, 2, 4, 2]
# print(Pi)   # [0, 10, 20, 10, 20, 15, 40, 200]

dp = [0] * (N + 1)    # 각 자리 수는 그 날짜에 일했을 때 받을 수 있는 최대 이익
for i in range(1, N + 1):
    # print(f'{i}일에 있했을 때 받을 수 있는 최대 이익 확인해보자!')

    # 조건: i일에 일할 때 N일 전에 끝나야함
    if N + 1 - i >= Ti[i]:
        # print(f'{i}일에 일을한다')
        dp[i] = Pi[i]


        # i일을 일하려면 그 전에 일이 끝나야 함.
        # print(f'{i}일로 올 수 있는 날은')
        for j in range(1, i):
            sum = Pi[i]
            if Ti[j] + j <= i:
                # print(f'{j}일 날!')
                sum += dp[j]
                # print(f'현재 sum = {sum}')
            
            if dp[i] < sum:
                dp[i] = sum
                # print(f'dp[{i}] 교체')
    # print(f'{i}일 확인했을 때 dp = {dp}')
print(max(dp))
                