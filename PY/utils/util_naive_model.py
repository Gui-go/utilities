import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""
Naive = 
baseline = 
"""

plt.close("all") # The close() method is used to close a figure window

n=666
h=120

# df = pd.DataFrame(np.random.randn(n), columns=["ts_data"], index=pd.date_range("1/1/2000", periods=n))
df = pd.DataFrame()
df["date"] = pd.date_range("1/1/2000", periods=n)
df["vl"] = np.random.randn(n)
df["vl"] = df["vl"].cumsum()

# Simple check plot:
df["vl"].plot()
plt.show()

train = df[:-h]
test = df[-h:]

df_pred = pd.DataFrame()
df_pred['date'] = test.date
df_pred['pred_historicalmean'] = np.mean(train.vl) # Historical mean
df_pred['pred_naivemodel'] = train.vl[len(train.vl)-h:].values # Naive pred
df_pred['pred_lastvl'] = train.vl[-1:].values[0] # Last value
df_pred

def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

mape(test.vl, df_pred.pred_historicalmean)
mape(test.vl, df_pred.pred_naivemodel)
mape(test.vl, df_pred.pred_lastvl)

fig, ax = plt.subplots()
ax.plot(train.date, train.vl, 'k', label='Train')
ax.plot(test.date, test.vl, 'b', label='Test')
ax.plot(df_pred.date, df_pred.pred_historicalmean, 'r-', label='historical mean')
ax.plot(df_pred.date, df_pred.pred_naivemodel, 'r-', label='naive preditction')
ax.plot(df_pred.date, df_pred.pred_lastvl, 'r-', label='last value')
ax.set_xlabel('date')
ax.set_ylabel('vl')
ax.legend(loc=2) # Legend of colors and variables
plt.show()

