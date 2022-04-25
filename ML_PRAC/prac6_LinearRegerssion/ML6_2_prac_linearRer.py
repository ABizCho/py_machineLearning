import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os

'''
Checkout the data
'''
#
os.chdir('C:\\Users\\he125\\OneDrive\\바탕 화면\\Dev\\Git\\py_machineLearning\\ML_PRAC\\prac6')
USAhousing = pd.read_csv('USA_Housing.csv')

#
USAhousing.head()
#
USAhousing.info()
#
USAhousing.describe()

'''
EDA
'''
# #
# sns.pairplot(USAhousing)
# plt.show()

# #
# sns.displot(data=USAhousing, x='Price', kde=True)
# plt.show()

# #
# USAhousing.corr()

# #
# sns.heatmap(USAhousing.corr())
# plt.show()

'''
Training a Linear Regression Model

    Let's now begin to train out regression model! We will need to first split up our data into an X array that contains the features to train on, and a y array with the target variable, in this case the Price column. We will toss out the Address column because it only has text info that the linear regression model can't use.
'''

# 1. X and y arrays
print(USAhousing.columns.tolist())

X = USAhousing[USAhousing.columns.tolist()]
Y = USAhousing['Price']


# 2. Train Test Split
    # Now let's split the data into a training set and a testing set. We will train out model on the training set and then use the test set to evaluate the model.
    
    
