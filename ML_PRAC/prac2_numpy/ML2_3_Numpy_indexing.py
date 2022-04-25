

'''
ML2_3

인덱싱, 참조, where 등에 관하여

'''
import numpy as np
from stylemod import *


'''
1. Boolean Indexing

    조건 배열( Boolean array ) 를 활용하여 인덱싱하는 방법
    
        - 조건에 해당하는 결과가 True인 요소를 반환한다.
        - 인덱싱 후 결과는 항상 1차원 배열로 반환한다.
'''
div(1)

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
2. Fancy Indexing

    다른 배열(array) or 리스트(list)를 인덱스로 사용하여 배열을 인덱싱하는 방법
    
'''
div(2)

arr = np.arange(100,111)

idx_lst = range(0,6,2)
idx_arr = np.arange(0,11,2)

print( arr[idx_lst] )

sp()
print( arr[idx_arr] )


'''
3. 배열 '참조' and 참조로 인한 Cascading 방지

    arr1 = arr 
    
    위와 같이 arr1 = arr을 수행하면 arr1은 arr을 연속적으로 '참조' 하는 상태가 된다 : 
    - arr1이 arr의 메모리주소를 참조하기 시작하는 것이지 값이 복사된 것이 아니라는 뜻
    
    따라서, 참조로 인한 Cacading(연쇄) 반응을 방지하기 위해서는
    
    (1) arr.copy() 메소드를 사용하여 참조가 아닌 복제본을 할당하는 방법을 사용해야 한다. 
    (2) fancy indexing 을 사용한 값을 할당하면 참조가 아닌 값을 할당하게 되므로 이 또한 방법이다.
'''
div(3)

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

'''
4. where() 조건 반환 메소드

    - np.where( 조건 배열, 참 반환값 배열, 거짓 반환값 배열 )
        (=> 만일 참,거짓 값에 배열이 아닌 단일 아이템을 줄 경우 브로드캐스팅으로 실행됨 -> (3) 참조 ) 

        : 조건배열 items 각각 위치의 참거짓에 따라 동일위치 참배열/거짓배열 값중 하나를 선택하기를 반복하여,
            이들이 혼합된 새로운 배열을 반환한다.
    
    + np.random.randn(행,열) : 난수로 채워지는 Row X Column 배열을 생성
'''
div(4)

#(1) 기본 where()
conditionArr = np.array( [True, False, True, True, False] )

x_arr = np.arange(1.1,1.6,0.1)
y_arr = np.arange(2.1,2.6,0.1)
print(x_arr,y_arr, conditionArr, sep=' / ')

sp()
print( np.where( conditionArr, x_arr, y_arr ) ) #where 조건 배열반환 메소드 실행

#(2) randn 사용한 조건
sp()
conditionArr = np.random.randn(1,5)
print( np.where( conditionArr > 0, x_arr, y_arr))

#(3) 브로드캐스팅 사례
sp()
conditionArr = np.random.randn(4,4)
print( np.where(conditionArr > 0, '양수','음수') ) # x, y에 하나의 값만 줄 경우 브로드캐스팅으로 실행됨