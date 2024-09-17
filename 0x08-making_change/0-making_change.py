#!/usr/bin/python3
"""
Interview Question on: fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """ return the fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        tmp = total // coin
        count += tmp
        total -= coin * tmp
    if total != 0:
        return -1
    return count
