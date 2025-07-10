# 29.	Даден е Series с времеви разлики във формат 'HH:MM:SS'. Напишете код, който го преобразува в Timedelta тип.

import pandas as pd

# Примерен Series с времеви разлики във формат 'HH:MM:SS'
time_diffs = pd.Series(['01:30:00', '00:45:15', '02:00:00', '00:10:30'])

# Преобразуване в тип Timedelta
time_deltas = pd.to_timedelta(time_diffs)

print(time_deltas)
print("\nТип на елементите:", time_deltas.dtype)
