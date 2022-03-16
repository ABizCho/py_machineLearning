
from stylemod import *

'''
 Numpy 
    
    넘파이는 파이썬이 계산과학 분야에 이용될 때 핵심 역할을 하는 라이브러리이다. ( 선형대수, 포리에 변형, 매트릭스 등 ) 
    Numpy는 고성능의 다차원 배열 객체(array)와 이를 다룰 도구를 제공한다. : http://aikorea.org/cs231n/python-numpy-tutorial/#numpy-arrays
    
    - why use? :  1.파이썬은 배열을 사용하기 위해 리스트를 쓰는데, 이는 느린 처리시간을 야기한다.
                 numpy는 array를 제공하는데 이는 파이썬의 기존 리스트보다 훨씬 빠른 처리시간을 보장한다.
      
      간단 튜토리얼 : https://teddylee777.github.io/python/numpy-tutorial
      심화 튜토리얼 : http://aikorea.org/cs231n/python-numpy-tutorial/#numpy-arrays
                 
'''


# 1. 넘파이 임포트 및 버전확인
div(1)

import numpy as np
print(np.__version__)


# 2. 넘파이 배열(ndarray)
div(2)

arr = np.array([1, 2, 3, 4, 5]) 

print(arr)
sp()
print(arr[0])
sp()
print(arr[0:2]) # 슬라이싱 할 경우 x : y-1 까지의 배열을 출력
sp()
print(type(arr)) # 타입: ndarray : Nested Array (다차원 배열 : 2 이상의 차원이 가능)
sp()
arr[0] = 0 # 인덱싱 할당
print(arr)

# 3. 2차원 ndarray
div(3)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
sp()
print(arr_2d[0])
sp()
print(arr_2d[0][0])
sp()
print(arr_2d[0 , : ]) # 행 슬라이싱
sp()
print(arr_2d[ : , 0]) # 열 슬라이싱


# 4. 3차원 ndarray
div(4)

arr_3d = np.array([ [[1,2,3],[4,5,6]], [[7,8,9,], [10,11,12]] ])
print(arr_3d)
sp()
print(arr_3d.shape)
sp()
print(arr_3d[0])
sp()
print(arr_3d[0][0][0])


# 5. 