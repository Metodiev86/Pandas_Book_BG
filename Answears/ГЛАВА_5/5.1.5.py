# Изчислете средната стойност за всеки ден от седмицата на колоната 'Стойност'. (Hint: Използвайте `.dt.day_name()` на индекса).

import pandas as pd
import numpy as np

# Създаване на примерния DataFrame
dates = pd.to_datetime(['2023-01-01', '2023-01-05', '2023-01-10', '2023-01-15', '2023-01-20'])
durations = pd.to_timedelta(['1 day', '2 days', '0.5 days', '3 days', '1.5 days'])
categories = pd.Categorical(['A', 'B', 'A', 'C', 'B'], categories=['A', 'B', 'C'], ordered=False)

data = pd.DataFrame({
    'Стойност': np.random.randn(5),
    'Продължителност': durations,
    'Категория': categories
}, index=dates)

# Групиране по ден от седмицата и изчисляване на средната стойност
mean_by_day = data.groupby(data.index.day_name())['Стойност'].mean()

# Показване на резултата
print("Средна стойност на 'Стойност' по ден от седмицата:")
print(mean_by_day)
