import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.close("all") # The close() method is used to close a figure window

ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

ts = ts.cumsum()

ts.plot()

plt.show()