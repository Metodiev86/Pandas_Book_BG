# 7.	Обработка на XML с повтарящи се елементи*: Представете си XML файл, където информацията за даден обект е разпределена в няколко повтарящи се елемента с еднакви имена, но различни атрибути. Създайте примерен XML файл repeating_elements.xml:
# <record>
#   <field name="name" value="Alice"/>
#   <field name="age" value="25"/>
#   <field name="city" value="Sofia"/>
#   <field name="interest" value="reading"/>
#   <field name="interest" value="hiking"/>
# </record>
#
# Напишете код, който да прочете този XML файл и да го преобразува в DataFrame, където 'name', 'age', 'city' са отделни колони, а 'interest' е колона, съдържаща списък от интереси за всеки запис. (Тази задача може да изисква малко по-напреднало използване на XML парсване, вероятно в комбинация с xml.etree.ElementTree преди създаването на DataFrame).

import xml.etree.ElementTree as ET
import pandas as pd

# --- 1. Четене на XML файл ---
tree = ET.parse('repeating_elements.xml')  # Четем XML файла
root = tree.getroot()  # Вземаме корена на XML документа

# --- 2. Инициализация на данни за DataFrame ---
record = {}

# --- 3. Извличане на данни от повтарящите се елементи ---
interests = []  # Списък за събиране на интереси
for field in root.findall('field'):
  name = field.get('name')  # Име на полето
  value = field.get('value')  # Стойност на полето

  if name == 'interest':  # Ако полето е interest, добавяме стойността към списъка
    interests.append(value)
  else:
    record[name] = value  # За останалите полета запазваме стойността

# --- 4. Добавяне на списък с интереси към записа ---
record['interest'] = interests

# --- 5. Преобразуване на записа в DataFrame ---
df = pd.DataFrame([record])

# --- 6. Извеждаме резултата ---
print(df)

#=============================================Обяснение:=====================================================
#
# Прочитаме XML файла с помощта на xml.etree.ElementTree.
#
# Извличаме стойностите от field елементите.
#
# Когато срещнем елемент interest, добавяме стойността му в списък interests.
#
# След като извлечем всички данни, ги добавяме в речник (record), който след това преобразуваме в DataFrame.