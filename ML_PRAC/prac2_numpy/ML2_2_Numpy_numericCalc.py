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


