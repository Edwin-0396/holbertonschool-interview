
def validUTF8(data):
    
    for data in data:
        if data > 255:
            return False
    return True