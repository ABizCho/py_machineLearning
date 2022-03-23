'''
ML4_1 

판다스(Pandas) 
    
    : 빅데이터 분석과 통계에 근거한 결론도출에 사용 :: Dataframe에 관련한 라이브러리임 : data sets를 작업할 때 사용 ,
      Analyzing, cleaning, exploring, manipulating 함수들을 제공
     
     * Descriptive statistics : Helpful in describing the data
        - Allows users to analyze big data and make conclusions based on statistical theories
     
     * Data cleaning : Useful in cleaning data
        - Enable to clean messy data sets and make them readable and relevant
            - Relevant data is critical for successful data science
     
     
'''
import pandas as pd
from stylemod import *

'''
(1) pd.Dataframe()

    데이터프레임 : 다차원 테이블 : Data sets를 다루기 위한 판다스의 자료구조 

            - 시리즈가 한 1열의 자료구조라면, 데이터프레임은 이들의 총 집합체이다.
            - 시리즈(열을 기준으로) 의 합으로 데이터프레임을 구성할 수 있다.
''' 
div(1)

mydataset = {
    'cars' : ['BMW','Volvo','Ford'],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)


'''
(2) pd.Series()

    시리즈 : 데이터프레임의 하위 구성단위
            하나의 속성(att)이자 열을 담당한다.
'''
div(2)

S = [1,7,2]
myvar = pd.Series(S)
print(myvar)

# 인덱싱
sp()
print(myvar[0])

# 시리즈 생성시 인덱스 명명 
sp()
myvar_labeled = pd.Series(S, index=['x','y','z'])
print(myvar_labeled)

# 딕셔너리 to pd.Series
sp()
calories = {'day1': 420,
            'day2': 380,
            'day3': 390}

series_calories = pd.Series(calories) 
print(series_calories,
      type(series_calories) )


# Series to Dataframe
    # 하나의 시리즈는 데이터프레임 한 열( attribute : 속성 )을 담당하여 구조화된다.
sp()
data = {
    'calories': [420,380,390],
    'duration': [50,40,45]
}

df = pd.DataFrame(data)
print(df)

# 데이터프레임 인덱싱
    # df.loc[ 인덱스 ] 
sp()
print(df.loc[0])

sp()
    # 인덱스 리스트를 사용
print( df.loc[[0, 1]]) # 두개 이상 행의 인덱싱엔 리스트를 사용할 수 있음


sp()
print( df.loc[range(len(df))] )

