import requests
import csv
import json

import requests

url = 'http://apis.data.go.kr/6430000/goodRestaService1/getGoodResta1'
params ={'serviceKey' : '#',
         'currentPage' : 1,
         'perPage' : 100}

response = requests.get(url, params=params)
data = response.json().get('body', [])

filtered_data = []
for item in data:
    filtered_item = {
        "업소명": item.get("BSSH_NM", ""),  
        "시군명": item.get("SIGUN_NM", ""), 
        "상세주소": item.get("DETAIL_ADRES", ""),
        "전화번호": item.get("TELNO", ""),       
        "주요메뉴": item.get("RM", "")           
    }
    filtered_data.append(filtered_item)

# JSON 저장
with open("/Users/jh/Desktop/DAY38 - Flask, 수준별학습/수준별-심화 day5/filtered_restaurants.json", "w", encoding="utf-8") as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=2)

# CSV 저장
with open("/Users/jh/Desktop/DAY38 - Flask, 수준별학습/수준별-심화 day5/filtered_restaurants.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ['업소명', '시군명', '상세주소', '전화번호', '주요메뉴']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(filtered_data)