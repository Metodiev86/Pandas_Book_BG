# Изведете уникалните категории от колоната 'Категория'.

import pandas as pd
import numpy as np

# Създаване на примерен DataFrame
dates = pd.to_datetime(['2023-01-01', '2023-01-05', '2023-01-10', '2023-01-15', '2023-01-20'])
durations = pd.to_timedelta(['1 day', '2 days', '0.5 days', '3 days', '1.5 days'])
categories = pd.Categorical(['A', 'B', 'A', 'C', 'B'], categories=['A', 'B', 'C'], ordered=False)

data = pd.DataFrame({
    'Стойност': np.random.randn(5),
    'Продължителност': durations,
    'Категория': categories
}, index=dates)

# Извеждане на уникалните категории от колоната 'Категория'
unique_categories = data['Категория'].unique()

print("Уникалните категории са:", unique_categories)


# Ако искаш уникалните стойности като списък от низове, можеш да направиш:
print("Уникалните категории като списък от низове са:", data['Категория'].dropna().unique().tolist())
