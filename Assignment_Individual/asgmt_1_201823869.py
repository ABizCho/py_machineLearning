'''
1. convertCelsius 
'''
def convertCelsius() :
    try: 
        Cel = float(input('Enter a temperature degree in Celsius(ºC) : '))
    except :
        print('Please enter a valid number.')
    
    Fah =  Cel * ( 9/5 ) + 32
    print('%0.2f degrees Fahrenheit(ºF)'%(Fah))
convertCelsius()


'''
2. getLength 
'''
def getLength() : 
    try : inputStr = input('Enter a word or phrase: ')
    except :
        print('Please enter a valid string.')
        
    print('The length of the input is %d characters'%(len(inputStr)))
getLength()



'''
3. quadraticRoot 
'''
def quadraticRoot() :
    try : 
        a,b,c = map(int, input('Enter two coefficients of x2 and x, and value of a constant, separating by space, respectively : ').split())
    except :
        print('Please enter a valid numbers.')
        
    q_root1: float = ( (-b + (b**2 - 4*a*c)**0.5 ) / (2*a) )
    q_root2: float = ( (-b - (b**2 - 4*a*c)**0.5 ) / (2*a) )
    print('The solutions include %0.1f and %0.1f.'%(q_root1,q_root2))
quadraticRoot()



'''
4. calcDistance 
'''
import math

def calcDistance(x1:int, y1:int, x2:int , y2 :int) :
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
print(calcDistance(5,10,15,20))