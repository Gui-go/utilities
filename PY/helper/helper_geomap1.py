import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



dict = {'lng': [46, 45, 44, 43], 'lat': [56, 57, 58, 59]}
df = pd.DataFrame(dict)

BBox = (df.lng.min(), df.lng.max(), df.lat.min(), df.lat.max())

