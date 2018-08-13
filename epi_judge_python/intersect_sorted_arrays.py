from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    """Return the intersection of two lists in O(n+m) time and 0(1)
    space. Iterate through each array and if the values are the same
    store at the beginning of the first array.
    """

    iA, iB, iout = 0,0,0

    while iA < len(A) and iB < len(B):
        if A[iA] == B[iB]:
            if A[iA] != A[iout-1] or iout is 0:
                A[iout] = A[iA]
                iout += 1

            iA += 1
            iB += 1

        elif A[iA] < B[iB]:
            iA += 1

        elif B[iB] < A[iA]:
            iB += 1
            
        #print(iA, iB, iout)
            
    return A[:iout]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
