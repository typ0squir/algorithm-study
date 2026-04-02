# import sys
# sys.stdin = open("input.txt")

N, M = map(int, input().split())

total_list = [0] * (N + M)

for i in range(N + M):
    total_list[i] = input()

# print(total_list)

total_dict = {}
for i in range(len(total_list)):
    if not total_list[i] in total_dict:
        total_dict[total_list[i]] = 1
    else:
        total_dict[total_list[i]] += 1
# print(total_dict)

arr = []    # 정답 행렬

arr = [k for k, v in total_dict.items() if v == 2]
arr.sort()

print(len(arr))
for i in range(len(arr)):
    print(arr[i])

# ---------------------------------------------
# 📌 지금 코드의 방식
# - N + M 전체를 다 넣고
# - dict로 카운팅 → 2인 것만 추출

# ⚠️ 하지만 비효율 포인트
# 굳이 카운팅까지 할 필요 없음
# “두 집합의 교집합”만 구하면 됨

# N, M = map(int, input().split())

# set_N = set()
# for _ in range(N):
#     set_N.add(input())

# result = []
# for _ in range(M):
#     name = input()
#     if name in set_N:
#         result.append(name)

# result.sort()

# print(len(result))
# for name in result:
#     print(name)
