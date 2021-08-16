def max_sum(arr, slide):
    max_ = None
    for x in range(len(arr) - slide + 1):
        if max_ is None:
            max_ = s = sum(arr[x:x + slide])
            continue
        # s = sum(arr[x:x + slide])
        s = s - arr[x-1] + arr[x+slide - 1]
        if s > max_:
            max_ = s
    return max_

if __name__ == '__main__':
    print('test')
    print(max_sum([1,4,6,2,1,7,8,3,45,76,3,2], 5))