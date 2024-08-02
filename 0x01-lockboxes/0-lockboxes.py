#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Checks if all boxes can be unlocked.

    Args:
    boxes (list of list of int): Boxes where each list contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    queue = [0]
    isopened = set()
    while queue:
        box = queue.pop(0)
        if box not in isopened:
            isopened.add(box)
            for key in boxes[box]:
                if key not in isopened:
                    queue.append(key)
    return len(boxes) == len(isopened)
