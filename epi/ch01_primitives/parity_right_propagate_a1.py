'''
Right propagate the rightmost set bit in x, e.g., turns (01010000) to (01011111)
'''

def right_propagate(x: int) -> int:
    last_set_bit = x & ~(x - 1)
    while last_set_bit:
        x |= last_set_bit
        last_set_bit >>= 1
    return x
