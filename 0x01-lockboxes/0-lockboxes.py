#!/usr/bin/python3
'''Working on the Lockboxes Challenge'''

def canUnlockAll(boxes):
    '''checks if all the box will be opened and opens them
    Returns:
        True: if all the boxes can be opened
        False: if not all the boxes can be opened
    '''
    keys = set()
    openedBoxes = []
    i = 0

    while i < len(boxes):
        oldi = i
        openedBoxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < len(boxes) and key not in openedBoxes:
                i = key
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(len(boxes)):
        if i not in openedBoxes and i != 0:
            return False
    return True