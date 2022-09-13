from operator import concat
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pmdarima.arima import auto_arima

plt.close("all") # The close() method is used to close a figure window

n=666
h=60
# df = pd.DataFrame(np.random.randn(n), columns=["ts_data"], index=pd.date_range("1/1/2000", periods=n))
df = pd.DataFrame()
df["date"] = pd.date_range("1/1/2000", periods=n)
df["vl"] = np.random.randn(n)
df["vl"] = df["vl"].cumsum()

# Simple check plot:
# df["vl"].plot()
# plt.show()

train = df[:-h]
test = df[-h:]


model = auto_arima(train.vl, start_p=0, start_q=0)
model.summary()
model.order
# model.plot_diagnostics()
# plt.show()

model.fit(train.vl)
lpred = model.predict(steps=h).tolist()
df["pred_arima"] = [None] * n
df.loc[n-h:n-h+len(lpred)-1, 'pred_arima'] = lpred



fig, ax = plt.subplots()
ax.plot(train.date, train.vl, 'k', label='Train')
ax.plot(test.date, test.vl, 'b', label='Test')
ax.plot(df.date, df.pred_arima, 'r-', label='arima')
ax.set_xlabel('date')
ax.set_ylabel('vl')
ax.legend(loc=2) # Legend of colors and variables
plt.show()

# ----------------------------------------------------------



model.predict(steps=h).tolist()