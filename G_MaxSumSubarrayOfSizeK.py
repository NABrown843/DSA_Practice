def max_sub_array_of_size_k(k, arr):
    # TODO: Write your code here
    curr_sum, max_sum, window_start = 0, 0, 0
    for window_end in range(len(arr)):
        curr_sum += arr[window_end]
        if window_end >= k - 1:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= arr[window_start]
            window_start += 1

    return max_sum
