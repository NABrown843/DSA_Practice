def make_squares(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    highest_square_index = n - 1
    left, right = 0, n - 1
    while left <= right:
        left_square = arr[left] ** 2
        right_square = arr[right] ** 2
        if left_square > right_square:
            squares[highest_square_index] = left_square
            left += 1
        else:
            squares[highest_square_index] = right_square
            right -= 1
        highest_square_index -= 1
    return squares
