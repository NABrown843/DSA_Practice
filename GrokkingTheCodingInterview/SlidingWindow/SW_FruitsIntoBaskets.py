def fruits_into_baskets(fruits):
    window_start = 0
    num_fruits = 0
    fruit_freq = {}

    for window_end in range(len(fruits)):
        fruit_freq[fruits[window_end]] = fruit_freq.setdefault(fruits[window_end], 0) + 1

        while len(fruit_freq) > 2:
            fruit_freq[fruits[window_start]] -= 1
            if fruit_freq[fruits[window_start]] == 0:
                fruit_freq.pop(fruits[window_start])
            window_start += 1

        num_fruits = max(num_fruits, window_end - window_start + 1)

    return num_fruits


print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))
