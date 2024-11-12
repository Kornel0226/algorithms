unsorted_numbers = [1, 45, 2, 5, 44, 22, 4, 88, 77, 56, 23, 99]

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    p = arr[len(arr) // 2]

    left = [x for x in arr if x < p]
    middle = [x for x in arr if x == p]
    right = [x for x in arr if x > p]

    print("left: ", left)
    print("middle: ", middle)
    print("right:", right)

    return quick_sort(left) + middle + quick_sort(right)

sorted_array = quick_sort(unsorted_numbers)