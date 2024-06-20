#!/usr/bin/python3
"""
Solving this problem

n = 9
H => Copy All => Paste => HH => Paste =>HHH
        => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
Number of operations: 6
"""


def minOperations(target: int) -> int:
    operation_count = 0
    if target == 2:
        return 2
    if target > 1:
        cursor = 2
        while cursor <= target:
            if target % cursor == 0:
                operation_count += cursor
                target = target/cursor
                cursor = 2
            if cursor >= target/2:
                return int(operation_count + target)
            cursor += 1
    return operation_count
