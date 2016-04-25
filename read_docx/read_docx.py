#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from docx import Document
document = Document("Обеденное меню 777.docx")

# Регулярка для поиска последовательностей пробелов: от двух подряд и более
import re
multi_space_pattern = re.compile(r'[ ]{2,}')

for table in document.tables:
    for row in table.rows:
        name, weight, price = [multi_space_pattern.sub(' ', i.text.strip()) for i in row.cells]
        print('name: {}, weight: {}, price: {}'.format(name, weight, price))

    # Таблицы в меню дублируются
    break
