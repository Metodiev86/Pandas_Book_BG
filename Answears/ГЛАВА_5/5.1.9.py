# Създайте `IntervalIndex` от списъка `[(0, 2), (1.5, 3.5)]`. Проверете кои от стойностите `[0.5, 2.5, 4.5]` се съдържат във всеки от интервалите на този нов индекс.

import pandas as pd

# Създаване на IntervalIndex
intervals = [(0, 2), (1.5, 3.5)]
interval_index = pd.IntervalIndex.from_tuples(intervals)

# Проверка кои стойности се съдържат във всеки от интервалите
values_to_check = [0.5, 2.5, 4.5]
containment_check = [interval_index.contains(value) for value in values_to_check]

print(interval_index)
print(containment_check)
