def longest_substring_with_k_distinct(str1, k):
    max_length = 0
    window_start = 0
    dict1 = {}
    for window_end in range(len(str1)):
        dict1[str1[window_end]] = dict1.setdefault(str1[window_end], 0) + 1
        while len(dict1) > k:
            dict1[str1[window_start]] -= 1
            if dict1[str1[window_start]] == 0:
                dict1.pop(str1[window_start])
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


print(longest_substring_with_k_distinct('araaci', 2))
