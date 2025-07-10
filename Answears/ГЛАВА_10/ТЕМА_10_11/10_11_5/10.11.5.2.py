# 5.	Работа с облачно съхранение (симулирано): Ако имате достъп до облачно хранилище (например, AWS S3), опитайте да прочетете и запишете Feather файл, използвайки storage_options. Ако не, можете да симулирате това, като използвате локални файлове и се фокусирате върху синтаксиса на storage_options (например, за HTTP/HTTPS URL).

# Пример за работа с storage_options с AWS S3:
# Ако имате достъп до AWS S3, можете да използвате библиотеката s3fs за работа с S3. В този случай ще използваме параметъра storage_options за предоставяне на необходимите ключове за достъп и други опции за връзка.

import pandas as pd
import numpy as np
import s3fs

# Създаване на DataFrame
data = {
    'int_column': np.random.randint(1, 100, 10),
    'float_column': np.random.random(10),
    'str_column': np.random.choice(['A', 'B', 'C', 'D'], 10),
    'bool_column': np.random.choice([True, False], 10)
}
df = pd.DataFrame(data)

# Конфигуриране на S3 (параметри за достъп, като ключове)
s3_options = {
    'key': 'your-access-key',  # Вашият AWS access key
    'secret': 'your-secret-key'  # Вашият AWS secret key
}

# Запис в Feather файл в S3
file_path_s3 = 's3://your-bucket-name/data_feather.feather'
df.to_feather(file_path_s3, storage_options=s3_options)

# Четене от Feather файл в S3
df_read_s3 = pd.read_feather(file_path_s3, storage_options=s3_options)

# Показване на първите няколко реда
print(df_read_s3.head())
