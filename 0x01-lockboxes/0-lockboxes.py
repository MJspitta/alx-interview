#!/usr/bin/python3
""" determines if all the boxes can be opened """


def canUnlockAll(boxes):
    """ if boxes can be opened return true """
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
