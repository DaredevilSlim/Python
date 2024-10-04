#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
from os import mkdir
from argparse import ArgumentParser
import logging

from data import read_all
from data import in_depth

ap = ArgumentParser(description='Search path in graph')
ap.add_argument('first',
                type=str,
                help='First vertex in path'
                )
ap.add_argument('last',
                type=str,
                help='Last vertex in path'
                )
ap.add_argument('--data-path',
                '-d',
                dest='path',
                action='store',
                type=str,
                default='../data',
                help='Path to directory where data files are located'
                )
ap.add_argument('--nodes',
                '-n',
                dest='nodes',
                action='store',
                type=str,
                default='nodes.csv',
                help='Name of nodes file'
                )
ap.add_argument('--links',
                '-l',
                dest='links',
                action='store',
                type=str,
                default='links.csv',
                help='Name of links file'
                )
ap.add_argument('--debug',
                dest='loglevel',
                action='store_const',
                const=logging.DEBUG,
                default=logging.WARNING,
                help='log level = DEBUG'
                )
ap.add_argument('--no-warning',
                dest='loglevel',
                action='store_const',
                const=logging.ERROR,
                default=logging.WARNING,
                help='log level = ERROR'
                )
args = ap.parse_args()

log_path = path.expanduser(path.join('~', '.depth'))
try:
    mkdir(log_path)
except FileExistsError:
    print('Directory already exist')

logging.basicConfig(
    level=args.loglevel,
    style='{',
    format='{levelname:8} {asctime} {name:10} {message}',
    # filename=path.join(log_path, 'general.log')
)

path_to_file = path.abspath(args.path)

logging.debug(f'First: {args.first} Last {args.last}')
logging.debug(f'Data path: {args.path} ({path_to_file})')
logging.debug(f'Nodes: {args.nodes} Links: {args.links}')
logging.info('Test')
logging.warning('Test')
logging.error('Test')
logging.critical('Test')

graph, names = read_all(path_to_file, args.nodes, args.links)

first = names[args.first]['number']
last = names[args.last]['number']

for path in in_depth(graph, first, last):
    print(path)
