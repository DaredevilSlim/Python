#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

__all__ = ('read_nodes',)


def read_nodes(file_path, encoding='utf-8'):
    with open(file_path, 'rt', encoding=encoding) as src:
        rdr = csv.reader(src)
        for number, name in rdr:
            yield int(number), name
