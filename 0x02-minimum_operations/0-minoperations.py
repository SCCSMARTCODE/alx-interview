#!/usr/bin/python3
"""
Solving this problem

n = 9
H => Copy All => Paste => HH => Paste =>HHH
        => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
Number of operations: 6
"""
import typing


def minOperations(n: int) -> int:
    """
    this is the minOperations function
    :param n:
    :return: operation_count
    """
    operation_count = 0
    current = 1
    cursor = 1

    while current != n:
        if current > n:
            return 0
        cap_opr = copy_all_paste(current)
        p_opr = paste(cursor, current)
        if n % cap_opr == 0:
            current = cursor = cap_opr
            operation_count += 2
            continue

        cursor, current = p_opr
        operation_count += 1
    return operation_count


def copy_all_paste(current: int) -> int:
    """
    this is the copy_all & paste function
    :param current:
    :return: current
    """
    current *= 2
    return current


def paste(cursor: int, current: int) -> typing.Tuple[int, int]:
    """
    this is the paste function
    :param cursor:
    :param current:
    :return: (cursor, new_current)
    """
    return cursor, current + cursor

