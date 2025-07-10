# Създайте `TimedeltaIndex` от колоната 'Продължителност' на DataFrame-а. Изведете общата продължителност (сумата на всички елементи в индекса).

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

# Създаване на TimedeltaIndex от колоната 'Продължителност'
timedelta_index = pd.TimedeltaIndex(df['Продължителност'])

# Изчисляване на общата продължителност
total_duration = timedelta_index.sum()

# Резултат
print("TimedeltaIndex:\n", timedelta_index)
print("\nОбща продължителност:", total_duration)
