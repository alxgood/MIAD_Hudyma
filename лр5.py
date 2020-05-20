# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import pandas_profiling as pandas_profiling
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sb
df = pd.read_csv('data.csv', sep=',')
df[:10]

corrP = df.corr(method ='pearson') 
corrP

corr10 = corrP.iloc[:10, :10]
sb.heatmap(corr10,xticklabels=corr10.columns,yticklabels=corr10.columns,cmap='RdBu_r',annot=True)
plt.show()

corrS = df.corr(method ='spearman') 
corrS

corr10s = corrS.iloc[:10, :10]
sb.heatmap(corr10s,xticklabels=corr10s.columns,yticklabels=corr10s.columns,cmap='RdBu_r',annot=True)
plt.show()