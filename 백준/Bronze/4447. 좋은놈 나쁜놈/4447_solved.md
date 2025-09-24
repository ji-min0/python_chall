# 문제 제목: [Bronze II] 좋은놈 나쁜놈 - 4447

## 문제 정보
- **출처:**  백준
- **난이도:** Easy

## 문제 설명
입력값에 b, g의 갯수에 따라 b가 많으면 좋은놈, g가 많으면 나쁜놈, 갯수가 같으면 중립이다.
GOOD, BADDY, NEUTRAL 중 하나.

출력 양식은 이름 is GOOD/BADDY/NEUTRAL .



## 해결 과정
일단 대.소문자를 따로 검증하기 보다는 한 번에 하기 위해서 lower로 맞춰준다.
그런 후 g 개수, b 개수를 count해주고 갯수별로 GOOD/BADDY/NEUTRAL 중 하나를  반환하게 한다.

이때, 출력 양식을 지킨다.


-> 출력할 때는 lower로 바꿔준 단어를 출력해서는 안된다!! 따라서 입력받은 단어와 lower로 변환한 단어는 따로 분리해준다.

## 코드
```python
n = int(input())

def check_good_or_bad():
    for _ in range(n):
        name = input()
        lower_name = name.lower()
        g_count = lower_name.count('g')
        b_count = lower_name.count('b')
    
        if g_count > b_count:
            print(f"{name} is GOOD")
        
        elif b_count > g_count:
            print(f"{name} is A BADDY")
        
        else:
            print (f"{name} is NEUTRAL")
    
check_good_or_bad()
```
