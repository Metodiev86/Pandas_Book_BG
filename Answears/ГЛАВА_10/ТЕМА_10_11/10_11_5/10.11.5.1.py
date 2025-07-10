# 5.	Работа с облачно съхранение (симулирано): Ако имате достъп до облачно хранилище (например, AWS S3), опитайте да прочетете и запишете Feather файл, използвайки storage_options. Ако не, можете да симулирате това, като използвате локални файлове и се фокусирате върху синтаксиса на storage_options (например, за HTTP/HTTPS URL).

# Пример за работа с storage_options с локални файлове (симулация):

import pandas as pd
import numpy as np

# Създаване на DataFrame
data = {
    'int_column': np.random.randint(1, 100, 10),
    'float_column': np.random.random(10),
    'str_column': np.random.choice(['A', 'B', 'C', 'D'], 10),
    'bool_column': np.random.choice([True, False], 10)
}
df = pd.DataFrame(data)

# Запис в Feather файл с "storage_options"
file_path = 'data_simulated.feather'
df.to_feather(file_path)

# Четене от Feather файл с "storage_options" (симулираме чрез локален файл)
df_read = pd.read_feather(file_path)

# Показване на първите няколко реда
print(df_read.head())
