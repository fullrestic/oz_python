# 변수 => 어떤 값을 담는 그릇, 상자, 컨테이너 같은 존재
# 파이썬 변수에 어떤 것도 담을 수 있음

# 왼쪽에는 변수의 이름, 오른쪽에는 변수에 담을 값, =로 연결

"""
- 특수 문자는 언더바 _만 허용
- 숫자로 시작하면 안됨
- 공백을 포함할 수 없음
- 가급적 알파벳을 사용
- 유의한 뜻으로 짓되 누구나 알 수 있어야 함
"""

# 키워드 불러오기와 목록 확인하기 
import keyword
print(keyword.kwlist)

# format을 사용해 {}안에 값 넣기 
# {}갯수만큼 ,로 구분해서 값을 연결해줘야함
print("우리는 {}기입니다.".format(13))
print("{} {}".format(12, "기"))
print("3 + 4 = {}".format(3+4))

# 변수 활용하기 
number_1=3
number_2=4
print("{} + {} = {}".format(number_1, number_2, number_1+number_2))

name = "주현"   #str => 문자열
age = 20    #정수, int, 숫자

# f-string 방식 사용하기
print(f"제 이름은 {name}이고 나이는 {age}살입니다.")

