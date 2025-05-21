#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
    boxes (list of list of int): Each box contains a list of keys.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)  # Number of boxes
    unlocked = [False] * n  # Track which boxes are unlocked
    unlocked[0] = True  # The first box is always unlocked
    keys = set(boxes[0])  # Keys found so far (from box 0)

    found_new = True
    while found_new:
        found_new = False
        for i in range(n):
            if not unlocked[i] and i in keys:
                unlocked[i] = True  # Unlock box i
                keys.update(boxes[i])  # Add new keys found in box i
                found_new = True  # Found a new box to unlock
    return all(unlocked)  # Return True if all boxes are unlocked

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Example usage
