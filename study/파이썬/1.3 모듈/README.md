# 🐍 Python Module (모듈)

파이썬의 **모듈(Module)** 과 **패키지(Package)** 사용법을 정리한 학습 노트입니다.

---

# 📚 목차

1. 모듈(Module)이란?
2. import 문
3. from 절
4. as 키워드
5. 사용자 정의 모듈
6. Package
7. 외부 패키지(requests)
8. import 방식 비교
9. 자주 발생하는 오류
10. SSAFY TIP
11. 핵심 정리

---

# 1. 모듈(Module)이란?

모듈(Module)은 **함수, 변수, 클래스 등을 하나의 파일(.py)에 모아놓은 것**입니다.

예를 들어

```python
math.py
```

안에는

- sqrt()
- pi
- sin()
- cos()

등이 들어 있습니다.

---

## 사용하는 이유

- 코드 재사용
- 유지보수 편리
- 기능별 파일 분리

---

# 2. import 문

가장 기본적인 모듈 사용 방법입니다.

```python
import math

print(math.pi)
print(math.sqrt(4))
```

출력

```
3.141592...
2.0
```

### 특징

- 모듈 전체를 가져옴
- 반드시

```python
모듈명.이름
```

으로 접근

예시

```python
math.sqrt(16)
```

---

## 장점

- 출처가 명확하다.
- 이름 충돌이 적다.

---

# 3. from 절

필요한 기능만 가져오는 방법입니다.

```python
from math import pi, sqrt

print(pi)
print(sqrt(4))
```

### 특징

모듈명을 생략할 수 있습니다.

```
math.sqrt()
```

↓

```
sqrt()
```

---

## 장점

코드가 짧아집니다.

---

## 단점

출처를 알기 어렵습니다.

이름이 겹치면 충돌이 발생할 수 있습니다.

---

### 실무 예

```python
from datetime import datetime

print(datetime.now())
```

---

# 4. as 키워드 (별칭)

이름이 길거나 충돌이 발생할 때 사용합니다.

```python
from math import sqrt

from my_math import sqrt as my_sqrt
```

사용

```python
sqrt(16)

my_sqrt(16)
```

---

## 실무에서 많이 사용하는 예

```python
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt
```

---

# 5. 사용자 정의 모듈

직접 만든 파이썬 파일도 모듈입니다.

### my_math.py

```python
def add(x, y):
    return x + y

def sqrt(x):
    return x ** 0.5
```

사용

```python
import my_math

print(my_math.add(1,2))
```

---

# 6. Package

패키지는

> 여러 개의 모듈을 모아놓은 폴더입니다.

예시

```
my_package
│
├── math
│      └── my_math.py
│
└── statistics
       └── tools.py
```

사용

```python
from my_package.math import my_math
from my_package.statistics import tools

print(my_math.add(1,2))
print(tools.mod(5,2))
```

---

# Package 구조

```
Package

↓

Module

↓

Function
```

---

# 7. 외부 패키지

대표적인 예

```
requests
```

설치

```bash
pip install requests
```

사용

```python
import requests

response = requests.get("https://www.google.com")

print(response.status_code)
```

---

## 설치하지 않으면

```
ModuleNotFoundError
```

가 발생합니다.

---

# pip

패키지를 설치하는 명령어

```
pip install 패키지명
```

예시

```
pip install requests
```

```
pip install numpy
```

```
pip install pandas
```

---

# 8. import 방식 비교

## import

```python
import math

math.sqrt(4)
```

장점

- 출처 명확

단점

- 코드가 길다.

---

## from

```python
from math import sqrt

sqrt(4)
```

장점

- 코드가 짧다.

단점

- 이름 충돌 가능

---

## as

```python
import pandas as pd
```

장점

- 이름 단축

- 충돌 방지

---

# import 우선순위

가장 많이 사용하는 순서

```
import

↓

from

↓

as
```

---

# 9. 자주 발생하는 오류

## ModuleNotFoundError

```python
import requests
```

설치 안 되어 있으면

```
ModuleNotFoundError
```

---

## ImportError

존재하지 않는 함수

```python
from math import hello
```

↓

```
ImportError
```

---

## 이름 충돌

```python
from math import sqrt

from my_math import sqrt
```

둘 다

```
sqrt()
```

가 되어 충돌합니다.

↓

```python
from my_math import sqrt as my_sqrt
```

사용

---

# SSAFY TIP ⭐

## 1.

모듈 =

```
하나의 .py 파일
```

---

## 2.

패키지 =

```
모듈들의 집합
```

---

## 3.

실무에서는

```python
import pandas as pd
```

처럼 as를 매우 많이 사용합니다.

---

## 4.

`from`은 편하지만

출처가 사라집니다.

---

## 5.

패키지는 설치해야 사용할 수 있습니다.

```
pip install 패키지명
```

---

# 핵심 비교

| 구분 | 설명 |
|------|------|
| Module | 하나의 Python 파일 |
| Package | 여러 Module의 집합 |
| import | 모듈 전체 가져오기 |
| from | 필요한 것만 가져오기 |
| as | 별칭 사용 |
| pip | 외부 패키지 설치 |

---

# 핵심 문법

```python
import math

math.sqrt(4)
```

```python
from math import sqrt

sqrt(4)
```

```python
from math import sqrt as s

s(4)
```

```python
import requests
```

```bash
pip install requests
```

---

# ✅ 한 줄 요약

- **Module** → 하나의 `.py` 파일
- **Package** → 여러 Module을 모아놓은 폴더
- **import** → 모듈 전체 사용
- **from** → 필요한 기능만 가져오기
- **as** → 별칭 사용
- **pip** → 외부 패키지 설치