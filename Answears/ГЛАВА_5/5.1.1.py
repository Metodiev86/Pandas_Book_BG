# Изведете индекса на DataFrame-а и неговия тип.

import pandas as pd
import numpy as np

# Създаване на примерен DataFrame
dates = pd.to_datetime(['2023-01-01', '2023-01-05', '2023-01-10', '2023-01-15', '2023-01-20'])
durations = pd.to_timedelta(['1 day', '2 days', '0.5 days', '3 days', '1.5 days'])
categories = pd.Categorical(['A', 'B', 'A', 'C', 'B'], categories=['A', 'B', 'C'], ordered=False)
intervals = pd.IntervalIndex.from_tuples([(0, 1), (1, 3), (2, 4), (3, 5), (4, 6)])

# Конструиране на DataFrame с дефинирани индекси
data = pd.DataFrame({
    'Стойност': np.random.randn(5),
    'Продължителност': durations,
    'Категория': categories
}, index=dates)

# Извеждане на индекса
print("Индекс на DataFrame-а:")
print(data.index)

# Извеждане на типа на индекса
print("\nТип на индекса:")
print(type(data.index))
