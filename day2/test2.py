import requests

# f 스트링을 이용해서 이강인이라는 값이 들어간 변수를 활용하기
# 문자열 +, * ->
# keyword + url 
# 누가 미리 만들어 놓은 기능 -> 내장함수 => input()을 사용해 키워드 입력받기
# input 값을 입력받으면 무조건 데이터 타입은 문자형

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
keyword = input("키워드를 입력해주세요 : ")

search = url + keyword

req = requests.get(search)
print(req.text)
