'''
ML7 
Logistic Regression

    Linear Regression은 Continuous data에 관한 예측을 위함 - unsupervised
    
    반면, 
    Logistic Regression은 Binary data( yes / no ) or (classification 문제)  를 예측하기 위함 - supervised 
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os
os.chdir('C:\\Users\\he125\\OneDrive\\바탕 화면\\Dev\\Git\\py_machineLearning\\prac7')

train = pd.read_csv('titanic_train.csv')

'''
Exploratory D/a
'''

print(train.head())

# Missing Data
sns.heatmap(train.isnull(),
            yticklabels=False,
            cbar=False,
            cmap='viridis')

# Visualize the dependant variable
sns.set_style('whitegrid')
sns.countplot(x='Survived', 
              data = train,
              palette='RdBu_r')

sns.set_style('whitegrid')
sns.countplot(x='Survived',
              hue='Sex', data=train)

sns.countplot(x='Survived',
              hue='Pclass', data=train, 
              palette='rainbow')

sns.displot(data=train, x=train['Age'].dropna(),kde=False,color='darkred',bins=30)

sns.countplot(x='SibSp',data=train)


'''
Data Cleaning

'''

# 1. Dealing with Missing Values
    #We want to fill in missing age data instead of just dropping the missing age data rows. One way to do this is by filling in the mean age of all the passengers (imputation). 

        #**Question: What is the average age of all the passengers?** 
plt.figure(figsize=(12,7))
sns.boxplot(x='Pclass', y= 'Age', 
            data= train, 
            palette='winter')

        #We can see the wealthier passengers in the higher classes tend to be older, which makes sense. We'll use these average age values to impute based on Pclass for Age.
def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    
    if pd.isnull(Age):

        if Pclass == 1:
            return 37

        elif Pclass == 2:
            return 29

        else:
            return 24

    else:
        return Age

    #Apply the function
train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)

    #check the heatmap again
sns.heatmap(train.isnull(),
            yticklabels=False,cbar=False,
            cmap='viridis')

    # drop the Cabin column and the row in Embarked that is NaN
train.drop('Cabin',axis=1,inplace=True)
train.head()

train.dropna(inplace=True)
