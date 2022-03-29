'''
Individual Assignment - 2

    Analyzing Salaries data
'''
def div(n,str) :
    print('\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ<   Result %d : %s   >ㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n'%(n,str))

def sp() :
    print('\nI-------------------------------------------I\n')



'''
Exploring Data
'''
div(1,'Exploring')

# (1) import modules and set env
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

os.chdir('C:\\Users\\he125\\OneDrive\\바탕 화면\\Dev\\Git\\py_machineLearning\\Assignment_Individual')
currDir = os.getcwd()

# (2) read csv 
df_sal = pd.read_csv('Salaries.csv',encoding='CP949')

# (3) summary
print(df_sal.head()) # 상위 레코드

sp()
df_sal.info() # 정보

sp()
print(df_sal.describe()) # 요약 통계량


# (4) 결측값 및 이상값 탐색
sp()
print('Num of Not Provided : ', len(df_sal[df_sal['BasePay'] == 'Not Provided'])) # 'Not Provided' 값을 지닌 Data 개수 탐색 : 4개

sp()  
print('Num of Na in BasePay : ',df_sal['BasePay'].isnull().sum()) # BasePay의 NA값 탐색 : 605개


'''
Cleaning Data
'''
div(1,'Cleaning')

# (1) 불필요한 컬럼 제외한 df 재구성
    # ref 
        # 특정 컬럼 제외 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wideeyed&logNo=221250746480
df_sal = df_sal[df_sal.columns.difference(['Notes','Agency','Status'])]
print('Selected Columns : ',df_sal.columns.values) 

# (2) df_sal에서 Not Provided 값 제외하여 저장
sp()
df_sal = df_sal[df_sal['BasePay'] != 'Not Provided']
print('Len of df_sal excluded Not Provided : ', len(df_sal))

# (3) 
sp()


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

print('The average of “BasePay” : ',df_sal['BasePay'].astype('float64').mean()) 


'''
Q3.
What is the highest value of the variable “OvertimePay”?
'''
div(4,'Q3')

print('The highest value of "OvertimePay" : ', df_sal['OvertimePay'].astype('float64').max())

'''
Q4.
What is the job title of the observation, “JOSEPH DRISCOLL”? Tip: Use all capitalized letters to search the name. 
Otherwise, your code may provide a different answer that doesn’t match up the observation because the data set 
has another observation of “Joseph Driscoll” with the first letters of each word capitalized.
'''
div(5,'Q4')

print('The jobtitle of JOSEPH DRISCOLL : ', df_sal[ df_sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'].values)


'''
Q5.
How much has “JOSEPH DRISCOLL” earned (including the variable “Benefits”)?
'''
div(6,'Q5')

print('JOSEPH DRISCOLL earned : ', df_sal[df_sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'].values[0])

'''
Q6.
Who is the person paid the most (including benefits)?
'''
div(7,'Q6')

print('The one who paid the most : ', df_sal[df_sal['TotalPayBenefits'] == df_sal['TotalPayBenefits'].max()]['EmployeeName'].values[0])


'''
Q7.
Who is the person paid the least (including benefits)? Explain if you notice anything
strange about the salaries paid to the person with the lowest earnings?
'''
div(8,'Q7')

print('The one paid the least : ', df_sal[df_sal['TotalPayBenefits'] == df_sal['TotalPayBenefits'].min()]['EmployeeName'].values[0])
print('The total pay benefits Joe lopez was paid : ', df_sal[df_sal['TotalPayBenefits'] == df_sal['TotalPayBenefits'].min()]['TotalPayBenefits'].values[0])

print('\n# It is weired Joe Lopez was paid minus $')

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