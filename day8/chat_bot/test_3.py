# n = len('hello')

# if n > 3 :
#     print(f'문자열 길이 : {n}')

# 바다코끼리 연산자 사용 예시
if ( n := len('hello')) > 3 :
    print(f'문자열 길이 : {n}')

# while문에 사용하면 편함
while (text := input('>>> ')) != 'exit' : 
    print('당신이 입력한 값 : ', text)