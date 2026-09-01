# BOJ 15686 - 치킨 배달

## 🔗 문제

[백준 15686 - 치킨 배달](https://www.acmicpc.net/problem/15686)

## 📌 문제 유형

* 브루트포스
* 조합
* 구현

---

## 📝 문제 풀이

도시의 치킨집 중에서 **최대 M개를 선택**하여 남겼을 때,
각 집에서 가장 가까운 치킨집까지의 거리인 **치킨 거리의 합**이 최소가 되는 경우를 구한다.

### 풀이 순서

1. 입력받은 행렬에서 집(`1`)과 치킨집(`2`)의 좌표를 각각 저장한다.
2. 모든 집과 모든 치킨집 사이의 **맨해튼 거리**를 미리 계산한다.
3. 치킨집 중에서 `M`개를 선택하는 모든 경우를 **조합**으로 탐색한다.
4. 선택된 치킨집에 대해 각 집에서 가장 가까운 치킨집까지의 거리를 구한다.
5. 모든 집의 치킨 거리 합을 계산한다.
6. 모든 조합 중 치킨 거리의 최솟값을 `result`에 저장한다.

---

## 🔑 주요 변수

| 변수             | 설명                    |
| -------------- | --------------------- |
| `arr`          | 입력받은 도시 정보            |
| `home_rc`      | 집(`1`)의 `(행, 열)` 좌표   |
| `restorant_rc` | 치킨집(`2`)의 `(행, 열)` 좌표 |
| `pick_number`  | 현재 조합에서 선택한 치킨집의 인덱스  |
| `distances`    | 각 집과 치킨집 사이의 거리       |
| `result`       | 최소 치킨 거리 합            |

---

## 🧠 핵심 개념

### 1. 좌표 저장

```python
if 1 == arr[i][j]:
    home_rc.append((i, j))

if 2 == arr[i][j]:
    restorant_rc.append((i, j))
```

집과 치킨집의 위치를 `(행, 열)` 형태의 튜플로 저장한다.

---

### 2. 맨해튼 거리 미리 계산

두 좌표 `(r1, c1)`, `(r2, c2)` 사이의 거리는:

```text
|r1 - r2| + |c1 - c2|
```

이다.

```python
distances[i][j] = abs(home_rc[i][0] - restorant_rc[j][0]) \
                + abs(home_rc[i][1] - restorant_rc[j][1])
```

모든 집과 치킨집 사이의 거리를 미리 계산하여 저장한다.

---

### 3. 조합을 이용한 치킨집 선택

```python
for i in range(idx, len(restorant_rc)):
    pick_number.append(i)
    combo(depth + 1, i + 1)
    pick_number.pop()
```

치킨집 중에서 `M`개를 선택하는 모든 경우를 탐색한다.

`i + 1`을 사용하여 이미 선택한 치킨집을 다시 선택하지 않는다.

---

### 4. 각 집의 최소 치킨 거리 계산

```python
min_distance = float('inf')

for chicken_idx in pick_number:
    distance = distances[home_idx][chicken_idx]
    min_distance = min(distance, min_distance)

total += min_distance
```

현재 선택된 치킨집들 중에서
각 집과 가장 가까운 치킨집까지의 거리를 선택한다.

---

### 5. 가지치기

```python
if total >= result:
    return
```

현재까지 계산한 치킨 거리 합이 이미 기존 최솟값보다 크거나 같다면
더 탐색해도 최솟값이 될 수 없으므로 해당 경우의 탐색을 중단한다.

---

## 💻 코드

```python
N, M = map(int,input().split()) 
# N = 행렬 사이즈
# M = 폐업시키지 않을 치킨집 최대 개수

arr = [list(map(int,input().split())) for _ in range(N)]

home_rc = []
restorant_rc = []
pick_number = []

result = float('inf')


# 집 & 치킨집 좌표 저장
for i in range(N):
    for j in range(N):
        if 1 == arr[i][j]:
            home_rc.append((i, j))

        if 2 == arr[i][j]:
            restorant_rc.append((i, j))


# 집과 치킨집 사이의 거리 미리 계산
distances = [
    [0] * len(restorant_rc)
    for _ in range(len(home_rc))
]

for i in range(len(home_rc)):
    for j in range(len(restorant_rc)):
        distances[i][j] = (
            abs(home_rc[i][0] - restorant_rc[j][0])
            + abs(home_rc[i][1] - restorant_rc[j][1])
        )


def combo(depth, idx):
    # 조합

    global result

    if depth == M:
        total = 0

        # 모든 집에 대해
        for home_idx in range(len(home_rc)):

            # 최소 거리 치킨집 선정
            min_distance = float('inf')

            for chicken_idx in pick_number:
                distance = distances[home_idx][chicken_idx]
                min_distance = min(distance, min_distance)

            total += min_distance

            # 가지치기
            if total >= result:
                return

        result = total
        return

    # 치킨집 M개 선택
    for i in range(idx, len(restorant_rc)):
        pick_number.append(i)
        combo(depth + 1, i + 1)
        pick_number.pop()


combo(0, 0)

print(result)
```

---

## ⏱️ 시간 복잡도

치킨집의 개수를 `C`라고 하면 `C ≤ 13`이므로,

```text
C C M
```

개의 조합을 탐색한다.

각 조합마다 모든 집에 대해 선택된 치킨집과의 최소 거리를 확인한다.

따라서 대략:

```text
O(C M × H × M)
```

수준으로 볼 수 있으며, `C ≤ 13`이므로 브루트포스 + 조합으로 충분히 해결할 수 있다.

---

## 💡 배운 점

* 2차원 좌표를 `(행, 열)` 튜플로 저장하는 방법
* 맨해튼 거리 계산
* 조합을 이용한 경우의 수 탐색
* 미리 거리를 계산하여 반복 계산 줄이기
* `float('inf')`를 이용한 최솟값 초기화
* 가지치기를 이용한 탐색 범위 줄이기
