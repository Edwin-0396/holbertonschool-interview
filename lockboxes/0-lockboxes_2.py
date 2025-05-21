import sys
import ast


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
    boxes (list of list of int): Each position is a box and each list inside a set of keys.
    
    Returns:
    bools: True if all boxes can be unlocked, False otherwise.
    """

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = set(boxes[0])

    found_new = True
    while found_new:
        found_new = False
        for i in range(n):
            if not unlocked[i] and i in keys:
                unlocked[i] = True
                keys.update(boxes[i])
                found_new = True
    return all(unlocked)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        boxes = ast.literal_eval(sys.argv[1])
    else:
        boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))