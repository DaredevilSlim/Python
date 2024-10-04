#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
from weakref import ref
from collections import UserDict

from profiling import timing
from .read_nodes import read_nodes
from .read_links import read_links

__all__ = ('read_all',)


class CorruptedData(Exception):
    pass


@timing
def read_all(path_to_file, nodes='nodes.csv', links='links.csv'):
    nodes_path = path.join(path_to_file, nodes)
    links_path = path.join(path_to_file, links)

    graph = dict()
    names = dict()

    for number, name in read_nodes(nodes_path):
        node = UserDict({
            'number': number,
            'name': name,
            'neighbors': dict(),
            'prohibited': set()
        })
        graph[number] = node
        if name in names:
            raise CorruptedData(f'{name} already exists')
        names[name] = node

    for node_one, node_two, penalty in read_links(links_path):
        graph[node_one]['neighbors'][node_two] = (penalty, ref(graph[node_two]))
        graph[node_two]['neighbors'][node_one] = (penalty, ref(graph[node_one]))
    return graph, names
