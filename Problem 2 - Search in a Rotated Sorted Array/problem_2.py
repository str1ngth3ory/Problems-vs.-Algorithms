def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list == []:
        raise ValueError('Input cannot be empty list.')
    return ra_search_recur(input_list, 0, len(input_list)-1, number)

def ra_search_recur(arr, start, end, n):

    if start == end:
        if arr[start] == n:
            return start
        else:
            return -1

    mid = (start + end) // 2

    if arr[start] < arr[mid]:
        if n >= arr[start] and n <= arr[mid]:
            return ra_search_recur(arr, start, mid, n)
        else:
            return ra_search_recur(arr, mid+1, end, n)
    else:
        if n >= arr[mid+1] and n <= arr[end]:
            return ra_search_recur(arr, mid+1, end, n)
        else:
            return ra_search_recur(arr, start, mid, n)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 5]) # edge case 1 - mid number is greater than numbers on both sides
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 1, 2, 3, 4], 4]) # edge case 2 - mid number is smaller than numbers on both sides
test_function([[6], 1]) # edge case 3 - one number
print(rotated_array_search([], 1)) # edge case 4 - empty input, it should raise error
