# 2.	Четене на XML с атрибути: Създайте XML файл sensors.xml със следната структура:
# <sensors>
#   <sensor id="S1" type="temperature" value="25.5"/>
#   <sensor id="S2" type="humidity" value="60.2"/>
#   <sensor id="S3" type="pressure" value="1012.3"/>
# </sensors>
#
# Прочетете данните в DataFrame, като използвате само атрибутите 'id', 'type' и 'value' като колони.

import pandas as pd


# --- 1. Четене на XML и извличане на атрибутите ---
# Използваме xpath='./sensor' за да достъпим всеки <sensor>
# Атрибутите автоматично се превръщат в колони в DataFrame

df = pd.read_xml(
    'sensors.xml',
    xpath='./sensor',
    parser='lxml'  # гарантира, че XPath ще работи коректно
)

# --- 2. Преобразуване на колоната 'value' в числов тип (по избор) ---
df['value'] = pd.to_numeric(df['value'])

# --- 3. Преглед на резултата ---
print(df)
