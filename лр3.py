#task1
import numpy as np
import pandas as pd
import pandas_profiling as pandas_profiling
import matplotlib.pyplot as plt
df = pd.read_csv('2019_nCoV_data.csv', sep=';')
df.describe()
pandas_profiling.ProfileReport(df)

#task2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_profiling as pandas_profiling
df = pd.read_csv('2019_nCoV_data.csv', sep=';')
plt.boxplot([df.Confirmed.values,df.Deaths.values])
plt.show()