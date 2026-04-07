import sys
sys.stdin = open("input.txt")

n = int(input())

sqr = [0] * 300
last_idx = 0    # sqr에 채워진 마지막 인덱스

# arr 배열 생성
for i in range(1, len(sqr)):
    if i * i <= n:
        sqr[i] = i * i
    else:
        break
    last_idx = i

sqr = sqr[1 : last_idx + 1]
print(sqr)

result = [0] * 4
idx = 3

# 최소 개수로 제곱수의 합 구하기
# 뭔가 백 트래킹 써야할 것 같은데 어떻게 해야할 지 잘 모르겠다;;


# for i in range(last_idx, 0, -1):
#     if arr[i] <= n:
#         dp
        
#         n -= dp[i]
#         print(f'n에 {dp[i]} 빼기, i = {i}, n = {n}')
#         min_num += 1
        
# print(min_num)