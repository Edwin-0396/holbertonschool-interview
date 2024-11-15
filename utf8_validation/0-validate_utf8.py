#!/usr/bin/python3


def validUTF8(data):
    """ Function that determines if a given data set represents a valid UTF-8 encoding
    """
    for data in data:
        if data > 255:
            return False
    return True