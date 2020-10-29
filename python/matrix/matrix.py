class Matrix:
    def __init__(self, matrix_string):
        #create a list with lists inside of it, each embedded list is a row.
        self.matrix_rows = [[int(num) for num in line.split()] for line in matrix_string.split("\n")]

    def row(self, index):
        #return the row that is asked for.
        return self.matrix_rows[index - 1]

    def column(self, index):
        #return a list that is made up of a single index from each row.
        return [col[index - 1] for col in self.matrix_rows]
