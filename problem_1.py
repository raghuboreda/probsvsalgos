def sqrt_helper(arr, s, e, number):
    if s == e:
        return arr[s]
    mid = (s+e)//2
    lowBound = arr[mid] * arr[mid]
    upperBound = arr[mid+1] * arr[mid+1]
    if number == lowBound:
        return arr[mid]
    if number == upperBound:
        return arr[mid+1]
    if lowBound < number < upperBound:
        return arr[mid]
    if number > lowBound:
        return sqrt_helper(arr,mid,e,number)
    return sqrt_helper(arr,s,mid,number)
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None
    elif number == 0:
        return 0
    elif 1 < number <= 3:
        return 1
    input_map = [i for i in range(1, (number//2)+2)]
    return sqrt_helper(input_map, 0, len(input_map)-1, number)

if __name__ == '__main__':
    assert sqrt(2) == 1
    assert sqrt(63) == 7
    assert sqrt(200) == 14
    assert sqrt(-200) == None
