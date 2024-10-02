#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class InvalidMixin(Exception):
    pass


def mixin(module):
    def mix(cls):
        for name in module.__all__:
            if hasattr(cls, name):
                raise InvalidMixin(f'Duplicate attribute \'{name}\' in class \'{cls.__name__}\'')
            setattr(cls, name, getattr(module, name))
        return cls
    return mix
