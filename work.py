import pandas as pd
import numpy as np

# Generating a datetime index
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')

# Shuffling the datetime index
shuffled_index = np.random.permutation(date_rng)

# Generating random data
data = np.random.randn(len(date_rng))

# Creating pandas series with shuffled datetime index
pandas_series = pd.Series(data, index=shuffled_index)

lst = pandas_series['2023-01-05':'2023-01-06'].dropna().tolist()

print(pandas_series)
print('-------------------------------------------------')
#print(lst)

import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 75000]}

df = pd.DataFrame(data)

# Convert the entire DataFrame into a one-dimensional Series
#series_from_df_flat = df.values.ravel()

# Display the resulting Series
print(pd.Series(df))