def shortest_window_sort(arr):
    right = len(arr) - 1
    while right > 0:
        if arr[right] > arr[right - 1]:
            right -= 1
        else:
            break
    if right == 0:
        return 0
    left = 0
    while left < right:
        if arr[left] < arr[left + 1] and arr[left] < arr[right]:
            left += 1
        else:
            break
    return right - left + 1
