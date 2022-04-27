def length_of_longest_substring(str1, k):
    window_start = 0
    max_length = 0
    max_repeats = 0
    char_freq = {}

    for window_end in range(len(str1)):
        char_freq[str1[window_end]] = char_freq.setdefault(str1[window_end], 0) + 1
        max_repeats = max(max_repeats, char_freq[str1[window_end]])

        if window_end - window_start + 1 - max_repeats > k:
            char_freq[str1[window_start]] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length
