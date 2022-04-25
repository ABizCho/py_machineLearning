'''
Core Python DataType

1. Numbers
2. Strings
3. Lists
4. Dictionaries
5. Tuples
6. Files
7. Sets
'''


'''
<1. Numbers>
'''
# a = 3
# b = 4.56
# c = a / b

# print(type(a),type(b),type(c))
# print('%d \n%d \n%d\n'%(a,b,c))

# # 명시적 타입변환
# x = int(1)
# y = int(2.8)
# z = int('3')

# print(type(x),type(y),type(z))
# print('%d\n%d\n%d\n'%(x,y,z))

# x = float(1)
# x = float(2.8)
# z = float('3')
# w = float('4.2')

# print(type(x),type(y),type(z),type(w))
# print('%f\n%f\n%f\n%f\n'%(x,y,z,w))

# x= str('s1')
# y= str(2)
# z = str(3.0)

# print(type(x),type(y),type(z))
# print('%s\n%s\n%s'%(x,y,z))


'''
<2. Strings>
'''
# a = 'Hello'
# print(len(a))

# print(a[0])
# print(a[-1])
# print(a[0:5]) # 콜론으로 늘릴때는 n-1까지 펼친다. (즉 0 ~ 5-1)

# # string 산술연산
# a = 'Hello'
# print(a + ' world!')
# print(a*4)
# print(a + ' World!' * 4)
# print(( a + ' World! ') * 4 ) # 산술연산 순서가 적용됨


'''
<3. Booleans>
True or False
'''
# print(10 > 9)
# print(10 >= 9)
# print(10 == 9)
# print(10 != 9)
# print(10 < 9)
# print(10 <= 9)

# a = 200
# b = 200

# if b > a :
#     print('b is greater than a')
# else : 
#     print('b is not greater than a')

# if b > a :
#     print('b is greater than a')
# elif b < a :
#     print('b is lower than a')
# else :
#     print('b is eqaul with a')


'''
<4. Lists>
multiple items in a single varible

orderd, changeable, allow duplicate values
indexed

Tuple / set / Dictionaries
'''

# L = [123, 3.14, 'Hello']
# print(L)
# print(L[0])

# nested_list = [[1,2,3],[4,5,6],[7,8,9]]
# print(nested_list[0][1])
# print(nested_list[2][1])

# for x in L :
#     print(x)
    
# i = 0
# while i < len(L):
#     print(L[i])
#     i = i + 1

# # sort() method 
# fruit_list = ['apple','banana','cherry','mango','kiwi']
# num_list = [100,50,65,353,2134]

# print(sorted(num_list)) # sorted : 저장x / 반환o
# a = sorted(num_list)
# fruit_list.sort()

# num_list.sort() # .sort() 메소드 : 저장o

# print(a == num_list)
# print(fruit_list)

'''
< Dictionaries >
{   key: value,
    key: value,
    key: value
    }
    
a collection
ordered, changeable, do not allow duplicates

'''
# D = {
#     'id': 5,
#     'name': 'apple',
#     'color': 'red',
#     'taste': 'sweet',    
# }

# print(D['name']) # key로 인덱싱하여 value 가져오기
# print(D.get('name')) # key로 지정하여 value 가져오기

# print(D.keys()) # keys 출력
# print(D.items()) # items(키 : 값) 출력

# D.pop('id') # key값 지정하여 item 제거 및 저장
# print(D) # item 제거된 모습 확인


'''
<5. Files>
File object
    for interacting with files
    
    Mode : 'r', 'w', 'a ( append )', 'x ( create )'
'''

# f = open('ML1_2_FileObject.txt','w') #쓰기전용
# f.write('Hello text files and')
# f.write(' world!')
# f.close()

# f = open('ML1_2_FileObject.txt','r') #default 모드는 read
# fileObject = f.read() 
# print(fileObject)
# f.close()

# f = open('ML1_1_FileObject.txt','a') # a : append Mode
# f.write(', I\'ts me HorizD!')
# f.close()
# f = open('ML1_1_FileObject.txt','r')
# fileObject = f.read()
# print(fileObject)

# f = open('ML1_1_FileObjectCreated.txt','x')
# f.write('Create new one in new named file')
# f.close()
# f = open('ML1_1_FileObjectCreated.txt','r')
# fileObject = f.read()
# print(fileObject)