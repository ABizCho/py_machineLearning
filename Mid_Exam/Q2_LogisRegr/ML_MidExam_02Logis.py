###### import library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

sp = '\n'

#
os.chdir('C:\\Users\\he125\\OneDrive\\바탕 화면\\Dev\\Git\\py_machineLearning\\Mid_Exam\\Q1_LinearRegr\\')

##### Q0. read
df = pd.read_csv('.csv')

'''
Q6. Descriptive statistics
'''
print('=====< Q6. Descriptive statistics >=====\n\n')

#(1)
print(df.info(),sp) # print columns and detailed info
#(2)
print(df.head(),sp) # print head of the dataset
#(3)
print(df.describe(),sp) # print count / min / max / average 
#(+)
print(df.isnull().sum()) #null값 개수 확인

'''
Q7. Deal with missing values to clean the data set by removing the observations that have 'etc' in the 'industry' variable. Use the where function in the Numpy.
'''
# (1) Using numpy's where() method to convert 'etc' value into None for removing missing values collectively
df['industry'] = np.where(df['industry'] == 'etc',None,df['industry'])

# (2) Removing missing values in dataset across the board
df = df.dropna(axis=0)

'''
Q8. Generate dummies of the categorical variable
'''
#0. checking categorical Feature
df.info()

#1. 
df = pd.get_dummies( data=df, columns=['industry',...etc], drop_first=True )


'''
Q9. Build a logistic regression model using the sklearn.logistic_model
'''
# 1. Splitting Train / Test
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df.drop('종속변수',axis=1),df['종속변수'], test_size=0.30, random_state=101)

# 2. Training and Predicting
from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression(solver='liblinear') 

predictions = logmodel.predict(X_test)
probs = logmodel.predict_proba(X_test)

'''
Q10. Show the accuracy and precision metrics on the predictions of the logistic 
regression model. Use the “sklearn.metrics”
'''
from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))

'''
Q11. Print your own suggestions on how to improve the predictions with more accuracy and more precision.”
'''
print('There is trade-off between Precision and Recall therefore it is not that easy to increase precision and accuracy, while improving the pure predicting performance. Inspite of the trade-off, if improving model\'s precision is required, it will be helpful that optimizing the balance ( accuracy : precision : Recall ) by adjusting threshold of model building. + For improving the model\'s performance, it is one easy way to simplify dataset by removing unnecessary features in model building process. ')