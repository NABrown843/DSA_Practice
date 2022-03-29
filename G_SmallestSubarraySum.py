import sys


def smallest_subarray_sum(s, arr):
    # TODO: Write your code here
    curr_sum = 0
    min_count = sys.maxsize
    window_start = 0

    for window_end in range(len(arr)):
        curr_sum += arr[window_end]
        while curr_sum >= s:
            min_count = min(min_count, window_end - window_start + 1)
            curr_sum -= arr[window_start]
            window_start += 1

    if min_count == sys.maxsize:
        return 0
    return min_count
