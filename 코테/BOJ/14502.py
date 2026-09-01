# BOJ 14502 - 연구소

## 🔗 문제

[백준 14502 - 연구소](https://www.acmicpc.net/problem/14502)

## 📌 문제 유형

* 브루트포스
* 조합
* DFS
* 시뮬레이션

---

## 📝 문제 풀이

연구소에 **벽을 3개 설치**한 후 바이러스를 퍼뜨렸을 때,
바이러스가 퍼지지 않은 **안전 영역의 최대 크기**를 구한다.

### 풀이 순서

1. `0`인 위치를 `(행, 열)` 형태의 튜플로 저장한다.
2. `2`인 바이러스의 위치도 저장한다.
3. `0`인 위치 중에서 **3개의 위치를 조합**으로 선택한다.
4. 선택한 3개의 위치에 벽을 설치한다.
5. 기존 행렬을 복사하여 `arr_check`를 만든다.
6. 바이러스 위치에서 DFS를 실행하여 바이러스를 확산시킨다.
7. 바이러스 확산이 끝난 후 `0`의 개수를 센다.
8. 모든 경우 중 안전 영역의 최댓값을 `result`에 저장한다.

---

## 🔑 주요 변수

| 변수          | 설명                  |
| ----------- | ------------------- |
| `arr`       | 입력받은 연구소 원본 행렬      |
| `safe`      | 벽을 설치할 수 있는 `0`의 좌표 |
| `pick_safe` | 현재 조합에서 선택한 3개의 좌표  |
| `poizen`    | 바이러스(`2`)의 좌표       |
| `rd`        | 행 방향 이동             |
| `cd`        | 열 방향 이동             |
| `arr_check` | 바이러스 확산에 사용하는 복사 행렬 |
| `result`    | 안전 영역의 최대 크기        |

---

## 🧠 핵심 개념

### 1. 2차원 좌표를 튜플로 저장

```python
safe.append((i, j))
```

`0`인 위치를 `(행, 열)` 형태로 저장한다.

예:

```text
(1, 2)
(2, 3)
(4, 1)
```

---

### 2. 조합

```python
pick_safe.append(safe[i])
comb(depth + 1, i + 1)
pick_safe.pop()
```

`safe`에 있는 위치 중 **3개를 선택**한다.

`i + 1`을 사용하여 같은 위치를 다시 선택하지 않도록 한다.

---

### 3. 2차원 리스트 복사

```python
arr_check = [row[:] for row in arr]
```

원본 `arr`을 유지하면서 각 경우마다 새로운 연구소를 만들어 사용한다.

`row[:]`는 각 행을 새로운 리스트로 복사한다.

---

### 4. DFS를 이용한 바이러스 확산

```python
if arr_check[xd][yd] == 0:
    arr_check[xd][yd] = 2
    count_safe(xd, yd)
```

바이러스가 이동할 수 있는 `0`을 `2`로 변경하고
재귀적으로 주변 영역까지 바이러스를 확산시킨다.

---

## 💻 코드

```python
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

safe = []
pick_safe = []
poizen = []

rd = [-1, 1, 0, 0]
cd = [0, 0, -1, 1]

arr_check = []
result = 0


for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            safe.append((i, j))
        elif arr[i][j] == 2:
            poizen.append((i, j))


def count_safe(x, y):
    global arr_check

    if arr_check[x][y] == 2:
        for direc in range(4):
            xd = x + rd[direc]
            yd = y + cd[direc]

            if 0 > xd or N <= xd or 0 > yd or M <= yd:
                continue

            if arr_check[xd][yd] == 0:
                arr_check[xd][yd] = 2
                count_safe(xd, yd)


def comb(depth, idx):
    global arr_check
    global result

    if depth == 3:
        count = 0

        # 원본 행렬 복사
        arr_check = [row[:] for row in arr]

        # 선택한 3곳에 벽 설치
        for row, col in pick_safe:
            arr_check[row][col] = 1

        # 바이러스 확산
        for poizen_row, poizen_col in poizen:
            count_safe(poizen_row, poizen_col)

        # 안전 영역 계산
        for i in range(N):
            for j in range(M):
                if arr_check[i][j] == 0:
                    count += 1

        result = max(count, result)
        return

    # 벽 3개를 선택하는 조합
    for i in range(idx, len(safe)):
        pick_safe.append(safe[i])
        comb(depth + 1, i + 1)
        pick_safe.pop()


comb(0, 0)

print(result)
```

---

## ⏱️ 시간 복잡도

빈칸의 개수를 `K`라고 하면 벽 3개를 선택하는 경우는

```text
K C 3
```

이다.

각 경우마다 연구소 전체를 탐색하며 바이러스를 확산시키므로
전체적으로 **브루트포스 + DFS** 방식으로 모든 벽 설치 경우를 확인한다.

---

## 💡 배운 점

* 2차원 리스트를 `row[:]`를 이용해 복사하는 방법
* 튜플을 이용한 2차원 좌표 관리
* DFS를 이용한 영역 탐색
* 재귀함수를 이용한 조합 구현
* 브루트포스를 이용한 모든 경우의 수 탐색
* 원본 배열을 유지하면서 복사본을 이용해 시뮬레이션하는 방법
