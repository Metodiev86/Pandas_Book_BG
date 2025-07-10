# 5.	Извършете дясно (right) сливане на два DataFrame-а, като запазите всички редове от десния DataFrame и добавите съответстващите от левия (ако има такива).

import pandas as pd

# Създаваме левия DataFrame с информация за служители
df_employees = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

# Създаваме десния DataFrame с информация за проекти
df_projects = pd.DataFrame({
    'ID': [2, 3, 4],
    'Project': ['Alpha', 'Beta', 'Gamma']
})

# Извършваме дясно сливане по колоната 'ID'
result = pd.merge(df_employees, df_projects, on='ID', how='right')

# Резултат: всички редове от df_projects + съответстващите имена от df_employees (ако има такива)
print(result)

# Какво прави how='right'?
#
# Запазва всички редове от десния DataFrame (df_projects).
#
# Добавя информация от левия DataFrame (df_employees), когато има съвпадения по 'ID'.
#
# При липса на съвпадения – в съответните колони от левия DataFrame стойностите ще бъдат NaN.









