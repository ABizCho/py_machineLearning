'''
ML2_4

Numpy - 기초 통계 함수들

    axis(축) : 배열의 통계 함수는 요소별로 동작하며, 축(axis) 지정으로 '연산의 방향'을 지정할 수 있다.
    
        - axis를 디폴트로 할 경우, 모든 요소에 대한 단일 통계 결과를 반환한다.
        
            * axis = 0 : 행(row) 들 사이의 연산 결과를 반환한다.
            * axis = 1 : 열(column) 들 사이의 연산 결과를 반환한다.

'''
import numpy as np
from stylemod import *


'''
1. sum()
'''
div(1)
arr = np.arange(1, 13).reshape(3,4)
print(arr)

sp()
print( arr.sum() ) # 모든 items를 대상으로 단일 합계
print( arr.sum(axis=0) ) # 행들 간의 연산 수행 : 행 length의 스칼라 결과값 반환
print( arr.sum(axis=1))  # 열들 간의 연산 수행 : 열 length의 스칼라 결과값 반환

'''
2. mean()
'''
div(2)

arr = np.arange(1,13).reshape(3,4)
print(arr)

sp()
print( arr.mean() )         # 모든 items 사이의 평균연산 수행 : 단일 평균 반환
print( arr.mean(axis=0) )   # 행값들 사이의 평균연산 수행 : 행길이의 스칼라 결과값 반환
print( arr.mean(axis=1) )   # 열값들 사이의 평균연산 수행 : 열길이의 스칼라 결과값 반환


'''
3. min() , max()    : 최소값 최대값

        + np.random.permutation()
            - np.random.permutation(n) : n까지의 숫자를 가진 무작위순서의 배열을 만든다.
            - np.random.permutation(arr) : arr의 기존 shape를 유지한 채 items 순서를 무작위로 변경한 배열을 반환
'''
div(3)

# 표본 배열 생성

arr = np.arange(1,13).reshape(3,4)
print(arr)

# min 수행
sp()
print( arr.min() )
print( arr.min(axis = 0) ) 
print( arr.min(axis = 1) )

# max 수행
sp()
print( arr.max() )
print( arr.max(axis = 0) )
print( arr.max(axis = 1) )


'''
4. 표준편차, 분산
    : 데이터가 평균으로부터 얼마나 퍼져있는지(분포)의 정도를 나타내는 지표

    표준편차 : std()
    분산 : var()   
    
'''
div(4)


# 샘플 배열 생성
arr = np.arange(1,13).reshape(3,4)
print(arr)

# std() 표준편차 수행 
sp()
print( arr.std() )
print( arr.std(axis = 0) )
print( arr.std(axis = 1) )

# var() 분산 수행
sp()
print( arr.var() )
print( arr.var(axis = 0) )
print( arr.var(axis = 1) )
