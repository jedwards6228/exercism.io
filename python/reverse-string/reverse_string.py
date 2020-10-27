def reverse(text):
    lst = [str(x) for x in text]
    lst.reverse()
    word = ""
    for y in lst:
        word += y
    return word
