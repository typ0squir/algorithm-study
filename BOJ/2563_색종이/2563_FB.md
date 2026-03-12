## 문제

BOJ 2563 색종이(2026-03-12)

---

## 접근

처음에는 효율적으로 하고자 평면을 직접 채우는 방식 대신 y좌표를 구간으로 나누고 → 각 구간에서 x를 채우는 방식 사용

---

## 사용한 알고리즘

* Sweep Line / 구간 분할
  - 평면을 한 줄씩 쓸어가면서(sweep) 상태를 업데이트하며 계산하는 방식
* Coordinate Compression(좌표 압축)
  - 실제 좌표 대신 의미 있는 좌표들만 모아서 인덱스로 재표현하는 것

---

## 시행착오

- y 구간이 색종이에 포함되는 조건을
여러 경우로 나누어 작성했는데 하나로 줄일 수 있었음.

  ```python
  if (arr[j][1] == y_arr[i] and arr[j][1] + 10 > y_arr[i+1]):
  if (arr[j][1] < y_arr[i] and arr[j][1] + 10 == y_arr[i+1]):
  if (arr[j][1] < y_arr[i] and arr[j][1] + 10 > y_arr[i+1]):
  if (arr[j][1] == y_arr[i] and arr[j][1] + 10 == y_arr[i+1]):
  ```
  네 가지 의미는 결국 하나
  ```
  현재 y구간 [y_arr[i], y_arr[i+1]] 이 색종이의 y범위 [y, y+10] 안에 포함되는가?
  ```

  ```
  색종이 y범위: [y, y+10]
  현재 구간: [y_arr[i], y_arr[i+1]]

  겹침 조건:
  y <= y_arr[i] and y+10 >= y_arr[i+1]
  ```

- 좌표 범위가 작아서 100×100 배열 브루트포스로 진행하는 것이 더 효율적
  ```python
    n = int(input())

    paper = [[0]*100 for _ in range(100)]

    for _ in range(n):
        x, y = map(int, input().split())

        for i in range(x, x+10):
            for j in range(y, y+10):
                paper[i][j] = 1

    S = 0
    for i in range(100):
        for j in range(100):
            if paper[i][j] == 1:
                S += 1

    print(S)
  ```
  - 시간 복잡도 100 * 100 = 10000
---

## 배운 점
- 알고리즘 방향은 맞는데 문제에 비해 과한 해결책
- 좌표 범위가 더 커지면 내가 전개한 알고리즘이 더 적합
