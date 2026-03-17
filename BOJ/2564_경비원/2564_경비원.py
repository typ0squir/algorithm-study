import sys
sys.stdin = open("input.txt")

width, height = map(int, input().split())
stores = int(input())   # 상점 수
locations = [list(map(int, input().split())) for _ in range(stores+1)]

length = 2 * width + 2 * height # 둘레
coord = [0] * len(locations)

# print(width, height)
# print(stores)
# print(locations)

# 주어진 위치를 좌표로 변환
for i in range(len(locations)):
    if locations[i][0] == 1:
        coord[i] = [locations[i][1], height]
    elif locations[i][0] == 2:
        coord[i] = [locations[i][1], 0]
    elif locations[i][0] == 3:
        coord[i] = [0, height - locations[i][1]]
    elif locations[i][0] == 4:
        coord[i] = [width, height - locations[i][1]]
# print(coord)

# 주어진 좌표를 한 줄로 표현
arr = [0] * length
arr[-1] = 'X'
# print(arr)

point = coord[-1] # 출발점
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
d = 0

# arr의 모든 요소에 접근할 수 있다.
for i in range(length):
    # 'X'를 기준으로 모든 좌표를 출력해보기
    # print(f"point = {point}")
    point[0] += direction[d % 4][0]
    point[1] += direction[d % 4][1]

    # coor의 요소와 같은 좌표에 상점 번호 찍기
    for j in range(len(coord) - 1):
        if point[0] == coord[j][0] and point[1] == coord[j][1]:
            arr[i] = j + 1

    # 영역의 경계선을 따라 이동
    if point in [[0, 0], [0, height], [width, height], [width, 0]]:
        d += 1
# print(arr)

S = 1   # 최단 거리 합
# 동근이의 위치 ~ 상점 위치의 최단 거리 구하기
for i in range(len(locations) - 1):
    # print(f"{i + 1}번 상점까지의 최단 거리")
    s = arr.index(i + 1)
    if length - s < s:
        s = length - s
    # print(f"s = {s}")
    # 구한 최단 거리를 모두 더하기  
    S += s

print(S)


    