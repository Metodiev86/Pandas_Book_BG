# 3.	(Записване с различни опции за if_exists):
# o	Създайте примерен Pandas DataFrame.
# o	Свържете се с MySQL база данни.
# o	Опитайте да запишете DataFrame-а в таблица logs, използвайки if_exists='fail'. Какво се случва, ако таблицата вече съществува?
# o	Запишете същия DataFrame в таблица logs, използвайки if_exists='replace'. Проверете съдържанието на таблицата след записа.
# o	Добавете нови данни към DataFrame-а и го запишете в таблица logs, използвайки if_exists='append'. Проверете отново съдържанието на таблицата.

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError, ProgrammingError

# Данни за връзка с MySQL (замени с реалните)
username = 'your_username'
password = 'your_password'
host = 'localhost'
port = '3306'
database = 'your_database'

# Създаване на SQLAlchemy engine
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

# 1. Създаване на примерен DataFrame
df = pd.DataFrame({
    'event': ['login', 'logout', 'purchase'],
    'timestamp': pd.to_datetime(['2025-07-01 08:00', '2025-07-01 08:30', '2025-07-01 09:00']),
    'user_id': [101, 102, 103]
})

print("=== Опит за запис с if_exists='fail' ===")
try:
    df.to_sql(name='logs', con=engine, if_exists='fail', index=False)
    print("Таблицата беше създадена успешно.")
except ValueError as ve:
    print(f"ГРЕШКА: {ve} (таблицата вероятно вече съществува)")

print("\n=== Запис с if_exists='replace' ===")
df.to_sql(name='logs', con=engine, if_exists='replace', index=False)
print("Таблицата беше презаписана.\n")

# Проверка на съдържанието след replace
df_replace = pd.read_sql("SELECT * FROM logs", con=engine)
print("Съдържание на таблицата след 'replace':")
print(df_replace)

print("\n=== Добавяне на нови данни с if_exists='append' ===")

# Добавяме още редове към DataFrame-а
df_new = pd.DataFrame({
    'event': ['search', 'checkout'],
    'timestamp': pd.to_datetime(['2025-07-01 09:30', '2025-07-01 10:00']),
    'user_id': [104, 105]
})

# Добавяне към съществуващата таблица
df_new.to_sql(name='logs', con=engine, if_exists='append', index=False)
print("Данни бяха добавени към таблицата.\n")

# Проверка на съдържанието след append
df_final = pd.read_sql("SELECT * FROM logs", con=engine)
print("Съдържание на таблицата след 'append':")
print(df_final)
