# 3.	Четене на подмножество от колони: Създайте DataFrame с няколко колони и го запишете във Feather файл. След това прочетете файла обратно, като изберете само две от колоните.

import pandas as pd
import numpy as np

# Създаване на DataFrame с няколко колони
data = {
    'int_column': np.random.randint(1, 100, 10),
    'float_column': np.random.random(10),
    'str_column': np.random.choice(['A', 'B', 'C', 'D'], 10),
    'bool_column': np.random.choice([True, False], 10)
}
df = pd.DataFrame(data)

# Запис в Feather файл
df.to_feather('data.feather')

# Четене на Feather файл с избрани колони (например 'int_column' и 'str_column')
df_read = pd.read_feather('data.feather')[['int_column', 'str_column']]

# Показване на първите няколко реда от избраните колони
print(df_read.head())
