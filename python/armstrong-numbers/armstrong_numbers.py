def is_armstrong_number(number):
    numList = [int(x) for x in str(number)]
    total = 0
    for n in numList:
        total += n ** len(numList)
    if total == number:
        return True
    else:
        return False