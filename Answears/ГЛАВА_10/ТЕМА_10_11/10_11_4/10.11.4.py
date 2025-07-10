# 4.	Изследване на компресия: Запишете голям DataFrame във Feather формат, използвайки различни методи на компресия ('uncompressed', 'lz4', 'zstd'). Сравнете размера на получените файлове и времето за запис/четене за всеки метод.

import pandas as pd
import numpy as np
import time
import os

# Създаване на голям DataFrame с няколко милиона реда и различни типове данни
n_rows = 10 ** 6  # брой редове
n_cols = 5  # брой колони
data = {
  'int_column': np.random.randint(1, 100, n_rows),
  'float_column': np.random.random(n_rows),
  'str_column': np.random.choice(['A', 'B', 'C', 'D'], n_rows),
  'date_column': pd.date_range('2020-01-01', periods=n_rows, freq='min'),
  'bool_column': np.random.choice([True, False], n_rows)
}

df = pd.DataFrame(data)


# Функция за измерване на времето за запис и четене
def measure_compression(file_format, compression):
  # Запис
  start_time = time.time()
  df.to_feather(f'data_{file_format}_{compression}.feather', compression=compression)
  write_time = time.time() - start_time

  # Четене
  start_time = time.time()
  df_read = pd.read_feather(f'data_{file_format}_{compression}.feather')
  read_time = time.time() - start_time

  # Връщане на резултати
  file_size = os.path.getsize(f'data_{file_format}_{compression}.feather') / (1024 * 1024)  # в MB
  return write_time, read_time, file_size


# Измерване на времето за запис и четене за всеки формат и компресия
compressions = ['uncompressed', 'lz4', 'zstd']
results = {}

for compression in compressions:
  write_time, read_time, file_size = measure_compression('feather', compression)
  results[compression] = (write_time, read_time, file_size)

# Извеждаме резултатите
for compression, (write_time, read_time, file_size) in results.items():
  print(f"Компресия: {compression}")
  print(f"Размер на файла: {file_size:.2f} MB")
  print(f"Време за запис: {write_time:.4f} сек")
  print(f"Време за четене: {read_time:.4f} сек")
  print("-" * 50)


#=============================================Обяснение:=====================================================
#
# Създаване на DataFrame: Генерираме голям DataFrame с различни типове данни (цифрови, низови, булеви и времеви).
#
# Функция measure_compression:
#
# Записваме DataFrame във Feather файл с различна компресия.
#
# Четем файла обратно и измерваме времето за запис и четене.
#
# Използваме os.path.getsize, за да изчислим размера на файла в MB.
#
# Измерване за различни компресии: Извършваме теста за трите вида компресия: uncompressed, lz4, и zstd.
#
# Извеждане на резултати: Показваме времето за запис и четене, както и размера на файла за всяка компресия.