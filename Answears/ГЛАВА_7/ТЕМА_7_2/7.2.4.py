# 4. Имате Series с имена на градове. Напишете код, който преобразува всички имена в горни букви, използвайки .map() и lambda функция.

import pandas as pd

# Примерна Series с имена на градове
cities = pd.Series(['София', 'Пловдив', 'Варна', 'Бургас', 'Русе'])

# Преобразуване на имената в главни букви чрез .map() и lambda
cities_upper = cities.map(lambda x: x.upper())

print(cities_upper)
