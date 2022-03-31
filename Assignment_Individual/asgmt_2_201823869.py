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
from tkinter import font
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

os.chdir('C:\\Users\\he125\\OneDrive\\바탕 화면\\Dev\\Git\\py_machineLearning\\Assignment_Individual')
currDir = os.getcwd()

# (2) read csv 
df_sal = pd.read_csv('Salaries.csv',encoding='CP949')

# (3) summary
print(df_sal.head()) # heads for summary

sp()
df_sal.info() # information

sp()
print(df_sal.describe()) # summaries for describing


# (4) Exploring missing values and outliers
sp()
print('Num of Not Provided : ', len(df_sal[df_sal['BasePay'] == 'Not Provided'])) # 'Not Provided' 값을 지닌 Data 개수 탐색 : 4개

sp()  
print('Num of Na in BasePay : ',df_sal['BasePay'].isnull().sum()) # BasePay의 NA값 탐색 : 605개


'''
Cleaning Data
'''
div(1,'Cleaning')

# (1) Excluding unnecessary columns
    # ref 
        # 특정 컬럼 제외 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wideeyed&logNo=221250746480
df_sal = df_sal[df_sal.columns.difference(['Notes','Agency','Status'])]
print('Selected Columns : ',df_sal.columns.values) 

# (2) df_sal에서 Not Provided(str) 값 제외하여 저장
sp()
df_sal = df_sal[df_sal['BasePay'] != 'Not Provided']
print('Len of df_sal excluded Not Provided : ', len(df_sal))

# (3) df_sal에서 na값은 무분별하게 제거했을 시 일부 문제에 error를 야기한다 
    # 따라서 현재 시점에선 따로 처리하지 않고 향후 문제 풀이에서 필요에 따라 처리한다.

'''
Q1.
Generate texts with a couple of sentences that describe the data set based on your empirical insight and statistical approach.  
'''
div(2,'Q1')

print('# 1. There is too many outliers in the boxplot made in my additional analysis part.')
print('# 2. Q12-histogram is skewed to left. and Few people earned more than 200000.')
print('# 3. Q14-bar chart show there is few people who are classified in "high class" , even in "medium class"')
print('# 4. From 1, 2, and 3, we can presume that there is huge gap in paying.')
print('# 5. Top3 the most paid jobtitle is "Chief Investment Officer","Chief of Police, and "Chief, Fire Department"')
print('# 6. At least in my results of analysis like #5, the people whose jobtitle has the word "chief" tend to be paid more than others ')


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

## 문제의 'How many people'의 모호함 해소를 위해 이름이 중복되는 레코드 확인 
# df_groupByEmpName = df_sal.groupby('EmployeeName')['Id'].count()[df_sal.groupby('EmployeeName')['Id'].count() >= 2 ]
# print('2 이상 중복된 이름의 수 : ',len(df_groupByEmpName)) 

## There is too many cases that record names are overlapped. so, I'll assume that the whole overlapped record names are homonym cases and exclude preprocessing for this.
## ( 이름이 두번 이상 중복되는 레코드가 대략 34273개로 너무 큰 수가 존재 하므로, 이 모든 중복을 동명이인으로 가정하고 동일인 중복에 대한 고려 없이 모든 레코드에 대해 Chief를 조사 및 카운트하여 이 수를 해당 문제에 대한 답으로 정하도록 하겠습니다. )


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
# ref : 
    # 서브플롯 : https://teddylee777.github.io/visualization/matplotlib-tutorial
    # 서브플롯 타이틀 : https://www.delftstack.com/ko/howto/matplotlib/how-to-add-title-to-subplots-in-matplotlib/
    
    # 히스토그램 특정 구간 강조 : https://velog.io/@khnn/TIL-Matplotlib%EC%9C%BC%EB%A1%9C-%ED%9E%88%EC%8A%A4%ED%86%A0%EA%B7%B8%EB%9E%A8-%EA%BE%B8%EB%AF%B8%EA%B8%B0
    
div(13,'Q12')
import matplotlib.pyplot as plt


plt.style.use('Solarize_Light2')

fig, ax = plt.subplots(2, 1)

n,bins,patches = ax[0].hist(df_sal['TotalPay'],edgecolor='black',linewidth=1.2 )
patches[1].set_facecolor('gold')

n,bins,patches = ax[1].hist(df_sal['TotalPay'],edgecolor='black',linewidth=1.2,bins=30 )
patches[0].set_facecolor('gold')
patches[3].set_facecolor('gold')

