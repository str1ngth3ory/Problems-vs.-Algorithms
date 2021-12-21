def sort_012(arr):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    n = len(arr)

    if n == 0:
        return None

    idx_0 = 0
    idx_1 = 0
    idx_2 = len(arr) - 1
    i = 0

    while i < n and i <= idx_2:
        if arr[i] == 0:
            arr[idx_0] = 0
            if idx_0 != idx_1:
                arr[i] = arr[idx_1-1]
            idx_0 += 1
            idx_1 += 1
            i += 1
        elif arr[i] == 1:
            idx_1 += 1
            i += 1
        elif arr[i] == 2:
            arr[i] = arr[idx_2]
            arr[idx_2] = 2
            idx_2 -= 1

    return arr



def test_function(test_case):

    sorted_array = sort_012(test_case)

    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# edge case 1 - empty list, return None
print(sort_012([]))

# edge case 2 - single element list of 0, 1, or 2
test_function([0])
test_function([1])
test_function([2])

# regular cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
