import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
note = [0] * N
searching = [0] * M

# 사이트 - 비밀번호 목록
for i in range(N):
    note[i] = list(map(str, input().split()))
note.sort()

# 사이트 - 비밀번호 목록 나누기
note_site = [0] * N
note_pw = [0] * N
for i in range(N):
    note_site[i] = note[i][0]
    note_pw[i] = note[i][1] 

# 사이트 인덱스 만들기
dict = {}

for i in range(len(note_site)):
    if note_site[i][0] not in dict.keys():
        dict[note_site[i][0]] = i
    else:
        dict[note_site[i][0]] = min(dict[note_site[i][0]], i)

# 비밀번호 찾을 사이트 목록
for i in range(M):
    searching[i] = input()

# 찾으려는 사이트의 비밀번호를 찾자!
for i in range(len(searching)):
    k = dict[searching[i][0]]
    for j in range(k, len(note)):
        if note_site[j] == searching[i]:
            print(note_pw[j])
            break
