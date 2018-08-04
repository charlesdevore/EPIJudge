import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A):
    return find_min_max_brute_force(A)
    #return find_min_max_efficient_execution(A)

def find_min_max_brute_force(A):
    # Use as baseline comparison. Find by evaluating each value
    # against a stored value for min and max. Results in O(1) memory
    # and O(2(n-1)) execution.

    min_value, max_value = A[0], A[0]

    for a in A[1:]:
        if a < min_value:
            min_value = a

        if a > max_value:
            max_value = a

    return MinMax(min_value, max_value)

def find_min_max_efficient_execution(A):
    # Find the min and max using an efficient algorithm that minimizes
    # comparison calls. Start with a pairwise comparison of each
    # element and then split into two subarrays containing the lesser
    # values and the greater values. Recursively compare to find min
    # or max values. O(n) memory and O(n) execution.

    lesser_values, greater_values = [], []

    n = len(A)
    
    # If array is odd-length than pop an element and add to both
    # subarrays
    if n%2 == 1:
        a = A.pop()
        lesser_values.append(a)
        greater_values.append(a)
        n -= 1

    for ii in range(0, n//2):
        if A[ii] < A[n//2 + ii]:
            lesser_values.append(A[ii])
            greater_values.append(A[n//2 + ii])
            
        else:
            lesser_values.append(A[n//2 + ii])
            greater_values.append(A[ii])

    min_value = recursive_min(lesser_values)
    max_value = recursive_max(greater_values)
    
    return MinMax(min_value, max_value)

    return False

def recursive_min(lesser_values):

    n = len(lesser_values)
    smaller_lesser = []

    if n == 1:
        return lesser_values[0]

    elif n%2 == 0:
        for ii in range(0, n//2):
            if lesser_values[ii] < lesser_values[n//2 + ii]:
                smaller_lesser.append(lesser_values[ii])

            else:
                smaller_lesser.append(lesser_values[n//2 + ii])

        return recursive_min(smaller_lesser)

    else:
        if lesser_values[0] < lesser_values[-1]:
            return recursive_min(lesser_values[:-1])

        else:
            return recursive_min(lesser_values[1:])


def recursive_max(greater_values):

    n = len(greater_values)
    smaller_greater = []

    if n == 1:
        return greater_values[0]

    elif n%2 == 0:
        for ii in range(0, n//2):
            if greater_values[ii] > greater_values[n//2 + ii]:
                smaller_greater.append(greater_values[ii])

            else:
                smaller_greater.append(greater_values[n//2 + ii])

        return recursive_max(smaller_greater)

    else:
        if greater_values[0] > greater_values[-1]:
            return recursive_max(greater_values[:-1])

        else:
            return recursive_max(greater_values[1:])
            
                
    

def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            'search_for_min_max_in_array.tsv',
            find_min_max,
            res_printer=res_printer))
