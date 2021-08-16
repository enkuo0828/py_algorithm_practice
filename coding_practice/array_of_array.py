def collector(arr):
    # if len(arr) == 0:
    #     return 
    result = []
    for a in arr:
        if type(a) is list:
            result.extend(collector(a))
            continue
        result.extend([a])
    return result

if __name__ == "__main__":
    arr = [[[["a",[["b",["c"]],["d"]]], [["e"]], [[["f","g","h"]]]]]]
    print(collector(arr))
