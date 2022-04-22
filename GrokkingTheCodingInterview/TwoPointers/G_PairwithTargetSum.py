def pair_with_targetsum(arr, target_sum):
    left = 0
    right = len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target_sum:
            return [left, right]
        if curr_sum > target_sum:
            right -= 1
        else:
            left += 1
    return [-1, -1]
