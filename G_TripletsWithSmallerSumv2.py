def triplet_with_smaller_sum_v2(arr, target):
    arr.sort()
    triplets = []
    # TODO: Write your code here
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            curr_sum = arr[i] + arr[left] + arr[right]
            if curr_sum < target:
                for j in range(right, left, -1):
                    triplets.append([arr[i], arr[left], arr[j]])
                left += 1
            else:
                right -= 1

    return triplets
    
