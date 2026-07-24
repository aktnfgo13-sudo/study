# 🐍 Python Control of Flow (제어문)

파이썬의 **조건문(Conditional Statement)** 과 **반복문(Loop Statement)**, 그리고 반복문에서 자주 사용하는 `break`, `continue`, `pass`, `map()`, `zip()`, `enumerate()` 등을 정리한 학습 노트입니다.

---

# 📚 목차

1. 제어문(Control of Flow)
2. 조건문(if)
3. 반복문(for)
4. 반복문(while)
5. break
6. continue
7. pass
8. map()
9. zip()
10. enumerate()
11. for-else
12. SSAFY TIP
13. 핵심 정리

---

# 1. 제어문(Control of Flow)

프로그램은 기본적으로 **위에서 아래로 순차적으로 실행**됩니다.

제어문(Control of Flow)은 이러한 실행 흐름을 변경하는 문법입니다.

대표적으로

- 조건문(if)
- 반복문(for)
- 반복문(while)

가 있습니다.

---

# 2. 조건문 (if)

조건이 참(True)일 때만 실행합니다.

```python
score = 90

if score >= 80:
    print("합격")
```

출력

```
합격
```

---

## if - else

```python
score = 60

if score >= 80:
    print("합격")
else:
    print("불합격")
```

---

## if - elif - else

```python
score = 75

if score >= 90:
    print("A")

elif score >= 80:
    print("B")

else:
    print("C")
```

---

## 비교 연산자

| 연산자 | 의미 |
|--------|------|
| == | 같다 |
| != | 다르다 |
| > | 크다 |
| < | 작다 |
| >= | 크거나 같다 |
| <= | 작거나 같다 |

---

## 논리 연산자

| 연산자 | 의미 |
|--------|------|
| and | 모두 참 |
| or | 하나라도 참 |
| not | 반대 |

---

# 3. 반복문 (for)

반복 횟수가 정해져 있을 때 사용합니다.

```python
for i in range(5):
    print(i)
```

출력

```
0
1
2
3
4
```

---

## range()

```python
range(5)
```

↓

```
0 1 2 3 4
```

---

```python
range(1,6)
```

↓

```
1 2 3 4 5
```

---

```python
range(1,10,2)
```

↓

```
1 3 5 7 9
```

---

## 리스트 순회

```python
fruits = ["apple","banana","orange"]

for fruit in fruits:
    print(fruit)
```

---

## 문자열 순회

```python
word = "Python"

for ch in word:
    print(ch)
```

---

# 4. while

조건이 참인 동안 계속 반복합니다.

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

## while True

무한 반복

```python
while True:
    print("Hello")
```

종료하려면

```python
break
```

를 사용합니다.

---

# 5. break

반복문을 즉시 종료합니다.

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

출력

```
0
1
2
3
4
```

---

# 6. continue

현재 반복만 건너뛰고 다음 반복을 수행합니다.

```python
for i in range(6):

    if i == 3:
        continue

    print(i)
```

출력

```
0
1
2
4
5
```

---

## break vs continue

| break | continue |
|--------|----------|
| 반복 종료 | 현재 반복만 건너뜀 |

---

# 7. pass

아무 동작도 하지 않습니다.

```python
if True:
    pass
```

주로

- 함수 작성 전
- 조건문 작성 전

사용합니다.

---

# 8. map()

여러 데이터를 한 번에 변환합니다.

```python
numbers = list(map(int,input().split()))
```

입력

```
1 2 3
```

결과

```
[1,2,3]
```

---

## map 구조

```python
map(함수, 반복가능객체)
```

예시

```python
list(map(str,[1,2,3]))
```

↓

```
['1','2','3']
```

---

# 9. zip()

여러 리스트를 묶어줍니다.

```python
name=["A","B","C"]
score=[90,80,70]

for n,s in zip(name,score):
    print(n,s)
```

출력

```
A 90
B 80
C 70
```

---

# 10. enumerate()

인덱스와 값을 함께 반환합니다.

```python
fruits=["apple","banana","orange"]

for idx,value in enumerate(fruits):
    print(idx,value)
```

출력

```
0 apple
1 banana
2 orange
```

---

## 시작 번호 변경

```python
enumerate(fruits,start=1)
```

↓

```
1 apple
2 banana
3 orange
```

---

# 11. for - else

반복문이 **정상 종료**되면 else가 실행됩니다.

```python
for i in range(5):
    print(i)

else:
    print("끝")
```

---

break가 실행되면

else는 실행되지 않습니다.

```python
for i in range(5):

    if i==2:
        break

else:
    print("끝")
```

---

# SSAFY TIP ⭐

## range()

```python
range(N)
```

가 가장 많이 사용됩니다.

---

## map()

알고리즘에서 가장 많이 사용

```python
arr=list(map(int,input().split()))
```

---

## enumerate()

인덱스가 필요하면

```python
for idx,value in enumerate(arr):
```

사용

---

## zip()

두 리스트를 동시에 순회할 때 사용

```python
for a,b in zip(arr1,arr2):
```

---

## while True

무한 반복

```python
while True:
```

↓

종료

```python
break
```

---

## continue

현재 반복만 건너뜀

---

## pass

빈 코드 작성용

---

# 자주 하는 실수 ⚠️

### while 무한루프

```python
i=0

while i<5:
    print(i)
```

↓

증가 코드 없음

```python
i+=1
```

필수

---

### continue 위치

```python
while i<5:

    continue

    i+=1
```

↓

무한루프 발생

---

### range(5)

```
1~5
```

가 아니라

```
0~4
```

입니다.

---

# 핵심 비교

| 문법 | 설명 |
|------|------|
| if | 조건 실행 |
| for | 횟수 반복 |
| while | 조건 반복 |
| break | 반복 종료 |
| continue | 현재 반복 건너뜀 |
| pass | 아무 작업 안 함 |
| map | 데이터 변환 |
| zip | 여러 리스트 묶기 |
| enumerate | 인덱스와 값 반환 |

---

# 자주 사용하는 코드

```python
for i in range(N):
```

```python
while True:
```

```python
arr=list(map(int,input().split()))
```

```python
for idx,value in enumerate(arr):
```

```python
for a,b in zip(arr1,arr2):
```

---

# ✅ 한 줄 요약

- **if** → 조건 실행
- **for** → 횟수 반복
- **while** → 조건 반복
- **break** → 반복 종료
- **continue** → 현재 반복만 건너뜀
- **pass** → 빈 코드 작성
- **map()** → 데이터 변환
- **zip()** → 여러 리스트 동시 순회
- **enumerate()** → 인덱스와 값을 함께 사용