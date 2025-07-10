# 1.	Сравнение на скорост: Създайте голям DataFrame (например, с няколко милиона реда и няколко колони с различни типове данни). Измерете времето за запис и четене на този DataFrame, използвайки CSV, pickle и Feather (с и без компресия 'lz4'). Сравнете резултатите.

import pandas as pd
import numpy as np
import time

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
def measure_time(file_format, compression=None):
    # Запис
    start_time = time.time()
    if file_format == 'csv':
        df.to_csv(f'data_{file_format}.csv', index=False, compression=compression)
    elif file_format == 'pickle':
        df.to_pickle(f'data_{file_format}.pkl')
    elif file_format == 'feather':
        # Компресията трябва да е една от 'uncompressed', 'lz4' или 'zstd' за Feather
        df.to_feather(f'data_{file_format}.feather', compression=compression)
    write_time = time.time() - start_time

    # Четене
    start_time = time.time()
    if file_format == 'csv':
        df_read = pd.read_csv(f'data_{file_format}.csv', compression=compression)
    elif file_format == 'pickle':
        df_read = pd.read_pickle(f'data_{file_format}.pkl')
    elif file_format == 'feather':
        df_read = pd.read_feather(f'data_{file_format}.feather')
    read_time = time.time() - start_time

    return write_time, read_time


# Измерване на времето за запис и четене за всеки формат
formats = ['csv', 'pickle', 'feather']
compressions = [None, 'zstd']  # За Feather, само тези са поддържани

# Резултати за запис и четене
results = {}

for file_format in formats:
    for compression in compressions:
        write_time, read_time = measure_time(file_format, compression)
        results[f'{file_format}_{compression if compression else "no_compression"}'] = (write_time, read_time)

# Извеждаме резултатите
for key, value in results.items():
    print(f"Формат: {key}, Запис: {value[0]:.4f} сек, Четене: {value[1]:.4f} сек")


