'''
ML6 
seaborn Visualization library

'''
#%%

from stylemod import *
import numpy as np 

import matplotlib.pyplot as plt
import seaborn as sns


'''
1. displot()

    method for distribution plot
''' 

sns.displot([0,1,2,3,4,5])
plt.show()

'''
2. 
Seaborn makes plots more pretty

    ref : numpy - linspace :  https://numpy.org/doc/stable/reference/generated/numpy.linspace.html

'''
x = np.linspace(0, 10, 1000)
y = np.power(x ,2)
plt.plot(x,y)


plt.show()


'''
3.
Linear Regression in python
scipy - stats Library

    # ref : scipy - stats : https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
'''

# 1. prepare - scatters
import matplotlib.pyplot as plt

    
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x,y)
plt.show()

# 2. scipy for visulize linear regression

from scipy import stats

    # 2.1 x axis와 y axis를 대표하는 두 array를 생성 
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    # 2.2 선형회귀의 인자 를 반환하는 stats.linregress() 에
        #  앞서 생성한 x,y array를 두 인자로 넣어 메소드 실행
slope, intercept, r, p, std_err = stats.linregress(x, y)

    # 2.3 선형회귀 함수 정의 
        # x배열을 인자로 받아, 기울기*x + 절편 을 반환 하도록
def myfunc(x) :
    return slope * x + intercept

    # 2.4 x array 내 각 값을, 사용자 정의 선형회귀함수의 인자로 넣는 map(myfunc,x)
        # 를 실행해 각 array의 길이만큼 실행되어 반환 되는 각 y 추정값 (결과값) 을 mymodel에 리스트로 저장
mymodel = list(map(myfunc, x)) # 선형 회귀모델 결과값인 y 추정값을  저장

    
    # 2.5 x-axis,y-axis arrays를 인자로 scatter plot 생성
plt.scatter(x, y)

    # 2.6 x values와 estimated y values 로 선형회귀선 생성
plt.plot(x, mymodel)

plt.show()


'''
4. Polynomial Regression
    다중 선형회귀
        : 종속변수(y)는 하나이고,
          독립변수(x : 실험변수)가 다수인 선형회귀 분석법
          
    ref : 
        np.polyfit() : https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html
          
'''

import matplotlib.pyplot as plt

# 0 Data prepare : 예를들어, 톨게이트를 지나가는 18개의 자동차가 있다고 하자.

    # 톨게이트를 지나친 하루 중의 시각
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
    # 톨게이트를 지나는 차량 속도
y = [100,90,80,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

plt.scatter(x,y)
plt.show()


# 1. Polynomial Regression
mymodel = np.ply1d(np.plyfit(x, y, 3))

myline = np.linspace(1, 22 ,100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()


# %%