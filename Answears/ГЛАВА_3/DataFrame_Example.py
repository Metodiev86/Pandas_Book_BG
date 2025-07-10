import pandas as pd
import numpy as np

# За възпроизводимост
np.random.seed(42)

# Генериране на примерни данни
n = 30
df = pd.DataFrame({
    'employee_id': range(1001, 1001 + n),  # int
    'name': np.random.choice(
        ['Ана', 'Борис', 'Весела', 'Георги', 'Десислава', 'Емил', 'Зоя', 'Иво', 'Емил'], n),
    'age': np.random.randint(22, 60, n),  # int
    'salary': np.round(np.random.uniform(1800, 5200, n), 2),  # float
    'department': np.random.choice(
        ['Маркетинг', 'Финанси', 'ИТ', 'Човешки ресурси'], n),  # str
    'start_date': pd.to_datetime('2020-01-01') +
        pd.to_timedelta(np.random.randint(0, 1000, n), unit='D'),  # datetime
    'is_remote': np.random.choice([True, False], n),  # bool
    'performance_rating': np.random.choice(
        [1, 2, 3, 4, 5, np.nan], n),  # float + NaN
    'contract_type': pd.Categorical(np.random.choice(
        ['постоянен', 'временен', 'почасов'], n))  # category
})

