import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('FILE_ADDRESS', names=['Index', 'X', 'Y', 'Z', 'Class'])
df = df[['Index', 'X']]

df['Moving_Average_1'] = df['X'].rolling(window=10).mean()
df['Moving_Average_2'] = df['X'].rolling(window=100).mean()
df['Moving_Average_3'] = df['X'].rolling(window=1000).mean()

df.plot.line(x='Index', y=['X','Moving_Average_1','Moving_Average_2','Moving_Average_3'])
plt.show()