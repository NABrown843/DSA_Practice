def triplet_with_smaller_sum(arr, target):
    count = 0
    arr.sort()
    # TODO: Write your code here
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            curr_sum = arr[i] + arr[left] + arr[right]
            if curr_sum < target:
                count += right - left
                left += 1
            else:
                right -= 1

    return count