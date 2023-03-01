'''
Test if x is a power of 2, i.e., evaluates to true for x = 1,2,4,8,... and false for all other values
'''
def is_pow_2(x: int) -> bool:
    if x == 0:
        return False
    return (x & (x - 1)) == 0
