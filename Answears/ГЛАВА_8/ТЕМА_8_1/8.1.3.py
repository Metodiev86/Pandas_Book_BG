# 3.	Дадени са три Series обекта. Напишете код, който ги конкатенира по редове, като игнорира оригиналните им индекси и създава нов, последователен индекс.

import pandas as pd

# Примерни Series обекти
series1 = pd.Series([1, 2, 3])
series2 = pd.Series([4, 5, 6])
series3 = pd.Series([7, 8, 9])

# Конкатениране на трите Series по редове и игнориране на оригиналните индекси
result = pd.concat([series1, series2, series3], ignore_index=True)

print(result)
