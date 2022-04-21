import numpy as np
import pandas as pd

df=  pd.DataFrame({'industry':[1,2,'etc','etc'],'NAME':[3,2,'a',1],'ATT':[0,'b',1,3]})
print(df)

# Using numpy's where() method to convert 'etc' value into None for removing missing values collectively
df['industry'] = np.where(df['industry'] == 'etc',None,df['industry'])
print(df)

# Removing missing values in dataset across the board
df.dropna(axis=0)

