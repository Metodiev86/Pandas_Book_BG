# 1.	Запис и четене с data_columns: Създайте голям DataFrame (например, с 10000 реда и няколко колони, включително колона с дати и колона с категорийни данни). Запишете го в HDF5 файл, като укажете две от колоните като data_columns. След това прочетете само редовете, където дадена data_column отговаря на определено условие.

import pandas as pd
import numpy as np

# --- 1. Генериране на данни ---
np.random.seed(42)

dates = pd.date_range(start='2022-01-01', periods=10000, freq='D')
categories = np.random.choice(['A', 'B', 'C'], size=10000)
values1 = np.random.rand(10000) * 100
values2 = np.random.randint(0, 1000, size=10000)

df = pd.DataFrame({
    'Дата': dates,
    'Категория': categories,
    'Стойност1': values1,
    'Стойност2': values2
})

# --- 2. Запис в HDF5 с data_columns ---
df.to_hdf('filtered_data.h5', key='таблица', mode='w',
          format='table', data_columns=['Дата', 'Категория'])

print("Файлът 'filtered_data.h5' е записан успешно.")

# --- 3. Четене само на редовете с Категория = 'B' ---
filtered_df = pd.read_hdf('filtered_data.h5', key='таблица',
                          where="Категория == 'B'")

print("Филтрирани редове (Категория == 'B'):")
print(filtered_df.head())
