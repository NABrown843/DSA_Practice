def length_of_longest_subarray(arr, k):
    window_start = 0
    max_length = 0
    num_ones = 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            num_ones += 1

        if window_end - window_start + 1 - num_ones > k:
            if arr[window_start] == 1:
                num_ones -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length
