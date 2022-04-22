def remove_duplicates(arr):
    non_dupe = 1
    i = 0
    while i < len(arr):
        if arr[non_dupe - 1] != arr[i]:
            arr[non_dupe] = arr[i]
            non_dupe += 1
        i += 1
    return non_dupe
