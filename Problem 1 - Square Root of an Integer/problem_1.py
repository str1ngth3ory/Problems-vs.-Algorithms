def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        raise ValueError('Negative Integer Input')

    if number == 0:
        return 0

    a = 1
    b = number

    while (a*2) <= (b/2):
        a *= 2
        b /= 2

    while (a+1)*(a+1) <= number:
        a += 1

    return a


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
