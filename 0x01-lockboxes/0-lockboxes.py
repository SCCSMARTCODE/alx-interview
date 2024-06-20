#!/usr/bin/python3
"""This is a module that contains the canUnlockAll function"""


def canUnlockAll(boxes):
    """
    This functions unlocks available boxes
    :param boxes:
    :return:
    """

    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False
