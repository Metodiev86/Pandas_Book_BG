#38.	Имате категориален Series със статуси ('Ниско', 'Средно', 'Високо'). Напишете код, който задава ред на категориите: 'Ниско' < 'Средно' < 'Високо'.

import pandas as pd

# Създаване на категориален Series без подредба
statuses = pd.Series(pd.Categorical(['Средно', 'Високо', 'Ниско', 'Средно'],
                                    categories=['Ниско', 'Средно', 'Високо'],
                                    ordered=False))

# Задаване на подредба на категориите
statuses = statuses.cat.as_ordered()

print(statuses)
print("\nКатегориите с подредба:", statuses.cat.categories)
print("Проверка дали категориите са подредени:", statuses.cat.ordered)
