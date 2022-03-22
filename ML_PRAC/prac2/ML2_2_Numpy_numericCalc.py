from stylemod import *
import numpy as np
'''
ML2_2

넘파이-배열계산 

'''


'''
1. 행열계산

    element-wise perations : 
    
        - 행과 열이 같은 배열을 계산하면 같은 위치에 있는 값끼리 계산된다.
        - 두 연산대상의 shape가 같아야 한다.
'''
div(1)

x = np.array( [1,2] )
y = np.array( [10,20] )
print(x + y)

sp()
x = np.array( [ [1,2], [3,4] ] )
y = np.array( [ [4,3], [2,1] ] )
print(x + y)

sp()
print(x - y)

sp()
print(x * y) # 일반 스칼라곱셈 , 행렬곱(@) 과는 다르다

sp()
print(x / y)

sp()
print(x // y)

sp()
print(x % y)


'''
2. 브로드캐스팅 
    
        단순 스칼라값 연산
        제곱, 거듭제곱 연산
'''
div(2)

x = np.array( [[1,2], [3,4]] )

print(x + 1)

sp()
print(x - 1)

sp()
print(x * 2)

sp()
print(x // 2)

sp()
print(x ** 2)

sp()
print( np.sqrt(x) ) # 루트 연산

sp()
print( np.exp(x) ) # exponential 연산 = 지수


'''
3. 행렬 곱셈연산 

        (https://seong6496.tistory.com/110)
        (+ 행렬곱셈이란 : https://gosamy.tistory.com/6 )


   -  * : 일반 스칼라 곱셈연산
   -  @ : 행렬 곱셈연산(matmul) : 보통은 외적 연산시 사용
   -  .dot() : 내적 연산(dot product)

'''
div(3)

x = np.array( [[1,2],[3,4]] )
y = np.array( [5,6] )

#일반 스칼라 곱셈 : 브로드캐스팅 수행
print(x * y)   

# 내적 연산
sp()
print( x.dot(y) )

# 행렬곱
sp()
print( x @ y )


'''
4. Boolean Indexing

    조건 배열( Boolean array ) 를 활용하여 인덱싱하는 방법
    
        - 조건에 해당하는 결과가 True인 요소를 반환한다.
        - 인덱싱 후 결과는 항상 1차원 배열로 반환한다.
'''
div(4)

arr = np.arange(1, 13).reshape(3, 4)
print(arr)

# array의 조건연산을 통한 boolean값을 items로 하는 배열 생성
sp()
bool_arr = arr > 5 
print(bool_arr)

# 위에서 생성한 boolean배열을 이용한 특정 itmes 인덱싱 : 인덱싱 반환값은 항상 1차원배열
sp()
print(arr[bool_arr])

'''
5. Fancy Indexing

    다른 배열(array) or 리스트(list)를 인덱스로 사용하여 배열을 인덱싱하는 방법
    
'''
div(5)

arr = np.arange(100,111)

idx_lst = range(0,6,2)
idx_arr = np.arange(0,11,2)

print( arr[idx_lst] )

sp()
print( arr[idx_arr] )


'''
6. 배열 '참조' and 참조로 인한 Cascading 방지

    arr1 = arr 
    
    위와 같이 arr1 = arr을 수행하면 arr1은 arr을 연속적으로 '참조' 하는 상태가 된다 : 
    - arr1이 arr의 메모리주소를 참조하기 시작하는 것이지 값이 복사된 것이 아니라는 뜻
    
    따라서, 참조로 인한 Cacading(연쇄) 반응을 방지하기 위해서는
    
    (1) arr.copy() 메소드를 사용하여 참조가 아닌 복제본을 할당하는 방법을 사용해야 한다. 
    (2) fancy indexing 을 사용한 값을 할당하면 참조가 아닌 값을 할당하게 되므로 이 또한 방법이다.
'''
div(6)

arr = np.ones(5, dtype='int')
print(arr)

# 메모리 주소 참조로 인한 cascading
sp()
arrRef = arr
arrRef[0] = 0

print(arr,arrRef,sep=' / ') # arrRef를 수정헀지만 arr도 수정된 모습 : 참조로 인해 서로 같은 값을 변경했기 떄문

# (1) 복사 할당을 통한 cascading 방지
sp()
arrCopy = arr.copy()
arrCopy[1] = 0

print(arr,arrCopy, sep=' / ')

# (2) fancy Indexing을 이용한 배열 할당 사용으로 참조방지
sp()
arr = np.ones(5, dtype=int)
arrCopy = arr[range(len(arr))]

arrCopy[0] = 0

print(arrCopy,arr,sep=' / ')



