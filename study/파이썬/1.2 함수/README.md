# 🐍 Python 함수 및 스코프 종합 가이드

파이썬의 **함수(Function)**, **매개변수와 인자(Parameters & Arguments)**, **스코프(Scope)**, **패킹/언패킹(Packing/Unpacking)** 및 **람다 표현식(Lambda Expression)**에 대해 다루는 정리 노트입니다.

---

## 📑 목차
1. [함수 정의와 Docstring](#1-함수-정의와-docstring)
2. [함수 호출과 반환값 (Return vs Print)](#2-함수-호출과-반환값-return-vs-print)
3. [매개변수(Parameter) vs 인자(Argument)](#3-매개변수parameter-vs-인자argument)
4. [함수의 인자 종류](#4-함수의-인자-종류)
   - [위치 인자 (Positional Arguments)](#1-위치-인자-positional-arguments)
   - [기본값 인자 (Default Argument Values)](#2-기본값-인자-default-argument-values)
   - [키워드 인자 (Keyword Arguments)](#3-키워드-인자-keyword-arguments)
   - [가변 인자 (*args)](#4-가변-인자-args)
   - [가변 키워드 인자 (**kwargs)](#5-가변-키워드-인자-kwargs)
   - [인자의 올바른 작성 순서](#6-인자의-올바른-작성-순서-종합)
5. [재귀 함수 (Recursion)](#5-재귀-함수-recursion)
6. [내장 함수 (Built-in Functions)](#6-내장-함수-built-in-functions)
7. [스코프 (Scope) & LEGB Rule](#7-스코프-scope--legb-rule)
8. [global 키워드](#8-global-키워드)
9. [함수 스타일 가이드 & 좋은 설계](#9-함수-스타일-가이드--좋은-설계)
10. [패킹과 언패킹 (Packing & Unpacking)](#10-패킹과-언패킹-packing--unpacking)
11. [람다 표현식 (Lambda Expression)](#11-람다-표현식-lambda-expression)
12. [다중 반환값의 실체 (Return과 Tuple)](#12-다중-반환값의-실체-return과-tuple)

---

## 1. 함수 정의와 Docstring
* `def 함수명(매개변수):` 형태로 정의합니다.
* 함수 첫 줄의 `""" """`는 **docstring**으로, 함수의 설명서(문서화) 역할을 합니다.
* `return`은 값을 돌려주고 함수를 즉시 종료합니다.

```python
def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    result = pram1 + pram2
    return result
```

---

## 2. 함수 호출과 반환값 (Return vs Print)
* 호출된 위치는 **반환된 값(return value)**으로 대체됩니다.
* **`print()`와 `return`의 차이**:
  * `print()`: 화면에 출력만 수행하며, 반환값은 `None`입니다.
  * `return`: 함수 외부로 결과 값을 전달합니다.
  * `return` 문이 없는 함수는 기본적으로 `None`을 반환합니다.

```python
# 반환값이 없는 print() 함수
value = print('hello world')
print(value)  # None

# return문이 없는 사용자 정의 함수
def my_func():
    print('hello')

result = my_func()
print(result)  # None
```

---

## 3. 매개변수(Parameter) vs 인자(Argument)
* **매개변수 (Parameter)**: 함수를 **정의**할 때 값을 받기 위해 선언하는 변수명
* **인자 (Argument)**: 함수를 **호출**할 때 실제로 전달하는 값

```python
def add_numbers(x, y):  # x, y는 매개변수(Parameter)
    result = x + y
    return result

a = 2
b = 3
sum_result = add_numbers(a, b)  # a, b는 인자(Argument)
print(sum_result)  # 5
```

---

## 4. 함수의 인자 종류

> ⚠️ **주의**: 인자의 종류에 따른 문법 규칙을 어기면 `SyntaxError` 또는 `TypeError`가 발생합니다.

### 1) 위치 인자 (Positional Arguments)
전달한 **순서대로** 매개변수에 할당됩니다. 개수가 맞지 않으면 `TypeError`가 발생합니다.

```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Alice', 25)  # 정상 동작
greet(25, 'Alice')  # 순서가 바뀌어 잘못된 값 출력
# greet('Alice')    # TypeError: missing 1 required positional argument: 'age'
```

### 2) 기본값 인자 (Default Argument Values)
매개변수에 미리 기본값을 지정하면, 호출 시 인자를 생략할 수 있습니다.
* ⚠️ **주의**: 기본값이 있는 매개변수는 반드시 **기본값이 없는 매개변수 뒤**에 위치해야 합니다.

```python
def greet(name, age=20):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob')           # 안녕하세요, Bob님! 20살이시군요.
greet('Charlie', 40)   # 안녕하세요, Charlie님! 40살이시군요.
```

### 3) 키워드 인자 (Keyword Arguments)
매개변수 이름을 지정하여 전달하므로 순서를 지키지 않아도 됩니다.
* ⚠️ **규칙**: 키워드 인자 뒤에는 위치 인자가 올 수 없습니다. (`SyntaxError` 발생)

```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='Dave', age=35)
greet(age=35, name='Dave')
# greet(age=35, 'Dave')  # SyntaxError: positional argument follows keyword argument
```

### 4) 가변 인자 (`*args`)
개수가 정해지지 않은 위치 인자를 여러 개 받을 때 사용하며, 전달된 값들은 **튜플(tuple)**로 패킹됩니다.

```python
def calculate_sum(*args):
    print(args)        # (1, 100, 5000, 30)
    print(type(args))  # <class 'tuple'>

calculate_sum(1, 100, 5000, 30)
```

### 5) 가변 키워드 인자 (`**kwargs`)
개수가 정해지지 않은 키워드 인자를 받을 때 사용하며, 전달된 값들은 **딕셔너리(dict)**로 패킹됩니다.

```python
def print_info(**kwargs):
    print(kwargs)  # {'name': 'Eve', 'age': 30}

print_info(name='Eve', age=30)
```

### 6) 인자의 올바른 작성 순서 (종합)
매개변수를 선언할 때는 다음 순서를 엄격히 지켜야 합니다:
> **위치 매개변수 -> 기본값 매개변수 -> `*args` -> `**kwargs`**

```python
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)

func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
# 출력:
# pos1: 1
# pos2: 2
# default_arg: 3 (기본값이 3으로 덮어써짐)
# args: (4, 5, 6)
# kwargs: {'key1': 'value1', 'key2': 'value2'}
```

---

## 5. 재귀 함수 (Recursion)
함수가 자기 자신을 다시 호출하는 구조입니다.
* 무한 루프 방지를 위해 반드시 **종료 조건(Base case)**이 있어야 합니다.

```python
def factorial(n):
    # 종료 조건
    if n == 0:
        return 1
    # 재귀 호출
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120
```

---

## 6. 내장 함수 (Built-in Functions)
별도의 `import` 없이 파이썬에서 기본으로 제공하는 함수들입니다. (예: `len`, `max`, `min`, `sum`, `sorted` 등)

```python
numbers = [1, 2, 3, 4, 5]

print(len(numbers))                   # 5
print(max(numbers))                   # 5
print(min(numbers))                   # 1
print(sum(numbers))                   # 15
print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]
```

---

## 7. 스코프 (Scope) & LEGB Rule

### 1) 변수의 유효 범위
* **지역 스코프 (Local Scope)**: 함수 내부에서 생성된 변수는 함수 내부에서만 접근 가능합니다.

```python
def func():
    num = 20
    print('local', num)

func()
# print('global', num)  # NameError: name 'num' is not defined
```

* ⚠️ **주의**: 내장 함수 이름을 변수명으로 사용하면 기존 내장 함수가 덮어씌워져 오류가 발생할 수 있습니다.
```python
sum = 5
# sum(range(3))  # TypeError: 'int' object is not callable
```

### 2) LEGB Rule
파이썬이 변수 이름을 찾을 때 검색하는 우선순위 범위입니다:
1. **L (Local)**: 지역 범주 (함수 내부)
2. **E (Enclosing)**: 감싸는 함수 범주 (바깥쪽 함수)
3. **G (Global)**: 전역 범주 (모듈/파일 전체)
4. **B (Built-in)**: 파이썬 내장 범주

```python
x = 'G'
y = 'G'

def outer_func():
    x = 'E'
    y = 'E'

    def inner_func(y):
        z = 'L'
        print(x, y, z)  # E P L (x는 Enclosing, y는 Local 매개변수 'P', z는 Local)

    inner_func('P')
    print(x, y)  # E E

outer_func()
print(x, y)  # G G
```

---

## 8. global 키워드
함수 안에서 전역 변수(Global Variable)의 값을 변경하고자 할 때 사용합니다.

```python
num = 0

def increment():
    global num
    num += 1

increment()
print(num)  # 1
```

### ⚠️ 주의사항
1. **사용 전 참조 불가**: `global` 선언 전에 동일한 변수를 미리 참조하면 `SyntaxError`가 발생합니다.
2. **매개변수로 사용 불가**: 매개변수는 이미 지역 변수이므로 `global` 선언을 할 수 없습니다.
3. *실무에서는 가급적 `global` 사용을 지양하고, 인자로 전달받아 반환값(`return`)으로 재할당하는 패턴을 권장합니다.*

---

## 9. 함수 스타일 가이드 & 좋은 설계

### 1) 명확한 함수명
* **동사 + 대상** 형태로 역할이 잘 드러나도록 작성합니다.
* 예: `calculate_total_price(price, tax)` (Good) vs `calc_price(p, t)` (Bad)

### 2) 단일 책임 원칙 (Single Responsibility Principle)
하나의 함수는 오직 **하나의 일(책임)**만 수행해야 합니다.

```python
# ❌ 나쁜 설계: 한 함수에 여러 책임(검증, 저장, 메일 발송)이 섞임
def process_user_data(user_data):
    if len(user_data['password']) < 8:
        raise ValueError('비밀번호는 8자 이상이어야 합니다')
    user_data['password'] = hash_password(user_data['password'])
    db.users.insert(user_data)
    send_email(user_data['email'], '가입을 환영합니다!')

# 단일 책임으로 분리된 구조
def validate_password(password):
    if len(password) < 8:
        raise ValueError('비밀번호는 8자 이상이어야 합니다')

def save_user(user_data):
    user_data['password'] = hash_password(user_data['password'])
    db.users.insert(user_data)

def send_welcome_email(email):
    send_email(email, '가입을 환영합니다!')

# ⭕ 좋은 설계: 메인 함수는 순서와 목차만 관리
def process_user_data(user_data):
    validate_password(user_data['password'])
    save_user(user_data)
    send_welcome_email(user_data['email'])
```

---

## 10. 패킹과 언패킹 (Packing & Unpacking)

### 1) 패킹 (Packing)
여러 값을 하나의 튜플이나 딕셔너리로 묶는 과정입니다.

```python
# 기본 패킹 (소괄호 없이도 튜플 생성)
packed = 1, 2, 3, 4, 5  # (1, 2, 3, 4, 5)

# *를 통한 가변 위치 인자 패킹
def my_func(*args):
    print(args)  # (1, 2, 3, 4, 5)

# **를 통한 가변 키워드 인자 패킹
def my_func2(**kwargs):
    print(kwargs)  # {'a': 1, 'b': 2}
```

### 2) 언패킹 (Unpacking)
묶여 있는 컬렉션의 요소를 하나씩 풀어내는 과정입니다.

```python
# 기본 언패킹
a, b, c, d, e = (1, 2, 3, 4, 5)

# *를 사용한 인자 언패킹 (리스트/튜플)
def my_function(x, y, z):
    print(x, y, z)

names = ['alice', 'jane', 'peter']
my_function(*names)  # alice jane peter

# **를 사용한 인자 언패킹 (딕셔너리)
my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)  # 1 2 3
```

---

## 11. 람다 표현식 (Lambda Expression)
이름 없이 일회성으로 즉석에서 작성하는 한 줄짜리 익명 함수입니다.
* **문법**: `lambda 매개변수: 반환값`

```python
# 일반 함수
def addition(x, y):
    return x + y

# 람다 함수
addition_lambda = lambda x, y: x + y
```

### `sorted()`와 람다의 활용
`sorted()` 함수의 `key` 매개변수에 람다를 전달하면 고차원의 정렬 기준을 손쉽게 설정할 수 있습니다.

```python
students = [('지민', 25), ('서준', 20), ('민우', 30)]

# 나이(1번 인덱스)를 기준으로 정렬
result = sorted(students, key=lambda student: student[1])
print(result)  # [('서준', 20), ('지민', 25), ('민우', 30)]
```

---

## 12. 다중 반환값의 실체 (Return과 Tuple)
파이썬 함수는 표면적으로 여러 값을 반환하는 것처럼 보이지만, **실제로는 항상 단 하나의 값(튜플)**만 반환합니다.

```python
def get_user_info():
    name = 'Alice'
    age = 30
    return name, age  # 실제로는 (name, age) 튜플 1개를 반환

user_data = get_user_info()
print(user_data)  # ('Alice', 30)

# 언패킹을 통해 각각 받아 사용 가능
name, age = get_user_info()
print(name, age)  # Alice 30
```
