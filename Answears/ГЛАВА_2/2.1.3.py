#3.	Създаване на DataFrame от NumPy array: Създайте DataFrame от случаен NumPy array с размери 5x3 (използвайте np.random.rand(5, 3)). Задайте имената на колоните като 'Колона A', 'Колона B', 'Колона C'. Изведете първите два реда от DataFrame-а (подсказка: използвайте slicing).

import numpy as np
import pandas as pd

# Създаване на случаен NumPy array с размери 5x3
random_array = np.random.rand(5, 3)

# Създаване на DataFrame от масива и задаване на имена на колоните
df = pd.DataFrame(random_array, columns=['Колона A', 'Колона B', 'Колона C'])

# Извеждане на първите два реда чрез slicing
print("Първите два реда на DataFrame-а:\n")
print(df[:2])
