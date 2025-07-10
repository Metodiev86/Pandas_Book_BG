# Изведете стойността на реда с етикет '2023-01-15', използвайки `.loc`.

import pandas as pd
import numpy as np

# 1. Дефиниране на входните данни
dates = pd.to_datetime(['2023-01-01', '2023-01-05', '2023-01-10', '2023-01-15', '2023-01-20'])
durations = pd.to_timedelta(['1 day', '2 days', '0.5 days', '3 days', '1.5 days'])
categories = pd.Categorical(['A', 'B', 'A', 'C', 'B'], categories=['A', 'B', 'C'], ordered=False)

# 2. Създаване на DataFrame с индекс дати
data = pd.DataFrame({
    'Стойност': np.random.randn(5),
    'Продължителност': durations,
    'Категория': categories
}, index=dates)

# 3. Извеждане на целия DataFrame
print("Оригинален DataFrame:")
print(data)

# 4. Извличане на реда с дата '2023-01-15' чрез .loc
row_value = data.loc['2023-01-15']

# 5. Показване на извлечения ред
print("\nРед с етикет '2023-01-15':")
print(row_value)
