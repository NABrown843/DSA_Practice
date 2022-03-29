def non_repeat_substring(str):
    # TODO: Write your code here
    window_start = 0
    max_length = 0
    char_index = {}
    for window_end in range(len(str)):
        if str[window_end] in char_index:
            window_start = max(window_start, char_index[str[window_end]] + 1)
        char_index[str[window_end]] = window_end

        max_length = max(max_length, window_end - window_start + 1)

    return max_length
