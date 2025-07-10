# 3.	Изследване на компресия: Запишете голям DataFrame във ORC формат, използвайки различни методи на компресия ('snappy', 'gzip', None). Сравнете размера на получените файлове. (Може да изисквате измерване на времето за запис/четене, ако е приложимо).

import pandas as pd
import numpy as np
import time
import os

# Създаване на голям DataFrame
n_rows = 10 ** 4  # 1 милион реда за теста
data = {
  'int_column': np.random.randint(1, 100, n_rows),
  'float_column': np.random.random(n_rows),
  'str_column': np.random.choice(['A', 'B', 'C', 'D'], n_rows),
  'bool_column': np.random.choice([True, False], n_rows),
  'date_column': pd.date_range('2020-01-01', periods=n_rows, freq='D')
}
df = pd.DataFrame(data)


# Функция за измерване на време за запис и четене с различна компресия
def measure_compression(file_name, compression):
  start_time = time.time()

  # Записване във ORC файл с определена компресия
  df.to_orc(file_name, compression=compression)
  write_time = time.time() - start_time

  # Четене на ORC файла
  start_time = time.time()
  df_read = pd.read_orc(file_name)
  read_time = time.time() - start_time

  # Връщаме резултати
  file_size = os.path.getsize(file_name)  # Размер на файла
  return file_size, write_time, read_time


# Метод на компресия и имена на файлове
compressions = ['snappy', 'gzip', None]
file_names = ['data_snappy.orc', 'data_gzip.orc', 'data_no_compression.orc']

# Сравнение на файловете
results = {}
for compression, file_name in zip(compressions, file_names):
  print(f"Записване и четене с компресия: {compression if compression else 'None'}")
  file_size, write_time, read_time = measure_compression(file_name, compression)

  results[compression] = {
    'file_size': file_size,
    'write_time': write_time,
    'read_time': read_time
  }

  # Изтриване на файла след измерванията
  os.remove(file_name)

# Извеждаме резултатите
for compression, result in results.items():
  print(f"\nКомпресия: {compression if compression else 'None'}")
  print(f"Размер на файла: {result['file_size'] / 1024 / 1024:.2f} MB")
  print(f"Време за запис: {result['write_time']:.4f} сек")
  print(f"Време за четене: {result['read_time']:.4f} сек")
