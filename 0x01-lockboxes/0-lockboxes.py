#!/usr/bin/python3
"""This is a module that contains the canUnlockAll function"""


def canUnlockAll(boxes):
    """
    This functions unlocks available boxes
    :param boxes:
    :return:
    """

    if len(boxes) <= 1:
        return True
    available_keys = boxes[0]
    for x, box in enumerate(boxes[1:]):
        if x + 1 in available_keys:
            available_keys.extend(box)
        else:
            for y in available_keys:
                if x + 1 in boxes[y]:
                    return True
            return False
    return True
