def length_of_longest_substring(arr, k):
    window_start, max_length, num_zeroes = 0, 0, 0
    for window_end in range(len(arr)):
        if arr[window_end] == 0:
            num_zeroes += 1
        while num_zeroes > k:
            if arr[window_start] == 0:
                num_zeroes -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)

    return max_length
