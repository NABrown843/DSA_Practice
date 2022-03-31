def find_subarrays(arr, target):
    result = []
    for left in range(len(arr)):
        subs = [arr[left]]
        pointer = left + 1
        running_prod = arr[left]
        while running_prod < target:
            result.append(list(subs))
            if pointer >= len(arr):
                break
            else:
                running_prod *= arr[pointer]
                if running_prod < target:
                    subs.append(arr[pointer])
                pointer += 1
    return result


print(find_subarrays([2, 5, 3, 10], 30))