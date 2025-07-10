# 8.	Слейте два DataFrame-а и използвайте параметъра validate за да проверите дали връзката между ключовите колони е 'one-to-many'.

import pandas as pd

# Създаваме DataFrame със служители – всеки служител принадлежи на един отдел
df_employees = pd.DataFrame({
    'employee_id': [1, 2, 3],
    'name': ['Anna', 'Boris', 'Charlie'],
    'department_id': [10, 20, 10]
})

# Създаваме DataFrame с отдели – всеки отдел може да има много служители
df_departments = pd.DataFrame({
    'department_id': [10, 20],
    'department_name': ['HR', 'Finance']
})

# Извършваме сливане и валидираме връзката one-to-many:
merged_df = pd.merge(
    df_employees,
    df_departments,
    on='department_id',
    validate='many_to_one'  # потвърждаваме, че служители (много) -> отдели (един)
)

# Показваме резултата
print(merged_df)


# Коментари:
# validate='many_to_one' указва, че в df_employees може да има много редове с една и съща department_id, но в df_departments всяка department_id трябва да е уникална (т.е. one-to-many).
#
# Ако това условие не е спазено, Pandas ще върне MergeError, което предпазва от логически грешки при обединяване на таблици.