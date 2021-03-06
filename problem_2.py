def rsearch(arr, target, s, e):
    if s >= e and arr[s] != target:
        return -1
    mid = (s+e)//2
    if arr[mid] == target:
        return mid
    if arr[s] < arr[mid]:
        if arr[s] <= target < arr[mid]:
            return rsearch(arr, target, s, mid)
        else:
            return rsearch(arr, target, mid, e)
    elif arr[mid] < arr[e]:
        if arr[mid] < target <= arr[e]:
            return rsearch(arr, target, mid, e)
        else:
            return rsearch(arr, target, s, mid)
    return -1

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return rsearch(input_list, number, 0, len(input_list)-1)

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
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])