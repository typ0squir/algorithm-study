import sys
sys.stdin = open("input.txt")

def calculate_distance(direction, distance):
    order = [3, 1, 4, 2]
    idx = order.index(security[0])
    print(f"시작 인덱스 : {idx}")

    if security[0] == 1 or security[0] == 3:
        s = security[1]
    elif security[0] == 2:
        s = width - security[1]
    elif security[0] == 4:
        s = height - security[1]
    print(f"시작 거리 : {s}")
    idx += 1

    while True:
        print(f"방향 변화 : {order[idx % 4]}")
        val = order[idx % 4]
        
        if val == direction:
            if direction == 1 or direction == 4:
                s += distance
            elif direction == 2:
                s += width - distance
            elif direction == 3:
                s += height - distance
            break
        else:
            if val == 1 or val == 2:
                s += width
            elif val == 3 or val == 4:
                s += height
            
        print(f"한 지점까지의 중간 거리 : {s}")    
        idx += 1
    print(f"한 지점까지의 거리 : {s}")

    # 각 거리와 (둘레-거리)를 비교해 작은 수를 저장
    if length - s < s:
        s = length - s
    print(f"한 지점까지의 최소 거리 : {s}")
    return s
        

width, height = map(int, input().split())
stores = int(input())   # 상점 수
locations = [list(map(int, input().split())) for _ in range(stores+1)]

length = 2 * width + 2 * height # 둘레
security = locations[-1]    # 동근이 위치
S = 0   # 최단 거리 합

print(width, height)
print(stores)
print(locations)
print(security)

for i in range(stores):
    # 서 > 북 > 동 > 순서로 모든 상점이 동근이로부터 떨어진 거리 구하기
    # 저장한 모든 수를 더하기
    print(locations[i][0], locations[i][1])
    S += calculate_distance(locations[i][0], locations[i][1])

print(f"최종 결과 : {S}")