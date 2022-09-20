

# https://www.kaggle.com/code/robikscube/time-series-forecasting-with-machine-learning-yt/notebook


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import os

# Get current wd:
os.curdir


# Colors adjustment:
color_pal = sns.color_palette()
plt.style.use('fivethirtyeight')

# Load data
df = pd.read_csv('data/AEP_hourly.csv')
df = df.set_index('Datetime')
df.index = pd.to_datetime(df.index)

# Initial plot:
df.plot(style='.', figsize=(15, 5), color=color_pal[0], title='PJME Energy Use in MW')
plt.show()

# Create exogenous variables:
def create_features(df):
    """
    Create time series features based on time series index.
    """
    df = df.copy()
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    df['dayofmonth'] = df.index.day
    df['weekofyear'] = df.index.week
    return df

df = create_features(df)

# Train / Test:
train = df.loc[df.index < '01-01-2015']
test = df.loc[df.index >= '01-01-2015']

# Train/Test plot
fig, ax = plt.subplots(figsize=(15, 5))
train["AEP_MW"].plot(ax=ax, label='Training Set', title='Data Train/Test Split')
test["AEP_MW"].plot(ax=ax, label='Test Set')
ax.axvline('01-01-2015', color='black', ls='--')
ax.legend(['Training Set', 'Test Set'])
plt.show()

# Week window plot:
df.loc[(df.index > '01-01-2010') & (df.index < '01-08-2010')]["AEP_MW"] \
    .plot(figsize=(15, 5), title='Week Of Data')
plt.show()

# Boxplot by hour:
fig, ax = plt.subplots(figsize=(10, 8))
sns.boxplot(data=df[["AEP_MW", "hour"]], x='hour', y='AEP_MW')
ax.set_title('MW by Hour')
plt.show()

# Boxplot by month:
fig, ax = plt.subplots(figsize=(10, 8))
sns.boxplot(data=df[["AEP_MW", "month"]], x='month', y='AEP_MW', palette='Blues')
ax.set_title('MW by Month')
plt.show()

# Select variables and dfs:
FEATURES = ['dayofyear', 'hour', 'dayofweek', 'quarter', 'month', 'year']
TARGET = 'AEP_MW'

X_train = train[FEATURES]
y_train = train[TARGET]
X_test = test[FEATURES]
y_test = test[TARGET]

# Fit the model
reg = xgb.XGBRegressor(base_score=0.5, booster='gbtree',    
                       n_estimators=1000,
                       early_stopping_rounds=50,
                       objective='reg:linear',
                       max_depth=3,
                       learning_rate=0.01)
reg.fit(X_train, y_train,
        eval_set=[(X_train, y_train), (X_test, y_test)],
        verbose=100)


fi = pd.DataFrame(data=reg.feature_importances_,
             index=reg.feature_names_in_,
             columns=['importance'])
fi.sort_values('importance').plot(kind='barh', title='Feature Importance')
plt.show()


test['prediction'] = reg.predict(X_test)
df = df.merge(test[['prediction']], how='left', left_index=True, right_index=True)
ax = df[['PJME_MW']].plot(figsize=(15, 5))
df['prediction'].plot(ax=ax, style='.')
plt.legend(['Truth Data', 'Predictions'])
ax.set_title('Raw Dat and Prediction')
plt.show()

ax = df.loc[(df.index > '04-01-2018') & (df.index < '04-08-2018')]['PJME_MW'] \
    .plot(figsize=(15, 5), title='Week Of Data')
df.loc[(df.index > '04-01-2018') & (df.index < '04-08-2018')]['prediction'] \
    .plot(style='.')
plt.legend(['Truth Data','Prediction'])
plt.show()


score = np.sqrt(mean_squared_error(test['PJME_MW'], test['prediction']))
print(f'RMSE Score on Test set: {score:0.2f}')


test['error'] = np.abs(test[TARGET] - test['prediction'])
test['date'] = test.index.date
test.groupby(['date'])['error'].mean().sort_values(ascending=False).head(10)