def search_quadruplets(arr, target):
    arr.sort()
    quadruples = []
    for i in range(len(arr) - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            left = j + 1
            right = len(arr) - 1
            while left < right:
                curr_sum = arr[i] + arr[j] + arr[left] + arr[right]
                if target == curr_sum:
                    quadruples.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1
                elif target > curr_sum:
                    left += 1
                else:
                    right -= 1
    return quadruples

print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))