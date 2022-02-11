import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# see the pre-defined styles provided.
plt.style.available
# use the 'seaborn-colorblind' style
plt.style.use('seaborn-colorblind')

np.random.seed(123)
df = pd.DataFrame({'A': np.random.randn(365).cumsum(0),
                   'B': np.random.randn(365).cumsum(0) + 20,
                   'C': np.random.randn(365).cumsum(0) - 20},
                  index=pd.date_range('1/1/2017', periods=365))
df.head()
df.plot()
plt.show()

df.plot('A', 'B', kind='scatter')
plt.show()

# create a scatter plot of columns 'A' and 'C', with changing color (c) and size (s) based on column 'B'
df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
plt.show()

ax = df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
ax.set_aspect('equal')
plt.show()

df.plot.box()
plt.show()

df.plot.hist(alpha=0.7)
plt.show()

# df.plot.kde()
# plt.show()
