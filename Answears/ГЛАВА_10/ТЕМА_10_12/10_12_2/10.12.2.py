# 2.	Партициониране и четене на партиции: Създайте DataFrame с колона за дата. Партиционирайте го по година и месец при запис във Parquet формат. След това прочетете само данните за определен месец от определена година, като укажете пътя към съответната партиция. Прочетете и всички данни наведнъж.

import pandas as pd
import numpy as np
import os

# Създаване на DataFrame с колона за дата
n_rows = 10000
data = {
    'date_column': pd.date_range('2020-01-01', periods=n_rows, freq='D'),
    'int_column': np.random.randint(1, 100, n_rows),
    'float_column': np.random.random(n_rows),
    'str_column': np.random.choice(['A', 'B', 'C', 'D'], n_rows)
}

df = pd.DataFrame(data)

# Извличане на годината и месеца от колоната за дата
df['year'] = df['date_column'].dt.year
df['month'] = df['date_column'].dt.month

# Път за запис на партиционираните данни
output_dir = 'data_partitions/'

# Запис в Parquet с партиции по година и месец
df.to_parquet(output_dir, engine='pyarrow', partition_cols=['year', 'month'])

# Проверка за наличието на партиции
print(f"Партиции в директорията '{output_dir}':")
print(os.listdir(output_dir))

# Четене на данни за конкретен месец (например, март 2021)
specific_month_path = os.path.join(output_dir, 'year=2021', 'month=3')
df_specific_month = pd.read_parquet(specific_month_path)

# Показване на първите няколко реда от избраната партиция
print(f"\nДанни за март 2021:")
print(df_specific_month.head())

# Четене на всички данни наведнъж
df_all_data = pd.read_parquet(output_dir)

# Показване на първите няколко реда от всички данни
print(f"\nВсички данни:")
print(df_all_data.head())
