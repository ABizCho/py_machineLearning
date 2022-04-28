'''
SubPlot
( MatPlot의 SubPlot 추가 조사, 정리, 실습 내용 ) 

    * SubPlot이란 : 두 개 이상의 plot을 서브플롯으로 레이아웃을 구성하여 한 화면에 담아내는 plt의 플롯팅 방법
        
        - plt.subplot() 메소드를 사용하여 서브플롯 레이아웃 초기화
        - plt.subplot( 1. 행 크기, 2. 열 크기 , 3. 다음 서브플롯 위치 지정 )
            
            - subplot 의 3번째 파라미터 index는 인덱싱 진행방향을 행 우선(->) 기준으로 잡는다.
                ( 2x2 Subplot Layout의 경우 
                index = 1: [0,0] =>
                index = 2: [0,1] => 
                index = 3: [1,0] => 
                index = 4: [1,1]   )
    
    plt.subplot()
    


    Ref :
        - 서브플롯 :   https://teddylee777.github.io/visualization/matplotlib-tutorial
'''
from stylemod import *

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


'''
1.
    plt.subplot(nrow_subplot, ncol_subplot, 다음 생성 플롯 인덱스 위치 지정 ) 메소드 사용법

'''
div(1)

# 2X1 로 서브플롯 레이아웃
sp()
plt.subplot() # 서브플롯 레이아웃 생성

data = np.arange(100, 201)
plt.subplot(2, 1, 1) # 2X1 의 서브플롯 레이아웃 중 첫번째 인덱스에 다음에 생성될 플롯 위치 지정
plt.plot(data)

data2 = np.arange(200,301)
plt.subplot(2, 1, 2) # 2X1 의 서브플롯 레이아웃 중 두번째 인덱스에 다음에 생성될 플롯 위치 지정
plt.plot(data2)

plt.show() 


# 1X2 로 서브플롯 레이아웃
sp()
plt.subplot()

carB1 = np.array(['M Series','Avante','Grandeur'])
carS1 = np.array([180,120,150])

carB2 = np.array(['Palisade', 'Veloster', 'Santafe'])
carS2 = np.array([150, 180, 130])

plt.subplot(2,1,1)
plt.bar(carB1,carS1)

plt.subplot(2,1,2)
plt.bar(carB2,carS2)

plt.show()

# 2X2로 서브플롯 레이아웃
sp()
plt.subplot()

carB1 = np.array(['M Series','Avante','Grandeur'])
carS1 = np.array([180,120,150])

carB2 = np.array(['Palisade', 'Veloster', 'Santafe'])
carS2 = np.array([150, 180, 130])

plt.subplot(2,2,3)  # index = 4 : [1,1] 에 위치
plt.bar(carB1,carS1)

plt.subplot(2,2,1)  # index = 1 : [0,0] 에 위치
plt.bar(carB2,carS2)

plt.show()

 
# 서브플롯 디테일 설정 : 

    #히스토그램 예제 : ref my assignment #2
    
'''

import matplotlib.pyplot as plt


plt.style.use('Solarize_Light2')

fig, ax = plt.subplots(2, 1)

n,bins,patches = ax[0].hist(df_sal['TotalPay'],edgecolor='black',linewidth=1.2 )
patches[1].set_facecolor('gold')

n,bins,patches = ax[1].hist(df_sal['TotalPay'],edgecolor='black',linewidth=1.2,bins=30 )
patches[0].set_facecolor('gold')
patches[3].set_facecolor('gold')

ax[0].set_title("Histogram of TotalPay (default)")
ax[1].set_title("Histogram of TotalPay (bins=30)")

plt.xlabel('TotalPay')
plt.ylabel('Count of records')

fig.set_size_inches(9, 9)
plt.show()


    # 서브플롯 : https://teddylee777.github.io/visualization/matplotlib-tutorial
    # 서브플롯 타이틀 : https://www.delftstack.com/ko/howto/matplotlib/how-to-add-title-to-subplots-in-matplotlib/
    
    # 히스토그램 특정 구간 강조 : https://velog.io/@khnn/TIL-Matplotlib%EC%9C%BC%EB%A1%9C-%ED%9E%88%EC%8A%A4%ED%86%A0%EA%B7%B8%EB%9E%A8-%EA%BE%B8%EB%AF%B8%EA%B8%B0

'''


    #라인차트 예제 : ref my assignment #2
'''
TP_year = df_sal.groupby('Year').mean().index.values
TP_avg = df_sal.groupby('Year').mean()['TotalPay'].values

xpoints = TP_year
ypoints = TP_avg


fig = plt.figure(figsize=(7,7)) # canvas
ax = fig.add_subplot()          # frame

ax.spines['right'].set_visible(False) # unvisible right spine
ax.spines['top'].set_visible(False) # # unvisible top spine

ax.plot(xpoints,ypoints, 'g', marker='o',linestyle='--')

ax.axhline( TP_avg.mean(), label='mean')
ax.text(2011,TP_avg.mean()+20, 'Mean : %f'%(TP_avg.mean()),fontsize=9,color='gray')

plt.title('Avgs of TotalPay by years')

plt.xticks(TP_year)
plt.yticks(TP_avg)

plt.xlabel('Years')
plt.ylabel('Averages of whole TotalPay')
plt.show()


    # linear graph styling(goodRef): https://zephyrus1111.tistory.com/21
'''


    # bar chart 예제-1 : ref my assignment#3
'''
fig, ax = plt.subplots(2, 1)

# WAY 1.
    # pd.cut() method by default options
df_sal['pay_class'] = pd.cut(df_sal['TotalPay'],3, labels=['low','medium','high'])

df_sal_class = df_sal.groupby('pay_class')['pay_class'].count()

ax[0].bar(df_sal_class.index.values,df_sal_class.values)
ax[0].set_title('Way 1 : Dividing classes by default cut() options')


# WAY 2.
    # Dividing 3 class in the same range of value ( Using cut() method too) 

endP = int(df_sal['TotalPay'].max())
startP = int(df_sal['TotalPay'].min())


intv = int((endP - startP) / 3)

bins = range(startP,endP,intv)
bins_label = ['low','medium','high']

df_sal['pay_class'] = pd.cut( df_sal['TotalPay'], bins,right=False, labels=bins_label )

ax[1].bar(df_sal_class.index.values,df_sal_class.values)
ax[1].set_title('Way 2 : Dividing classes by the same range of value')



plt.xlabel('TotalPay Class')
plt.ylabel('Count of obs')

print('Showing Counts of classes of Total pay bar chart...')

fig.set_size_inches(9, 9)
plt.show()
'''


    # bar chart 예제 - 2 : ref my assignment #2
'''
# Additional : Top10 the most paid jobtitles
div(17,'Additional Analysis 2 : Top10 the most paid jobtitles ')
import numpy as np
top10_paidJts = df_sal.groupby('JobTitle').mean()['TotalPayBenefits'].sort_values(ascending=False)[0:10].astype(int)
print(top10_paidJts)

sp()

fig, ax = plt.subplots(figsize=(8,8))

ax.bar(top10_paidJts.index.str.lower(),top10_paidJts.values,
       color = 'red',alpha=0.5)
plt.title('Additional Analysis 2 : Top10 the most paid jobtitles')

plt.subplots_adjust(bottom=0.5)
plt.xticks(rotation=75)
print('Showing Top10 the most paid jobtitles...')
plt.show()
'''
