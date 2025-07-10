# 1.	Запис и четене с различни engine-и: Създайте DataFrame и го запишете във Parquet файл, използвайки както 'pyarrow', така и 'fastparquet' engine (ако е инсталиран). След това прочетете и двата файла и се уверете, че данните са еднакви. Забелязвате ли разлики в скоростта или размера на файла?

import pandas as pd
import numpy as np
import time
import os

# Създаване на DataFrame
data = {
    'int_column': np.random.randint(1, 100, 1000),
    'float_column': np.random.random(1000),
    'str_column': np.random.choice(['A', 'B', 'C', 'D'], 1000),
    'bool_column': np.random.choice([True, False], 1000)
}
df = pd.DataFrame(data)

# Запис в Parquet файл с engine 'pyarrow'
start_time = time.time()
df.to_parquet('data_pyarrow.parquet', engine='pyarrow')
pyarrow_write_time = time.time() - start_time

# Запис в Parquet файл с engine 'fastparquet'
start_time = time.time()
df.to_parquet('data_fastparquet.parquet', engine='fastparquet')
fastparquet_write_time = time.time() - start_time

# Четене на Parquet файл с engine 'pyarrow'
start_time = time.time()
df_pyarrow = pd.read_parquet('data_pyarrow.parquet', engine='pyarrow')
pyarrow_read_time = time.time() - start_time

# Четене на Parquet файл с engine 'fastparquet'
start_time = time.time()
df_fastparquet = pd.read_parquet('data_fastparquet.parquet', engine='fastparquet')
fastparquet_read_time = time.time() - start_time

# Проверка дали данните са същите
data_equal = df.equals(df_pyarrow) and df.equals(df_fastparquet)

# Размер на файловете
pyarrow_size = os.path.getsize('data_pyarrow.parquet') / (1024 * 1024)  # в MB
fastparquet_size = os.path.getsize('data_fastparquet.parquet') / (1024 * 1024)  # в MB

# Извеждаме резултатите
print(f"Време за запис с pyarrow: {pyarrow_write_time:.4f} сек")
print(f"Време за запис с fastparquet: {fastparquet_write_time:.4f} сек")
print(f"Време за четене с pyarrow: {pyarrow_read_time:.4f} сек")
print(f"Време за четене с fastparquet: {fastparquet_read_time:.4f} сек")
print(f"Размер на файла с pyarrow: {pyarrow_size:.2f} MB")
print(f"Размер на файла с fastparquet: {fastparquet_size:.2f} MB")
print(f"Данните са еднакви: {data_equal}")
