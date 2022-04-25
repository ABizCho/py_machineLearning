
from stylemod import *

'''
 Numpy 
    
    넘파이는 파이썬이 계산과학 분야에 이용될 때 핵심 역할을 하는 라이브러리이다. ( 선형대수, 포리에 변형, 매트릭스 등 ) 
    Numpy는 고성능의 다차원 배열 객체(array)와 이를 다룰 도구를 제공한다. : http://aikorea.org/cs231n/python-numpy-tutorial/#numpy-arrays
    
    - why use? :  1.파이썬은 배열을 사용하기 위해 리스트를 쓰는데, 이는 아래의 장단점이 존재한다.
                    - 확장성이 좋다.
                    - 성능이 안좋다.
                    - 리스트간 수치계산이 어렵다(지원하지 않는다)
                    - 행렬연산 / 고차원 연산도 지원하지 않는다.
                    
                 numpy는 array를 제공하는데 이는 파이썬의 기존 리스트보다 훨씬 빠른 처리시간을 보장하며, 다양한 연산을 지원한다.
      
      간단 튜토리얼 : https://teddylee777.github.io/python/numpy-tutorial
      심화 튜토리얼 : http://aikorea.org/cs231n/python-numpy-tutorial/#numpy-arrays
      조작 메서드 튜토리얼 : https://ddolcat.tistory.com/697
                 
'''

'''
# 1. 넘파이 임포트 및 버전확인
'''
div(1)

import numpy as np
print(np.__version__)


'''
# 2. 넘파이 배열(ndarray)
'''

# div(2)

# arr = np.array([1, 2, 3, 4, 5])  # 1차원 배열 생성
# print(arr)

# sp()
# print(arr[0])

# sp()
# print(arr[0:2]) # 슬라이싱 할 경우 x : y-1 까지의 배열을 출력

# sp()
# print(arr.shape) # shape: 크기확인 : 튜플로 출력 :: 5행 1열 

# sp()
# print(type(arr)) # 타입: ndarray : n-dimensional Array (다차원 배열 : 2 이상의 차원이 가능)

# sp()
# arr[0] = 0 # 인덱싱 할당
# print(arr)

'''
# 2+. dtype 타입 지정을 통한
        item 명시적 타입 지정 배열 생성
'''
# div(2.1)

# arr_dtype = np.array([1,2,3,4,5], dtype=float)
# print(arr_dtype)

'''
# 3. 2차원 ndarray
'''
# div(3)

# arr_2d = np.array([[1, 2, 3], [4, 5, 6]]) # 2차원 배열 생성
# print(arr_2d)

# sp()
# print(arr_2d.shape) # 2행 3열 : (2,3) 튜플로 출력

# sp()
# print(arr_2d.dtype) # 요소 타입 및 크기 확인

# sp()
# print(arr_2d.size) # 총 item 수 확인

# sp() # 행열 교환(Transpose) : .T 
# print(arr_2d.T)

# sp()
# print(arr_2d[0])

# sp()
# print(arr_2d[0][0])

# sp()
# print(arr_2d[0 , : ]) # 행 슬라이싱

# sp()
# print(arr_2d[ : , 0]) # 열 슬라이싱


'''
# 4. 3차원 ndarray
'''
# div(4)

# arr_3d = np.array([ [[1,2,3],[4,5,6]], [[7,8,9,], [10,11,12]] ])
# print(arr_3d)
# sp()
# print(arr_3d.shape)
# sp()
# print(arr_3d[0])
# sp()
# print(arr_3d[0][0][0])


'''
# 5. np.arange() 메소드를 이용한 배열생성 : range()와 유사

    arange(start, stop(n-1), step)
    arange(n) : 0부터 시작하여, n의 크기로 생성
'''
# div(5)

# print(np.arange(10))
# print(np.arange(2,10))
# print(np.arange(0,11,2))


'''
# 6. np.linspace() : 범위 내 균일 간격으로(실수범위까지) 나눠진 배열생성

    np.linspace(start, stop, count) - start부터 stop까지 count개 구간으로 나눈다. (itme은 실수로 생성됨)
'''
# div(6)

# print(np.linspace(1, 10, 3))


'''
# 7. 일괄지정 배열 생성
    
    np.zeros()
    np.ones()
    np.full(shape, fill_value)
'''
# div(7)

# print( np.zeros(5) )
# print( np.zeros(shape=(3 , 5)) )

# sp()
# print( np.ones(5) )
# print( np.ones(shape=(2, 3)) )

# sp()
# print( np.full(shape=(2,3), fill_value=5) )


'''
# 8.   np.eye()
        -identical Matrix 생성 : 대각선으로 1이 채워진 행렬
'''
# div(8)

# print(np.eye(4)) # 인자 : nXn의 identical 행렬 생성


'''
# 9. arr.reshape( x, y ) : 배열 구조 변경

        - 형태는 자유롭게 변경 가능하지만, 변경 후의 데이터 개수(size)는 변경 전과 동일해야함 : size가 다른 경우 오류 출력
        - -1을 (x or y) 값으로 넣을 경우 상대값에 맞게 자동계산된다.
'''
div(9)

arr_befSp = np.arange( 10 )
print(arr_befSp)

sp()
arr_aftSp = arr_befSp.reshape(2,5)
print(arr_aftSp)

sp()
try:
    arr_aftSp = arr_aftSp.reshape(3,5)
except : 
    print('전후 items 사이즈가 다르므로 에러를 출력합니다.')
    
sp()
arr_minusOne = arr_befSp.reshape(5,-1)
print(arr_minusOne)



