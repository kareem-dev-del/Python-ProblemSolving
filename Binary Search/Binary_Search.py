def Binary_Search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# تجربة
arr = sorted([1,5,7,9,3,1,0])
target = 3
print(Binary_Search(arr, target))