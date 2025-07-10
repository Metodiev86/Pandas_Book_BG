# 6.	Извършете външно (outer) сливане на два DataFrame-а и покажете как да идентифицирате редовете, които съществуват само в единия от оригиналните DataFrame-и, използвайки параметъра indicator=True.

import pandas as pd

# Създаваме първия DataFrame – клиенти от система 1
df_customers_sys1 = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

# Създаваме втория DataFrame – клиенти от система 2
df_customers_sys2 = pd.DataFrame({
    'CustomerID': [2, 3, 4],
    'Name': ['Bob', 'Charlie', 'David']
})

# Извършваме външно (outer) сливане и включваме индикатор
result = pd.merge(df_customers_sys1, df_customers_sys2, on='CustomerID', how='outer', suffixes=('_sys1', '_sys2'), indicator=True)

# Резултатът съдържа колоната '_merge', която показва произхода на всеки ред:
# - 'left_only': редът е само в df_customers_sys1
# - 'right_only': редът е само в df_customers_sys2
# - 'both': редът присъства и в двата DataFrame-а
print(result)

# Коментари:
# indicator=True добавя колона _merge, която ясно показва откъде произлиза всяка комбинация от редове.
#
# Това е изключително полезно за анализ на разлики, интеграция на данни от различни източници, и откриване на липсващи записи.
