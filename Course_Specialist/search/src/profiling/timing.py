#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import logging

__all__ = ('timing',)


def timing(received_function):
    def timed_function(*args, **kwargs):
        time_0 = datetime.now()
        result = received_function(*args, **kwargs)
        time_0 = datetime.now() - time_0
        logging.debug(f'{received_function.__name__}: {time_0.microseconds}')
        return result
    return timed_function
