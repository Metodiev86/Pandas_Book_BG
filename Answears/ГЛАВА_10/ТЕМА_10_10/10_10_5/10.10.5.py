# 5.	Изследване на компресия: Създайте голям DataFrame и го запишете в HDF5 файл няколко пъти с различни нива на компресия (complevel) и различни библиотеки за компресия (complib). Наблюдавайте как се променя размерът на файла на диска. (Тази задача може да изисква инсталиране на допълнителни библиотеки за компресия като lzo или bzip2).
import time

import pandas as pd
import numpy as np
import os

# Създаване на голям DataFrame
df = pd.DataFrame({
  'ID': np.arange(1_000_000),
  'Стойност': np.random.rand(1_000_000),
  'Категория': np.random.choice(['A', 'B', 'C', 'D'], 1_000_000)
})

# Запис и четене с различни формати за компресия
compressions = [
  ('zlib', 1),
  ('zlib', 5),
  ('zlib', 9),
  ('bzip2', 5),
  ('blosc:zstd', 5),
]

# Запис с %timeit
for complib, level in compressions:
  filename = f'hdf_{complib.replace(":", "_")}_lvl{level}.h5'

  # Време за запис
  start_fixed = time.time()
  print(f"Записване с {complib} и нивото {level}:")

  df.to_hdf(
    filename,
    key='df',
    mode='w',
    format='table',
    complevel=level,
    complib=complib
  )

  # Време за четене
  print(f"Четене с {complib} и нивото {level}:")
  end_fixed = time.time()
  print(f"{(end_fixed-start_fixed):.6f} sec")
  pd.read_hdf(filename, key='df')
  print("-" * 50)

