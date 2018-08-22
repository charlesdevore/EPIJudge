from test_framework import generic_test


def search_first_of_k(A, k):

    if len(A) == 0:
        return -1

    keys = [i for i in range(0, len(A))]

    return search_first_of_k_recursive(A, k, keys)

def search_first_of_k_recursive(A, k, keys):
    if len(keys) == 1 and A[keys[0]] == k:
        return keys[0]
    elif len(keys) == 1:
        return -1

    if len(keys) == 2:
        if A[keys[0]] == k:
            return keys[0]
        elif A[keys[1]] == k:
            return keys[1]
        else:
            return -1
    
    mid = len(keys)//2
    #print(keys, keys[mid])
    
    if A[keys[mid]] >= k:
        return search_first_of_k_recursive(A, k, keys[:mid+1])
    else:
        return search_first_of_k_recursive(A, k, keys[mid:])
    
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
