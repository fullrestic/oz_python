# 문자열은 [이뮤터블] - 변경 불가능 / [뮤터블] - 변경 가능
# 문자열은 이뮤터블(변경이 불가능)
# +=, -=, *= 복합 할당 연산자
"""
x = "Answer : "
x += 'Yes'

print(x)
"""

# 문자열은 이뮤터블이라 문자열에 연산을 적용하면 매번 새로운 주소를 만듦
# +를 쓰는 것보다 +=를 쓰는게 좋은 이유...
"""
x = ''

for i in range(100000):
    x += '*/*-*'

print(x)
"""

# 또는 *를 사용해서 빠르게 만들 수 있음
# 아래처럼 만들면 '*/*-*' 부분을 새로 만들지 않고 같은 곳을 계속 참조하기 때문에 더 빠르고 효율적
"""
x = '*/*-*' * 100000
print(x)
"""



# 문자열은 이뮤터블 하면서 시퀀스 성격을 띄고 있음
# 시퀀스 : 순서가 있는 자료형에세 부여되는 성격이고 시퀀스 성격을 갖게 되면 인덱스를 가짐
# 이뮤터블이기 때문에 아래와 같은 대입 행위는 오류가 뜸
"""
x = 'hello.txt'
x[5] = '-'
"""

# 리스트는 뮤터블이기 때문에 대입 가능
"""
x_list = [1, 2, 3, 4, 5, 6]
x_list[5] = '안녕'
"""



# 슬라이싱
# x[시작 인덱스 : 종료 인덱스]
# 출력을 원하는 마지막 값의 + 1
"""
x = 'hello.txt'
print(x[-3:])
"""

# 스트라이드(보폭)
# x[시작 인덱스 : 종료 인덱스 : 스트라이드(보폭)]
"""
x = '-H-E-L-L-O-'
print(x[1::2])
print(x[::-1])  # 보폭에 -1을 넣으면 거꾸로 출력
print(x[::-2])
print(x[-2::-2])
"""

# 단어를 거꾸로 했을때 동일한 언어를 찾는 로직
"""
y = input('거꾸로 해도 동일한 단어인지를 확인하는 서비스입니다. 단어를 입력해주세요. ')
print(y == y[::-1]) 
"""



# 내장 메서드
# 함수 -> 함수명()
# 메서드 -> 변수.메서드명()
"""
x = 'Python'
print(x.upper())
print(x.lower())
print(x.startswith("Py")) # 지정한 값으로 시작하는지 확인, 대소문자 구별
print(x.endswith("on")) # 지정한 값으로 끝나는지 확인, 대소문자 구별

print(x.lower().startswith("py"))   # 여러 메서드 같이 쓸 수 있음

y = 'hello.py'
print(y.lower().endswith(".py"))    # 확장자 확인
"""

# replace 
"""
file = 'hello.py'
print(file.replace('py', 'txt'))

x = 'ababacvada'
print(x.replace('a','A'))
print(x.replace('a','A',1)) # 첫번째만 바꿈
print(x.replace('a','A',3)) # 세번쨰까지 바꿈 
"""

# count
"""
x = 'banana'
print(x.count('a'))
print(x.count('na'))
"""

name = 'Guido van Rossum'
print(name[:5])
print(name.find(' '))   # 가장 처음으로 나오는 위치만 반환, 이후는 무시
print(name[:name.find(' ')])
print(name.find('*'))   # 값이 없으면 -1이 출력됨
if name.find('*') == -1 :
    print("입력한 값중에 '*'를 찾을 수 없습니다.")
    # 이런 식으로 활용 가능