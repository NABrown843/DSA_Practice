import sys


def find_substring(str1, pattern):
    window_start, matched, right_char, left_char = 0, 0, 0, 0
    min_substring = sys.maxsize
    char_freq = {}

    for i in range(len(pattern)):
        char_freq[pattern[i]] = char_freq.setdefault(pattern[i], 0) + 1

    for window_end in range(len(str1)):
        if str1[window_end] in char_freq:
            char_freq[str1[window_end]] -= 1
            if char_freq[str1[window_end]] == 0:
                matched += 1

        while matched == len(char_freq):
            if min_substring > window_end - window_start + 1:
                min_substring = window_end - window_start + 1
                left_char = window_start

            if str1[window_start] in char_freq:
                if char_freq[str1[window_start]] == 0:
                    matched -= 1
                char_freq[str1[window_start]] += 1
            window_start += 1
    if min_substring == sys.maxsize:
        return ''
    else:
        return str1[left_char:left_char + min_substring]
