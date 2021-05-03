# importing pandas and numpylibraries
import pandas as pd
import numpy as np
  
# creating and initializing a nested list
values_list = [[1.5, 2.5, 10.0], [2.0, 4.5, 5.0], [2.5, 5.2, 8.0],
               [4.5, 5.8, 4.8], [4.0, 6.3, 70], [4.1, 6.4, 9.0],
               [5.1, 2.3, 11.1]]
  
# creating a pandas dataframe
df = pd.DataFrame(values_list, columns=['Field_1', 'Field_2', 'Field_3'],
                  index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
  
  
# Apply function numpy.square() to square 
# the values of 2 rows only i.e. with row
# index name 'b' and 'f' only
df = df.apply(lambda x: np.square(x) if x.name in ['b', 'f'] else x, axis=1)
  
# Applying lambda function to find product of 3 columns
# i.e 'Field_1', 'Field_2' and 'Field_3'
df = df.assign(Product=lambda x: (x['Field_1'] * x['Field_2'] * x['Field_3']))
  
  
# printing dataframe
df