import pandas as pd
import matplotlib.pyplot as plt # 그래프 그리는 애
import matplotlib.font_manager as fm # 한글 폰트 깨짐 방지
import seaborn as sns # matplot이 만들어주는 리포트를 조금 더 예쁘게 만들어주는 테마

df = pd.read_csv(r'/Users/jh/Desktop/DAY38 - Flask, 수준별학습/수준별-심화 day5/shopping_data.csv')
# Data Frame (pandas가 다루는 자료구조)


"""
print(df.head())    # 앞에 있는 5개만 보여줌
print(df.tail())    # 뒤에 있는 5개만 보여줌
print(df.iloc[10:15])   # 10번째 줄에서 14번째 줄까지 보여줌

print(df.shape) # 행과 열의 갯수 => (35, 9)
print(df.columns)   # 열을 출력

print(df.info())    # 어떤 정보가 있는지 출력 

print(df['price'])  # 가격만 출력
print(df.describe())    # 통계 정보 - 숫자 타입만 분석

print(df.describe(include='object'))    # object(문자열) 관련 통계도 출력하게 옵션 줌
"""

# 가격 데이터 숫자로 변환
df['price'] = df['price'].str.replace(',', '')
df['price'] = df['price'].astype(int) # int, float, str, bool



# 날짜 데이터를 날짜형으로 변환하고 요일, 월 추출
df['date'] = pd.to_datetime(df['date'])
df['weekday'] = df['date'].dt.day_name() # 요일 추출
# print(df[['date', 'weekday']].head())
df['month'] = df['date'].dt.month # 월 추출




"""
import numpy as np
df.loc[5, 'rating'] = np.nan    # Not a Number
df.loc[10, 'price'] = np.nan

print(df.isnull().sum())    # 널값 체크


df_clean = df.dropna()  # 결측치 제거
print(f"원본 : {len(df)}행 -> 제거 후 : {len(df_clean)}행")

df['rating'].fillna(df['rating'].mean(), inplace=True)  # 빈값 평균값으로 채움
df['price'].fillna(0, inplace=True) # 빈값 0으로 채움
# inplace=True 원본 수정, False로 하면 새로 생성됨

df['price'] = df['price'].interpolate   # 앞뒤 값으로 추정


print(df.duplicated().sum())    # 중복값 체크
print(df.duplicated(subset=['name', 'brand']).sum())
"""



df_unique = df.drop_duplicates()    # 중복값 제거
df_unique = df.drop_duplicates(subset=['name', 'brand'], keep='first')  # 첫번째만 남기고 삭제

print((df['price'].describe() / 10000).round(1))

# 사분위수
Q1 = df['price'].quantile(0.25) # 하위 25% 1/4
Q3 = df['price'].quantile(0.75) # 상위 25% 3/4

IQR = Q3 - Q1 

lower_bound = max(0, Q1 - 1.5 * IQR) # 너무 싼 것의 경계
upper_bound = Q3 + 1.5 * IQR # 너무 비싼 것의 경계

print(f"정상 범위: {lower_bound:,.0f}원 ~ {upper_bound:,.0f}원")

# 이상치 뽑기
outliers = df[(df['price'] < lower_bound) | (df['price'] > upper_bound)]
print(f"이상치 {len(outliers)}개 발견!")




# 100만원 이상 & 평점 4.5 이상인 제품
expensive = df[(df['price'] > 1000000) & (df['rating'] >= 4.5)] # 각 조건을 ()로 묶어줘야 함
print(f"100만원 이상이고 평점이 4.5 이상인 제품 : {len(expensive)}개")
print(expensive[['name', 'price']])

# 애플 또는 삼성 제품
print(df[(df['brand'] == '삼성') | (df['brand'] == '애플')])

# 리스트 안에 있는 브랜드 제품들 -- isin
target_brands = ['삼성', 'LG', '애플']
selected = df[df['brand'].isin(target_brands)]

print(f"선택된 브랜드 제품들 : {len(selected)}")
print(selected)

galaxy = df[df['name'].str.contains('갤럭시')]
print(galaxy[['name', 'price']])

galaxy = df[df['name'].str.contains('갤럭시|galaxy', case=False)]





# 정렬
df_sorted = df.sort_values('price', ascending=True) # 오름차순
print(df_sorted[['name', 'price']].head()) 

df_sorted = df.sort_values('price', ascending=False)    # 내림차순
print(df_sorted[['name', 'price']].head()) 




# 그룹핑
grouped = df.groupby('brand')
brand_avg = df.groupby('brand')['price'].mean() / 10000 # 브랜드 별 평균 가격
# print(brand_avg)




# 피벗 테이블
pivot = pd.pivot_table(
    data=df,
    index='category',
    columns='brand',
    values='price',
    aggfunc='mean',
    fill_value=0
)

# print(pivot)





# 시각화 -- matplot
plt.rcParams['font.family'] = 'AppleGothic'   # 한글 폰트 설정
plt.rcParams['axes.unicode_minus'] = False      # 음수 기호 깨짐 방지

# 막대 그래프
# brand_avg = df.groupby('brand')['price'].mean().sort_values()
# plt.figure(figsize=(10, 6)) # 캔버스 생성
# plt.bar(brand_avg.index, brand_avg.values)  # 막대 그래프
# plt.title('브랜드 별 평균 가격')
# plt.xlabel('브랜드')
# plt.ylabel('평균 가격 (만원)')
# plt.show()


# 시계열 그래프
# daily_sales = df.groupby('date')['sales'].sum() # 날짜별 매출
# plt.figure(figsize=(12, 6))
# plt.plot(daily_sales.index, daily_sales.values, marker='o', markersize=8, linewidth=2)
# plt.title('일별 매출 추이')
# plt.xlabel('날짜')
# plt.ylabel('매출')
# plt.xticks(rotation=45)     # 글자가 겹쳐서 안보일 수 있으니 45도 기울임
# plt.grid(True, alpha=0.3)   # 격자 추가, alpha=투명화
# plt.tight_layout()          # 그래프 요소들이 다 잘 보이게 여백 자동 조정
# plt.show()                  # show() 이후에는 설정 바꿀 수 없음


# 산점도 -- 상관관계를 보여줌
# plt.figure(figsize=(10, 6))
# scatter = plt.scatter(df['price'], df['rating'], c=df['sales'], s=100, alpha=0.6, cmap='viridis')
# # 첫번째 인자 - x축, 두번째 인자 - y축
# # c - 색상 (판매량에 따라 색상 다르게 설정)
# # s - 사이즈
# # cmap - 컬러맵, 어떤 색으로 표현할지 (virdis:초록색)

# plt.colorbar(scatter, label='판매량')   # 막대 형태로 색상이 어떤 값을 의미하는지 보여줌
# plt.xlabel('가격')
# plt.ylabel('평점')
# plt.title('가격 vs 평점 (색상:판매량)')
# plt.show()


# 파이 차트
category_counts = df['category'].value_counts()

plt.figure(figsize=(8, 8))
colors = plt.cm.Set3(range(len(category_counts)))
plt.pie(category_counts.values,
        labels=category_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors)
plt.title('카테고리 별 상품 비율', fontsize=16)
plt.show()