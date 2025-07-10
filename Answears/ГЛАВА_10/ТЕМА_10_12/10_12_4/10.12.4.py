# 4.	Четене само на подмножество от колони: Създайте DataFrame с няколко колони и го запишете във Parquet файл. Прочетете файла обратно, като изберете само две от колоните. Измерете времето и сравнете го с четенето на всички колони.

import pandas as pd
import numpy as np
import time

# Намаляваме броя на редовете, за да избегнем Overflow
n_rows = 10000  # 10,000 реда, вместо 1 милион

# Генерираме DataFrame с няколко колони
data = {
    'int_column': np.random.randint(1, 100, n_rows),
    'float_column': np.random.random(n_rows),
    'str_column': np.random.choice(['A', 'B', 'C', 'D'], n_rows),
    'bool_column': np.random.choice([True, False], n_rows),
    'date_column': pd.date_range('2020-01-01', periods=n_rows, freq='D')  # Коригирано с по-малък брой периоди
}

df = pd.DataFrame(data)

# Записваме DataFrame в Parquet
df.to_parquet('data.parquet', engine='pyarrow')

# Четене на всички колони
start_time = time.time()
df_all = pd.read_parquet('data.parquet', engine='pyarrow')
read_all_time = time.time() - start_time

# Четене на само избрани колони (например, 'int_column' и 'float_column')
start_time = time.time()
df_subset = pd.read_parquet('data.parquet', engine='pyarrow', columns=['int_column', 'float_column'])
read_subset_time = time.time() - start_time

# Извеждаме резултатите
print(f"Време за четене на всички колони: {read_all_time:.4f} сек")
print(f"Време за четене на подмножество от колони: {read_subset_time:.4f} сек")

