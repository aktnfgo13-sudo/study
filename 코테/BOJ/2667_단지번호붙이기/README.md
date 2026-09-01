# BOJ 2667 - 단지번호붙이기

## 🔗 문제

[백준 2667 - 단지번호붙이기](https://www.acmicpc.net/problem/2667)

## 📌 문제 유형

* DFS
* 재귀
* 그래프 탐색

---

## 📝 문제 풀이

`1`은 집, `0`은 집이 없는 위치를 의미한다.

상하좌우로 연결된 `1`들을 하나의 **단지**로 보고,
각 단지에 포함된 집의 개수를 구한 뒤 오름차순으로 출력한다.

### 풀이 순서

1. `N × N` 형태의 2차원 배열을 입력받는다.
2. 전체 배열을 순회하면서 `1`인 위치를 찾는다.
3. 새로운 단지를 발견하면 `home_local`에 `0`을 추가한다.
4. 해당 위치에서 DFS를 실행한다.
5. 방문한 집을 `2`로 변경하여 다시 방문하지 않도록 한다.
6. 방문할 때마다 `home_local[-1]`을 1 증가시킨다.
7. DFS가 종료되면 해당 단지의 집 개수가 저장된다.
8. 모든 단지를 탐색한 후 오름차순으로 정렬한다.
9. 단지의 개수와 각 단지의 집 개수를 출력한다.

---

## 🔑 주요 변수

| 변수           | 설명                   |
| ------------ | -------------------- |
| `N`          | 지도의 크기               |
| `arr`        | 아파트 단지 지도            |
| `rd`         | 행 방향 이동              |
| `cd`         | 열 방향 이동              |
| `home_local` | 각 단지의 집 개수를 저장하는 리스트 |

---

## 🧠 핵심 개념

### 1. DFS를 이용한 단지 탐색

```python
def search(x, y):
    arr[x][y] = 2
    home_local[-1] += 1

    for direc in range(4):
        rn = x + rd[direc]
        cn = y + cd[direc]

        if rn < 0 or rn >= N or cn < 0 or cn >= N or arr[rn][cn] != 1:
            continue

        search(rn, cn)
```

현재 위치를 방문 처리한 후 상하좌우를 확인한다.

연결된 `1`을 발견하면 재귀적으로 DFS를 실행한다.

---

### 2. 방문 처리

```python
arr[x][y] = 2
```

방문한 집을 `2`로 변경한다.

이렇게 하면 이후 탐색에서 이미 방문한 집을 다시 방문하지 않는다.

```text
1 → 방문하지 않은 집
2 → 방문한 집
0 → 집이 없는 위치
```

---

### 3. 현재 단지의 집 개수 저장

```python
home_local[-1] += 1
```

새로운 단지를 발견하면:

```python
home_local.append(0)
```

을 먼저 실행한다.

따라서 `home_local[-1]`은 **현재 탐색 중인 단지의 집 개수**를 의미한다.

예를 들어:

```text
home_local = [7, 8, 9]
```

라면 현재 단지의 탐색 중에는 마지막 값인 `9`를 증가시킨다.

---

### 4. 새로운 단지 발견

```python
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home_local.append(0)
            search(i, j)
```

전체 지도를 순회하면서 아직 방문하지 않은 `1`을 발견하면 새로운 단지로 판단한다.

새로운 단지를 발견할 때마다 `home_local`에 새로운 값을 추가하고 DFS를 시작한다.

---

### 5. 정렬

```python
home_local.sort()
```

각 단지의 집 개수를 오름차순으로 정렬한다.

---

## 💻 코드

```python
N = int(input())

arr = [list(map(int, input())) for _ in range(N)]

rd = [-1, 1, 0, 0]
cd = [0, 0, -1, 1]

home_local = []


def search(x, y):

    arr[x][y] = 2
    home_local[-1] += 1

    for direc in range(4):
        rn = x + rd[direc]
        cn = y + cd[direc]

        if rn < 0 or rn >= N or cn < 0 or cn >= N or arr[rn][cn] != 1:
            continue

        search(rn, cn)


for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home_local.append(0)
            search(i, j)


home_local.sort()

print(len(home_local))

for x in home_local:
    print(x)
```

---

## ⏱️ 시간 복잡도

전체 `N × N` 배열을 탐색한다.

각 집(`1`)은 DFS 과정에서 한 번만 방문하고 `2`로 변경되므로 전체 시간 복잡도는:

```text
O(N²)
```

이다.

---

## 💡 배운 점

* DFS를 이용한 연결된 영역 탐색
* 재귀함수를 이용한 DFS 구현
* 상하좌우 방향 탐색
* 방문한 위치를 값 변경으로 처리하는 방법
* 하나의 DFS 탐색이 하나의 단지가 되는 구조
* `home_local[-1]`을 이용하여 현재 단지의 크기를 관리하는 방법
