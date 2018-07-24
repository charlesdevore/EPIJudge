from test_framework import generic_test


def parity(x):

    #return brute_force_parity(x)
    return improved_parity(x)


def improved_parity(x):

    """Determine the parity of a binary number using an improved
algorithm. The algorithm works by dropping the last bit in the number
and then finding the XOR for the result. If the number of bits is odd,
the while loop will execute an extra time resulting in a True result.

    """

    result = False
    while x:
        result ^= 1
        x &= (x-1)

    return result


def brute_force_parity(x):
    
    """
Determine the parity of a binary number. The parity is defined as
true for an odd number of bits and false for an even number of bits.

The function works by finding whether the current bit is true and then
finding the XOR of the result.
    """
    
    result = False
    while x:
        result ^= x & 1
        x >>= 1
        
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
