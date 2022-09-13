import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.close("all") # The close() method is used to close a figure window

n=666
k_ma=60
# df = pd.DataFrame(np.random.randn(n), columns=["ts_data"], index=pd.date_range("1/1/2000", periods=n))
df = pd.DataFrame()
df["date"] = pd.date_range("1/1/2000", periods=n)
df["vl"] = np.random.randn(n)
df["vl"] = df["vl"].cumsum()
df['sma_vl'] = df['vl'].rolling(k_ma).mean() # simple moving average
df['ema_vl'] = df['vl'].ewm(span=3).mean() # Exponential moving average

# Simple check plot:
df["vl"].plot()
df["sma_vl"].plot()
df['ema_vl'].plot()
plt.show()







 