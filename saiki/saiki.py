def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def find_max(array: list[int], left: int, right: int):
    if len(array) == 1:
        return array[0]

    middle = (left + right) // 2
    left_value = find_max(array, left, middle)
    right_value = find_max(array, middle, right)
    return max(left_value, right_value)