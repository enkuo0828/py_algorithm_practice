
def is_subsequnce(str1, str2):
    if len(str1) > len(str2):
        return False
    p1 = 0
    p2 = 0
    str1_len = len(str1) - 1
    final = len(str2) - 1
    print(f"{p1}, {str1_len}")
    step = 0
    while p1 <= str1_len:
        step += 1
        if str1[p1] == str2[p2]:
            print(f"{str2[p2]}")
            p1 += 1
            p2 += 1
        else:
            p2 += 1
        if (final - p2) < (str1_len - p1):
            return False
    return True


if __name__ == '__subsequnce__':
    print(is_subsequnce('book', 'brooklyn'))
