import pandas as pd
import numpy as np
df=pd.raed_csv('D://data1/submission.csv')
#print(df)
print(df.shape)
df.drop(['cabin'],axix=1,inplace=True)
df.fillna(method='ffill',inplace=True)
print(pd.crosstab(index=df['sex'],coloumns=df[survied']))
print(pd.pivot_table(df,index=['sex,age'],aggfun=np.

