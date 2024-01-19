import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#데이터 불러오기
shop=pd.read_excel('C:/Users/user/Documents/bigdata/미니프로젝트-쇼핑몰 실습데이터.xlsx')
shop.head()

#얼마나 많이 지출했는지(M : 수량*판매금액=이익)
shop['업체별 지출']=shop['판매금액']*shop['주문수량']
company1=shop['업체별 지출'].groupby(shop['업체명']).sum()
company1
company2=company1.sort_values()

#상위 10개 선정
top_companies = company2.nlargest(10)
top_df=pd.DataFrame(top_companies)
top_df

#시각화-파이차트
plt.subplots(figsize=(10,5))
fig = px.pie(top_df, values=top_df['업체별 지출'], names='업체별 지출', title='업체별 지출')  
fig.show()

#지니 월별 매출분석
#매출, 주문시기 컬럼 지정
shop['매출']=shop['주문수량']*shop['판매금액']
shop['주문시기']=shop['주문일자'].dt.strftime('%Y-%m')
shop

#업체명 지니만 출력
shop_an1=shop.query("업체명 == '지니'")
shop_an1

#주문시기별 매출 합산
shop_aan=shop_an1.groupby(['주문시기'])['매출'].agg('sum').reset_index()
shop_aan

#그래프 그리기
fig = plt.figure(figsize=(10,10))                #캔버스 생성
fig.set_facecolor('white')                       #캔버스 색상 설정
ax = fig.add_subplot()                           #그림 뼈대(프레임) 생성 
plt.xticks(rotation=90)
ax.plot(shop_aan['주문시기'],shop_aan['매출'])

#데이터 값 표시
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='top',
                xytext=(0, 9),
                textcoords='offset points')
    
#1000단위로 컴마     
n = 20
data=np.random.normal(loc=0,size=n, scale=500000) + 1000000
current_values = plt.gca().get_yticks()
ax.set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.show()

#다우 월별 매출분석
shop_an2=shop.query("업체명 == '다우기술'")
shop_an2
shop_aan2=shop_an2.groupby(['주문시기'])['매출'].agg('sum').reset_index()
shop_aan2

#그래프 그리기
fig = plt.figure(figsize=(10,10))             
fig.set_facecolor('white')                   
ax = fig.add_subplot() 
plt.xticks(rotation=90)
ax.plot(shop_aan2['주문시기'],shop_aan2['매출'])

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='top',
                xytext=(0, 9),
                textcoords='offset points')
    

n = 20
data=np.random.normal(loc=0,size=n, scale=500000) + 1000000
current_values = plt.gca().get_yticks()
ax.set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.show()

# 쥬크박스 월별 매출분석
shop_an3=shop.query("업체명 == '쥬크박스'")
shop_an3
shop_aan3=shop_an3.groupby(['주문시기'])['매출'].agg('sum').reset_index()
shop_aan3

fig = plt.figure(figsize=(10,10)) ## 캔버스 생성
fig.set_facecolor('white') ## 캔버스 색상 설정
ax = fig.add_subplot() ## 그림 뼈대(프레임) 생성
plt.xticks(rotation=90)
ax.plot(shop_aan3['주문시기'],shop_aan3['매출'])

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='top',
                xytext=(0, 9),
                textcoords='offset points')
    
    
n = 20
data=np.random.normal(loc=0,size=n, scale=500000) + 1000000
current_values = plt.gca().get_yticks()
ax.set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.show()

# 상위 3개 기업 매출이 높은 상품명 10개 추출하기
# 지니 매출이 높은 상품명
shop_genie=shop.query("업체명 == '지니'")

#상품명 결측치 처리
shop['상품명'].fillna('기타', inplace=True)            
shop['상품명'].isna().sum()

#상품별 매출 합산
shop_pr1=shop_genie.groupby(['상품명'])['매출'].agg('sum').nlargest(10).reset_index()

#그래프 그리기
fig = plt.figure(figsize=(10,10)) ## 캔버스 생성
fig.set_facecolor('white') ## 캔버스 색상 설정
ax = fig.add_subplot() ## 그림 뼈대(프레임) 생성
plt.xticks(rotation=90)
ax.plot(shop_pr1['상품명'],shop_pr1['매출'])

for index, value in enumerate(shop_pr1['매출']):
    plt.text(index, value, f'{int(value):,}원', ha='center', va='bottom') 

n = 20
data=np.random.normal(loc=0,size=n, scale=500000) + 1000000
current_values = plt.gca().get_yticks()
ax.set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.show()


# 다우기술 매출이 높은 상품명
shop_dawoo=shop.query("업체명 == '다우기술'")

shop_pr2=shop_dawoo.groupby(['상품명'])['매출'].agg('sum').nlargest(10).reset_index()

#그래프 그리기
fig = plt.figure(figsize=(10,10)) ## 캔버스 생성
fig.set_facecolor('white') ## 캔버스 색상 설정
ax = fig.add_subplot() ## 그림 뼈대(프레임) 생성
plt.xticks(rotation=90)
ax.plot(shop_pr2['상품명'],shop_pr2['매출'])

for index, value in enumerate(shop_pr2['매출']):
    plt.text(index, value, f'{int(value):,}원', ha='center', va='bottom') 

n = 20
data=np.random.normal(loc=0,size=n, scale=500000) + 1000000
current_values = plt.gca().get_yticks()
ax.set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.show()

# 쥬크박스 매출이 높은 상품명
shop_juke=shop.query("업체명 == '쥬크박스'")

shop_pr3=shop_juke.groupby(['상품명'])['매출'].agg('sum').nlargest(10).reset_index()
shop_pr3

#그래프 그리기
fig = plt.figure(figsize=(10,10)) ## 캔버스 생성
fig.set_facecolor('white') ## 캔버스 색상 설정
ax = fig.add_subplot() ## 그림 뼈대(프레임) 생성
plt.xticks(rotation=90)
ax.plot(shop_pr3['상품명'],shop_pr3['매출'])

for index, value in enumerate(shop_pr3['매출']):
    plt.text(index, value, f'{int(value):,}원', ha='center', va='bottom') 

n = 20
data=np.random.normal(loc=0,size=n, scale=500000) + 1000000
current_values = plt.gca().get_yticks()
ax.set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.show()




















