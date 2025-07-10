# 5.	Работа с индекс: Създайте DataFrame с нетривиален индекс (например, MultiIndex). Запишете го във Parquet файл веднъж със запазване на индекса (по подразбиране) и веднъж без (index=False). Прочетете обратно и двата файла и наблюдавайте как се обработва индексът.

import pandas as pd
import numpy as np

# Създаване на MultiIndex
arrays = [
    ['A', 'A', 'A', 'B', 'B', 'B'],  # първи слой
    [1, 2, 3, 1, 2, 3]              # втори слой
]
index = pd.MultiIndex.from_arrays(arrays, names=('letter', 'number'))

# Създаване на DataFrame с MultiIndex
n_rows = 6
data = {
    'value1': np.random.randint(1, 100, n_rows),
    'value2': np.random.random(n_rows)
}
df = pd.DataFrame(data, index=index)

# Записване на DataFrame във Parquet файл със запазване на индекса
df.to_parquet('data_with_index.parquet', engine='pyarrow')

# Записване на DataFrame във Parquet файл без запазване на индекса
df.to_parquet('data_without_index.parquet', engine='pyarrow', index=False)

# Четене на файла с индекс
df_with_index = pd.read_parquet('data_with_index.parquet', engine='pyarrow')

# Четене на файла без индекс
df_without_index = pd.read_parquet('data_without_index.parquet', engine='pyarrow')

# Извеждаме резултатите
print("Четене на Parquet файл със запазване на индекса:")
print(df_with_index)
print("\nЧетене на Parquet файл без запазване на индекса:")
print(df_without_index)
