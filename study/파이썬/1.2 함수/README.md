# 📘 05. Functions (함수)

> SSAFY Python 과정 - Functions 학습 내용 정리

---

# 📚 학습 목표

- 함수를 정의하고 호출할 수 있다.
- 매개변수(Parameter)와 인자(Argument)의 차이를 이해한다.
- 다양한 Argument 전달 방식을 사용할 수 있다.
- 재귀 함수의 원리를 이해한다.
- Python 내장 함수를 활용할 수 있다.
- Scope와 global 키워드를 이해한다.
- Packing / Unpacking을 활용할 수 있다.
- Lambda Expression을 사용할 수 있다.

---

# 📂 파일 구성

| 파일 | 학습 내용 |
|------|-----------|
|01_basic.py|함수 정의 및 호출, Docstring, return|
|02_parameter_argument.py|Parameter와 Argument|
|03_arguments.py|위치 인자, 기본값 인자, 키워드 인자 등|
|04_recursion.py|재귀 함수|
|05_built_in_function.py|Python 내장 함수|
|06_scope.py|지역변수(Local)와 전역변수(Global)|
|07_global.py|global 키워드|
|08_function_style_guide.py|함수 작성 스타일 가이드|
|09_packing.py|Packing|
|10_unpacking.py|Unpacking|
|99_lambda_expressions.py|Lambda Expression|
|99_return.py|return 심화|

---

# 1️⃣ 함수(Function)

함수(Function)는 특정 기능을 수행하는 코드의 묶음이다.

같은 코드를 여러 번 작성하지 않아도 되며 재사용성을 높여준다.

```python
def hello():
    print("Hello SSAFY!")

hello()
```

---

# 2️⃣ Parameter와 Argument

```python
def add(x, y):
    return x + y

add(3, 5)
```

- **Parameter**
  - 함수를 정의할 때 사용하는 변수

- **Argument**
  - 함수를 호출할 때 전달하는 실제 값

---

# 3️⃣ 다양한 Argument

본 예제에서는 다음 내용을 학습한다.

- Positional Argument
- Default Argument
- Keyword Argument

⚠️ 일부 예제는 의도적으로 `SyntaxError`와 `TypeError`를 발생시키므로
주석을 해제하며 하나씩 실행하는 것이 좋다.

---

# 4️⃣ Return

```python
def square(x):
    return x*x
```

return의 역할

- 함수 종료
- 값 반환

또한 여러 값을 반환하는 것처럼 보여도 실제로는 **Tuple 하나를 반환**한다.

```python
return name, age
```

---

# 5️⃣ Recursion (재귀 함수)

함수가 자기 자신을 다시 호출하는 방식이다.

예제에서는 factorial을 이용하여 재귀 호출 과정을 설명한다.

```text
factorial(5)

↓

factorial(4)

↓

factorial(3)

↓

...

↓

종료 조건(Base Case)
```

재귀 함수에서는 **종료 조건(Base Case)** 이 반드시 존재해야 한다.

---

# 6️⃣ Built-in Function

Python에서 자주 사용하는 내장 함수

- print()
- len()
- max()
- min()
- sum()
- sorted()
- range()
- type()

특히

```python
sorted(list)
```

는 원본을 변경하지 않고 새로운 리스트를 반환한다.

---

# 7️⃣ Scope

변수가 사용할 수 있는 범위를 의미한다.

- Local Scope
- Global Scope

```python
x = 10

def func():
    x = 20
```

함수 내부의 x와 외부의 x는 서로 다른 변수이다.

---

# 8️⃣ global

global 키워드를 이용하면 함수 내부에서도 전역변수를 수정할 수 있다.

```python
count = 0

def increase():
    global count
    count += 1
```

실무에서는 global 사용을 최소화하는 것이 좋다.

---

# 9️⃣ Function Style Guide

좋은 함수의 조건

- 함수명은 동사 사용
- 하나의 기능만 수행
- 함수 길이는 짧게
- 의미 있는 변수명 사용
- Docstring 작성

---

# 🔟 Packing

여러 개의 값을 하나로 묶는 과정

```python
numbers = 1,2,3
```

자동으로 Tuple이 생성된다.

---

# 1️⃣1️⃣ Unpacking

묶여있는 값을 다시 분리한다.

```python
a,b,c = (1,2,3)
```

또는

```python
first, *middle, last = numbers
```

처럼 사용할 수 있다.

---

# 1️⃣2️⃣ Lambda Expression

람다는 이름이 없는 한 줄 함수이다.

```python
square = lambda x: x*x
```

주로

- sorted()
- map()
- filter()

와 함께 많이 사용된다.

---

# ⭐ 핵심 정리

- 함수는 코드의 재사용성을 높인다.
- Parameter와 Argument를 구분한다.
- return은 값을 반환하고 함수를 종료한다.
- 재귀 함수에는 종료 조건이 반드시 필요하다.
- Scope를 이해해야 변수 충돌을 막을 수 있다.
- global은 필요한 경우에만 사용한다.
- Packing과 Unpacking은 Tuple과 함께 자주 사용된다.
- Lambda는 간단한 함수를 표현할 때 사용한다.

---

# ⚠️ 실습 시 주의사항

일부 예제는 **의도적으로 오류를 발생시키도록 작성**되어 있다.

예를 들어

- SyntaxError
- TypeError
- NameError

등을 직접 확인하며 학습할 수 있도록 구성되어 있으므로,
필요한 부분만 주석 처리하며 실행하는 것을 권장한다.

---

# 📝 복습 체크리스트

- [ ] 함수를 직접 정의할 수 있다.
- [ ] Parameter와 Argument를 설명할 수 있다.
- [ ] return의 역할을 설명할 수 있다.
- [ ] 재귀 함수의 종료 조건을 설명할 수 있다.
- [ ] Scope를 설명할 수 있다.
- [ ] global 사용 이유를 설명할 수 있다.
- [ ] Packing과 Unpacking을 사용할 수 있다.
- [ ] Lambda Expression을 사용할 수 있다.

---

> 💡 **한 줄 정리**
>
> 함수는 Python에서 가장 중요한 재사용 도구이며, Parameter, Return, Scope를 정확히 이해하는 것이 핵심이다.