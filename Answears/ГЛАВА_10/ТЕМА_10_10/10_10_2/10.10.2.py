# 2.	Използване на различни формати: Създайте малък DataFrame и го запишете в два различни HDF5 файла, веднъж с format='table' и веднъж с format='fixed'. След това прочетете и двата файла и сравнете времето за четене (можете да използвате %timeit в Jupyter Notebook или time модула в Python).

import pandas as pd
import numpy as np
import time

# 1. Създаваме примерен DataFrame
df = pd.DataFrame({
    'Име': ['Анна', 'Боби', 'Соня', 'Иво', 'Диди'],
    'Град': ['София', 'Пловдив', 'Варна', 'Русе', 'Бургас'],
    'Възраст': [28, 34, 22, 41, 30]
})

# 2. Записване във fixed формат (по подразбиране)
df.to_hdf('fixed_format.h5', key='df', mode='w', format='fixed')

# 3. Записване в table формат
df.to_hdf('table_format.h5', key='df', mode='w', format='table')

# 4. Измерване на време за четене
start_fixed = time.time()
df_fixed = pd.read_hdf('fixed_format.h5', key='df')
end_fixed = time.time()

start_table = time.time()
df_table = pd.read_hdf('table_format.h5', key='df')
end_table = time.time()

# 5. Резултати
print("Време за четене от fixed формат: {:.6f} секунди".format(end_fixed - start_fixed))
print("Време за четене от table формат: {:.6f} секунди".format(end_table - start_table))

# Проверка дали данните са еднакви
print("\nСравнение на съдържанието:", df_fixed.equals(df_table))
