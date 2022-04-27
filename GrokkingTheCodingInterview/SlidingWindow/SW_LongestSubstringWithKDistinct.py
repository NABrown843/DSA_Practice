def longest_substring_with_k_distinct(str1, k):
    window_start = 0
    longest_substring = 0
    char_freq = {}

    for window_end in range(len(str1)):
        char_freq[str1[window_end]] = char_freq.setdefault(str1[window_end], 0) + 1

        while len(char_freq) > k:
            char_freq[str1[window_start]] -= 1

            if char_freq[str1[window_start]] == 0:
                char_freq.pop(str1[window_start])

            window_start += 1

        longest_substring = max(longest_substring, window_end - window_start + 1)

    return longest_substring
