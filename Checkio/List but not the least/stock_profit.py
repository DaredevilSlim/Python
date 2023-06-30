#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are a broker on the stock exchange. You've decided to make just one complete operation: to buy a stock and sell it
# later to make a profit.
# Your function must return this maximum possible profit for given price fluctuations. If it's not possible to make any
# profit with given prices (it's <= 0), your function should return 0.
# Input: Stock prices as list of integers (int).
# Output: Maximum possible profit as an integer (int).
# Preconditions:
# len(stock) > 1;
# 0 <= price <= 1000.
def stock_profit(stock: list[int]) -> int:
    a = stock.index(min(stock))
    b = stock.index(max(stock))
    if len(stock) > 1:
        if b < a:
            return stock_profit(stock[:a] if len(stock) - 1 == a else stock[b + 1:])
        return stock[b] - stock[a]
    return 0


print(stock_profit([2, 3, 4, 5]))                    # 3
print(stock_profit([3, 1, 3, 4, 5, 1]))              # 4
print(stock_profit([4, 3, 2, 1]))                    # 0
print(stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]))  # 4
print(stock_profit([1, 1, 1, 2, 1, 1, 1]))           # 1
print(stock_profit([4, 3, 2, 1, 2, 1, 2, 1]))        # 1
print(stock_profit([1, 1, 1, 1]))                    # 0
print(stock_profit([22, 10, 4, 4, 1]))               # 0
print(stock_profit([80, 70, 10, 3, 7]))              # 4
print(stock_profit([60, 50, 51, 52, 40]))            # 2
