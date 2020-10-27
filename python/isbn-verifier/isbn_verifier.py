def is_valid(isbn):
    isbn = isbn.replace("-", "")
    total = 0
    if len(isbn) != 10:
        return False
    for index, i in enumerate(isbn):
        if i == "X" and index == 9:
            i = "10"
        if i.isdigit():
            total += int(i) * (len(isbn) - index)
        else:
            return False
    return total % 11 == 0
