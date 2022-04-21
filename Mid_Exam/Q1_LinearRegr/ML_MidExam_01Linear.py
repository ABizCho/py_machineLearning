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
df_pet = pd.read_csv('petrol_consumption.csv')

'''
Q1. 기술 통계 및 요약을 사용하여 데이터를 설명하라
'''
print('=====< Q1. Descriptive statistics >=====\n\n')

#(1)
print(df_pet.info(),sp) # print columns and detailed info
#(2)
print(df_pet.head(),sp) # print head of the dataset
#(3)
print(df_pet.describe(),sp) # print count / min / max / average 
#(+)
print(df_pet.isnull().sum()) #null값 없음

'''
Q2. visualization
'''
print('=====< Q2. Visualizations >=====\n\n')
# (1) heatmap : strong correlation between driver-license and petrol_consumption
sns.heatmap(df_pet.corr())
# print(df_pet.corr())
# plt.show()


# (2) histogram (petrol_consumption)
sns.histplot(data=df_pet, x='Petrol_Consumption', kde=True)
# plt.show()

# (+) boxPlot
plt.boxplot(df_pet['Petrol_Consumption'], showmeans=True)
# plt.show()


'''
Q3. Build a Linear Regression Model 

'''
#(0) Split data (Test/Train)
    # Assign two arrays
y = df_pet['Petrol_Consumption']
X = df_pet[['Petrol_tax','Average_income','Paved_Highways','Population_Driver_licence(%)']]

    # Split
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.4, random_state=101)

# print(X_train)
# print(X_test)
# print(y_train)
# print(y_test)

#(1) Creating and Training the Model
print('=====< Q3.1 Creating and Training the Model >=====\n\n')
from sklearn.linear_model import LinearRegression 

lm = LinearRegression()

lm.fit(X_train,y_train)

#(2) Show Coefficients values of the four independent variables.
    
    #coefficients
coeff_df = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficient'])
print('=====< Q3.2 Coefficient >=====\n\n')
print(coeff_df)
    # (+)intercept
print(lm.intercept_)


'''
Q4. Model Evaluation
MAE,MSE,RMSE
'''
    #[1] Predictions testset from our Model
predictions = lm.predict(X_test)
plt.scatter(y_test, predictions)

print('=====< Q4-1 Comparing for Evaluating the model >=====\n\n')
    #[2] compare the actual price with the predicted one in the test set
y_test1 = y_test.to_frame()
y_test1['Predictions'] = predictions
print(y_test1.head())

    #[+3]displot of Redisual
sns.displot((y_test-predictions),bins=30)
plt.show()

  
    #[4] compute the erorrs for Evaluation 
y_test1['Error'] = y_test1['Predictions'] - y_test1['Petrol_Consumption']



print('=====< Q4-2 Evaluations : MSE, MAE, RMSE >=====\n\n')
from sklearn import metrics

# MSE
MSE = (sum(y_test1['Error']**2))/len(y_test1['Error']) 
MAE =(sum(y_test1['Error'].abs())) / len(y_test1['Error']) 
RMSE = np.sqrt(metrics.mean_squared_error(y_test, predictions))

print('MAE: ', MAE)
print('MSE: ', MSE)
print('RMSE: ', RMSE)

'''
Q5. My own thoughts on minimizing the error rates( MAE, MSE, RMSE to improve)
'''
print('First of all, there are too short records in the dataset. Too short dataset generally makes errors. Thus, getting a bigger one might be a good solution. In other perspective, to reduce the error rates, There are some ways like removing outliers, minimizing data skewness, selecting features, but this dataset has too short length of records, it may be not that cool. This last suggestion could be better one. On the proposition there are over or under fitting issue, Checking ROC curve and then using more complex model like polynomial regression and regularization for minimizing the error rates and improving model will be the best solution')
