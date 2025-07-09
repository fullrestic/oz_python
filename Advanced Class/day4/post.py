# httpbin.org : HTTP 요청을 테스트할 수 있는 사이트

import requests

# 폼 데이터 작성
form_data = {
    'username' : 'testuser',
    'email' : 'test@example.com',
    'age' : 30
}

response = requests.post('https://httpbin.org/post', data=form_data)    # post에서는 url과 함께 데이터 전달
print(response.json())

#JSON 전송
# 폼 데이터보다 Json 데이터를 보내는 게 일반적
json_data = {
    'name' : 'Kim',
    'age' : 25,
    'hobbies' : ['gaming', 'playing', 'reading'],
    'address' : {
        'city' : 'Seoul',
        'country' : 'South Korea'
    }
}

response = requests.post('https://httpbin.org/post', json=json_data)
print(response.json())