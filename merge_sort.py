
unsorted_numbers = [1, 45, 2, 5, 44, 22, 4, 88, 77, 56, 23, 99]

def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort each half
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left[0] < right[0]:
        # Take the first element from `left` and merge the rest
        return [left[0]] + merge(left[1:], right)
    else:
        # Take the first element from `right` and merge the rest
        return [right[0]] + merge(left, right[1:])

sorted_numbers = merge_sort(unsorted_numbers)
print(sorted_numbers)
