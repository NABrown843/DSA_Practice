def find_averages_of_subarrays(k, arr):
    result = []
    window_start = 0
    curr_sum = 0

    for window_end in range(len(arr)):
        curr_sum += arr[window_end]
        if window_end >= k - 1:
            result.append(curr_sum / k)
            curr_sum -= arr[window_start]
            window_start += 1

    return result
