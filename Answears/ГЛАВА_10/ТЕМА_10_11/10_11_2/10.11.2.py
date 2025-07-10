# 2.	Крос-езиков обмен: Създайте DataFrame в Pandas и го запишете във Feather формат. След това (ако имате инсталиран R и пакета feather), прочетете този файл в R и покажете първите няколко реда. Създайте DataFrame в R и го запишете във Feather формат. Прочетете го обратно в Pandas и покажете първите няколко реда.

import pandas as pd
import numpy as np

# Създаване на DataFrame в Pandas
data = {
    'int_column': np.random.randint(1, 100, 10),
    'float_column': np.random.random(10),
    'str_column': np.random.choice(['A', 'B', 'C', 'D'], 10),
    'bool_column': np.random.choice([True, False], 10)
}
df = pd.DataFrame(data)

# Запис в Feather формат
df.to_feather('data.feather')
