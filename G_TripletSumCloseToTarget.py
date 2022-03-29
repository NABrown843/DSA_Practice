import sys

def triplet_sum_close_to_target(arr, target_sum):
  # TODO: Write your code here
  arr.sort()
  min_sum = sys.maxsize
  min_diff = sys.maxsize

  for i in range(len(arr)):
    left = i + 1
    right = len(arr) - 1

    while left < right:
      curr_sum = arr[i] + arr[left] + arr[right]
      curr_diff = abs(target_sum - curr_sum)

      if target_sum == curr_sum:
        break
      elif target_sum > curr_sum:
        left += 1
      else:
        right -= 1

      if curr_diff < min_diff:
        min_diff = curr_diff
        min_sum = curr_sum
      elif curr_diff == min_diff:
        min_sum = min(min_sum, curr_sum)

  return min_sum
