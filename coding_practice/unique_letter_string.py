def unique_letter_string(s):
    start = 0
    end = 0
    length = len(s)
    counter = {}
    max_length = 0
    step = 0
    while end < length:
        step += 1
        print(f"counter: {counter}")
        print(f"start: {start}, end: {end}")
        print(f"-------------------------------- {step}")
        if end == length or counter.get(s[end]):
            if len(counter) > max_length:
                max_length = len(counter)
            counter.pop(s[start])
            start += 1
            continue
        if counter.get(s[end], None) is None:
            counter[s[end]] = 1
            end += 1
    return max_length
        

if __name__ == '__main__':
    print(unique_letter_string('thisishowwedoit'))