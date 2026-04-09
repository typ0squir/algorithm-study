import sys
sys.stdin = open("input.txt")

T = int(input())

N_arr = [0] * T
for n in range(T):
    N_arr[n] = int(input())

if max(N_arr) > 1:
    dp = [0] * (max(N_arr) + 1)
    dp[0] = [1, 0]
    dp[1] = [0, 1]

    for i in range(2, len(dp)):
        dp[i] = [0, 0]
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

for i in range(len(N_arr)):
    if N_arr[i] == 0:
        print(1, 0)
    elif N_arr[i] == 1:
        print(0, 1)
    else:
        print(dp[N_arr[i]][0], dp[N_arr[i]][1])

# print(dp)