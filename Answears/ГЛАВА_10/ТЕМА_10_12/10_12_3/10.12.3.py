# 3.	Изследване на компресия: Запишете голям DataFrame във Parquet формат, използвайки различни методи на компресия ('snappy', 'gzip', None). Сравнете размера на получените файлове и времето за запис/четене.

import pandas as pd
import numpy as np
import time
import os

# Създаване на голям DataFrame с няколко милиона реда и различни типове данни
n_rows = 10 ** 6  # брой редове
data = {
  'int_column': np.random.randint(1, 100, n_rows),
  'float_column': np.random.random(n_rows),
  'str_column': np.random.choice(['A', 'B', 'C', 'D'], n_rows),
  'bool_column': np.random.choice([True, False], n_rows),
  'date_column': pd.date_range('2020-01-01', periods=n_rows, freq='min')
}
df = pd.DataFrame(data)


# Функция за измерване на времето за запис и четене
def measure_compression(compression):
  # Запис
  start_time = time.time()
  df.to_parquet(f'data_{compression}.parquet', engine='pyarrow', compression=compression)
  write_time = time.time() - start_time

  # Четене
  start_time = time.time()
  df_read = pd.read_parquet(f'data_{compression}.parquet', engine='pyarrow')
  read_time = time.time() - start_time

  # Връщане на резултати
  file_size = os.path.getsize(f'data_{compression}.parquet') / (1024 * 1024)  # в MB
  return write_time, read_time, file_size


# Измерване на времето за запис и четене за всеки формат
compressions = ['snappy', 'gzip', None]
results = {}

for compression in compressions:
  write_time, read_time, file_size = measure_compression(compression)
  results[compression] = (write_time, read_time, file_size)

# Извеждаме резултатите
for compression, (write_time, read_time, file_size) in results.items():
  print(f"Компресия: {compression if compression else 'без компресия'}")
  print(f"Размер на файла: {file_size:.2f} MB")
  print(f"Време за запис: {write_time:.4f} сек")
  print(f"Време за четене: {read_time:.4f} сек")
  print("-" * 50)
