#!/usr/bin/python3
"""this modules makes change from coins"""


def makeChange(coins, total):
    """determines and returns fewest number of coins needed to meet total"""
    if total <= 0:
        return (0)

    """sort coins"""
    coins = sorted(coins)[::-1]
    change = 0
    for coin in coins:
        if total <= 0:
            break
        while total >= coin:
            total -= coin
            change += 1
    if total:
        return (-1)
    return (change)
