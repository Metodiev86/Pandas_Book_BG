# 34.	Даден е Series от datetime обекти. Напишете код, който извлича годината от всяка дата.

import pandas as pd

# Примерен Series с datetime обекти
dates = pd.Series([
    pd.Timestamp('2023-01-01'),
    pd.Timestamp('2024-05-15'),
    pd.Timestamp('2022-11-25'),
    pd.Timestamp('2025-07-30')
])

# Извличане на годината от всяка дата
years = dates.dt.year

print(years)
