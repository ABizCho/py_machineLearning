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

print('The jobtitle of JOSEPH DRISCOLL : ', df_sal[ df_sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'].values[0])


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

unq_jt = df_sal.groupby('JobTitle')['Id'].count()[df_sal.groupby('JobTitle')['Id'].count() == 1] # 취합개수 1 여부 참거짓 에 따른 직업 반환
# print(unq_jt.keys()) # 유니크 직업 인덱스 출력

print('Num of Unique JobTitles : ', unq_jt.count()) # 개수 출력


'''
Q9.
What are the top 5 job titles we can most frequently see in the data set?
'''
div(10,'Q9')

jt_top5frq = df_sal.groupby('JobTitle')['Id'].count().sort_values(ascending=False)[0:5]
print('<< Top 5 the most frequent job titles >> \n\n', jt_top5frq)


'''
Q10.
How many job titles were occupied by a single person only in 2013?
'''
div(11,'Q10')

df_sal_2013 = df_sal[df_sal['Year'] == 2013]

jt_ocpBySingle = df_sal_2013.groupby('JobTitle')['Id'].count()[df_sal_2013.groupby('JobTitle')['Id'].count() == 1]
print('Num of Job titles occupied by a single person in 2013 : ', jt_ocpBySingle.count())

'''
Q11.
How many people have the word “Chief” in their job titles?
'''
    # ref : 
        # 파이썬 정규표현식 탐색 : https://ponyozzang.tistory.com/279
div(12,'Q11')

from re import search

# # 문제의 'How many people'의 모호함 해소를 위해 이름이 중복되는 레코드 확인 
# df_groupByEmpName = df_sal.groupby('EmployeeName')['Id'].count()[df_sal.groupby('EmployeeName')['Id'].count() >= 2 ]
# print('2 이상 중복된 이름의 수 : ',len(df_groupByEmpName)) 

## 이름이 두번 이상 중복되는 레코드가 대략 34273개로 너무 큰 수가 존재 하므로, 이를 동명이인으로 가정하고 동일인 중복에 대한 고려 없이 모든 레코드에 대해 Chief를 조사하여 이 수를 해당 문제에 대한 답으로 정하도록 하겠습니다.


# 개수 확인

cnt_chief = 0
df_sal_jt = df_sal['JobTitle'].values.astype('str')

for job in df_sal_jt :
    if search(r'CHIEF',job) != None :
        cnt_chief += 1

print('Num of "CHIEF" job titles : ', cnt_chief)


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