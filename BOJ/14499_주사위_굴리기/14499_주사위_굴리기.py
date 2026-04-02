import sys
sys.stdin = open("input.txt")

# 주사위 옮기는 함수
def shift_dice():
    pass

N, M, x, y, K = map(int, input().split())
num_map = [list(map(int, input().split())) for _ in range(N)]
arr = list(map(int, input().split()))

# 처음 위치
