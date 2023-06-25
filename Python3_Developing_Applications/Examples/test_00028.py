#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Форматирование строк

html = """<html>
<head><title>%(title)s</title>
</head>
<body>
<h1>%(hl)s</hl>
<div>%(content)s</div>
</body>
</html>"""
arr = {'title':   'Это название документа',
       'hl':      'Это заголовок первого уровня',
       'content': 'Это основное содержание страницы'}
print(html % arr)  # Подставляем значения и выводим шаблон
input()