ax[0].set_title("Histogram of TotalPay (default)")
ax[1].set_title("Histogram of TotalPay (bins=30)")

plt.xlabel('TotalPay')
plt.ylabel('Count of records')

fig.set_size_inches(9, 9)
plt.show()


'''
Q13.
Visualize a line chart where the x-axis indicates the year (over time) whereas the y-axis indicates 
the average “TotalPay” of all the observations.
'''
# ref : 
    # linear graph styling(goodRef): https://zephyrus1111.tistory.com/21
div(14,'Q13')


TP_year = df_sal.groupby('Year').mean().index.values
TP_avg = df_sal.groupby('Year').mean()['TotalPay'].values

xpoints = TP_year
ypoints = TP_avg


fig = plt.figure(figsize=(7,7)) # canvas
ax = fig.add_subplot()          # frame

ax.spines['right'].set_visible(False) # unvisible right spine
ax.spines['top'].set_visible(False) # # unvisible top spine

ax.plot(xpoints,ypoints, 'g', marker='o',linestyle='--')

ax.axhline( TP_avg.mean(), label='mean')
ax.text(2011,TP_avg.mean()+20, 'Mean : %f'%(TP_avg.mean()),fontsize=9,color='gray')

plt.title('Avgs of TotalPay by years')

plt.xticks(TP_year)
plt.yticks(TP_avg)

plt.xlabel('Years')
plt.ylabel('Averages of whole TotalPay')
plt.show()


'''
Q14.
Visualize a bar chart with the counts of observations across the three different ranges of 
the variable “TotalPay”: i.e., low, medium, high salaries.
'''
div(15,'Q14')

# + There is no standard for dividing class interval (high,medium,low), so I used 2 different ways. 
            # 1.  pd.cut() method by default options
            # 2.  Dividing 3 class in the same range of value ( Using cut() method too) 

fig, ax = plt.subplots(2, 1)

# WAY 1.
    # pd.cut() method by default options
df_sal['pay_class'] = pd.cut(df_sal['TotalPay'],3, labels=['low','medium','high'])

df_sal_class = df_sal.groupby('pay_class')['pay_class'].count()

ax[0].bar(df_sal_class.index.values,df_sal_class.values)

ax[0].set_title('Way 1 : Dividing classes by default cut() options')


# WAY 2.
    # Dividing 3 class in the same range of value ( Using cut() method too) 

endP = int(df_sal['TotalPay'].max())
startP = int(df_sal['TotalPay'].min())


intv = int((endP - startP) / 3)

bins = range(startP,endP,intv)
bins_label = ['low','medium','high']

df_sal['pay_class'] = pd.cut( df_sal['TotalPay'], bins,right=False, labels=bins_label )

ax[1].bar(df_sal_class.index.values,df_sal_class.values)
ax[1].set_title('Way 2 : Dividing classes by the same range of value')



plt.xlabel('TotalPay Class')
plt.ylabel('Count of obs')

print('Showing Counts of classes of Total pay bar chart...')

fig.set_size_inches(9, 9)
plt.show()

print('\nOpinion : I figured out the pd.cut() method runs similarly with my way2 formula.\n')





'''
+ Additional Analysis and Visualization
'''

# Additional 1 : Boxplot of TotalPay
div(16,'Additional Analysis 1 : BoxPlot of TotalPay')
plt.style.use('seaborn-dark')

plt.boxplot(df_sal['TotalPay'], showmeans=True)
plt.title('Additional Analysis 1 : BoxPlot of TotalPay')
plt.xlabel('TotalPay')

print(' Opinion : There is too many outliers in the boxplot using default options.\n -> We can presume that there is leaning phenomenon in paying')
plt.show()


# Additional 2 : Top10 the most paid jobtitles
div(17,'Additional Analysis 2 : Top10 the most paid jobtitles ')
import numpy as np
top10_paidJts = df_sal.groupby('JobTitle').mean()['TotalPayBenefits'].sort_values(ascending=False)[0:10].astype(int)
print(top10_paidJts)

sp()

fig, ax = plt.subplots(figsize=(8,8))

ax.bar(top10_paidJts.index.str.lower(),top10_paidJts.values,
       color = 'red',alpha=0.5)
plt.title('Additional Analysis 2 : Top10 the most paid jobtitles')

plt.subplots_adjust(bottom=0.5)
plt.xticks(rotation=75)
print('Showing Top10 the most paid jobtitles...')
plt.show()

sp()