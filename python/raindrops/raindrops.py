def convert(number):
    output = ''
    if number % 3 == 0:
        output = output + 'Pling'
    if number % 5 == 0:
        output = output + 'Plang'
    if number % 7 == 0:
        output = output + 'Plong'
    if output == '':
        output = str(number) #why does this need to be a string for the test?
    return output