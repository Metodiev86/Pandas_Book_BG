# 2.	Четене на подмножество от колони: Създайте DataFrame с няколко колони и го запишете във ORC файл. Прочетете го отново, като изберете само две от колоните.

import pandas as pd
import numpy as np

# Създаване на DataFrame с няколко колони
n_rows = 1000  # 1000 реда за теста
data = {
    'int_column': np.random.randint(1, 100, n_rows),
    'float_column': np.random.random(n_rows),
    'str_column': np.random.choice(['A', 'B', 'C', 'D'], n_rows),
    'bool_column': np.random.choice([True, False], n_rows),
    'date_column': pd.date_range('2020-01-01', periods=n_rows, freq='D')
}
df = pd.DataFrame(data)

# Записване на DataFrame в ORC файл с pyarrow
df.to_orc('data.orc')

# Четене на ORC файла, като избираме само две колони
df_read = pd.read_orc('data.orc', columns=['int_column', 'str_column'])

# Извеждаме първите няколко реда на прочетените данни
print("Четене на подмножество от колони:")
print(df_read.head())

# Сравняваме дали прочетените данни отново съдържат само избраните колони
print("\nПроверка на колоните:", df_read.columns.tolist())
