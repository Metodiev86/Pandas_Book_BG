# Създайте нов DataFrame, съдържащ само редовете от оригиналния DataFrame, чиито дати са след 2023-01-07.

import pandas as pd
import numpy as np

# Примерни данни
dates = pd.to_datetime(['2023-01-01', '2023-01-05', '2023-01-10', '2023-01-15', '2023-01-20'])
durations = pd.to_timedelta(['1 day', '2 days', '0.5 days', '3 days', '1.5 days'])
categories = pd.Categorical(['A', 'B', 'A', 'C', 'B'], categories=['A', 'B', 'C'], ordered=False)

# Създаване на оригиналния DataFrame
data = pd.DataFrame({
    'Стойност': np.random.randn(5),
    'Продължителност': durations,
    'Категория': categories
}, index=dates)

# === ФИЛТРИРАНЕ НА РЕДОВЕТЕ С ДАТИ СЛЕД 2023-01-07 ===

# Създаваме нов DataFrame, който съдържа само редове с дати след 2023-01-07
filtered_data = data[data.index > pd.to_datetime("2023-01-07")]

# Извеждаме резултата
print("Редове с дати след 2023-01-07:")
print(filtered_data)
