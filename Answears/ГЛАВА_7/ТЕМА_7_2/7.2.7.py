# Имате DataFrame с числови колони. Напишете код, който намира максималната стойност за всяка колона, използвайки .apply() с axis=0.

import pandas as pd

# Примерен DataFrame с числови колони
df = pd.DataFrame({
    'A': [5, 12, 8],
    'B': [3, 15, 7],
    'C': [10, 6, 9]
})

# Извличане на максималната стойност за всяка колона (axis=0 означава по колони)
max_values = df.apply(lambda col: col.max(), axis=0)

print(max_values)
