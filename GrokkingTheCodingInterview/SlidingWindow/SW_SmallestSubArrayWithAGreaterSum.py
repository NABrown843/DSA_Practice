import sys


def smallest_subarray_sum(s, arr):
    smallest_subarray = sys.maxsize
    window_start = 0
    curr_sum = 0

    for window_end in range(len(arr)):
        curr_sum += arr[window_end]

        while curr_sum >= s:
            smallest_subarray = min(smallest_subarray, window_end - window_start + 1)
            curr_sum -= arr[window_start]
            window_start += 1

    if smallest_subarray == sys.maxsize:
        return 0
    return smallest_subarray
