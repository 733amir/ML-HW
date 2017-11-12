import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# plt.interactive(False)

df = pd.read_excel('data.xlsx', names=['X', 'Y'])
df.plot.scatter(title='All data read from data.xlsx', x='X', y='Y')