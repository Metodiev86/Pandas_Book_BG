# 4.	Имате DataFrame с колона 'ProductID' и друг DataFrame, където 'ProductID' е индекс. Използвайте .join() за да ги съедините.

import pandas as pd

# Левият DataFrame с 'ProductID' като колона
df_products = pd.DataFrame({
    'ProductID': [101, 102, 103],
    'Quantity': [5, 10, 3]
})

# Десният DataFrame с 'ProductID' като индекс
df_prices = pd.DataFrame({
    'Price': [9.99, 14.99, 7.99]
}, index=[101, 102, 103])  # индекс = ProductID

# Първо задаваме 'ProductID' като индекс на левия DataFrame
df_products_indexed = df_products.set_index('ProductID')

# Съединяваме по индекс
joined = df_products_indexed.join(df_prices)

# Показваме резултата
print(joined)

# Коментар:
# Използваме .join() за съединяване по индекс — затова предварително правим set_index('ProductID') на левия DataFrame.
#
# В резултата получаваме комбинирана таблица със Quantity и Price, обединени по ProductID.