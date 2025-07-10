# 1.	Четене на XML с XPath: Създайте XML файл data.xml със следната структура:
# <data>
#   <person id="1">
#     <name>Alice</name>
#     <age>25</age>
#     <city>Sofia</city>
#   </person>
#   <person id="2">
#     <name>Bob</name>
#     <age>30</age>
#     <city>Plovdiv</city>
#   </person>
# </data>
#
#  Прочетете само имената и възрастите на хората в DataFrame, използвайки подходящ XPath израз. Задайте 'id' като индекс.


import pandas as pd

# --- 1. Създаване на XML файл ---
xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<data>
  <person id="1">
    <name>Alice</name>
    <age>25</age>
    <city>Sofia</city>
  </person>
  <person id="2">
    <name>Bob</name>
    <age>30</age>
    <city>Plovdiv</city>
  </person>
</data>
'''

with open('data.xml', 'w', encoding='utf-8') as f:
    f.write(xml_content)

# --- 2. Четене на XML чрез XPath ---
# Използваме xpath='./person' за да достъпим всички <person> елементи
# Извличаме само name и age, а 'id' се ползва като индекс

df = pd.read_xml(
    'data.xml',
    xpath='./person',
    dtype={'age': int},
    parser='lxml'  # по-надежден XML парсър, препоръчително е да го имаш
)

# --- 3. Задаване на 'id' като индекс и изчистване на ненужните колони ---
df.set_index('id', inplace=True)
df = df[['name', 'age']]

# --- 4. Преглед на резултата ---
print(df)
