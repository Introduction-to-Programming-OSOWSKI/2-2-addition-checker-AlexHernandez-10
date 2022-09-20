from fcntl import F_SEAL_SEAL


def addCheck(x, y, z):


    if x + y == z:
        return True
    
    else: 
        return False