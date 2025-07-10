

import pandas as pd
from sqlalchemy import create_engine

# 🔧 Конфигурация на връзката (замени с реални данни)
username = 'your_username'
password = 'your_password'
host = 'localhost'
port = '5432'
database = 'your_database'

# Създаване на SQLAlchemy engine
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

# 🧾 SQL заявка – свързване на employees и departments по department_id
query = """
SELECT
    e.name AS employee_name,
    d.name AS department_name
FROM employees e
JOIN departments d ON e.department_id = d.id
"""

# 📥 Изпълняваме заявката и зареждаме в DataFrame
df = pd.read_sql_query(query, con=engine)

# Показване на служителите и отделите
print("Служители и техните отдели:")
print(df.head())

# 📊 Анализ – брой служители по отдел
department_counts = df['department_name'].value_counts().sort_index()

print("\nБрой служители по отдел:")
print(department_counts)
