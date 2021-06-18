import heapq
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    heapq.heapify(input_list)
    sum1 = sum2 = 0
    prod = 1
    while len(input_list) != 0:
        try:
            x = heapq.heappop(input_list)
            sum1 += x * prod
            y = heapq.heappop(input_list)
            sum2 += y * prod
            prod = prod * 10
        except IndexError:
            pass
    return [sum1, sum2]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[5,5,5,5,5],[555,55]])
test_function([[6,1,8,4,9,3,2],[9631,842]])
