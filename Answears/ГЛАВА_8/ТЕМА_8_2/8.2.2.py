#Имате два DataFrame-а: df_orders с колони ('Номер на поръчка', 'ID на клиент') и df_clients с колони ('CustomerID', 'Име на клиент'). Слейте ги, използвайки съответните колони за ID на клиент като ключове.

import pandas as pd

# DataFrame с поръчки
df_orders = pd.DataFrame({
    'Номер на поръчка': [1001, 1002, 1003],
    'ID на клиент': [1, 2, 3]
})

# DataFrame с клиенти
df_clients = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Име на клиент': ['Алиса', 'Боб', 'Чарли']
})

# Сливане по различноименни колони – използваме left_on и right_on
df_result = pd.merge(df_orders, df_clients,
                       left_on='ID на клиент',
                       right_on='CustomerID')

print(df_result)

# Забележки:
#
# Използваме left_on и right_on, защото ключовите колони имат различни имена в двата DataFrame-а.
#
# Резултатът ще съдържа всички колони от двата DataFrame-а, включително и двете ID колони (може да премахнете едната с drop() при нужда).