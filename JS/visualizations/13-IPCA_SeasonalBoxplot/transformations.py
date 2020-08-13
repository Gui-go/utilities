# Libraries
import pandas as pd
import numpy as np

# Data
df = pd.read_csv("./ipca.csv")
df.shape
df.columns = ['date', 'ipca']
df['ipca'].min()
df['ipca'].max()
df['ipca'].median()
df.describe()

# split method
df['date'].split('/')
df['date'][1].split('/')

# Getting the months
df['months'] = None
df['years'] = None
for i in range(len(df['date'])):
    #print(i)
    df['months'][i] = int(df['date'][i][0:2])
    df['years'][i] = int(df['date'][i][3:9])

# Filtering for 2010+
df = df[df['years'] >= 2000]

# Creating Mean and Median variables, so I don need to worry for it on JS
df['median'] = np.median(df.ipca)
df['mean'] = np.mean(df.ipca)


df.to_csv('./ipca2.csv', index = False, header = True)
