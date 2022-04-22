def backspace_compare(str1, str2):
    idx1 = len(str1) - 1
    idx2 = len(str2) - 1

    while idx1 >= 0 or idx2 >= 0:
        i1 = get_next_valid_char_idx(str1, idx1)
        i2 = get_next_valid_char_idx(str2, idx2)

        if i1 < 0 and i2 < 0:
            return True
        if i1 < 0 or i2 < 0:
            return False
        if str1[i1] != str2[i2]:
            return False

        idx1 = i1 - 1
        idx2 = i2 - 1

    return True


def get_next_valid_char_idx(str, idx):
    backspace_count = 0
    while idx >= 0:
        if str[idx] == '#':
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break

        idx -= 1

    return idx
