## Merge Sort codes are borrowed from Udacity
## Data Structure and Algorithm Lesson 2-7

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list == []:
        return None

    if len(input_list) == 1:
        return input_list

    sorted_list = mergesort(input_list)

    left, right = [], []

    for i in sorted_list:
        if len(left) == len(right):
            left.append(str(i))
        else:
            right.append(str(i))

    return [int(''.join(left)), int(''.join(right))]


def mergesort(items):

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 1, 1, 1, 1], [111, 11]])
test_function([[1, 0, 1, 0, 1], [110, 10]])
print(rearrange_digits([1])) # edge case 1 - return original list
print(rearrange_digits([])) # edge case 2 - return None
