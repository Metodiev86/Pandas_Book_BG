# 5.	Запис с включен индекс като атрибут: Създайте DataFrame с произволен индекс (не поредица от числа) и една колона с данни. Запишете го в XML файл indexed_output.xml, като включите индекса като атрибут на елемента за ред.

import pandas as pd
import xml.etree.ElementTree as ET

df = pd.DataFrame({
    'Стойност': [100, 200, 300]
}, index=['ID_A', 'ID_B', 'ID_C'])

root = ET.Element('данни')

for idx, row in df.iterrows():
    запис = ET.SubElement(root, 'запис', attrib={'id': idx})
    for col, val in row.items():
        ET.SubElement(запис, col).text = str(val)

tree = ET.ElementTree(root)
tree.write('indexed_output2.xml', encoding='utf-8', xml_declaration=True)
