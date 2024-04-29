#!/usr/bin/python3
""" Code base for the lockboxes """


def canUnlockAll(boxes):
    """Implementation of canUnlockAll function"""
    opened = [0]

    for index in opened:
        for key in boxes[index]:
            if key not in opened and key < len(boxes):
                opened.append(key)

    return len(boxes) == len(opened)
