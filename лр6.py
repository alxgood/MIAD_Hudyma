import pandas as pd
import statsmodels.formula.api as sm
df = pd.DataFrame({"X": [0,5,10,15,20,25], "Y": [21,39,51,63,70,90]})
result = sm.ols(formula="Y ~ X", data=df).fit()
print(result.params)
sns.regplot(df.X, df.Y, order=1, ci=None, scatter_kws={'color':'r', 's':9})

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import seaborn as sns
from sklearn.preprocessing import scale
import sklearn.linear_model as skl_lm
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
import statsmodels.formula.api as smf
# %matplotlib inline
df = pd.read_csv('Advertising.csv', usecols=[1,2,3,4])
df.head()

df.info()

sns.pairplot(df);

fig, axs = plt.subplots(1, 3, sharey=True)
df.plot(kind='scatter', x='TV', y='sales', ax=axs[0], figsize=(16, 8))
df.plot(kind='scatter', x='radio', y='sales', color='red', ax=axs[1])
df.plot(kind='scatter', x='newspaper', y='sales', color='green', ax=axs[2])

df.corr()

lm = smf.ols(formula='sales~TV', data=df).fit()
print(lm.params)

X_new = pd.DataFrame({'TV': [50]})
print(X_new.head())
print(lm.predict(X_new))