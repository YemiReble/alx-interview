#!/usr/bin/python3
""" Method that Unlock Boxes """


def canUnlockAll(boxes):
    """ This function unlocks n numbers of boxes in the following manner
        First: it checks if the boxes can be unlocked and returns 'True'
        Secondly: If otherwise this boxes can't be unlocked it returns Flase
    """
    open_boxes = [0]
    for box_indx, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in open_boxes and key != box_indx:
                open_boxes.append(key)
    if len(open_boxes) == len(boxes):
        return True
    return False
