# import sys
# sys.stdin = open("input.txt")

N, M = map(int, input().split())
note = [0] * N
searching = [0] * M

for i in range(N):
    note[i] = list(map(str, input().split()))
note.sort()

for i in range(M):
    searching[i] = input()
# print(note)
# print(searching)

dict = {}

for i in range(len(note)):
    if note[i][0][0] not in dict.keys():
        dict[note[i][0][0]] = i
    else:
        dict[note[i][0][0]] = min(dict[note[i][0][0]], i)

# print(dict)

# 찾으려는 사이트의 비밀번호를 찾자!
for i in range(len(searching)):
    k = dict[searching[i][0]]
    for j in range(k, len(note)):
        if note[j][0] == searching[i]:
            print(note[j][1])
            break
