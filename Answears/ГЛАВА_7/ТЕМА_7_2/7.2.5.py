# Даден е DataFrame с числови стойности. Напишете код, който форматира всяка стойност като низ с две десетични места, използвайки .map() и f-string.

import pandas as pd
import numpy as np

# Създаваме примерен DataFrame с числови стойности
df = pd.DataFrame(np.random.randn(3, 3), columns=['A', 'B', 'C'])

# Форматираме всяка стойност като низ с 2 десетични знака
df_formatted = df.map(lambda x: f"{x:.2f}")

print(df_formatted)
