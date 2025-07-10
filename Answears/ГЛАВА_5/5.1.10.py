# За оригиналния DataFrame, създайте нов `MultiIndex`, използвайки оригиналния `DatetimeIndex` и колоната 'Категория' като нива. Преобразувайте DataFrame-а към този нов `MultiIndex`.

import pandas as pd
import numpy as np

# Оригинален DataFrame
dates = pd.to_datetime(['2023-01-01', '2023-01-05', '2023-01-10', '2023-01-15', '2023-01-20'])
durations = pd.to_timedelta(['1 day', '2 days', '0.5 days', '3 days', '1.5 days'])
categories = pd.Categorical(['A', 'B', 'A', 'C', 'B'], categories=['A', 'B', 'C'], ordered=False)
intervals = pd.IntervalIndex.from_tuples([(0, 1), (1, 3), (2, 4), (3, 5), (4, 6)])

data = pd.DataFrame({
    'Стойност': np.random.randn(5),
    'Продължителност': durations,
    'Категория': categories
}, index=dates)

print("Оригинален DataFrame:")
print(data)
print("-" * 30)

# Създаване на нов MultiIndex
# Ниво 1: Оригиналният DatetimeIndex (индексът на DataFrame-а)
# Ниво 2: Стойностите от колоната 'Категория'
new_index_levels = [data.index, data['Категория']]
new_multi_index = pd.MultiIndex.from_arrays(new_index_levels, names=['Дата', 'Категория'])

# Преобразуване на DataFrame-а към новия MultiIndex
# Първо, трябва да изтрием колоната 'Категория', тъй като тя става част от индекса
df_reindexed = data.drop(columns=['Категория'])
df_reindexed.index = new_multi_index

print("\nDataFrame с новия MultiIndex:")
print(df_reindexed)
print("\nИнформация за новия индекс:")
print(df_reindexed.index)