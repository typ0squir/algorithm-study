# import sys
# sys.stdin = open("input.txt")

N = int(input())
Ai = list(map(int, input().split()))   # 각 시험장에 있는 응시자 수
B, C = map(int, input().split())    # B : 총감 응시자 수 / C : 부감 응시자 수

num = len(Ai) # 필요한 감독관 수, default: 각 시험장에 총감 1명

# 총감이 감시 가능한 응시자 수 빼기
for i in range(len(Ai)):
    Ai[i] -= B
# print(Ai)

# 부감이 몇 명 필요한지 계산하기
for i in range(len(Ai)):
    if Ai[i] > 0 :
        # print(f'--------------{Ai[i]}명의 응시자가 남음--------------')
        if Ai[i] % C == 0 :
            num += Ai[i] // C
            # print(f'{Ai[i] // C}를 더함')
        else:
            num += Ai[i] // C + 1
            # print(f'{Ai[i] // C + 1}를 더함')

print(num)