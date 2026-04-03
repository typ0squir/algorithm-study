# import sys
# sys.stdin = open("input.txt")

T = int(input())
N_arr = [0] * T
for i in range(T):
    N_arr[i] = int(input())
# print(max(N_arr))

if max(N_arr) <= 3:
    for i in range(T):
        print(1)
else:
    P_arr = [0] * max(N_arr)
    P_arr[0] = P_arr[1] = P_arr[2] = 1

    for i in range(3, len(P_arr)):
        P_arr[i] = P_arr[i-3] + P_arr[i-2]

    for i in range(len(N_arr)):
        print(P_arr[N_arr[i] - 1])
