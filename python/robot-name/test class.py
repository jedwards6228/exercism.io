class Test:

    lst = []
    name = ""

    def __init__(self, best):
        self.test = best

    def add_to_lst(self):
        self.lst.append('abc')
        return self.lst
        
        #This is a working class to test with.  It just adds 'abc' to the list over and over.  Same logic should work for the main goal.
