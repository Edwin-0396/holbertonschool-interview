#!/usr/bin/python3
""" 
Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
"""

def validUTF8(data):
    """ Function that determines if a given data set 
    represents a valid UTF-8 encoding
    """
    for i in range(len(data)):
        if data[i] > 255:
            return False
    return True