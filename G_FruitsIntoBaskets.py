def fruits_into_baskets(fruits):
  # TODO: Write your code here
  window_start, max_fruit = 0,0
  fruit_freq = {}
  for window_end in range(len(fruits)):
    fruit_freq[fruits[window_end]] = fruit_freq.setdefault(fruits[window_end],0) + 1
    while len(fruit_freq) > 2:
      fruit_freq[fruits[window_start]] -= 1
      if fruit_freq[fruits[window_start]] == 0:
        fruit_freq.pop(fruits[window_start])
      window_start += 1
    max_fruit = max(max_fruit, window_end - window_start + 1)
  return max_fruit