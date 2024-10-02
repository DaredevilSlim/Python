#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

__all__ = ('read_links',)


def read_links(file_path, encoding='utf-8'):
    with open(file_path, 'rt', encoding=encoding) as src:
        rdr = csv.reader(src)
        for node_one, node_two, penalty in rdr:
            yield int(node_one), int(node_two), float(penalty)
