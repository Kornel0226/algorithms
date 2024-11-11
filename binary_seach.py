from array import array

sorted_numbers = [1,3,6,8,10,45,49,55,66]


def binary_search(arr, value):
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (first + last) // 2
        if arr[mid] < value:
            first = mid + 1
            mid = (first + last) // 2
        elif arr[mid] > value:
            last = mid - 1
            mid = (first + last) // 2
        else:
            return mid

    return None




s1 = binary_search(sorted_numbers, 3)
s2 = binary_search(sorted_numbers, 10)
s3 = binary_search(sorted_numbers, 66)
print(s1)
print(s2)
print(s3)

