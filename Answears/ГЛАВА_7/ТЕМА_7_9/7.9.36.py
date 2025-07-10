#36.	Даден е Series от datetime обекти. Напишете код, който изчислява разликата в дни между всяка дата и днешната дата.

import pandas as pd

# Примерен Series от datetime обекти
dates = pd.to_datetime([
    '2023-01-01', '2023-05-15', '2023-11-25', '2023-07-30'
])

series = pd.Series(dates)

# Днешната дата
today = pd.to_datetime('today')

# Изчисляване на разликата в дни
difference_in_days = (today - series).dt.days

print(difference_in_days)
