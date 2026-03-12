import sys
sys.stdin = open("input.txt")

# 특정 방향으로 돌 때 경비원 ~ 상점 거리
def calculate(standard) :
    pass

def direct(i):
    print("direct 함수 시작")
    start = direction.index(i)  # 특정 방향의 시작점 찾기
    print(start)



width, height = map(int, input().split())
stores = int(input())
locations = [list(map(int, input().split())) for _ in range(stores+1)]
direction = [4, 1, 3, 2]    # 특정 방향
length = 2 * width + 2 * height
security = locations[-1]

direct(security[1])


print(width, height)
print(stores)
print(locations)
print(security)