import sys
sys.stdin = open("input.txt")

def calculate_distance(direction, distance):
    s = 0   # 특정 상점 ~ 동근 거리
    idx = order.index(security[0])

    # 상점이 동근이와 같은 방향에 있는 경우
    if direction == security[0]:
        s += abs(security[1] - distance)
        print(f"상점이 동근이와 같은 방향 s = {s}")    
        return s
    
    
    # 상점이 동근이와 다른 방향에 있는 경우

    # 동근 ~ 꼭지점
    if security[0] == 2:
        s = security[1]
    elif security[0] == 3:
        s = security[1]
    elif security[0] == 1:
        s = width - security[1]
    elif security[0] == 4:
        s = height - security[1]
    
    while True:
        idx += 1    # 다음 방향으로 이동
        print(f"현재 방향 : {order[idx % 4]}")
        print(f"한 지점까지의 중간 거리 : {s}")    
        val = order[idx % 4]    # 현재 방향
        
        if val == direction:
            if val == 1 or val == 4:
                s += distance
            elif val == 2:
                s += width - distance
            elif val == 3:
                s += height - distance
            return s
        else:
            if val == 3 or val == 4:
                s += height
            elif val == 1 or val == 2:
                s += width
        

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

order = [3, 1, 4, 2]    # 시계 방향으로 계산


for i in range(stores):
    print("-------------------------------------------")
    # 서 > 북 > 동 > 순서로 모든 상점이 동근이로부터 떨어진 거리 구하기
    # 저장한 모든 수를 더하기
    print(locations[i][0], locations[i][1])
    s = calculate_distance(locations[i][0], locations[i][1])
    print(f"한 지점까지의 거리 : {s}")

    # 각 거리와 (둘레-거리)를 비교해 작은 수를 저장
    if length - s < s:
        s = length - s
    print(f"한 지점까지의 최소 거리 : {s}")

    S += s

print(f"최종 결과 : {S}")