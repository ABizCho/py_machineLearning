'''
Individual Assignment - 2

    Analyzing Salaries data
'''
def div(n,str) :
    print('\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ<   Result %d : %s   >ㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n'%(n,str))

def sp() :
    print('\nI-------------------------------------------I\n')



'''
Preparing
'''
div(1,'Preparing')

# (1) import modules and set env
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

os.chdir('C:\\Users\\he125\\OneDrive\\바탕 화면\\Dev\\Git\\py_machineLearning\\Assignment_Individual')
now = os.getcwd()

# (2) read csv 
sp()
df_salaries = pd.read_csv('Salaries.csv',encoding='CP949')
print(df_salaries)

sp()
df_salaries.info()


'''
Q1.
Generate texts with a couple of sentences that describe the data set based on your empirical insight and statistical approach.  
'''
div(2,'Q1')


'''
Q2.
What is the average of the variable “BasePay”?
'''
div(3,'Q2')

# (1) 결측값 처리 : 
    # 결측값을 변수별 평균으로 대체하는 방법 채택
    # ref : 
        # https://developer-ping9.tistory.com/111 : pd 조건에 맞는 컬럼 변경
        # https://rfriend.tistory.com/262  :  결측값 평균 대체
sp()

print(df_salaries['BasePay'])

'''
Q3.
What is the highest value of the variable “OvertimePay”?
'''
div(4,'Q3')

'''
Q4.
What is the job title of the observation, “JOSEPH DRISCOLL”? Tip: Use all capitalized letters to search the name. 
Otherwise, your code may provide a different answer that doesn’t match up the observation because the data set 
has another observation of “Joseph Driscoll” with the first letters of each word capitalized.
'''
div(5,'Q4')

'''
Q5.
How much has “JOSEPH DRISCOLL” earned (including the variable “Benefits”)?
'''
div(6,'Q5')

'''
Q6.
Who is the person paid the most (including benefits)?
'''
div(7,'Q6')

'''
Q7.
Who is the person paid the least (including benefits)? Explain if you notice anything
strange about the salaries paid to the person with the lowest earnings?
'''
div(8,'Q7')

'''
Q8.
How many unique job titles can we see in the data set?
'''
div(9,'Q8')

'''
Q9.
What are the top 5 job titles we can most frequently see in the data set?
'''
div(10,'Q9')

'''
Q10.
How many job titles were occupied by a single person only in 2013?
'''
div(11,'Q10')

'''
Q11.
How many people have the word “Chief” in their job titles?
'''
div(12,'Q11')

'''
Q12.
Visualize a histogram to show the distribution of the variable “TotalPay” with all the 
observations in the data set.
'''
div(13,'Q12')

'''
Q13.
Visualize a line chart where the x-axis indicates the year (over time) whereas the y-axis indicates 
the average “TotalPay” of all the observations.
'''
div(14,'Q13')

'''
Q14.
Visualize a bar chart with the counts of observations across the three different ranges of 
the variable “TotalPay”: i.e., low, medium, high salaries.
'''
div(15,'Q14')