def find_string_anagrams(str, pattern):
  result_indexes = []
  window_start = 0
  matched = 0
  char_freq = {}

  for i in range(len(pattern)):
    char_freq[pattern[i]] = char_freq.setdefault(pattern[i], 0) + 1

  for window_end in range(len(str)):
    if str[window_end] in char_freq:
      char_freq[str[window_end]] -= 1
      if char_freq[str[window_end]] == 0:
        matched += 1
    if matched == len(char_freq):
      result_indexes.append(window_start)
    if window_end >= len(pattern) - 1:
      if str[window_start] in char_freq:
        if char_freq[str[window_start]] == 0:
          matched -= 1
        char_freq[str[window_start]] += 1
      window_start += 1

  return result_indexes