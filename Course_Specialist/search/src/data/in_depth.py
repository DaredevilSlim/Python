#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ('in_depth',)


def in_depth(graph, first, last):
    start_vertex = [first]
    while start_vertex:
        node = graph[start_vertex[-1]]
        result = set(node['neighbors'].keys()) - node['prohibited']
        try:
            next_vertex = result.pop()
            node['prohibited'].add(next_vertex)
            if next_vertex == last:
                yield start_vertex + [next_vertex]
            elif next_vertex in start_vertex:
                pass
            else:
                start_vertex.append(next_vertex)
        except KeyError:
            node['prohibited'] = set()
            del start_vertex[-1]
