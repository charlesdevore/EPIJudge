import collections

from test_framework import generic_test

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_longest_increasing_subarray(A):

    n = len(A)
    end_values = []
    
    for i in range(1,n):
        if A[i] <= A[i-1]:
            end_values.append(i-1)

    if not end_values:
        return Subarray(0, n-1)

    # Add the ending index to end values
    end_values.append(n-1)
    
    start, end = 0, 0
    max_subarray = Subarray(0, 0)

    for end in end_values:
        if end - start > max_subarray.end - max_subarray.start:
            max_subarray = Subarray(start, end)

        start = end + 1

    #print(max_subarray.start, max_subarray.end)
    
    return max_subarray


def find_longest_increasing_subarray_wrapper(A):
    result = find_longest_increasing_subarray(A)
    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_increasing_subarray.py",
            'longest_increasing_subarray.tsv',
            find_longest_increasing_subarray_wrapper))
