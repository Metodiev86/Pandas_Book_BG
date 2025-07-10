# Създайте `PeriodIndex` от индекса на оригиналния DataFrame с честота 'седмица' ('W').

import pandas as pd
import numpy as np

# Примерни данни
dates = pd.to_datetime(['2023-01-01', '2023-01-05', '2023-01-10', '2023-01-15', '2023-01-20'])
durations = pd.to_timedelta(['1 day', '2 days', '0.5 days', '3 days', '1.5 days'])
categories = pd.Categorical(['A', 'B', 'A', 'C', 'B'], categories=['A', 'B', 'C'], ordered=False)

df = pd.DataFrame({
    'Стойност': np.random.randn(5),
    'Продължителност': durations,
    'Категория': categories
}, index=dates)

# Създаване на PeriodIndex с честота 'W' (седмица)
weekly_period_index = df.index.to_period('W')

# Присвояваме новия индекс обратно към DataFrame-а (по избор)
df_weekly = df.copy()
df_weekly.index = weekly_period_index

# Показване на резултата
print("Нов индекс от тип PeriodIndex с честота 'W':")
print(df_weekly.index)
