def slices(series, length):
    if length <= 0:
        raise Exception("Invalid Length")
    digit_list = [str(x) for x in str(series)]
    num_list = []
    i = 0
    while i + length <= len(digit_list):
        pos = 0
        new_num = ""
        while pos < length:
            new_num += digit_list[i + pos]
            pos += 1
        num_list.append(new_num)
        i += 1
    if len(num_list) == 0:
        raise Exception("Invalid Parameter(s)")
    return num_list
