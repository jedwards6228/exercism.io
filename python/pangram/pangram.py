def is_pangram(sentence):
    #make sentence lowercase and part of a set
    mySet = {str(x) for x in sentence.lower()}
    #remove non-alphanumeric characters and spaces
    for x in sentence:
        if x.isalpha() == False:
            mySet.discard(x)
    #check length against the target length
    if len(mySet) == 26:
        return True
    else:
        return False
