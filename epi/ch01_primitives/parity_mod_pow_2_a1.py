'''
Compute x mod a power of 2, e.g., returns 13 for 77 mod 64
'''
def mod_pow_2(x: int, power: int) -> int:
    den = 1 << power
    quo = x >> power
    mod = x - quo * den
    return mod
