import requests

response = requests.get("https://api.github.com")   #https 통신 완료

# 메타 데이터
print(f"상태 코드 : {response.status_code}")
print(f"응답 헤더 : {response.headers}")
print(f"인코딩 : {response.encoding}")
print(f"응답 시간 : {response.elapsed}")

# 본문
print(response.text)
print(response.content)
print(response.json())

