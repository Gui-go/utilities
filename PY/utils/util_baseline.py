

import pandas as pd
from sklearn.datasets import load_boston
from sklearn import (model_selection, preprocessing)

#
b = load_boston()
bos_X = pd.DataFrame(b.data, columns=b.feature_names)
bos_y = b.target

#
bos_X_train, bos_X_test, bos_y_train, bos_y_test = model_selection. \
    train_test_split(bos_X, bos_y, test_size=0.3, random_state=42)

#
bos_sX = preprocessing.StandardScaler().fit_transform(bos_X)

#
bos_sX_train, bos_sX_test, bos_sy_train, bos_sy_test = model_selection. \
    train_test_split(bos_sX, bos_y, test_size=0.3, random_state=42)


from sklearn.dummy import DummyRegressor
dr = DummyRegressor()
dr.fit(bos_X_train, bos_y_train)
dr.score(bos_X_test, bos_y_test)

