#2.	(Четене на определени колони):
# o	Свържете се с PostgreSQL база данни.
# o	Използвайте read_sql_table(), за да прочетете само колоните 'name' и 'email' от таблица users.
# o	Задайте колоната 'name' като индекс на DataFrame-а.


import pandas as pd
from sqlalchemy import create_engine

# Данни за достъп до PostgreSQL (замени със своите)
username = 'your_username'
password = 'your_password'
host = 'localhost'
port = '5432'
database = 'your_database'

# Създаване на SQLAlchemy engine за PostgreSQL
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

# Четене само на определени колони от таблицата users
df = pd.read_sql_table(
    table_name='users',
    con=engine,
    columns=['name', 'email']
)

# Задаване на колоната 'name' като индекс
df.set_index('name', inplace=True)

# Показване на резултата
print("Резултатен DataFrame:")
print(df)
