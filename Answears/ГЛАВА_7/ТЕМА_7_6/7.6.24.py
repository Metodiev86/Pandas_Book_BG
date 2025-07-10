#Даден е Series с числови стойности, включващ NaN. Напишете код, който сортира Series-а във възходящ ред, като NaN стойностите бъдат поставени в края.

import pandas as pd
import numpy as np

# Примерен Series с NaN стойности
s = pd.Series([4.5, np.nan, 2.1, 8.3, np.nan, 5.7])

# Сортиране във възходящ ред, като NaN отиват в края
sorted_s = s.sort_values(na_position='last')

print(sorted_s)
