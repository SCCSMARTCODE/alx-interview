#!/usr/bin/python3
"""
This is the function that solves the make change problem
"""


def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed to make the total amount.

    :param coins: List of coin denominations
    :param total: Total amount to make
    :return: Minimum number of coins needed
    """
    if total <= 0:
        return 0
    return make_change_brain(coins, total)


def make_change_brain(coins, total, count=0, least_count=None):
    """
    :param coins:
    :param total:
    :param count:
    :param least_count:
    :return: least_count
    """
    if least_count is None:
        least_count = [total + 1]
    if count >= least_count[0]:
        return
    for coin in coins:
        if total >= 0 and total >= coin:
            new_val = total - coin
            if new_val == 0:
                least_count[0] = min(least_count[0], count + 1)
                return
            elif new_val < 0:
                return
            make_change_brain(coins, new_val, count + 1, least_count)
    return least_count[0]
