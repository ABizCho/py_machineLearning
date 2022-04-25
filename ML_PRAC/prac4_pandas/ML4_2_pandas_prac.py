'''
ML4_3 

 csv 예제자료를 사용한 pandas 실습
'''
import os
import pandas as pd
from stylemod import *


'''
1. 디렉토리 접근/조작 : using os
  https://linuxize.com/post/python-get-change-current-working-directory/
'''
div(1)

# 디렉토리 경로 출력
csw = os.getcwd() 
print('current Working Directory: ',csw)


# 디렉토리 변경 및 출력
sp()
os.chdir('C:\\Users\\he125\\OneDrive\\바탕 화면\\Dev\\Git\\py_machineLearning\\ML_PRAC\\prac4')
csw = os.getcwd() 
print('currect Dir : ',csw)


'''
2. 데이터 조작 및 처리 : using pandas
'''
div(2)
df = pd.read_csv('data.csv')
print( df, type(df) ) #위5/아래5로 요약되어서 출력됨


# dataframe의 요약출력을 전체출력으로 변경하기
sp()
print( pd.options.display.max_rows ) # pd의 MAX 출력속성값 확인 : default값은 60

print(df) # 전체 출력

sp()
print(df.info)

'''
3. 시각화 : Basic Visualization 
    
    ( using matplotlib.pyplot )
'''
div(3)
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# 선형 그래프
sp()
print('시각화1 : 선형그래프 출력')

df.plot()
plt.show() # 저장된 그래프 출력

# Scatter plot : 산점도
sp()
print('시각화2 : 산점도 출력')
df.plot( kind = 'scatter', x= 'Duration', y= 'Calories' ) # x축을 Duraion 속성으로, y축을 Calories로 하는 산점도를 그린다.
plt.show() # 저장된 그래프 출력