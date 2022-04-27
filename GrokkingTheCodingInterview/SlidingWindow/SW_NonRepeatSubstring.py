def non_repeat_substring(str1):
    window_start = 0
    max_length = 0
    char_index_map = {}

    for window_end in range(len(str1)):
        if str1[window_end] in char_index_map:
            window_start = max(window_start, char_index_map[str1[window_end]] + 1)
        char_index_map[str1[window_end]] = window_end
        max_length = max(max_length, window_end - window_start + 1)

    return max_length
