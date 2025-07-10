#Даден е Series с оценки (числа). Напишете код, който създава нов Series, където всяка оценка се увеличава с 5, използвайки .map() и lambda функция.

import pandas as pd

# Примерен Series с оценки
grades = pd.Series([70, 85, 90, 60, 76])

# Увеличаване на всяка оценка с 5 чрез .map() и lambda функция
increased_grades = grades.map(lambda x: x + 5)

print(increased_grades)
