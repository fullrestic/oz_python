import requests

# 방법 1 - URL에 직접 붙이기
# 권장되는 방식 아님
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
response = requests.get(url)


# 방법 2 - 파라미터 변수를 만들어서 같이 전달
# 권장되는 방식
params = {
    "q" : 'python',
    'sort' : 'stars'
}

url = 'https://api.github.com/search/repositories'
response = requests.get(url, params=params)

print(response.json())