
n = int(input())  # n : 색종이 수
arr = [list(map(int, input().split())) for _ in range(n)]
x_max = -1  # x_max : 색종이의 위치 중 최대 x좌표
S = 0 # S : 총 넓이

y_set = set() # y_set : 가능한 y좌표들의 집합
for i in range(len(arr)):
  # 색종이 각 꼭지점의 좌표를 y 집합으로 각각 나누기
  y_set.add(arr[i][1])
  y_set.add(arr[i][1]+10)

  # 색종이의 위치 중 최대 x좌표
  if x_max < arr[i][0] :
    x_max = arr[i][0]

x_max += 11 # 인덱스 번호 고려 10 + 1

y_arr = list(y_set)
y_arr.sort()

# 높이 구간 별로 넓이 계산
for i in range(len(y_arr)-1):

  # x_arr : x좌표 중 중복 확인할 배열
  x_arr = [0] * x_max

  # 색종이 1개 씩 가져오기
  for j in range(len(arr)):

    # 색종이의 y좌표가 구간의 최소값과 같고 y좌표 + 10이 구간의 최대값보다 큰 경우
    if (arr[j][1] == y_arr[i] and arr[j][1] + 10 > y_arr[i+1]):
      for k in range(arr[j][0], arr[j][0]+10):
        if x_arr[k] == 0:
          x_arr[k] = 1

    # 색종이의 y좌표가 구간의 최소값보다 작고 y좌표 +10이 구간의 최대값과 같은 경우      
    if (arr[j][1] < y_arr[i] and arr[j][1] + 10 == y_arr[i+1]):
      for k in range(arr[j][0], arr[j][0]+10):
        if x_arr[k] == 0:
          x_arr[k] = 1

    # 색종이의 y좌표가 구간의 최소값과 작고 y좌표 +10이 구간의 최대값과 큰 경우
    if (arr[j][1] < y_arr[i] and arr[j][1] + 10 > y_arr[i+1]):
      for k in range(arr[j][0], arr[j][0]+10):
        if x_arr[k] == 0:
          x_arr[k] = 1

    # 색종이의 y좌표가 구간의 최소값과 같고 y좌표 +10이 구간의 최대값과 같은 경우
    if (arr[j][1] == y_arr[i] and arr[j][1] + 10 == y_arr[i+1]):
      for k in range(arr[j][0], arr[j][0]+10):
        if x_arr[k] == 0:
          x_arr[k] = 1
  


  for m in range(len(x_arr)):
    if x_arr[m] == 1:
      S += y_arr[i+1] - y_arr[i]

print(S)