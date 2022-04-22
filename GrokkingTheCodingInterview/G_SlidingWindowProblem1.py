def find_permutation(str, pattern):
    window_start = 0
    matched = 0
    pattern_char_freq = {}

    for i in range(len(pattern)):
        pattern_char_freq[pattern[i]] = pattern_char_freq.setdefault(pattern[i], 0) + 1

    for window_end in range(len(str)):
        if str[window_end] in pattern_char_freq:
            pattern_char_freq[str[window_end]] -= 1
            if pattern_char_freq[str[window_end]] == 0:
                matched += 1
        if matched == len(pattern_char_freq):
            return True
        if window_end >= len(pattern) - 1:
            if str[window_start] in pattern_char_freq:
                if pattern_char_freq[str[window_start]] == 0:
                    matched -= 1
                pattern_char_freq[str[window_start]] += 1
            window_start += 1

    return False
