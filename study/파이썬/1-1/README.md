# 🐍 Python 기초 정리

## Python이란?

- **Python**은 인터프리터(Interpreter) 언어이다.
- 컴파일 언어(C, Java)처럼 `int main(){}`와 같은 선언부가 필요하지 않다.
- 코드를 한 줄씩 해석하며 실행한다.

---

# 프로그램이란?

프로그램(Program)은 **명령어의 집합**이며, 데이터를 처리하기 위해 작성된다.

대표적인 데이터 처리(CRUD)

- **Create** : 생성
- **Read** : 조회
- **Update** : 수정
- **Delete** : 삭제

데이터를 다룰 때 고려할 사항

- 어디에 저장할 것인가
- 무엇을 저장할 것인가
- 어떤 데이터 타입인가

---

# 데이터 타입(Data Type)

| 데이터 타입 | 분류 | 설명 | 예시 | 특징 |
|-------------|------|------|------|------|
| `int` | 숫자형 | 정수 | `10` | |
| `float` | 숫자형 | 실수 | `3.14` | |
| `complex` | 숫자형 | 복소수 | `1+2j` | |
| `str` | 시퀀스형 | 문자열 | `"hello"` | 변경 불가, 순서 O |
| `list` | 시퀀스형 | 리스트 | `[1,2,3]` | 변경 가능, 순서 O |
| `tuple` | 시퀀스형 | 튜플 | `(1,2)` | 변경 불가, 순서 O |
| `range` | 시퀀스형 | 범위 | `range(5)` | 변경 불가 |
| `set` | 집합형 | 집합 | `{1,2,3}` | 순서 X, 중복 X, 변경 가능 |
| `dict` | 매핑형 | 딕셔너리 | `{"a":1}` | Key-Value 구조 |
| `bool` | 기타 | 참/거짓 | `True`, `False` | |
| `None` | 기타 | 값이 없음 | `None` | |
| `function` | 기타 | 함수 | `def add(a,b)` | 재사용 가능한 코드 |

---

# 시퀀스(Sequence) 타입

시퀀스 타입

- `str`
- `list`
- `tuple`
- `range`

공통 특징

1. 순서(O)
2. 인덱싱(Indexing)
3. 슬라이싱(Slicing)
4. 길이(len)
5. 반복(Iteration)

---

## 인덱싱(Indexing)

```python
my_data = [10, 20, 30]

print(my_data[0])   # 10
print(my_data[-1])  # 30
```

---

## 슬라이싱(Slicing)

형식

```python
my_data[start:stop:step]
```

예시

```python
my_data = [0,1,2,3,4,5]

print(my_data[1:4])
```

결과

```python
[1,2,3]
```

> `stop`은 포함되지 않는다.

역방향

```python
print(my_data[-1:-5:-1])
```

---

# 변수명 작성 규칙

## Snake Case (Python 권장)

```python
my_name
```

---

## Pascal Case

```python
MyName
```

주로 클래스명

---

## Camel Case

```python
myName
```

주로 Java에서 사용

---

# 실수(Floating Point)

컴퓨터는 실수를 정확히 표현하지 못하는 경우가 있다.

```python
0.3 - 0.2 == 0.2 - 0.1
```

결과

```python
False
```

비교 방법

```python
abs((0.3-0.2) - (0.2-0.1)) < 0.00001
```

---

# 문자열(String)

특징

- 순서 O
- 인덱싱 O
- 슬라이싱 O
- **변경 불가(Immutable)**

예시

```python
text = "hello"

text[0] = "H"
```

결과

```
TypeError
```

---

# 이스케이프 시퀀스(Escape Sequence)

| 문자 | 의미 |
|------|------|
| `\n` | 줄바꿈 |
| `\t` | 탭 |
| `\\` | \ 출력 |
| `\'` | 작은따옴표 |
| `\"` | 큰따옴표 |

---

# Dictionary

생성

```python
my_dict = {
    "apple": 12,
    "list": [1,2,3]
}
```

## Key

- 값을 식별하기 위한 이름
- 중복 불가
- 변경 불가능한 자료형만 가능

가능

- str
- int
- float
- tuple

불가능

- list
- dict
- set

## Value

모든 자료형 사용 가능

---

# Other Types

## None

```python
None
```

값이 없음을 의미

---

## Boolean

```python
True
False
```

---

# 형 변환(Type Casting)

## 암시적 형 변환

Python이 자동 변환

- 정수 → 실수
- `True == 1`
- `False == 0`

예시

```python
3 + 2.5
```

결과

```python
5.5
```

---

## 명시적 형 변환

직접 변환

```python
int("10")
float(3)
str(100)
```

---

# 산술 연산자

| 연산자 | 의미 |
|---------|------|
| + | 덧셈 |
| - | 뺄셈 |
| * | 곱셈 |
| / | 나눗셈 |
| // | 몫 |
| % | 나머지 |
| ** | 거듭제곱 |

---

# 복합 대입 연산자

```python
a += 1
a -= 1
a *= 2
a /= 2
```

---

# 비교 연산자

## ==

**값(Value)** 비교

```python
2 == 2.0
```

결과

```python
True
```

---

## is

**객체의 주소(Identity)** 비교

```python
2 is 2.0
```

결과

```python
False
```

주로

- None
- True
- False

비교에 사용

### 예제 1

```python
a = [1,2,3]
b = [1,2,3]

print(a is b)
```

결과

```python
False
```

### 예제 2

```python
a = [1,2,3]
b = a

print(a is b)
```

결과

```python
True
```

---

# 논리 연산자

```python
and
or
not
```

---

# 단축 평가(Short Circuit)

## and

하나라도 `False`이면 뒤는 실행하지 않는다.

```python
False and print("Hello")
```

---

## or

하나라도 `True`이면 뒤는 실행하지 않는다.

```python
True or print("Hello")
```

### False로 취급되는 값(Falsy)

```python
''
0
[]
None
False
```

> **주의**
>
> ```python
> [None]
> ```
>
> 리스트 자체는 비어 있지 않으므로 `True`이다.

---

# 멤버십 연산자

```python
in
not in
```

예시

```python
3 in [1,2,3]
```

결과

```python
True
```

---

# 시퀀스 연산자

## 결합

```python
"Hello" + "Python"
```

결과

```python
HelloPython
```

---

## 반복

```python
"Hi" * 3
```

결과

```python
HiHiHi
```

---

# 연산자 우선순위

```
산술 연산
    ↓
비교 연산
    ↓
논리 연산
```

---

# 패킹(Packing)

여러 값을 하나의 **튜플(Tuple)** 로 자동 묶어주는 기능

```python
a = 1, 2, 3

print(a)
```

결과

```python
(1, 2, 3)
```

예시

```python
x, y = 10, 20
```

오른쪽 값은 자동으로 튜플로 패킹된 후 각각 변수에 언패킹된다.
