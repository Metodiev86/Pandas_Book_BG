# 1.	Запис и четене с pyarrow: Създайте DataFrame и го запишете във ORC файл. След това го прочетете обратно, като използвате pd.read_orc(). Уверете се, че данните са идентични.


import pandas as pd
import numpy as np

# Създаване на DataFrame
n_rows = 1000  # 1000 реда за теста
data = {
    'int_column': np.random.randint(1, 100, n_rows),
    'float_column': np.random.random(n_rows),
    'str_column': np.random.choice(['A', 'B', 'C', 'D'], n_rows),
    'bool_column': np.random.choice([True, False], n_rows),
    'date_column': pd.date_range('2020-01-01', periods=n_rows, freq='D')
}

df = pd.DataFrame(data)
# Премахваме времевата зона и конвертираме времето в стандартен формат
df['date_column'] = df['date_column'].dt.tz_localize(None).dt.strftime('%Y-%m-%d %H:%M:%S')

# Записване на DataFrame във ORC файл с pyarrow
df.to_orc('data.orc')

# Четене на ORC файла обратно в DataFrame
df_read = pd.read_orc('data.orc')

# Проверка дали данните са идентични
print("Данни след запис и четене:")
print(df_read.head())

# Сравняваме дали оригиналният и прочетеният DataFrame са идентични
print("\nДанни са идентични: ", df.equals(df_read))

