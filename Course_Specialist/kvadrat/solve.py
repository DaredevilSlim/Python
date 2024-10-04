#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt


def solve(aa, bb, cc):
    dd = bb * bb - 4.0 * aa * cc
    if dd >= 0:
        xx_1 = (-bb - sqrt(dd)) / (2.0 * aa)
        xx_2 = (-bb + sqrt(dd)) / (2.0 * aa)
        return [xx_1, xx_2]
    else:
        return []
