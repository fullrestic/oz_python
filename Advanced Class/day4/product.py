import requests
from bs4 import BeautifulSoup

response = requests.get('https://web-scraping.dev/products')
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title.text)   # 웹 페이지 타이틀 출력
print()

first_div = soup.find('div', class_='product')
first_a = first_div.find('a')
print(f"첫번째 상품명 : {first_a.text}")

first_price = first_div.find('div', class_='price')
print(f"첫번째 상품의 가격 : {first_price.text}달러")

print()

# find는 일치하는 첫번째 요소만 가져옴
# find_all은 일치하느나 모든 요소 가져옴

all_div = soup.find_all('div', class_='product')

for i, div in enumerate(all_div, 1) :
    ith_a = div.find('a')
    print(f"{i}번째 상품명 : {ith_a.text}")

    ith_price = div.find('div', class_='price')
    print(f"{i}번째 상품의 가격 : {ith_price.text}달러")

    print()
