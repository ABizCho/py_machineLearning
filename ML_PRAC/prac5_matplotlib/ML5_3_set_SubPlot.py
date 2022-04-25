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


