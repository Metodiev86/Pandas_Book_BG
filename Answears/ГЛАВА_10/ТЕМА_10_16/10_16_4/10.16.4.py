# 4.	(Четене на порции):
# o	Свържете се с MS SQL Server база данни, съдържаща голяма таблица sensor_data.
# o	Прочетете данните на порции по 5000 реда.
# o	За всяка порция, изчислете средната стойност на колоната 'temperature' и я отпечатайте.

import pandas as pd
import pyodbc

# Настройки за връзка с MS SQL Server (замени със своите)
server = 'localhost'             # или име на сървър
database = 'your_database'       # име на базата данни
username = 'your_username'       # потребителско име
password = 'your_password'       # парола

# Изграждане на връзка чрез ODBC
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
)
conn = pyodbc.connect(conn_str)

# SQL заявка
sql_query = "SELECT * FROM sensor_data"

# Размер на порцията
chunksize = 5000

# Четене на порции и обработка
print("Средни температури по порции:")
for i, chunk in enumerate(pd.read_sql(sql_query, conn, chunksize=chunksize)):
    avg_temp = chunk['temperature'].mean()
    print(f"Порция {i+1}: средна температура = {avg_temp:.2f}")

# Затваряне на връзката
conn.close()

